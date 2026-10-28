"""Run locally with Python 3.10+; no dependencies, network calls or file writes."""

import asyncio
import json
from dataclasses import dataclass
from typing import Protocol


@dataclass
class Order:
    order_id: str
    shipped: bool = False


class TextTool(Protocol):
    def execute(self, text: str) -> str:
        ...


class EchoTool:
    def execute(self, text: str) -> str:
        return text


def run_tool(tool: TextTool, text: str) -> str:
    return tool.execute(text)


def collect(value: str, items: list[str] | None = None) -> list[str]:
    if items is None:
        items = []
    items.append(value)
    return items


def add(a: int, b: int) -> int:
    return a + b


async def answer() -> str:
    return "done"


def main() -> None:
    users = [{"name": "Alice", "active": True}, {"name": "Bob", "active": False}]
    names = [u["name"] for u in users if u.get("active")]
    expanded = []
    for user in users:
        if user.get("active"):
            expanded.append(user["name"])
    assert names == expanded == ["Alice"]
    print("comprehension:", names)

    data = {"timeout": 10, **{"timeout": 20}}
    assert data["timeout"] == 20
    assert add(*[2, 3]) == add(**{"a": 2, "b": 3}) == 5
    print("unpacking:", data, add(2, 3))

    value = 0
    assert (value or 10) == 10
    assert (10 if value is None else value) == 0
    assert collect("a") == ["a"] and collect("b") == ["b"]
    print("truthiness/defaults: checked")

    values = [3, 1]
    assert sorted(values) == [1, 3] and values == [3, 1]
    assert values.sort() is None and values == [1, 3]
    iterator = (x * 2 for x in values)
    assert list(iterator) == [2, 6] and list(iterator) == []
    print("mutation/iteration: checked")

    order = Order("A001")
    assert not order.shipped
    assert run_tool(EchoTool(), order.order_id) == "A001"
    assert json.loads(json.dumps({"id": order.order_id})) == {"id": "A001"}
    print("dataclass/protocol:", order)
    assert asyncio.run(answer()) == "done"
    print("async: done")


if __name__ == "__main__":
    main()
