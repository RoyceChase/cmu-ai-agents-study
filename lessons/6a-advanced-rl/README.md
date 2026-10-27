# 6a · Training 3: Advanced RL Algorithms

- 官方日期：2026 · Tue, Sep 29（沿用官网日期）
- 课程分组：Training Methods
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
- [课件：Lecture 11 slides](https://www.cmu-agents.com/slides/lecture-11-rl-advanced.pdf)
- 视频：官网暂未提供，后续核对。

## 论文与参考资料

来源：[官方课表](https://www.cmu-agents.com/#/schedule)，核对日期：2026-10-27。资料可能包含论文、技术文档、博客和代码仓库；阅读优先级是本项目的初始建议。

| 资料 | 官网分类 | 阅读优先级 | 状态 |
| --- | --- | --- | --- |
| [MIXER](https://michaelauli.github.io/papers/iclr2016_mixer.pdf) | References | 参考 | 未阅读 |
| [InstructGPT](https://arxiv.org/abs/2203.02155) | References | 参考 | 未阅读 |
| [Generalized Advantage Estimation (GAE)](https://arxiv.org/abs/1506.02438) | References | 参考 | 未阅读 |
| [Let’s Verify Step by Step](https://arxiv.org/abs/2305.20050) | References | 参考 | 未阅读 |
| [AReaL](https://arxiv.org/abs/2505.24298) | References | 参考 | 未阅读 |
| [CTPO](https://arxiv.org/abs/2605.07331) | References | 参考 | 未阅读 |
| [Proximal Policy Optimization (PPO)](https://arxiv.org/abs/1707.06347) | References | 参考 | 未阅读 |
| [DeepSeekMath (GRPO)](https://arxiv.org/abs/2402.03300) | References | 参考 | 未阅读 |
| [MiniMax-M1 (CISPO)](https://arxiv.org/abs/2506.13585) | References | 参考 | 未阅读 |
| [Group Sequence Policy Optimization (GSPO)](https://arxiv.org/abs/2507.18071) | References | 参考 | 未阅读 |
| [DAPO](https://arxiv.org/abs/2503.14476) | References | 参考 | 未阅读 |
| [Introducing SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/) | References | 参考 | 未阅读 |
| [Why we no longer evaluate SWE-bench Verified](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) | References | 参考 | 未阅读 |
| [SABER (τ-bench audit)](https://arxiv.org/abs/2512.07850) | References | 参考 | 未阅读 |
| [τ-bench task fixes](https://taubench.com/blog/tau3-task-fixes.html) | References | 参考 | 未阅读 |
| [Reward Hacking in Reinforcement Learning](https://lilianweng.github.io/posts/2024-11-28-reward-hacking/) | References | 参考 | 未阅读 |
| [MAI-Thinking-1](https://microsoft.ai/pdf/mai-thinking-1.pdf) | References | 参考 | 未阅读 |
| [PostTrainBench](https://arxiv.org/abs/2603.08640) | References | 参考 | 未阅读 |
| [Curriculum Learning](https://doi.org/10.1145/1553374.1553380) | References | 参考 | 未阅读 |
| [OpenAI: calculator hacking and production evaluations](https://alignment.openai.com/prod-evals/) | References | 参考 | 未阅读 |
| [Where the goblins came from](https://openai.com/index/where-the-goblins-came-from/) | References | 参考 | 未阅读 |
| [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) | References | 参考 | 未阅读 |
| [On-Policy Distillation of Language Models (GKD)](https://arxiv.org/abs/2306.13649) | References | 参考 | 未阅读 |
| [Self-Distilled Reasoner (OPSD)](https://arxiv.org/abs/2601.18734) | References | 参考 | 未阅读 |
| [Policy Invariance Under Reward Transformations](https://people.eecs.berkeley.edu/~russell/papers/icml99-shaping.pdf) | References | 参考 | 未阅读 |

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
