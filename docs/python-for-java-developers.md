# Java 开发者的 Python 代码阅读指南

整理日期：2026-10-28。适合已有 Java 经验、环境配置熟悉，但对 Python 写法和 API 不熟悉的学习者。示例采用 Python 3.10+ 语法，除特别注明外只用标准库。这是自编学习资料，不是官方文档的翻译。

## 学习顺序

先读命名、折行、集合和函数，再读类型与对象，最后接触装饰器、生成器和异步。目标是看清每个变量是什么、表达式返回什么、是否改变原对象。无需先学框架。

配套 [python_examples.py](../tests/python_examples.py) 可在仓库根目录运行：

```shell
python tests/python_examples.py
```

## 1. 命名与排版

| 对象 | Python | Java 对照 |
| --- | --- | --- |
| 函数、参数、属性 | get_order、order_id | getOrder、orderId |
| 类 | OrderService | 同样使用大驼峰 |
| 常量 | MAX_RETRIES | 同 Java；命名不强制只读 |
| 模块文件 | order_service.py | 不要求与类同名 |
| 内部成员 | _client | 约定内部使用，不是强制 private |
| 特殊方法 | __init__、__str__ | Python 预定义协议入口 |

类中的 `__name` 会触发名称改写，主要避免继承冲突，不等于访问权限控制。不要自行发明双端下划线名称。避免用 list、str、id 覆盖内置名称。

使用四个空格缩进。括号内部自然折行，末尾逗号合法，不必添加反斜杠：

```python
messages = [
    {"role": "user", "content": "hello"},
]
```

注意 `(1)` 是整数，`(1,)` 才是单元素元组。花括号 `{}` 是空字典，空集合用 `set()`。

