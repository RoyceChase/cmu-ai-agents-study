# 1a 实验索引

- [订单工具调用循环](experiments/ToolsInvoke.py)：非流式请求、工具执行、结果回传和最终回答。

在仓库根目录运行：

```powershell
.\.venv\Scripts\python.exe -m lessons.1a-agent-overview.experiments.ToolsInvoke
```

依赖使用根目录 `requirements.txt`，运行前设置环境变量 `DEEPSEEK_API_KEY`。运行会请求远程模型并产生相应 API 用量；订单数据为本地模拟数据，无需 GPU。

默认输入订单 xxx（不存在）；可改为 A001（已发货）或 A002（待支付）。模型为 deepseek-flash，thinking disabled，最多请求 4 轮。程序打印每轮终止原因、工具结果和最终回答。预期最终回答依据工具结果；达到轮数上限时报错停止。

验证记录（2026-10-29）：语法检查通过；模拟模型响应验证了正常订单、不存在订单、未知工具和非法 JSON 的处理以及消息历史回传。未执行真实模型请求，尚无真实模型实验结论。运行后记录实际回复、请求轮数及异常，再分析是否符合预期。
