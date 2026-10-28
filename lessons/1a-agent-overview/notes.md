# 1a · What Is an Agent?

## 核心理解

Agent = 模型 + 执行循环 + 外围系统。模型选择动作，程序执行，环境返回反馈，再决定下一步。

## 1. 基础概念

- **Tool definition**：工具名称、用途、参数结构，供模型理解和选择。
- **Tool call**：模型生成的工具调用请求，不等于已经执行。
- **Tool result / Observation**：程序执行后返回的结果或错误。
- **Reward**：衡量任务表现的反馈，可来自测试、规则、环境或模型裁判。观察不等于奖励，执行循环也不要求每步都有奖励。
- **Next-token prediction**：根据已有上下文预测下一个 token，连续生成文本或动作请求；实际操作由程序完成。

例子：询问文件内容 → 请求 `read_file("test.py")` → 程序读取 → 返回内容或错误 → 模型回答或继续。读取通常只获取信息，写入才改变外部内容。

## 2. 执行循环与评估

任务 + 历史 → 请求模型 → 选择动作 → 执行 → 观察结果加入历史 → 下一轮。

需要终止条件：完成任务，或达到步数、时间、成本限制。

- **ReAct**：推理、行动、观察交替推进任务，是方法而非框架。
- **mini-swe-agent**：简洁的代码 Agent 实现，可参考执行循环。
- **SWE-bench**：真实代码问题与评估机制，相当于考题和判分规则。
- **Trajectory**：一次任务的完整执行轨迹。关注模型知道什么、做了什么、反馈是什么、是否据此调整。

