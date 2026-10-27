# 4b · Training 1: Supervised Fine-Tuning (SFT)

- 官方日期：2026 · Thu, Sep 17（沿用官网日期）
- 课程分组：Training Methods
- 学习状态：未开始
- 资源核对日期：2026-10-27
- 讲者：[Yueqi Song](https://yueqis.github.io/)

## 学习入口

- [课程笔记](notes.md)
- [论文与参考资料](#论文与参考资料)
- [代码实验](#代码实验)
- [实验记录](experiments.md)
- [全部课程](../README.md)

## 官方资源

- [官方课表](https://www.cmu-agents.com/#/schedule)
- [课件：Lecture 8 slides](https://www.cmu-agents.com/slides/lecture-08-sft.pdf)
- [视频：Lecture 8 recording](https://www.youtube.com/watch?v=O3HSU0AoILc&list=PLSN0qpDfUvTM&index=8)

## 论文与参考资料

来源：[官方课表](https://www.cmu-agents.com/#/schedule)，核对日期：2026-10-27。资料可能包含论文、技术文档、博客和代码仓库；阅读优先级是本项目的初始建议。

| 资料 | 官网分类 | 阅读优先级 | 状态 |
| --- | --- | --- | --- |
| [Kimi K3](https://arxiv.org/abs/2607.24653) | References | 参考 | 未阅读 |
| [DeepSeek-R1](https://arxiv.org/abs/2501.12948) | References | 参考 | 未阅读 |
| [Nemotron 3 Ultra](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf) | References | 参考 | 未阅读 |
| [MAI-Thinking-1](https://microsoft.ai/pdf/mai-thinking-1.pdf) | References | 参考 | 未阅读 |
| [K2 Horizon model card](https://huggingface.co/IFM/K2-Horizon-375B-A23B) | References | 参考 | 未阅读 |
| [Kimi K2](https://arxiv.org/abs/2507.20534) | References | 参考 | 未阅读 |
| [OpenThoughts-Agent](https://arxiv.org/abs/2606.24855) | References | 参考 | 未阅读 |
| [SWE-Gym](https://arxiv.org/abs/2412.21139) | References | 参考 | 未阅读 |
| [Agent Data Protocol](https://arxiv.org/abs/2510.24702) | References | 参考 | 未阅读 |
| [BalanceSFT](https://arxiv.org/abs/2505.20192) | References | 参考 | 未阅读 |
| [Instruction Modelling](https://arxiv.org/abs/2405.14394) | References | 参考 | 未阅读 |
| [Weighted Instruction Tuning](https://arxiv.org/abs/2507.07817) | References | 参考 | 未阅读 |
| [DAgger](https://proceedings.mlr.press/v15/ross11a.html) | References | 参考 | 未阅读 |
| [Transformers: chat templates](https://huggingface.co/docs/transformers/en/chat_templating) | References | 参考 | 未阅读 |
| [Transformers: apply_chat_template](https://huggingface.co/docs/transformers/en/main_classes/tokenizer) | References | 参考 | 未阅读 |
| [TRL: SFTTrainer](https://huggingface.co/docs/trl/en/sft_trainer) | References | 参考 | 未阅读 |
| [TRL: training chat templates](https://huggingface.co/docs/trl/en/chat_templates) | References | 参考 | 未阅读 |
| [Axolotl: conversation datasets](https://docs.axolotl.ai/docs/dataset-formats/conversation.html) | References | 参考 | 未阅读 |
| [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) | References | 参考 | 未阅读 |

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
