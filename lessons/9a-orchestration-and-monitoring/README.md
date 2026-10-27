# 9a · Frameworks 2: Orchestration and Monitoring

- 官方日期：2026 · Tue, Oct 20（沿用官网日期）
- 课程分组：Agent Frameworks
- 学习状态：[见课程索引](../README.md)
- 资源核对日期：2026-10-27

## 学习入口

- [课程笔记](notes.md)
- [论文与参考资料](#论文与参考资料)
- [代码实验](#代码实验)
- [实验索引](experiments.md)
- [全部课程](../README.md)

## 官方资源

- [官方课表](https://www.cmu-agents.com/#/schedule)
- [课件：Lecture 15 slides](https://www.cmu-agents.com/slides/lecture-15-orchestration-and-monitoring.pdf)
- 视频：官网暂未提供，后续核对。

## 论文与参考资料

来源：[官方课表](https://www.cmu-agents.com/#/schedule)，核对日期：2026-10-27。资料可能包含论文、技术文档、博客和代码仓库；阅读优先级是本项目的初始建议。

| 资料 | 官网分类 | 阅读优先级 | 状态 |
| --- | --- | --- | --- |
| [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) · [资料目录](../../references/articles/anthropic-building-effective-agents/) · [PDF](../../references/articles/anthropic-building-effective-agents/article.pdf) · [阅读笔记](../../references/articles/anthropic-building-effective-agents/notes.md) | Readings | 选读（待确定精读项） | [以阅读笔记为准](../../references/articles/anthropic-building-effective-agents/notes.md) |
| [Thinking in LangGraph](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph) | Readings | 选读（待确定精读项） | 未阅读 |
| [Diagnosing a performance regression on Terminal-Bench with Docent](https://transluce.org/docent/blog/terminal-bench) · [资料目录](../../references/articles/transluce-terminal-bench-regression/) · [PDF](../../references/articles/transluce-terminal-bench-regression/article.pdf) · [阅读笔记](../../references/articles/transluce-terminal-bench-regression/notes.md) | Readings | 选读（待确定精读项） | [以阅读笔记为准](../../references/articles/transluce-terminal-bench-regression/notes.md) |
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
| [Don’t Sleep on Single-Agent Systems](https://hub.openhands.dev/blog/dont-sleep-on-single-agent-systems) · [资料目录](../../references/articles/openhands-single-agent-systems/) · [PDF](../../references/articles/openhands-single-agent-systems/article.pdf) · [阅读笔记](../../references/articles/openhands-single-agent-systems/notes.md) | References | 参考 | [以阅读笔记为准](../../references/articles/openhands-single-agent-systems/notes.md) |
| [Agent Skills specification](https://agentskills.io/specification) | References | 参考 | 未阅读 |
| [Multi-Agent Computer Use (MACU)](https://arxiv.org/abs/2606.01533) | References | 参考 | 未阅读 |
| [OpenHands automations: Fujitsu talk slides](https://github.com/neubig/slides/tree/main/slides/2026-09-25-fujitsu-openhands-en) | References | 参考 | 未阅读 |
| [Black Hat USA 2026: The OpenAI–Hugging Face incident](https://www.youtube.com/watch?v=87DyyMV0kCY) | References | 参考 | 未阅读 |
| [OpenAI: Hugging Face incident and the road ahead](https://openai.com/index/hugging-face-incident-and-the-road-ahead/) | References | 参考 | 未阅读 |

论文原文和阅读笔记统一维护在 `references/papers/<论文ID>-<简称>/`，通过本 README 的相对 Markdown 链接访问。来源、版本、获取日期和阅读状态在统一笔记中维护；课程特定思考写入本课 `notes.md`。维护方法见 [论文索引](../../references/README.md)。

## 代码实验

本课实验放在 `experiments/<实验名>/`，代码、配置、结果和最终模型随实验保存，运行方式与结论写入该实验的 `notes.md`。已有实验见 [实验索引](experiments.md)。跨课复用组件按需提取到 `../../src/agent_study/`；当前尚未建立课程实验。

## 学习目标

待学习时根据本课内容填写。

## 完成检查

- [ ] 能解释核心问题、方法与适用条件。
- [ ] 完成核心材料阅读记录。
- [ ] 完成最小实验或案例分析。
- [ ] 整理结论、局限与未解决问题。