[GPT-OSS / Docent 示例](https://docent.transluce.org/dashboard/4a0a2b2a-a65b-452a-88c7-bb5d99745c75) · [操作说明](../../RESOURCES.md) · [mini-swe-agent](https://github.com/swe-agent/mini-swe-agent)

`Submitted` 只表示提交状态，是否成功要看测试和评估。输出的分析文本也不等于模型内部完整推理。

## 3. Agent 应具备的能力

两条改进路径：**模型训练**改善模型行为，**Harness engineering**改善外围执行系统，可以结合使用。

| 能力 | 系统侧做法 | 训练侧思路 |
| --- | --- | --- |
| 准确调用工具 | 参数校验、格式约束、错误处理 | 工具调用示范数据 SFT |
| 长上下文连贯性 | 压缩、记忆检索、子任务委派 | 对应数据与训练 |
| 可定制性 | Memory、Skills、自定义工具 | 微调或 RL |
| 复杂任务管理 | 规划 → 委派 → 验证 | 多步骤决策训练 |
| 环境理解 | 领域知识、Skills、环境反馈 | SFT / RL |
| 安全性 | 权限、沙箱、工具限制、监控 | 安全训练，不能替代权限控制 |

训练术语：Pretraining（预训练）、SFT（监督微调）、RL（强化学习）。SFT 通常基于示范数据优化预测目标，RL 利用奖励反馈优化行为。Mid-training 的具体阶段划分待核对，不能直接等同于 SFT。

## 4. Agent 是系统，不只是模型

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryTextColor': '#e2e8f0', 'lineColor': '#94a3b8', 'clusterBkg': '#1e293b', 'clusterBorder': '#64748b', 'titleColor': '#e2e8f0', 'edgeLabelBackground': '#1e293b'}}}%%
flowchart LR
    subgraph sandbox["Sandbox"]
        subgraph harness["Harness"]
            direction TB
            security["安全控制"]
            state["状态与数据"]
            tools["工具"]
            orchestration["执行编排"]
        end
    end

    harness <-->|Inference| model["Model"]
    sandbox -.- monitoring["Monitoring / 运行监控"]
    model -.- training["Training / 模型训练"]

    classDef component fill:#334155,stroke:#64748b,color:#f1f5f9
    class security,state,tools,orchestration,monitoring,training component
    style sandbox fill:#0f172a,stroke:#94a3b8,stroke-width:1px,stroke-dasharray:6 4,color:#e2e8f0
    style harness fill:#1e293b,stroke:#64748b,stroke-width:1px,color:#e2e8f0
    style model fill:#334155,stroke:#94a3b8,color:#f1f5f9
```

### Harness engineering

管理状态、工具、记忆和控制流；校验动作、处理错误、落实权限。

- 组成：Permissions、Memory、Tools、Control flow。
- 示例：CC、Codex、OpenHands、OpenCode、Pi；编排框架如 LangChain、CrewAI。
- 我的理解：类似后端应用执行层，连接模型决策与实际操作，改进它不必修改模型权重。

### Sandbox

隔离代码和工具执行，限制计算、网络和文件访问，提供可复现环境。

- 组成：Execution、Isolation、Resources、Access。
- 示例：Docker、Apptainer、Modal、Sail。
- 区别：Harness 管流程，Sandbox 管执行边界；隔离效果取决于具体配置。

### LM inference

可靠地提供模型生成服务，管理批处理、缓存复用、流式输出、并行和吞吐量。

- 示例：vLLM、SGLang。
- **KV cache**：复用已处理 token 的 Key/Value，减少重复计算；不是答案缓存或长期记忆。跨请求复用需要匹配前缀和服务支持。
- **Streaming**：逐步返回输出。
- **Latency**：单次调用或整个任务的耗时。
- **Throughput**：单位时间处理的请求或 token 数量。

Harness 提交输入，推理服务运行模型并返回输出；推理通常不更新权重。

### Training systems

准备数据、收集轨迹、协调分布式 workers、保存检查点、评估和复现实验。

- 示例：SkyRL、Miles。
- **Rollouts**：生成或交互轨迹，不只是最终答案。
- **Workers**：承担采样、执行、评分或更新等任务的进程或节点。
- **Rewards**：任务表现的反馈。
- **Update**：根据训练目标更新模型参数。

基于轨迹的 RL：采样 → 评分 → 更新 → 评估 → 继续迭代。训练可以调用推理服务采样；SFT 不要求同样的环境交互或显式奖励流程。

Checkpoint 用于恢复训练，通常还需优化器等状态，不等于只有最终权重。

### Observability and monitoring

采集轨迹和指标，追踪质量、成本与失败，对比不同运行和评估结果。

- 示例：Laminar、MLflow。
- 关注：Traces、Inspect、Quality、Latency、Cost。
- 我的理解：类似后端调用链、日志与监控，还要观察模型决策和反馈利用情况。

Docent 可以用来查看轨迹；发现问题后仍需验证原因，记录和监控不会自动修复错误。

## 5. 快速回顾

| 部分 | 核心问题 |
| --- | --- |
| Model | 生成什么？ |
| Harness | 如何组织和执行？ |
| Sandbox | 在哪里执行，权限和资源边界是什么？ |
| Inference | 如何提供模型计算？ |
| Training | 如何更新能力？ |
| Observability | 如何判断表现、定位问题？ |

这些职责可以集成在同一产品中，不必为每一项单独部署系统。

## 6. 来源与疑问

- [视频位置](https://www.youtube.com/watch?v=JQuI-0Yo1yw&t=1217s)；与 [课程入口](README.md) 的视频是否为同一版本，待核对。
- 论文笔记：[ReAct](../../references/papers/2210.03629-ReAct/notes.md)、[Toolformer](../../references/papers/2302.04761-toolformer/notes.md)。
- 待核对：mid-training 的原课件表述、CC 的完整名称。
- 待实践：错误工具或参数怎样处理？什么时候继续，什么时候终止？

## 7. 后续行动

先学 1b，追踪一条完整轨迹，再做最小工具调用实验。本课尚未完成代码验证。

整门课的能力目标：

- [ ] Build：基于开源 LLM 从零实现 Agent。
- [ ] Evaluate：设计多步骤任务评估。
- [ ] Train：通过训练改善能力。
- [ ] Safety：分析安全与可靠性权衡。
- [ ] Research：探索一个开放问题。

课程学习状态见 [课程索引](../README.md)。
