# 课程论文清单与个人阅读建议

来源：[CMU AI Agents 官方课表](https://www.cmu-agents.com/#/schedule)，核对日期：2026-10-27。

面向四年 Java 开发经验、希望从事 Agent 应用开发的学习者。下面的阅读优先级是个人建议，不是课程教师的必读要求，也不代表已经读完或验证全部论文。

## 统计口径

- 官网的 Readings 与 References 均纳入，保留官网显示的简称及分类。
- 论文与技术报告合计 208 次引用，按来源 URL 去掉 arXiv 版本后去重为 191 个条目。这是链接统计，未逐一校验所有链接中的论文身份或是否有效；不等于经过文献学核验的 191 篇独立研究成果。
- 识别范围为 arXiv、ACL Anthology、PMLR、Nature、DOI 页面及明确的论文/技术报告 PDF。课程 RL Fundamentals 幻灯片不算论文。
- 产品博客、代码、模型卡、标准、排行榜、文档及其他网页另列。官网个别链接形式特殊（例如 SkillRefiner 的 alphaXiv 链接），列为待核对，不猜测论文 ID。
- 官网目前没有为部分后续课程列出阅读链接，不表示这些课程不需要阅读；后续以官网为准。

## 你最值得优先掌握的内容

| 顺序 | 材料 | 阅读时机与深度 |
| --- | --- | --- |
| 1 | [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)（工程文章） | 第一课后先看工作流与 Agent 的区别、简单组合模式；旧工具细节不作为当前接口依据。 |
| 2 | [ReAct](https://arxiv.org/abs/2210.03629) | 现在读摘要、方法和一个完整执行轨迹，能解释动作与反馈即可。 |
| 3 | [Toolformer](https://arxiv.org/abs/2302.04761) | 工具课后概览：理解通过训练学习使用工具；暂缓损失函数与复现。 |
| 4 | [CodeAct](https://arxiv.org/abs/2402.01030) | 跑通工具实验后看方法，比较结构化调用与代码执行。 |
| 5 | [MemGPT](https://arxiv.org/abs/2310.08560) | 上下文与记忆课后看架构、读写过程和案例。 |
| 6 | [Reflexion](https://arxiv.org/abs/2303.11366) | 有失败案例后看反思与记忆机制，判断是否改善后续尝试。 |
| 7 | [SWE-bench](https://arxiv.org/abs/2310.06770) / [Agentless](https://arxiv.org/abs/2407.01489) | 代码 Agent 或评估课阶段，先理解任务、评估和简单基线，再读实验结果。 |
| 8 | [AgentDojo](https://arxiv.org/abs/2406.13352) | 接入外部网页/文件等不可信内容时读威胁模型与攻击案例。 |

必要的是掌握执行循环、工具接口、上下文/记忆、评估和安全边界，并用代码或案例解释。上述论文是建立理解的材料，不要求每篇从头精读或复现。研究型论文阅读与应用开发能力不能直接画等号。

近期只安排 ReAct 方法与轨迹、Toolformer 思路，不把全部清单变成待办。开始阶段不必下载所有原文。

## 可以后置的内容

- PPO、GAE、GRPO、DAPO、GSPO 等训练算法与数学推导：做 Training 作业或确定训练方向时再深入。
- RoPE、YaRN、Ring Attention、线性/稀疏注意力、模型技术报告：应用开发先理解上下文窗口、token、缓存与延迟，底层实现按需学习。
- 大量机器人规划、程序合成、GUI 专项、领域研究助手和多 Agent 优化论文：选择相应项目方向再精读。
- 任何论文中的历史榜单与分数只代表相应实验条件，不作为当前模型优劣判断。

## 官网论文与技术报告完整清单

“优先理解”指方法/任务和关键案例应理解；“择要阅读”指摘要、方法图、重要结论；“按需查阅”指先随课理解主题。Readings 不自动等同于全部精读，References 也不一定优先级低。


### 1a · Course Overview: What Is an Agent?

| 官网资料名与链接 | 官网分类 | 个人优先级 | 建议 |
| --- | --- | --- | --- |
| [Toolformer](https://arxiv.org/abs/2302.04761) | Readings | 择要阅读 | 先看问题、方法图与训练数据筛选思路，模型训练细节后读。 |
| [ReAct](https://arxiv.org/abs/2210.03629) | Readings | 优先理解 | 结合执行轨迹理解思考、动作、观察的循环。 |

### 1b · Agent Capabilities 1: Tool Use

| 官网资料名与链接 | 官网分类 | 个人优先级 | 建议 |
| --- | --- | --- | --- |
| [What Are Tools Anyway?](https://arxiv.org/abs/2403.15452) | Readings | 择要阅读 | 浏览定义与分类，帮助建立工具使用的知识地图。 |
| [CodeAct](https://arxiv.org/abs/2402.01030) | Readings | 优先理解 | 理解结构化工具调用与执行代码两种动作表示，以及执行反馈。 |
| [Toolformer](https://arxiv.org/abs/2302.04761) | Readings | 择要阅读 | 先看问题、方法图与训练数据筛选思路，模型训练细节后读。 |
| [XGrammar](https://arxiv.org/abs/2411.15100) | Readings | 择要阅读 | 了解结构化生成与格式约束，解码实现按需深入。 |

### 2a · Agent Capabilities 2: Context Management for Long-Context Agents

| 官网资料名与链接 | 官网分类 | 个人优先级 | 建议 |
| --- | --- | --- | --- |
| [DistServe](https://arxiv.org/abs/2401.09670) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | References | 择要阅读 | 先理解 token、注意力和上下文的基本关系，不急着推导。 |
| [Longformer](https://arxiv.org/abs/2004.05150) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Transformers are RNNs](https://arxiv.org/abs/2006.16236) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Linear Transformers Are Secretly Fast Weight Programmers](https://arxiv.org/abs/2102.11174) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Gated Delta Networks](https://arxiv.org/abs/2412.06464) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Kimi Linear](https://arxiv.org/abs/2510.26692) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [DeepSeek Sparse Attention](https://arxiv.org/abs/2512.02556) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Grouped-Query Attention](https://arxiv.org/abs/2305.13245) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [DeepSeek-V2](https://arxiv.org/abs/2405.04434) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [RoFormer](https://arxiv.org/abs/2104.09864) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [NoPE Length Generalization](https://arxiv.org/abs/2305.19466) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Position Interpolation](https://arxiv.org/abs/2306.15595) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [YaRN](https://arxiv.org/abs/2309.00071) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [GLM-5](https://arxiv.org/abs/2602.15763) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Kimi K3](https://arxiv.org/abs/2607.24653) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Nemotron 3 Ultra](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [DeepSeek V4](https://arxiv.org/abs/2606.19348) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Ring Attention](https://arxiv.org/abs/2310.01889) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Prompt Cache](https://arxiv.org/abs/2311.04934) | References | 择要阅读 | 了解前缀复用如何影响成本与延迟。 |
| [Can I Buy Your KV Cache?](https://arxiv.org/abs/2606.13361) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [PagedAttention / vLLM](https://arxiv.org/abs/2309.06180) | References | 择要阅读 | 有模型部署需求时了解 KV cache 与推理资源。 |
| [SGLang / RadixAttention](https://arxiv.org/abs/2312.07104) | References | 择要阅读 | 有推理服务需求时了解缓存复用与服务执行。 |
| [MemGPT](https://arxiv.org/abs/2310.08560) | References | 优先理解 | 理解有限上下文、分层记忆与信息读写。 |
| [LongLLMLingua](https://aclanthology.org/2024.acl-long.91/) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [ReSum](https://arxiv.org/abs/2509.13313) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |

### 2b · Agent Capabilities 3: Skills and Memory

| 官网资料名与链接 | 官网分类 | 个人优先级 | 建议 |
| --- | --- | --- | --- |
| [SkillsBench](https://arxiv.org/abs/2602.12670) | Readings | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [MemGPT](https://arxiv.org/abs/2310.08560) | Readings | 优先理解 | 理解有限上下文、分层记忆与信息读写。 |
| [Agent Workflow Memory (AWM)](https://arxiv.org/abs/2409.07429) | Readings | 择要阅读 | 了解如何复用任务流程经验。 |
| [Agent Skill Induction (ASI)](https://arxiv.org/abs/2504.06821) | Readings | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [ReasoningBank](https://arxiv.org/abs/2509.25140) | Readings | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Mem0](https://arxiv.org/abs/2504.19413) | References | 择要阅读 | 了解持久记忆的提取与管理。 |
| [Reflexion](https://arxiv.org/abs/2303.11366) | References | 择要阅读 | 看反馈、反思和记忆如何影响后续尝试；不等同于更新模型权重。 |
| [ExpeL](https://arxiv.org/abs/2308.10144) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Agent S](https://arxiv.org/abs/2410.08164) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Synapse](https://arxiv.org/abs/2306.07863) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [ICAL](https://arxiv.org/abs/2406.14596) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Voyager](https://arxiv.org/abs/2305.16291) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [DreamCoder](https://arxiv.org/abs/2006.08381) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Stitch](https://arxiv.org/abs/2211.16605) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [LAPS](https://arxiv.org/abs/2106.11053) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [LILO](https://arxiv.org/abs/2310.19791) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [SkillWeaver](https://arxiv.org/abs/2504.07079) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [PolySkill](https://arxiv.org/abs/2510.15863) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [TroVE](https://arxiv.org/abs/2401.12869) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Not All Skills Help](https://arxiv.org/abs/2606.15390) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [SAGE](https://aclanthology.org/2026.acl-long.69/) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [AgeMem](https://aclanthology.org/2026.acl-long.981/) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |

### 3a · Agent Capabilities 4: Planning, Task Decomposition, and Multi-Agent Coordination

| 官网资料名与链接 | 官网分类 | 个人优先级 | 建议 |
| --- | --- | --- | --- |
| [Least-to-Most Prompting](https://arxiv.org/abs/2205.10625) | Readings | 择要阅读 | 了解任务分解，结合小任务比较是否有收益。 |
| [Decomposed Prompting](https://arxiv.org/abs/2210.02406) | Readings | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Code as Policies](https://arxiv.org/abs/2209.07753) | Readings | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [SayCan](https://arxiv.org/abs/2204.01691) | Readings | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Plan-and-Act](https://arxiv.org/abs/2503.09572) | Readings | 择要阅读 | 阅读规划与执行如何分工。 |
| [Thinking vs. Doing](https://arxiv.org/abs/2506.07976) | Readings | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Calibrate-Then-Act](https://arxiv.org/abs/2602.16699) | Readings | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Recursive Agent Optimization (RAO)](https://arxiv.org/abs/2605.06639) | Readings | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Multi-Agent Computer Use (MACU)](https://arxiv.org/abs/2606.01533) | Readings | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Plan-and-Solve Prompting](https://arxiv.org/abs/2305.04091) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [STaR](https://arxiv.org/abs/2203.14465) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [DeepSeek-R1](https://arxiv.org/abs/2501.12948) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Recursive Language Models](https://arxiv.org/abs/2512.24601) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [PlanBench](https://arxiv.org/abs/2206.10498) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [ProgPrompt](https://arxiv.org/abs/2209.11302) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Binder](https://arxiv.org/abs/2210.02875) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [UGround](https://arxiv.org/abs/2410.05243) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Agent S](https://arxiv.org/abs/2410.08164) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Language Models as Zero-Shot Planners](https://arxiv.org/abs/2201.07207) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [LLM-Planner](https://arxiv.org/abs/2212.04088) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Inner Monologue](https://arxiv.org/abs/2207.05608) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [SwiftSage](https://arxiv.org/abs/2305.17390) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [The Danger of Overthinking](https://arxiv.org/abs/2502.08235) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Training Proactive and Personalized LLM Agents (PPP-Agent)](https://arxiv.org/abs/2511.02208) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Vending-Bench](https://arxiv.org/abs/2502.15840) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [The Illusion of Diminishing Returns](https://arxiv.org/abs/2509.09677) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [ADaPT](https://arxiv.org/abs/2311.05772) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Web Agents Should Adopt the Plan-Then-Execute Paradigm](https://arxiv.org/abs/2605.14290) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [TravelPlanner](https://arxiv.org/abs/2402.01622) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |

### 3b · Domains 1: Coding Agents

| 官网资料名与链接 | 官网分类 | 个人优先级 | 建议 |
| --- | --- | --- | --- |
| [OLMo](https://arxiv.org/abs/2402.00838) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [StarCoder](https://arxiv.org/abs/2305.06161) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Whitespace-run tokens](https://arxiv.org/abs/2107.03374) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Code Llama](https://arxiv.org/abs/2308.12950) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Qwen2.5-Coder](https://arxiv.org/abs/2409.12186) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [InCoder](https://arxiv.org/abs/2204.05999) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Scaling study](https://arxiv.org/abs/2207.14255) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [OctoPack](https://arxiv.org/abs/2308.07124) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [DrRepair](https://proceedings.mlr.press/v119/yasunaga20a.html) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [CodeRL](https://arxiv.org/abs/2207.01780) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [CodeExecutor](https://aclanthology.org/2023.findings-acl.308/) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Grammar-based code generation](https://aclanthology.org/P17-1041/) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [CodeBLEU](https://arxiv.org/abs/2009.10297) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [CodeBERTScore](https://aclanthology.org/2023.emnlp-main.859/) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [EvalPlus](https://arxiv.org/abs/2305.01210) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [CodeContests / AlphaCode](https://arxiv.org/abs/2203.07814) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [NoFunEval](https://arxiv.org/abs/2401.15963) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [SWE-agent](https://arxiv.org/abs/2405.15793) | References | 择要阅读 | 做代码 Agent 时看环境接口与执行流程。 |
| [Agentless](https://arxiv.org/abs/2407.01489) | References | 择要阅读 | 重点理解定位、修复、验证的简化流程，与自主循环比较。 |
| [LocAgent](https://arxiv.org/abs/2503.09089) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [SWE-bench](https://arxiv.org/abs/2310.06770) | References | 优先理解 | 重点看任务定义、测试与评估局限；原论文分数不代表当前能力。 |
| [SWE-Gym](https://arxiv.org/abs/2412.21139) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [R2E-Gym](https://arxiv.org/abs/2504.07164) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [SWE-smith](https://arxiv.org/abs/2504.21798) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Multi-SWE-bench](https://arxiv.org/abs/2504.02605) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [SWE-bench Multimodal](https://arxiv.org/abs/2410.03859) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [VisualWebArena](https://arxiv.org/abs/2401.13649) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Commit0](https://arxiv.org/abs/2412.01769) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [ProgramBench](https://arxiv.org/abs/2605.03546) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [SWE-Milestone](https://arxiv.org/abs/2603.13428) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [SWT-Bench](https://arxiv.org/abs/2406.12952) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [SWE-Playground](https://arxiv.org/abs/2512.12216) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Hybrid-Gym](https://arxiv.org/abs/2602.16819) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Code World Models](https://arxiv.org/abs/2405.15383) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |

### 4a · Computer Use Agents

| 官网资料名与链接 | 官网分类 | 个人优先级 | 建议 |
| --- | --- | --- | --- |
| [WebArena](https://arxiv.org/abs/2307.13854) | Readings | 择要阅读 | 了解 Web 任务环境与成功条件。 |
| [VisualWebArena](https://arxiv.org/abs/2401.13649) | Readings | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [OSWorld](https://arxiv.org/abs/2404.07972) | Readings | 择要阅读 | 了解桌面任务如何评估。 |
| [OpenCUA](https://arxiv.org/abs/2508.09123) | Readings | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [CUA-Gym](https://arxiv.org/abs/2605.25624) | Readings | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Multi-Agent Computer Use (MACU)](https://arxiv.org/abs/2606.01533) | Readings | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [MiniWoB](https://arxiv.org/abs/1704.04368) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [WebShop](https://arxiv.org/abs/2207.01206) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [ReAct](https://arxiv.org/abs/2210.03629) | References | 优先理解 | 结合执行轨迹理解思考、动作、观察的循环。 |
| [Mind2Web](https://arxiv.org/abs/2306.06070) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [WebVoyager](https://arxiv.org/abs/2401.13919) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [ScreenSpot-Pro](https://arxiv.org/abs/2504.07981) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Gym-Anything](https://arxiv.org/abs/2604.06126) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [MolmoWeb](https://arxiv.org/abs/2604.08516) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |

### 4b · Training 1: Supervised Fine-Tuning (SFT)

| 官网资料名与链接 | 官网分类 | 个人优先级 | 建议 |
| --- | --- | --- | --- |
| [Kimi K3](https://arxiv.org/abs/2607.24653) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [DeepSeek-R1](https://arxiv.org/abs/2501.12948) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Nemotron 3 Ultra](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [MAI-Thinking-1](https://microsoft.ai/pdf/mai-thinking-1.pdf) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Kimi K2](https://arxiv.org/abs/2507.20534) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [OpenThoughts-Agent](https://arxiv.org/abs/2606.24855) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [SWE-Gym](https://arxiv.org/abs/2412.21139) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Agent Data Protocol](https://arxiv.org/abs/2510.24702) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [BalanceSFT](https://arxiv.org/abs/2505.20192) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Instruction Modelling](https://arxiv.org/abs/2405.14394) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Weighted Instruction Tuning](https://arxiv.org/abs/2507.07817) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [DAgger](https://proceedings.mlr.press/v15/ross11a.html) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |

### 5a · Training 2: Reinforcement Learning Basics

| 官网资料名与链接 | 官网分类 | 个人优先级 | 建议 |
| --- | --- | --- | --- |
| [ReST](https://arxiv.org/abs/2308.08998) | Readings | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [ReST-EM](https://arxiv.org/abs/2312.06585) | Readings | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [DeepSeekMath](https://arxiv.org/abs/2402.03300) | Readings | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [DrGRPO](https://arxiv.org/abs/2503.20783) | Readings | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [REINFORCE](https://doi.org/10.1007/BF00992696) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |

### 5b · Domains 3: Deep Research Agents

| 官网资料名与链接 | 官网分类 | 个人优先级 | 建议 |
| --- | --- | --- | --- |
| [OpenScholar](https://www.nature.com/articles/s41586-025-10072-4) | Readings | 择要阅读 | 做研究助手时了解检索、证据与引用。 |
| [BrowseComp](https://arxiv.org/abs/2504.12516) | Readings | 择要阅读 | 了解搜索任务的难点和评估方法。 |
| [DeepResearch Bench](https://arxiv.org/abs/2506.11763) | Readings | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Tongyi DeepResearch](https://arxiv.org/abs/2510.24701) | Readings | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [DR Tulu](https://arxiv.org/abs/2511.19399) | Readings | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [AgentIR](https://arxiv.org/abs/2603.04384) | Readings | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [BrowseComp-Plus](https://arxiv.org/abs/2508.06600) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [FinSearchComp](https://arxiv.org/abs/2509.13160) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [MedBrowseComp](https://arxiv.org/abs/2505.14963) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [ScholarSearch](https://arxiv.org/abs/2506.13784) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [AutoResearchBench](https://arxiv.org/abs/2604.25256) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [A Critical Evaluation of Evaluations for Long-form Question Answering](https://aclanthology.org/2023.acl-long.181/) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [ResearchQA](https://arxiv.org/abs/2509.00496) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [DeepResearch Bench II](https://arxiv.org/abs/2601.08536) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [WebSailor-V2](https://arxiv.org/abs/2509.13305) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [WebDancer](https://arxiv.org/abs/2505.22648) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Scaling Agents via Continual Pre-training](https://arxiv.org/abs/2509.13310) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Search-R1](https://arxiv.org/abs/2503.09516) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [DeepSeekMath](https://arxiv.org/abs/2402.03300) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Dense Passage Retrieval](https://aclanthology.org/2020.emnlp-main.550/) | References | 择要阅读 | 做知识检索时了解召回与检索训练。 |

### 6a · Training 3: Advanced RL Algorithms

| 官网资料名与链接 | 官网分类 | 个人优先级 | 建议 |
| --- | --- | --- | --- |
| [MIXER](https://michaelauli.github.io/papers/iclr2016_mixer.pdf) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [InstructGPT](https://arxiv.org/abs/2203.02155) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Generalized Advantage Estimation (GAE)](https://arxiv.org/abs/1506.02438) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Let’s Verify Step by Step](https://arxiv.org/abs/2305.20050) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [AReaL](https://arxiv.org/abs/2505.24298) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [CTPO](https://arxiv.org/abs/2605.07331) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Proximal Policy Optimization (PPO)](https://arxiv.org/abs/1707.06347) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [DeepSeekMath (GRPO)](https://arxiv.org/abs/2402.03300) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [MiniMax-M1 (CISPO)](https://arxiv.org/abs/2506.13585) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Group Sequence Policy Optimization (GSPO)](https://arxiv.org/abs/2507.18071) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [DAPO](https://arxiv.org/abs/2503.14476) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [SABER (τ-bench audit)](https://arxiv.org/abs/2512.07850) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [MAI-Thinking-1](https://microsoft.ai/pdf/mai-thinking-1.pdf) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [PostTrainBench](https://arxiv.org/abs/2603.08640) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Curriculum Learning](https://doi.org/10.1145/1553374.1553380) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [On-Policy Distillation of Language Models (GKD)](https://arxiv.org/abs/2306.13649) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Self-Distilled Reasoner (OPSD)](https://arxiv.org/abs/2601.18734) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Policy Invariance Under Reward Transformations](https://people.eecs.berkeley.edu/~russell/papers/icml99-shaping.pdf) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |

### 7a · Safety 1: Agent Safety

| 官网资料名与链接 | 官网分类 | 个人优先级 | 建议 |
| --- | --- | --- | --- |
| [AgentDojo](https://arxiv.org/abs/2406.13352v3) | References | 优先理解 | 理解工具返回的不可信内容、提示注入与任务成功/安全的分别评估。 |
| [ToolEmu](https://arxiv.org/abs/2309.15817v2) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Security Challenges in AI Agent Deployment: Insights from a Large Scale Public Competition](https://arxiv.org/abs/2507.20526) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Jailbreaking Black Box Large Language Models in Twenty Queries (PAIR)](https://arxiv.org/abs/2310.08419) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Nemotron 3 Super technical report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [AI Control: Improving Safety Despite Intentional Subversion](https://arxiv.org/abs/2312.06942v5) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation](https://arxiv.org/abs/2503.11926) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [AgentHarm](https://arxiv.org/abs/2410.09024) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [OpenAgentSafety](https://arxiv.org/abs/2507.06134v2) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Monitoring Monitorability](https://arxiv.org/abs/2512.18311) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |

### 7b · Frameworks 1: OpenHands

| 官网资料名与链接 | 官网分类 | 个人优先级 | 建议 |
| --- | --- | --- | --- |
| [OpenHands Software Agent SDK report](https://arxiv.org/abs/2511.03690v1) | References | 择要阅读 | 结合 SDK 代码看架构，避免只记框架名。 |
| [HumanEval](https://arxiv.org/abs/2107.03374) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [SWE-bench](https://arxiv.org/abs/2310.06770v1) | References | 优先理解 | 重点看任务定义、测试与评估局限；原论文分数不代表当前能力。 |
| [SWE-agent](https://arxiv.org/abs/2405.15793) | References | 择要阅读 | 做代码 Agent 时看环境接口与执行流程。 |
| [CodeR](https://arxiv.org/abs/2406.01304) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [MetaGPT](https://arxiv.org/abs/2308.00352) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [OpenHands-Versa](https://arxiv.org/abs/2506.03011v1) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Code with Me or for Me?](https://arxiv.org/abs/2507.08149v1) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |

### 9a · Frameworks 2: Orchestration and Monitoring

| 官网资料名与链接 | 官网分类 | 个人优先级 | 建议 |
| --- | --- | --- | --- |
| [Hodoscope: Unsupervised Monitoring for AI Misbehaviors](https://arxiv.org/abs/2604.11072) | Readings | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |
| [Multi-Agent Computer Use (MACU)](https://arxiv.org/abs/2606.01533) | References | 按需查阅 | 先随课理解主题；项目、作业或研究遇到具体问题再读。 |

## 官网其他资料（不计入上述论文统计）

保留完整链接，方便查资料；以下分类不代表已经逐页核验。接口与框架文档在实现时读，比提前精读全部论文更直接。

### 1a · Course Overview: What Is an Agent?

- [Mini-SWE-Agent](https://github.com/swe-agent/mini-swe-agent) · Readings

### 1b · Agent Capabilities 1: Tool Use

- [OpenAI Chat Completions API](https://platform.openai.com/docs/api-reference/chat/create) · References
- [Hugging Face Chat Templates](https://huggingface.co/docs/transformers/chat_templating) · References
- [Qwen2.5 Chat Template](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/blob/main/tokenizer_config.json) · References
- [Berkeley Function-Calling Leaderboard V4](https://gorilla.cs.berkeley.edu/leaderboard.html) · References
- [BFCL V4 Methodology](https://gorilla.cs.berkeley.edu/blogs/15_bfcl_v4_web_search.html) · References
- [OpenRouter Provider Analytics](https://openrouter.ai/) · References
- [OpenAI Function Calling Guide](https://developers.openai.com/api/docs/guides/function-calling) · References
- [Qwen3.8 Tool-Call Template](https://huggingface.co/Qwen/Qwen3.8-27B/blob/main/tokenizer_config.json) · References
- [Mistral Small 4 Model Card](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603) · References
- [Mistral Tool-Call Tokenization Guide](https://github.com/mistralai/cookbook/blob/main/concept-deep-dive/tokenization/tool_calling.md) · References
- [DeepSeek V3.2 Tool-Call Encoding](https://huggingface.co/deepseek-ai/DeepSeek-V3.2/blob/main/encoding/encoding_dsv32.py) · References
- [OpenHands Tool System Architecture](https://docs.openhands.dev/sdk/arch/tool-system) · References
- [OpenHands Agent Dispatch Source](https://github.com/OpenHands/software-agent-sdk/blob/main/openhands-sdk/openhands/sdk/agent/agent.py) · References
- [OpenHands ToolDefinition Source](https://github.com/OpenHands/software-agent-sdk/blob/main/openhands-sdk/openhands/sdk/tool/tool.py) · References
- [JSON Schema 2020-12](https://json-schema.org/draft/2020-12/json-schema-core.html) · References
- [JSON Schema 2020-12 Validation](https://json-schema.org/draft/2020-12/json-schema-validation.html) · References
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) · References
- [FastAPI Generated OpenAPI](https://fastapi.tiangolo.com/tutorial/first-steps/#openapi) · References
- [FastAPI Security and OpenAPI](https://fastapi.tiangolo.com/tutorial/security/) · References
- [MCP 2026-07-28 Specification Release](https://blog.modelcontextprotocol.io/posts/2026-07-28/) · References
- [MCP TypeScript SDK v2 Overview](https://ts.sdk.modelcontextprotocol.io/v2/) · References
- [MCP Transports Specification](https://modelcontextprotocol.io/specification/draft/basic/transports) · References
- [MCP Tools Specification](https://modelcontextprotocol.io/specification/draft/server/tools) · References
- [FastMCP OpenAPI Integration](https://gofastmcp.com/integrations/openapi) · References
- [FastMCP Token Verification](https://gofastmcp.com/servers/auth/token-verification) · References
- [FastMCP Bearer Client Authentication](https://gofastmcp.com/clients/auth/bearer) · References

### 2a · Agent Capabilities 2: Context Management for Long-Context Agents

- [Needle in a Haystack](https://github.com/gkamradt/LLMTest_NeedleInAHaystack) · References
- [Qwen3.8-Flash-Next](https://qwen.ai/blog?id=qwen3.8-flash-next) · References
- [GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash) · References
- [Inkling](https://thinkingmachines.ai/news/introducing-inkling/) · References
- [Megatron Context Parallelism](https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/features/context_parallel.html) · References
- [DeepSeek API Pricing](https://api-docs.deepseek.com/quick_start/pricing/) · References
- [Z.AI API Pricing](https://docs.z.ai/guides/overview/pricing) · References
- [Kimi K3 Pricing](https://www.kimi.ai/resources/kimi-k3-pricing) · References
- [OpenAI Model Pricing](https://developers.openai.com/api/docs/models/compare) · References
- [Anthropic Prompt Caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) · References
- [SGLang Cache-Aware Load Balancing](https://lmsys.org/blog/2024-12-04-sglang-v0-4/) · References
- [Codex](https://github.com/openai/codex) · References
- [OpenCode](https://github.com/anomalyco/opencode) · References
- [Pi](https://github.com/badlogic/pi-mono) · References
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) · References
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) · References

### 2b · Agent Capabilities 3: Skills and Memory

- [OpenHands: How to Create Effective Agent Skills](https://www.openhands.dev/blog/20260227-creating-effective-agent-skills) · Readings
- [HermesAgent: prompt_builder.py](https://github.com/NousResearch/hermes-agent/blob/main/agent/prompt_builder.py) · References
- [HermesAgent: skills_tool.py](https://github.com/NousResearch/hermes-agent/blob/main/tools/skills_tool.py) · References

### 3a · Agent Capabilities 4: Planning, Task Decomposition, and Multi-Agent Coordination

- [Cursor: Introducing Plan Mode](https://cursor.com/blog/plan-mode) · Readings
- [Claude Code Permission Modes](https://code.claude.com/docs/en/cli-usage) · References
- [OpenAI Model Guidance](https://developers.openai.com/api/docs/guides/latest-model) · References
- [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) · References
- [Odysseys](https://odysseys-website.pages.dev/) · References
- [Don't Sleep on Single-Agent Systems](https://www.openhands.dev/blog/dont-sleep-on-single-agent-systems) · References

### 3b · Domains 1: Coding Agents

- [StarCoder2 tokenizer](https://huggingface.co/bigcode/starcoder2-3b/blob/main/tokenizer.json) · References
- [DeepCoder](https://www.together.ai/blog/deepcoder) · References
- [mini-SWE-agent](https://mini-swe-agent.com/latest/) · References
- [Aider edit formats](https://aider.chat/docs/more/edit-formats.html) · References
- [Aider unified diffs](https://aider.chat/docs/unified-diffs.html) · References
- [SWE-bench Multilingual](https://www.swebench.com/multilingual.html) · References
- [Playwright locators](https://playwright.dev/docs/locators) · References

### 4b · Training 1: Supervised Fine-Tuning (SFT)

- [K2 Horizon model card](https://huggingface.co/IFM/K2-Horizon-375B-A23B) · References
- [Transformers: chat templates](https://huggingface.co/docs/transformers/en/chat_templating) · References
- [Transformers: apply_chat_template](https://huggingface.co/docs/transformers/en/main_classes/tokenizer) · References
- [TRL: SFTTrainer](https://huggingface.co/docs/trl/en/sft_trainer) · References
- [TRL: training chat templates](https://huggingface.co/docs/trl/en/chat_templates) · References
- [Axolotl: conversation datasets](https://docs.axolotl.ai/docs/dataset-formats/conversation.html) · References
- [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) · References

### 5a · Training 2: Reinforcement Learning Basics

- [RL Fundamentals](https://cmu-l3.github.io/anlp-spring2026/static_files/anlp-s2026-16-rl.pdf) · References

### 5b · Domains 3: Deep Research Agents

- [Natural Questions example](https://ai.google.com/research/NaturalQuestions/databrowser) · References
- [Wikipedia source document](https://en.wikipedia.org/w/index.php?oldid=824425456) · References
- [CMU Archives: Herbert Simon](https://digitalcollections.library.cmu.edu/cmu-collection/herbert-simon) · References
- [1978 Nobel Prize in Economic Sciences](https://www.nobelprize.org/prizes/economic-sciences/1978/summary/) · References

### 6a · Training 3: Advanced RL Algorithms

- [Introducing SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/) · References
- [Why we no longer evaluate SWE-bench Verified](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) · References
- [τ-bench task fixes](https://taubench.com/blog/tau3-task-fixes.html) · References
- [Reward Hacking in Reinforcement Learning](https://lilianweng.github.io/posts/2024-11-28-reward-hacking/) · References
- [OpenAI: calculator hacking and production evaluations](https://alignment.openai.com/prod-evals/) · References
- [Where the goblins came from](https://openai.com/index/where-the-goblins-came-from/) · References

### 7a · Safety 1: Agent Safety

- [OpenClaw incident report](https://x.com/summeryue0/status/2025774069124399363) · References
- [PocketOS database-deletion incident](https://thenewstack.io/ai-agents-credential-crisis) · References
- [Microsoft advisory: CVE-2025-32711](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32711) · References
- [Cline supply-chain compromise postmortem](https://cline.bot/blog/post-mortem-unauthorized-cline-cli-npm) · References
- [Gambit Security: AI agents targeting online retailers](https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company) · References
- [Introducing Docent](https://transluce.org/docent/blog/introducing-docent) · References
- [Gray Swan Arena: Agent Red-Teaming Challenge](https://app.grayswan.ai/arena/challenge/agent-red-teaming/leaderboard) · References
- [Docker Engine security](https://docs.docker.com/engine/security/) · References
- [Modal sandbox networking and security](https://modal.com/docs/guide/sandbox-networking) · References
- [OpenShell architecture (pinned revision)](https://github.com/NVIDIA/OpenShell/blob/ec49209da25be39840742df29b64ec694d159c2f/docs/about/architecture.mdx) · References
- [Modal sandboxes](https://modal.com/docs/guide/sandboxes) · References
- [E2B sandbox persistence](https://docs.e2b.dev/sandbox/persistence) · References
- [Apptainer quick start](https://apptainer.org/docs/user/main/quick_start.html) · References
- [QEMU system emulation](https://www.qemu.org/docs/master/system/introduction.html) · References
- [E2B sandbox lifecycle](https://docs.e2b.dev/sandbox) · References
- [GitHub personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) · References
- [RFC 8693: OAuth 2.0 Token Exchange](https://www.rfc-editor.org/rfc/rfc8693.html) · References
- [GitHub App installation access tokens](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-an-installation-access-token-for-a-github-app) · References
- [OpenTelemetry generative AI attributes](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/) · References
- [Docent](https://transluce.org/docent) · References

### 7b · Frameworks 1: OpenHands

- [OpenHands SDK source and examples](https://github.com/OpenHands/software-agent-sdk/tree/69e26889401fe69157fff536e6a69049e6644cb3) · References
- [OpenHands](https://github.com/OpenHands/OpenHands) · References
- [Devin launch demo](https://www.youtube.com/watch?v=fjHtjT7GO1c) · References
- [OpenDevin: original callout](https://x.com/JustinLin610/status/1767769034186211557) · References
- [OpenDevin: early frontend demo](https://x.com/gneubig/status/1772735837479792761) · References
- [OpenDevin CodeAct 1.0](https://xwang.dev/blog/2024/opendevin-codeact-1.0-swebench/) · References
- [Don't Sleep on Single-agent Systems](https://hub.openhands.dev/blog/dont-sleep-on-single-agent-systems) · References
- [VS Code with Copilot: agent quickstart](https://code.visualstudio.com/docs/agents/quickstart) · References
- [Claude Code terminal demo](https://github.com/anthropics/claude-code/blob/71cdddec623889d38af14b7a489670a03186f659/demo.gif) · References
- [GitHub Copilot coding agent](https://github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent/) · References
- [OpenHands software-factory example](https://github.com/OpenHands/docs/pull/797) · References
- [SkillRefiner: offline skill refinement](https://www.alphaxiv.org/abs/2610.skillrefiner-offline-skill-refinement) · References（链接形式特殊，论文身份待核对）

### 9a · Frameworks 2: Orchestration and Monitoring

- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) · Readings
- [Thinking in LangGraph](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph) · Readings
- [Diagnosing a performance regression on Terminal-Bench with Docent](https://transluce.org/docent/blog/terminal-bench) · Readings
- [LangGraph: Workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents) · References
- [LangGraph: Persistence](https://docs.langchain.com/oss/python/langgraph/persistence) · References
- [LangGraph: Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts) · References
- [LangGraph: Testing](https://docs.langchain.com/oss/python/langgraph/test) · References
- [LangChain: Testing](https://docs.langchain.com/oss/python/langchain/test) · References
- [LangSmith: Evaluation](https://docs.langchain.com/langsmith/evaluation) · References
- [Course support demo: password-reset trace](https://smith.langchain.com/public/5e17b93a-17af-4386-ada0-9bd033f98a74/r) · References
- [Course support demo: billing trace before approval](https://smith.langchain.com/public/aeddf201-687b-4389-acdb-137dd9683000/r) · References
- [Course support demo: billing trace after approval](https://smith.langchain.com/public/416d3c74-4b43-4883-b189-92a57431a819/r) · References
- [Docent: Pairwise comparisons and failure-mode synthesis](https://docent.transluce.org/dashboard/9bafeb94-3f6e-4d03-bd01-1ae8476e3f6e/analysis-plan/81230a32-88e0-42af-82c9-101660ab1d89) · References
- [Docent: No-timeout task comparison](https://docent.transluce.org/dashboard/9bafeb94-3f6e-4d03-bd01-1ae8476e3f6e/analysis-plan/772c0920-0b0f-4355-a009-825d1dd553b4) · References
- [Hodoscope announcement](https://hodoscope.dev/blog/announcement.html) · References
- [Embedding Atlas](https://apple.github.io/embedding-atlas/) · References
- [OpenHands SDK](https://docs.openhands.dev/sdk) · References
- [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview) · References
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) · References
- [AG2 overview](https://docs.ag2.ai/latest/docs/user-guide/basic-concepts/overview/) · References
- [DSPy](https://dspy.ai/) · References
- [Don’t Sleep on Single-Agent Systems](https://hub.openhands.dev/blog/dont-sleep-on-single-agent-systems) · References
- [Agent Skills specification](https://agentskills.io/specification) · References
- [OpenHands automations: Fujitsu talk slides](https://github.com/neubig/slides/tree/main/slides/2026-09-25-fujitsu-openhands-en) · References
- [Black Hat USA 2026: The OpenAI–Hugging Face incident](https://www.youtube.com/watch?v=87DyyMV0kCY) · References
- [OpenAI: Hugging Face incident and the road ahead](https://openai.com/index/hugging-face-incident-and-the-road-ahead/) · References

## 目前官网未列阅读链接的授课条目

- 6b · Training 4: RL Systems
- 9b · Safety 2: Observability and Monitoring
- 10a · Agents and the Future of Work
- 10b · Interaction 1: Multi-Agent Interaction
- 12a · Interaction 2: Human-Agent Interaction
- 12b · Search 1: Reranking and Critic Models
- 13a · Search 2: Tree Search
- 13b · Guest Lecture
- 14a · Guest Lecture
