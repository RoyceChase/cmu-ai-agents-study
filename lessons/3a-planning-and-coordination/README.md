# 3a · Agent Capabilities 4: Planning, Task Decomposition, and Multi-Agent Coordination

- 官方日期：2026 · Tue, Sep 8（沿用官网日期）
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
- [课件：Lecture 5 slides](https://www.cmu-agents.com/slides/lecture-05-planning.pdf)
- [视频：Lecture 5 recording](https://www.youtube.com/watch?v=S8v-dR4s29M&list=PLSN0qpDfUvTM&index=5)

## 论文与参考资料

来源：[官方课表](https://www.cmu-agents.com/#/schedule)，核对日期：2026-10-27。资料可能包含论文、技术文档、博客和代码仓库；阅读优先级是本项目的初始建议。

| 资料 | 官网分类 | 阅读优先级 | 状态 |
| --- | --- | --- | --- |
| [Cursor: Introducing Plan Mode](https://cursor.com/blog/plan-mode) | Readings | 选读（待确定精读项） | 未阅读 |
| [Least-to-Most Prompting](https://arxiv.org/abs/2205.10625) | Readings | 选读（待确定精读项） | 未阅读 |
| [Decomposed Prompting](https://arxiv.org/abs/2210.02406) | Readings | 选读（待确定精读项） | 未阅读 |
| [Code as Policies](https://arxiv.org/abs/2209.07753) | Readings | 选读（待确定精读项） | 未阅读 |
| [SayCan](https://arxiv.org/abs/2204.01691) | Readings | 选读（待确定精读项） | 未阅读 |
| [Plan-and-Act](https://arxiv.org/abs/2503.09572) | Readings | 选读（待确定精读项） | 未阅读 |
| [Thinking vs. Doing](https://arxiv.org/abs/2506.07976) | Readings | 选读（待确定精读项） | 未阅读 |
| [Calibrate-Then-Act](https://arxiv.org/abs/2602.16699) | Readings | 选读（待确定精读项） | 未阅读 |
| [Recursive Agent Optimization (RAO)](https://arxiv.org/abs/2605.06639) | Readings | 选读（待确定精读项） | 未阅读 |
| [Multi-Agent Computer Use (MACU)](https://arxiv.org/abs/2606.01533) | Readings | 选读（待确定精读项） | 未阅读 |
| [Claude Code Permission Modes](https://code.claude.com/docs/en/cli-usage) | References | 参考 | 未阅读 |
| [OpenAI Model Guidance](https://developers.openai.com/api/docs/guides/latest-model) | References | 参考 | 未阅读 |
| [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916) | References | 参考 | 未阅读 |
| [Plan-and-Solve Prompting](https://arxiv.org/abs/2305.04091) | References | 参考 | 未阅读 |
| [STaR](https://arxiv.org/abs/2203.14465) | References | 参考 | 未阅读 |
| [DeepSeek-R1](https://arxiv.org/abs/2501.12948) | References | 参考 | 未阅读 |
| [Recursive Language Models](https://arxiv.org/abs/2512.24601) | References | 参考 | 未阅读 |
| [PlanBench](https://arxiv.org/abs/2206.10498) | References | 参考 | 未阅读 |
| [ProgPrompt](https://arxiv.org/abs/2209.11302) | References | 参考 | 未阅读 |
| [Binder](https://arxiv.org/abs/2210.02875) | References | 参考 | 未阅读 |
| [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) | References | 参考 | 未阅读 |
| [UGround](https://arxiv.org/abs/2410.05243) | References | 参考 | 未阅读 |
| [Agent S](https://arxiv.org/abs/2410.08164) | References | 参考 | 未阅读 |
| [Language Models as Zero-Shot Planners](https://arxiv.org/abs/2201.07207) | References | 参考 | 未阅读 |
| [LLM-Planner](https://arxiv.org/abs/2212.04088) | References | 参考 | 未阅读 |
| [Inner Monologue](https://arxiv.org/abs/2207.05608) | References | 参考 | 未阅读 |
| [SwiftSage](https://arxiv.org/abs/2305.17390) | References | 参考 | 未阅读 |
| [The Danger of Overthinking](https://arxiv.org/abs/2502.08235) | References | 参考 | 未阅读 |
| [Training Proactive and Personalized LLM Agents (PPP-Agent)](https://arxiv.org/abs/2511.02208) | References | 参考 | 未阅读 |
| [Vending-Bench](https://arxiv.org/abs/2502.15840) | References | 参考 | 未阅读 |
| [The Illusion of Diminishing Returns](https://arxiv.org/abs/2509.09677) | References | 参考 | 未阅读 |
| [ADaPT](https://arxiv.org/abs/2311.05772) | References | 参考 | 未阅读 |
| [Web Agents Should Adopt the Plan-Then-Execute Paradigm](https://arxiv.org/abs/2605.14290) | References | 参考 | 未阅读 |
| [TravelPlanner](https://arxiv.org/abs/2402.01622) | References | 参考 | 未阅读 |
| [Odysseys](https://odysseys-website.pages.dev/) | References | 参考 | 未阅读 |
| [Don't Sleep on Single-Agent Systems](https://www.openhands.dev/blog/dont-sleep-on-single-agent-systems) | References | 参考 | 未阅读 |

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