来源：[PEP 8](https://peps.python.org/pep-0008/)。

## 2. 变量、真假与比较

变量名绑定到对象，可以重新绑定不同类型；对象本身有类型。类型提示能帮助阅读，但通常不提供运行时校验。

```python
items = []
other = items
other.append(1)
assert items == [1]  # 两个名字引用同一对象
```

`==` 比较值，`is` 比较对象身份。判断空值使用 `value is None`，不要用 `is` 比较字符串或数字。

None、False、0、空字符串和空容器在条件中为假；字符串 `"false"` 仍为真。

```python
value = 0
result = value or 10  # 10：or 根据真假返回操作数，并非仅处理 None
result = 10 if value is None else value  # 0：只替换 None
```

`and`、`or` 会短路，返回的是操作数。`not` 返回布尔值。

## 3. 常用类型与方法速查

| 类型 | 常用操作 | 返回值和注意点 |
| --- | --- | --- |
| list | append(x)、extend(xs) | 原地修改，返回 None；前者添加一个对象，后者逐项添加 |
| list | pop() | 删除并返回末项；空列表报 IndexError |
| list | sort() | 原地排序，返回 None |
| 任意可迭代对象 | sorted(xs) | 返回新列表 |
| dict | d[key] | 缺键报 KeyError |
| dict | d.get(key, default) | 缺键返回默认值；已有值为 None 时仍返回 None |
| dict | items() | 可遍历键值对，不是列表副本 |
| str | split(sep)、sep.join(xs) | 拆分成列表；把字符串序列连接为字符串 |
| str | strip()、replace(a, b) | 返回新字符串，不修改原字符串 |
| set | add(x)、a & b、a | b | 添加、交集、并集；集合元素需要可哈希 |

`len(xs)` 取长度，`x in d` 判断字典的键，`range(3)` 依次产生 0、1、2。

```python
names = ["Bob", "Alice"]
ordered = sorted(names)
assert names == ["Bob", "Alice"]
assert ordered == ["Alice", "Bob"]
```

`xs[start:stop:step]` 的右边界不包含在结果里；`xs[-1]` 是末项，`xs[::-1]` 是反向切片。列表切片和 copy() 都只是浅拷贝，嵌套对象仍共享。

来源：[数据结构教程](https://docs.python.org/3/tutorial/datastructures.html)、[内置类型](https://docs.python.org/3/library/stdtypes.html)。

## 4. 函数与参数

```python
def get_order(order_id: str, *, include_items: bool = False) -> dict:
    return {"id": order_id, "include_items": include_items}

order = get_order("A001", include_items=True)
```

`def` 定义函数，冒号开始代码块，`-> dict` 是返回类型提示。没有 return 或只写 return 时返回 None。星号后的参数必须按名称传入。

| 写法 | 定义时 | 调用时 |
| --- | --- | --- |
| *args / *values | 收集额外位置参数为元组 | 展开可迭代对象为位置参数 |
| **kwargs / **options | 收集额外关键字参数为字典 | 展开字符串键字典为关键字参数 |
| / | 前面的参数只能按位置传入 | 不用于调用语法 |
| 单独的 * | 后面的参数只能按名称传入 | 不用于调用语法 |

```python
def add(a, b):
    return a + b

values = [2, 3]
assert add(*values) == 5
assert add(**{"a": 2, "b": 3}) == 5
```

默认参数在函数定义时计算，避免使用可变默认值：

```python
def collect(value, items=None):
    if items is None:
        items = []
    items.append(value)
    return items
```

不要写成 `items=[]`，否则省略参数的多次调用会共享同一列表。函数也是对象，可以放进字典：`tools = {"add": add}`，用 `tools["add"](2, 3)` 调用。

来源：[函数定义与参数](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)。

## 5. 看懂语法糖

```python
users = [{"name": "Alice", "active": True}, {"name": "Bob", "active": False}]
names = [u["name"] for u in users if u.get("active")]
```

等价的直白版本：

```python
names = []
for user in users:
    if user.get("active"):
        names.append(user["name"])
```

`{x: len(x) for x in names}` 是字典推导式；`{x for x in names}` 是集合推导式；`(len(x) for x in names)` 是生成器表达式，按需计算，通常遍历后就耗尽。

```python
for index, name in enumerate(names, start=1):
    print(index, name)

for key, value in {"a": 1}.items():
    print(key, value)
```

`enumerate` 提供序号和元素；`zip(a, b)` 成对遍历，默认以较短序列为止。`a, b = pair` 是解包，`first, *rest = values` 收集剩余元素。

`{**base, **override}` 合并字典，后者覆盖同名键；`[*left, *right]` 展开并合并列表。

`lambda x: x["score"]` 是单表达式匿名函数，常见于 `sorted(rows, key=...)`。`:=` 在表达式中赋值，先能识别即可，学习代码不必主动使用。

## 6. 类型提示、鸭子类型与接口

鸭子类型关注对象能否完成某个操作，不要求先继承指定接口；不代表自动转换类型，也不代表任意对象都能传进去。

```python
def run(tool, text: str) -> str:
    return tool.execute(text)
```

这段代码要求 tool 实际上有可调用且参数兼容的 execute。没有该属性时可能报 AttributeError，参数不兼容时可能报 TypeError。

不想猜类型，可以明确写结构契约：

```python
from typing import Protocol

class TextTool(Protocol):
    def execute(self, text: str) -> str:
        ...

class EchoTool:
    def execute(self, text: str) -> str:
        return text

def run(tool: TextTool, text: str) -> str:
    return tool.execute(text)
```

EchoTool 不必显式继承 TextTool；类型检查器可以按结构判断兼容性。Protocol 默认不是运行时参数校验器。`...` 在此表示省略协议方法体。

常见提示：`list[str]`、`dict[str, int]`、`str | None`、`Callable[[str], str]`。`Any` 会削弱静态检查；`object` 则要求先缩小类型再使用特定能力。

`TypedDict` 描述字典的键及其值类型，运行时仍是普通字典。对于字段固定的数据，可以用 dataclass，减少猜测。

来源：[typing](https://docs.python.org/3/library/typing.html)、[类教程](https://docs.python.org/3/tutorial/classes.html)。

## 7. 类与 dataclass

```python
from dataclasses import dataclass

@dataclass
class Order:
    order_id: str
    shipped: bool = False

order = Order("A001")
assert order.order_id == "A001"
```

dataclass 可自动生成初始化、展示和相等比较等方法，不是完整的运行时数据验证框架。普通实例方法第一个参数惯例叫 self，调用时由对象自动提供，类似显式写出的 this。

类中 `def __init__(self, ...)` 初始化实例。实例属性通常写成 `self.name = ...`；类体内的可变属性可能被多个实例共享，别把它当作每个实例各自的新集合。

`@staticmethod` 不隐式传 self，`@classmethod` 隐式传 cls。`@property` 让方法通过属性形式访问；看到 `obj.value` 不一定只是直接读取字段。

来源：[dataclasses](https://docs.python.org/3/library/dataclasses.html)。

## 8. 装饰器、上下文与异步：先读懂

`@decorate` 放在函数定义上方，可近似理解为定义后执行 `func = decorate(func)`。装饰器是在 Python 中实际执行的包装逻辑，与 Java 注解机制不同；暂时不必学习复杂装饰器实现。

`with` 使用上下文管理协议，在离开代码块时执行清理逻辑，常用于文件或锁。文件示例读取路径相对于当前工作目录，不自动相对于脚本所在目录：

```python
from pathlib import Path

script_folder = Path(__file__).resolve().parent
```

`async def` 定义协程函数，调用它先得到协程对象；需要 await 或交给事件循环运行。异步不意味着自动创建线程，也不会把阻塞函数自动变成非阻塞。

```python
import asyncio

async def answer() -> str:
    return "done"

if __name__ == "__main__":
    print(asyncio.run(answer()))
```

在已有事件循环的环境（例如某些 Notebook）通常直接 await，不再嵌套 asyncio.run。

来源：[asyncio](https://docs.python.org/3/library/asyncio-task.html)、[with](https://docs.python.org/3/reference/compound_stmts.html#the-with-statement)。

## 9. 异常、JSON、导入和入口

```python
import json

try:
    data = json.loads('{"order_id": "A001"}')
except json.JSONDecodeError as error:
    raise ValueError("订单 JSON 无效") from error
```

`json.loads`：字符串到 Python 对象；`json.dumps`：对象到 JSON 字符串。`load` / `dump` 不带 s 时面向文件对象。JSON 的 null/true/false 对应 Python 的 None/True/False。

异常不要求像 Java checked exception 那样声明；捕获具体异常并处理，不要用广泛 except 静默吞错。

`import json` 后写 `json.loads`；`from pathlib import Path` 后直接写 `Path`。导入模块会执行其顶层代码，因此把运行入口放在 `if __name__ == "__main__":` 内。导入时不要自动访问网络、付费接口或改写文件。

来源：[JSON](https://docs.python.org/3/library/json.html)、[模块](https://docs.python.org/3/tutorial/modules.html)、[异常](https://docs.python.org/3/tutorial/errors.html)。

## 10. 不认识函数时怎么查

先看它属于哪一层：`len(items)` 是内置函数；`items.append(x)` 是对象方法；`json.loads(text)` 是标准库；`client.generate(...)` 可能是第三方库或本项目的方法，不一定存在于每个 SDK。

操作顺序：看 import → IDE 跳转定义 → 看参数及返回类型 → 查对应版本官方文档 → 写最小输入观察返回值。`help()`、`type()`、`dir()` 适合辅助探索，但动态 SDK 未必能靠 dir 列出全部功能。

特别留意方法是否原地修改、是否返回 None、是否惰性执行，以及响应到底是字典还是带属性的对象。

## 11. 三次练习

1. 运行 python_examples.py。把推导式、字典展开与解包改成普通循环，保持输出一致。
2. 写订单查询与取消函数：处理不存在、已发货和正常取消；显式标注输入输出类型。然后说明哪些函数修改了原对象。
3. 阅读仓库的 scripts/update_bibliography.py，只追踪 main → extract_papers → merge_bibliography 的数据流，不要求一次看懂所有正则和 XML。

完成参考：能说明输入、返回类型、异常和副作用，能将常见简写改写为直白代码。元类、描述符实现、复杂泛型等留待实际需要。

## 官方资料入口

优先按问题查阅，而非通读全部参考文档：

- [Python 中文教程](https://docs.python.org/zh-cn/3/tutorial/)
- [内置函数](https://docs.python.org/3/library/functions.html)
- [标准类型](https://docs.python.org/3/library/stdtypes.html)
- [PEP 8 命名与风格](https://peps.python.org/pep-0008/)

Python 官方 /3/ 文档会随版本更新。本资料示例以 Python 3.10+ 常用写法为基线；第三方库的 API 应核对你实际安装的版本。
