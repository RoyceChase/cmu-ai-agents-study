from src.utils import AgentInvokeUtils


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
    orders = {
        "A001": "已发货",
        "A002": "待支付",
    }

    status = orders.get(order_id)

    if status is None:
        return {
            "order_id": order_id,
            "error": "订单不存在",
        }
    return {
        "order_id": order_id,
        "status": status,
    }



def main() -> None:
    print(get_order_status("A001"))
    print(get_order_status("A999"))


if __name__ == "__main__":
    main()
