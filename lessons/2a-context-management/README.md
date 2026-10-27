# 2a · Agent Capabilities 2: Context Management for Long-Context Agents

- 官方日期：2026 · Tue, Sep 1（沿用官网日期）
- 课程分组：Introduction and Agent Capabilities
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
- [课件：Lecture 3 slides](https://www.cmu-agents.com/slides/lecture-03-long-context.pdf)
- [视频：Lecture 3 recording](https://www.youtube.com/watch?v=AiwCCvFW1uE&list=PLSN0qpDfUvTM&index=3)

## 补充阅读（个人推荐）

- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) · [资料目录](../../references/articles/anthropic-effective-context-engineering/) · [PDF](../../references/articles/anthropic-effective-context-engineering/article.pdf) · [阅读笔记](../../references/articles/anthropic-effective-context-engineering/notes.md)

以上为个人补充材料，不属于官网列出的本课 Readings 或 References。阅读状态以对应笔记为准。

## 论文与参考资料

来源：[官方课表](https://www.cmu-agents.com/#/schedule)，核对日期：2026-10-27。资料可能包含论文、技术文档、博客和代码仓库；阅读优先级是本项目的初始建议。

| 资料 | 官网分类 | 阅读优先级 | 状态 |
| --- | --- | --- | --- |
| [DistServe](https://arxiv.org/abs/2401.09670) | References | 参考 | 未阅读 |
| [Needle in a Haystack](https://github.com/gkamradt/LLMTest_NeedleInAHaystack) | References | 参考 | 未阅读 |
| [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | References | 参考 | 未阅读 |
| [Longformer](https://arxiv.org/abs/2004.05150) | References | 参考 | 未阅读 |
| [Transformers are RNNs](https://arxiv.org/abs/2006.16236) | References | 参考 | 未阅读 |
| [Linear Transformers Are Secretly Fast Weight Programmers](https://arxiv.org/abs/2102.11174) | References | 参考 | 未阅读 |
| [Gated Delta Networks](https://arxiv.org/abs/2412.06464) | References | 参考 | 未阅读 |
| [Kimi Linear](https://arxiv.org/abs/2510.26692) | References | 参考 | 未阅读 |
| [DeepSeek Sparse Attention](https://arxiv.org/abs/2512.02556) | References | 参考 | 未阅读 |
| [Grouped-Query Attention](https://arxiv.org/abs/2305.13245) | References | 参考 | 未阅读 |
| [DeepSeek-V2](https://arxiv.org/abs/2405.04434) | References | 参考 | 未阅读 |
| [RoFormer](https://arxiv.org/abs/2104.09864) | References | 参考 | 未阅读 |
| [NoPE Length Generalization](https://arxiv.org/abs/2305.19466) | References | 参考 | 未阅读 |
| [Position Interpolation](https://arxiv.org/abs/2306.15595) | References | 参考 | 未阅读 |
| [YaRN](https://arxiv.org/abs/2309.00071) | References | 参考 | 未阅读 |
| [Qwen3.8-Flash-Next](https://qwen.ai/blog?id=qwen3.8-flash-next) | References | 参考 | 未阅读 |
| [GLM-5](https://arxiv.org/abs/2602.15763) | References | 参考 | 未阅读 |
| [GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash) | References | 参考 | 未阅读 |
| [Kimi K3](https://arxiv.org/abs/2607.24653) | References | 参考 | 未阅读 |
| [Nemotron 3 Ultra](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf) | References | 参考 | 未阅读 |
| [Inkling](https://thinkingmachines.ai/news/introducing-inkling/) | References | 参考 | 未阅读 |
| [DeepSeek V4](https://arxiv.org/abs/2606.19348) | References | 参考 | 未阅读 |
| [Ring Attention](https://arxiv.org/abs/2310.01889) | References | 参考 | 未阅读 |
| [Megatron Context Parallelism](https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/features/context_parallel.html) | References | 参考 | 未阅读 |
| [Prompt Cache](https://arxiv.org/abs/2311.04934) | References | 参考 | 未阅读 |
| [Can I Buy Your KV Cache?](https://arxiv.org/abs/2606.13361) | References | 参考 | 未阅读 |
| [DeepSeek API Pricing](https://api-docs.deepseek.com/quick_start/pricing/) | References | 参考 | 未阅读 |
| [Z.AI API Pricing](https://docs.z.ai/guides/overview/pricing) | References | 参考 | 未阅读 |
| [Kimi K3 Pricing](https://www.kimi.ai/resources/kimi-k3-pricing) | References | 参考 | 未阅读 |
| [OpenAI Model Pricing](https://developers.openai.com/api/docs/models/compare) | References | 参考 | 未阅读 |
| [Anthropic Prompt Caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) | References | 参考 | 未阅读 |
| [PagedAttention / vLLM](https://arxiv.org/abs/2309.06180) | References | 参考 | 未阅读 |
| [SGLang / RadixAttention](https://arxiv.org/abs/2312.07104) | References | 参考 | 未阅读 |
| [SGLang Cache-Aware Load Balancing](https://lmsys.org/blog/2024-12-04-sglang-v0-4/) | References | 参考 | 未阅读 |
| [MemGPT](https://arxiv.org/abs/2310.08560) · [论文目录](../../references/papers/2310.08560-memgpt/) · [PDF](../../references/papers/2310.08560-memgpt/paper.pdf) · [阅读笔记](../../references/papers/2310.08560-memgpt/notes.md) | References | 参考 | [以阅读笔记为准](../../references/papers/2310.08560-memgpt/notes.md) |
| [LongLLMLingua](https://aclanthology.org/2024.acl-long.91/) | References | 参考 | 未阅读 |
| [Codex](https://github.com/openai/codex) | References | 参考 | 未阅读 |
| [OpenCode](https://github.com/anomalyco/opencode) | References | 参考 | 未阅读 |
| [Pi](https://github.com/badlogic/pi-mono) | References | 参考 | 未阅读 |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | References | 参考 | 未阅读 |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | References | 参考 | 未阅读 |
| [ReSum](https://arxiv.org/abs/2509.13313) | References | 参考 | 未阅读 |

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
