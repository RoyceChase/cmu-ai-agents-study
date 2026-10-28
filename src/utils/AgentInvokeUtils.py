import os
from typing import Literal

from openai import OpenAI, Stream
from openai.types.chat import (
    ChatCompletion,
    ChatCompletionChunk,
    ChatCompletionMessageParam, ChatCompletionSystemMessageParam, ChatCompletionUserMessageParam,
)


def get_basic_client() -> OpenAI:
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("请先设置环境变量 DEEPSEEK_API_KEY")
    return OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com",
        timeout=60.0,
    )


def build_messages(
    user_prompt: str,
    system_prompt: str,
) -> list[ChatCompletionMessageParam]:
    return [
        ChatCompletionSystemMessageParam(
            role="system",
            content=system_prompt,
        ),
        ChatCompletionUserMessageParam(
            role="user",
            content=user_prompt,
        ),
    ]


def invoke_api_non_stream(
    user_prompt: str,
    *,
    client: OpenAI,
    model: str = "deepseek-flash",
    reasoning_effort: Literal["low", "medium", "high"] = "low",
    think_type: Literal["enabled", "disabled"] = "disabled",
    system_prompt: str = "You are a helpful assistant",
) -> ChatCompletion:
    return client.chat.completions.create(
        model=model,
        messages=build_messages(user_prompt, system_prompt),
        stream=False,
        reasoning_effort=reasoning_effort,
        extra_body={"thinking": {"type": think_type}},
    )


def invoke_api_stream(
    user_prompt: str,
    *,
    client: OpenAI,
    model: str = "deepseek-flash",
    reasoning_effort: Literal["low", "medium", "high"] = "low",
    think_type: Literal["enabled", "disabled"] = "disabled",
    system_prompt: str = "You are a helpful assistant",
) -> Stream[ChatCompletionChunk]:
    return client.chat.completions.create(
        model=model,
        messages=build_messages(user_prompt, system_prompt),
        stream=True,
        reasoning_effort=reasoning_effort,
        extra_body={"thinking": {"type": think_type}},
    )


def main() -> None:
    with get_basic_client() as client:
        response = invoke_api_non_stream(
            "请用中文简短解释什么是 Agent。",
            client=client,
        )
        print(response.choices[0].message.content)

        # 流式调用时，用下面的代码替换上面的非流式调用。
        # with invoke_api_stream("什么是 Agent？", client=client) as stream:
        #     for chunk in stream:
        #         if chunk.choices:
        #             print(chunk.choices[0].delta.content or "", end="", flush=True)
        # print()


if __name__ == "__main__":
    main()
