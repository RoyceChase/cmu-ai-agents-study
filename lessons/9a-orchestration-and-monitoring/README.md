# 9a · Frameworks 2: Orchestration and Monitoring

- 官方日期：2026 · Tue, Oct 20（沿用官网日期）
- 课程分组：Agent Frameworks
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
- [课件：Lecture 15 slides](https://www.cmu-agents.com/slides/lecture-15-orchestration-and-monitoring.pdf)
- 视频：官网暂未提供，后续核对。

## 论文与参考资料

来源：[官方课表](https://www.cmu-agents.com/#/schedule)，核对日期：2026-10-27。资料可能包含论文、技术文档、博客和代码仓库；阅读优先级是本项目的初始建议。

| 资料 | 官网分类 | 阅读优先级 | 状态 |
| --- | --- | --- | --- |
| [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | Readings | 选读（待确定精读项） | 未阅读 |
| [Thinking in LangGraph](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph) | Readings | 选读（待确定精读项） | 未阅读 |
| [Diagnosing a performance regression on Terminal-Bench with Docent](https://transluce.org/docent/blog/terminal-bench) | Readings | 选读（待确定精读项） | 未阅读 |
| [Hodoscope: Unsupervised Monitoring for AI Misbehaviors](https://arxiv.org/abs/2604.11072) | Readings | 选读（待确定精读项） | 未阅读 |
| [LangGraph: Workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents) | References | 参考 | 未阅读 |
| [LangGraph: Persistence](https://docs.langchain.com/oss/python/langgraph/persistence) | References | 参考 | 未阅读 |
| [LangGraph: Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts) | References | 参考 | 未阅读 |
| [LangGraph: Testing](https://docs.langchain.com/oss/python/langgraph/test) | References | 参考 | 未阅读 |
| [LangChain: Testing](https://docs.langchain.com/oss/python/langchain/test) | References | 参考 | 未阅读 |
| [LangSmith: Evaluation](https://docs.langchain.com/langsmith/evaluation) | References | 参考 | 未阅读 |
| [Course support demo: password-reset trace](https://smith.langchain.com/public/5e17b93a-17af-4386-ada0-9bd033f98a74/r) | References | 参考 | 未阅读 |
| [Course support demo: billing trace before approval](https://smith.langchain.com/public/aeddf201-687b-4389-acdb-137dd9683000/r) | References | 参考 | 未阅读 |
| [Course support demo: billing trace after approval](https://smith.langchain.com/public/416d3c74-4b43-4883-b189-92a57431a819/r) | References | 参考 | 未阅读 |
| [Docent: Pairwise comparisons and failure-mode synthesis](https://docent.transluce.org/dashboard/9bafeb94-3f6e-4d03-bd01-1ae8476e3f6e/analysis-plan/81230a32-88e0-42af-82c9-101660ab1d89) | References | 参考 | 未阅读 |
| [Docent: No-timeout task comparison](https://docent.transluce.org/dashboard/9bafeb94-3f6e-4d03-bd01-1ae8476e3f6e/analysis-plan/772c0920-0b0f-4355-a009-825d1dd553b4) | References | 参考 | 未阅读 |
| [Hodoscope announcement](https://hodoscope.dev/blog/announcement.html) | References | 参考 | 未阅读 |
| [Embedding Atlas](https://apple.github.io/embedding-atlas/) | References | 参考 | 未阅读 |
| [OpenHands SDK](https://docs.openhands.dev/sdk) | References | 参考 | 未阅读 |
| [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview) | References | 参考 | 未阅读 |
| [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) | References | 参考 | 未阅读 |
| [AG2 overview](https://docs.ag2.ai/latest/docs/user-guide/basic-concepts/overview/) | References | 参考 | 未阅读 |
| [DSPy](https://dspy.ai/) | References | 参考 | 未阅读 |
| [Don’t Sleep on Single-Agent Systems](https://hub.openhands.dev/blog/dont-sleep-on-single-agent-systems) | References | 参考 | 未阅读 |
| [Agent Skills specification](https://agentskills.io/specification) | References | 参考 | 未阅读 |
| [Multi-Agent Computer Use (MACU)](https://arxiv.org/abs/2606.01533) | References | 参考 | 未阅读 |
| [OpenHands automations: Fujitsu talk slides](https://github.com/neubig/slides/tree/main/slides/2026-09-25-fujitsu-openhands-en) | References | 参考 | 未阅读 |
| [Black Hat USA 2026: The OpenAI–Hugging Face incident](https://www.youtube.com/watch?v=87DyyMV0kCY) | References | 参考 | 未阅读 |
| [OpenAI: Hugging Face incident and the road ahead](https://openai.com/index/hugging-face-incident-and-the-road-ahead/) | References | 参考 | 未阅读 |

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
