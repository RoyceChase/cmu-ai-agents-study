# 1b · Agent Capabilities 1: Tool Use

- 官方日期：2026 · Thu, Aug 27（沿用官网日期）
- 课程分组：Introduction and Agent Capabilities
- 学习状态：未开始
- 资源核对日期：2026-10-27

## 学习入口

- [课程笔记](notes.md)
- [论文与参考资料](#论文与参考资料)
- [代码实验](#代码实验)
- [实验记录](experiments.md)
- [全部课程](../README.md)

## 官方资源

- [官方课表](https://www.cmu-agents.com/#/schedule)
- [课件：Lecture 2 slides](https://www.cmu-agents.com/slides/lecture-02-tool-use.pdf)
- [视频：Lecture 2 recording](https://www.youtube.com/watch?v=jXChFB4JSyw&list=PLSN0qpDfUvTM&index=2)

## 论文与参考资料

来源：[官方课表](https://www.cmu-agents.com/#/schedule)，核对日期：2026-10-27。资料可能包含论文、技术文档、博客和代码仓库；阅读优先级是本项目的初始建议。

| 资料 | 官网分类 | 阅读优先级 | 状态 |
| --- | --- | --- | --- |
| [What Are Tools Anyway?](https://arxiv.org/abs/2403.15452) | Readings | 选读（待确定精读项） | 未阅读 |
| [CodeAct](https://arxiv.org/abs/2402.01030) | Readings | 选读（待确定精读项） | 未阅读 |
| [Toolformer](https://arxiv.org/abs/2302.04761) | Readings | 选读（待确定精读项） | 未阅读 |
| [XGrammar](https://arxiv.org/abs/2411.15100) | Readings | 选读（待确定精读项） | 未阅读 |
| [OpenAI Chat Completions API](https://platform.openai.com/docs/api-reference/chat/create) | References | 参考 | 未阅读 |
| [Hugging Face Chat Templates](https://huggingface.co/docs/transformers/chat_templating) | References | 参考 | 未阅读 |
| [Qwen2.5 Chat Template](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/tokenizer_config.json) | References | 参考 | 未阅读 |
| [Berkeley Function-Calling Leaderboard V4](https://gorilla.cs.berkeley.edu/leaderboard.html) | References | 参考 | 未阅读 |
| [BFCL V4 Methodology](https://gorilla.cs.berkeley.edu/blogs/15_bfcl_v4_web_search.html) | References | 参考 | 未阅读 |
| [OpenRouter Provider Analytics](https://openrouter.ai/) | References | 参考 | 未阅读 |
| [OpenAI Function Calling Guide](https://developers.openai.com/api/docs/guides/function-calling) | References | 参考 | 未阅读 |
| [Qwen3.8 Tool-Call Template](https://huggingface.co/Qwen/Qwen3.8-27B/blob/main/tokenizer_config.json) | References | 参考 | 未阅读 |
| [Mistral Small 4 Model Card](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603) | References | 参考 | 未阅读 |
| [Mistral Tool-Call Tokenization Guide](https://github.com/mistralai/cookbook/blob/main/concept-deep-dive/tokenization/tool_calling.md) | References | 参考 | 未阅读 |
| [DeepSeek V3.2 Tool-Call Encoding](https://huggingface.co/deepseek-ai/DeepSeek-V3.2/blob/main/encoding/encoding_dsv32.py) | References | 参考 | 未阅读 |
| [OpenHands Tool System Architecture](https://docs.openhands.dev/sdk/arch/tool-system) | References | 参考 | 未阅读 |
| [OpenHands Agent Dispatch Source](https://github.com/OpenHands/software-agent-sdk/blob/main/openhands-sdk/openhands/sdk/agent/agent.py) | References | 参考 | 未阅读 |
| [OpenHands ToolDefinition Source](https://github.com/OpenHands/software-agent-sdk/blob/main/openhands-sdk/openhands/sdk/tool/tool.py) | References | 参考 | 未阅读 |
| [JSON Schema 2020-12](https://json-schema.org/draft/2020-12/json-schema-core.html) | References | 参考 | 未阅读 |
| [JSON Schema 2020-12 Validation](https://json-schema.org/draft/2020-12/json-schema-validation.html) | References | 参考 | 未阅读 |
| [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) | References | 参考 | 未阅读 |
| [FastAPI Generated OpenAPI](https://fastapi.tiangolo.com/tutorial/first-steps/#openapi) | References | 参考 | 未阅读 |
| [FastAPI Security and OpenAPI](https://fastapi.tiangolo.com/tutorial/security/) | References | 参考 | 未阅读 |
| [MCP 2026-07-28 Specification Release](https://blog.modelcontextprotocol.io/posts/2026-07-28/) | References | 参考 | 未阅读 |
| [MCP TypeScript SDK v2 Overview](https://ts.sdk.modelcontextprotocol.io/v2/) | References | 参考 | 未阅读 |
| [MCP Transports Specification](https://modelcontextprotocol.io/specification/draft/basic/transports) | References | 参考 | 未阅读 |
| [MCP Tools Specification](https://modelcontextprotocol.io/specification/draft/server/tools) | References | 参考 | 未阅读 |
| [FastMCP OpenAPI Integration](https://gofastmcp.com/integrations/openapi) | References | 参考 | 未阅读 |
| [FastMCP Token Verification](https://gofastmcp.com/servers/auth/token-verification) | References | 参考 | 未阅读 |
| [FastMCP Bearer Client Authentication](https://gofastmcp.com/clients/auth/bearer) | References | 参考 | 未阅读 |

阅读笔记按需放入 `papers/<资料简称>.md`，记录问题、方法、证据、局限与个人理解。原文统一保存在 `../../references/pdfs/` 并纳入 Git，在本节补充实际文件路径、版本与获取日期；当前尚未下载。

## 代码实验

状态：待实现。代码放在 `code/`，开始实验时在本节补充目标、依赖、入口、运行命令、输入与预期行为。共享组件位于 `../../src/agent_study/`，结果与失败原因记录在 [实验记录](experiments.md)。当前尚未初始化运行环境或实现代码。

## 学习目标

待学习时根据本课内容填写。

## 完成检查

- [ ] 能解释核心问题、方法与适用条件。
- [ ] 完成核心材料阅读记录。
- [ ] 完成最小实验或案例分析。
- [ ] 整理结论、局限与未解决问题。
