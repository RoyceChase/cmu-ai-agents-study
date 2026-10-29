import json

from openai import OpenAI

from src.utils import AgentInvokeUtils


# 这里只向模型描述工具及参数，不会自动执行本地函数。
# 即使只有一个工具，请求中的 tools 也必须传列表。
order_status_tool = {
    "type": "function",
    "function": {
        "name": "get_order_status",
        "description": "根据订单编号查询订单状态。",
        "parameters": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "string",
                    "description": "需要查询的订单编号，例如 A001。",
                }
            },
            "required": ["order_id"],
        },
    },
}

def get_order_status(order_id: str) -> dict[str, str]:
    """查询模拟订单状态。"""
    # 当前使用模拟数据；真实服务还需根据可信登录身份检查订单归属。
    # 工具白名单和参数校验不能代替业务授权，不能信任模型自报的用户身份。
    orders = {
        "A001": "已发货",
        "A002": "待支付",
    }

    status = orders.get(order_id)

    # 未查到订单是业务结果，不等于网络或程序故障，不应因此无条件重试。
    if status is None:
        return {
            "order_id": order_id,
            "error": "订单不存在",
        }
    return {
        "order_id": order_id,
        "status": status,
    }



def run_order_agent(user_prompt: str, *, client: OpenAI, max_rounds: int = 4) -> str:
    """保留消息历史，执行工具并回传结果；限制模型请求轮数。"""
    # 历史保存目标、模型动作和工具观察；只重发原问题会丢失已执行的查询结果。
    # 每次调用本函数都会新建历史，目前不支持跨用户输入的连续对话。
    messages = AgentInvokeUtils.build_messages(
        user_prompt, "你是订单助手。根据工具的真实结果回答；缺少订单号时询问用户。"
    )
    # 限制模型请求次数，防止重复调用持续消耗费用和时间；不是递归深度限制。
    # 一轮可能提出多个工具调用，所以该上限不等于工具调用次数上限。
    for round_number in range(1, max_rounds + 1):
        response = AgentInvokeUtils.invoke_api_non_stream(
            user_prompt, client=client, tools=[order_status_tool], messages=messages,
        )
        message = response.choices[0].message
        print(f"第 {round_number} 轮：{response.choices[0].finish_reason}")
        # 没有调用请求时返回文字；stop 只表示本轮生成结束。
        # 例如询问订单号也会 stop，此时业务任务仍未完成。
        if not message.tool_calls:
            if response.choices[0].finish_reason != "stop":
                raise RuntimeError("模型响应未正常完成，请检查 finish_reason")
            return message.content or ""

        # 必须先保存 assistant 的调用请求，再追加各工具的执行结果。
        # 模型提出调用不代表工具已执行；执行由下面的本地代码负责。
        messages.append(message.model_dump(exclude_none=True))
        for call in message.tool_calls:
            if call.type != "function":
                raise ValueError("不支持的工具调用类型")
            try:
                # 模型输出不可信：理解错误或提示注入都可能影响动作选择。
                # 用明确白名单分发，禁止通过 eval 等方式任意执行模型给出的名称。
                if call.function.name != "get_order_status":
                    raise ValueError("不允许调用该工具")
                # arguments 是 JSON 字符串，反序列化为 dict 后才能读取字段。
                # 工具描述和 Python 类型注解都不能代替运行时参数校验。
                arguments = json.loads(call.function.arguments)
                if not isinstance(arguments, dict) or set(arguments) != {"order_id"}:
                    raise ValueError("参数必须只包含 order_id")
                order_id = arguments["order_id"]
                # 这里只校验非空字符串；xxxx 会通过格式校验，再得到订单不存在。
                if not isinstance(order_id, str) or not order_id.strip():
                    raise ValueError("order_id 必须是非空字符串")
                result = get_order_status(order_id)
            # 把可预期的输入错误作为观察回传，让模型有机会修正；轮数上限兜底。
            except (ValueError, TypeError) as exc:
                result = {"error": str(exc)}
            print(f"工具 {call.function.name} 返回：{result}")
            # tool_call_id 把结果关联到具体请求，多工具调用时尤其不能混淆。
            # 下一轮模型只有收到真实结果，才有依据回答订单状态。
            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": json.dumps(result, ensure_ascii=False),
            })
    raise RuntimeError(f"已达到 {max_rounds} 轮请求上限，停止执行")

#####第一轮工具实验######
## prompt:帮我查询下订单,订单号是A001
## result:
# 第 1 轮：tool_calls
# 工具 get_order_status 返回：{'order_id': 'A001', 'status': '已发货'}
# 第 2 轮：stop
# 最终回复： 订单 A001 的当前状态是：**已发货**。

#####第二轮工具实验######
## prompt:帮我查询下订单,订单号是xxxx
## result:
# 第 1 轮：tool_calls
# 工具 get_order_status 返回：{'order_id': 'xxxx', 'error': '订单不存在'}
# 第 2 轮：stop
# 最终回复： 抱歉，系统查询结果显示：**订单 xxxx 不存在**。

#####第三轮工具实验######
## prompt:帮我查询下订单
## result:
# 第 1 轮：stop
# 最终回复： 请提供一下您的订单编号（例如 A001），我来帮您查询。


def main() -> None:
    with AgentInvokeUtils.get_basic_client() as client:
        answer = run_order_agent("帮我查询下订单", client=client)
        print("最终回复：", answer)


if __name__ == "__main__":
    main()
