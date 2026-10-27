# 2b · Agent Capabilities 3: Skills and Memory

- 官方日期：2026 · Thu, Sep 3（沿用官网日期）
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
- [课件：Lecture 4 slides](https://www.cmu-agents.com/slides/lecture-04-memory-and-skills.pdf)
- [视频：Lecture 4 recording](https://www.youtube.com/watch?v=6zigF2a-2Pw&list=PLSN0qpDfUvTM&index=4)

## 论文与参考资料

来源：[官方课表](https://www.cmu-agents.com/#/schedule)，核对日期：2026-10-27。资料可能包含论文、技术文档、博客和代码仓库；阅读优先级是本项目的初始建议。

| 资料 | 官网分类 | 阅读优先级 | 状态 |
| --- | --- | --- | --- |
| [OpenHands: How to Create Effective Agent Skills](https://www.openhands.dev/blog/20260227-creating-effective-agent-skills) · [资料目录](../../references/articles/openhands-effective-agent-skills/) · [PDF](../../references/articles/openhands-effective-agent-skills/article.pdf) · [阅读笔记](../../references/articles/openhands-effective-agent-skills/notes.md) | Readings | 选读（待确定精读项） | [以阅读笔记为准](../../references/articles/openhands-effective-agent-skills/notes.md) |
| [SkillsBench](https://arxiv.org/abs/2602.12670) | Readings | 选读（待确定精读项） | 未阅读 |
| [MemGPT](https://arxiv.org/abs/2310.08560) · [论文目录](../../references/papers/2310.08560-memgpt/) · [PDF](../../references/papers/2310.08560-memgpt/paper.pdf) · [阅读笔记](../../references/papers/2310.08560-memgpt/notes.md) | Readings | 选读（待确定精读项） | [以阅读笔记为准](../../references/papers/2310.08560-memgpt/notes.md) |
| [Agent Workflow Memory (AWM)](https://arxiv.org/abs/2409.07429) | Readings | 选读（待确定精读项） | 未阅读 |
| [Agent Skill Induction (ASI)](https://arxiv.org/abs/2504.06821) | Readings | 选读（待确定精读项） | 未阅读 |
| [ReasoningBank](https://arxiv.org/abs/2509.25140) | Readings | 选读（待确定精读项） | 未阅读 |
| [Mem0](https://arxiv.org/abs/2504.19413) | References | 参考 | 未阅读 |
| [Reflexion](https://arxiv.org/abs/2303.11366) · [论文目录](../../references/papers/2303.11366-reflexion/) · [PDF](../../references/papers/2303.11366-reflexion/paper.pdf) · [阅读笔记](../../references/papers/2303.11366-reflexion/notes.md) | References | 参考 | [以阅读笔记为准](../../references/papers/2303.11366-reflexion/notes.md) |
| [ExpeL](https://arxiv.org/abs/2308.10144) | References | 参考 | 未阅读 |
| [Agent S](https://arxiv.org/abs/2410.08164) | References | 参考 | 未阅读 |
| [Synapse](https://arxiv.org/abs/2306.07863) | References | 参考 | 未阅读 |
| [ICAL](https://arxiv.org/abs/2406.14596) | References | 参考 | 未阅读 |
| [Voyager](https://arxiv.org/abs/2305.16291) | References | 参考 | 未阅读 |
| [DreamCoder](https://arxiv.org/abs/2006.08381) | References | 参考 | 未阅读 |
| [Stitch](https://arxiv.org/abs/2211.16605) | References | 参考 | 未阅读 |
| [LAPS](https://arxiv.org/abs/2106.11053) | References | 参考 | 未阅读 |
| [LILO](https://arxiv.org/abs/2310.19791) | References | 参考 | 未阅读 |
| [SkillWeaver](https://arxiv.org/abs/2504.07079) | References | 参考 | 未阅读 |
| [PolySkill](https://arxiv.org/abs/2510.15863) | References | 参考 | 未阅读 |
| [TroVE](https://arxiv.org/abs/2401.12869) | References | 参考 | 未阅读 |
| [Not All Skills Help](https://arxiv.org/abs/2606.15390) | References | 参考 | 未阅读 |
| [SAGE](https://aclanthology.org/2026.acl-long.69/) | References | 参考 | 未阅读 |
| [AgeMem](https://aclanthology.org/2026.acl-long.981/) | References | 参考 | 未阅读 |
| [HermesAgent: prompt_builder.py](https://github.com/NousResearch/hermes-agent/blob/main/agent/prompt_builder.py) | References | 参考 | 未阅读 |
| [HermesAgent: skills_tool.py](https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_tool.py) | References | 参考 | 未阅读 |

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
