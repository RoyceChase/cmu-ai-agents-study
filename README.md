# CMU AI Agents 学习项目

围绕 [CMU 11-768 · AI Agents](https://www.cmu-agents.com/) 的个人学习仓库，按课组织笔记、论文阅读与代码实验，逐步完成综合作业和个人项目。

- [课程安排](https://www.cmu-agents.com/#/schedule)
- [课程作业](https://www.cmu-agents.com/#/assignments)
- [课程说明与政策](https://www.cmu-agents.com/#/syllabus)

## 学习导航

- [课程学习索引](lessons/README.md)：23 个授课条目的笔记、资料与实验入口。
- [官方完整日程](course/README.md)：30 个日程项，包括休课、项目时间与海报展示。
- [从第一课开始](lessons/1a-agent-overview/README.md)。
- [文献目录](references/bibliography.bib)与[论文原文](references/pdfs/)。
- 综合作业：[Harness](assignments/harness/)、[Eval](assignments/eval/)、[Training](assignments/training/)。
- [共享代码](src/agent_study/)、[综合项目](projects/)、[代码验证](tests/)。

课程资源核对日期：2026-10-27，学期：Fall 2026。已同步官网提供的课件、视频与阅读资料链接；官网尚未提供的资源在对应课程中标明。日期沿用官网，不进行时区换算。

## 项目结构

每节课对应一个学习目录，使用官方课次编号与英文主题命名，例如 `1a-agent-overview`、`1b-tool-use`。跨课复用的代码集中维护，综合作业独立组织。

以下目录已建立。每课使用一致的笔记、资料与实验模板，内容随学习进度补充：

```text
cmu-ai-agents-study/
├── README.md                     # 项目介绍、导航、结构与学习进度
├── AGENTS.md                     # 仓库协作约定
├── .gitignore                    # 临时文件与本地环境忽略规则
├── course/
│   ├── README.md                 # 完整官方日程
│   └── schedule.yaml             # 课次、资源链接及核对日期
├── lessons/
│   ├── README.md                 # 课程索引与学习进度
│   ├── 1a-agent-overview/
│   ├── 1b-tool-use/
│   ├── 2a-context-management/
│   ├── 2b-skills-and-memory/
│   ├── 3a-planning-and-coordination/
│   ├── 3b-coding-agents/
│   ├── 4a-computer-use-agents/
│   ├── 4b-supervised-fine-tuning/
│   ├── 5a-rl-basics/
│   ├── 5b-deep-research-agents/
│   ├── 6a-advanced-rl/
│   ├── 6b-rl-systems/
│   ├── 7a-agent-safety/
│   ├── 7b-openhands/
│   ├── 9a-orchestration-and-monitoring/
│   ├── 9b-observability-and-monitoring/
│   ├── 10a-future-of-work/
│   ├── 10b-multi-agent-interaction/
│   ├── 12a-human-agent-interaction/
│   ├── 12b-reranking-and-critic-models/
│   ├── 13a-tree-search/
│   ├── 13b-guest-lecture/
│   └── 14a-guest-lecture/
├── references/
│   ├── bibliography.bib          # 统一文献目录
│   └── pdfs/                     # 论文原文，纳入 Git
├── src/
│   └── agent_study/              # 跨课共用代码
├── assignments/
│   ├── harness/
│   ├── eval/
│   └── training/
├── projects/                     # 综合项目
├── tests/                        # 关键行为验证
├── results/                      # 指标、图表、配置与必要日志，纳入 Git
└── models/
    ├── final/                    # 最终模型成果，纳入 Git
    ├── pretrained/               # 下载的基础模型，忽略
    └── test/                     # 临时测试模型，忽略
```

每个课程目录均已包含以下结构；作业和综合项目也可沿用这套记录方式：

```text
<课次>-<英文主题>/
├── README.md                     # 目标、资源、论文列表、运行说明与状态
├── notes.md                      # 概念、方法、证据与个人理解
├── papers/                       # 论文阅读笔记
├── code/                         # 实验代码
└── experiments.md                # 配置、观察、结论及成果路径
```

`results/<实验名>/` 与 `models/final/<实验名>/` 按实际实验建立，分别保存结果和最终模型。`models/pretrained/` 与 `models/test/` 已预留为本地目录，其内容不随 Git 上传。新增或调整目录时同步维护本节结构。空目录用 `.gitkeep` 保留，添加实际文件后删除对应占位文件。

README 集中保留在根目录、课程索引、完整日程和每课目录。每课的论文列表与运行说明统一写在该课 README；作业和综合项目实际开始、有独立说明需求时再添加 README。

## 建议学习路径

结合四年 Java 开发经验，以 Agent 应用开发与服务化交付为实践目标。下面是个人学习顺序建议，官方课次与日程保持原样。

| 阶段 | 课次 | 实践目标 |
| --- | --- | --- |
| 基础能力 | 1a → 1b → 2a → 2b → 3a | 逐步实现工具调用、上下文管理、记忆与规划，推进 Harness 作业 |
| 应用与评估 | 3b → 4a → 5b → 7b → 9a | 选择一种应用深入实践，建立固定任务集，推进 Eval 作业 |
| 训练方法 | 4b → 5a → 6a → 6b | 理解 SFT、RL 与训练系统，推进 Training 作业 |
| 安全与交互 | 7a → 9b → 10a → 10b → 12a | 补齐权限、监控、人机协作与多 Agent 交互；基础权限和日志从首个实验开始加入 |
| 搜索与拓展 | 12b → 13a → 13b → 14a | 比较搜索与评判方法的效果及成本，结合客座课程完成综合项目 |

Python 随课程实验补充，先掌握环境管理、模块、类型提示、异步调用与测试。服务化实践可结合已有 Java / Spring Boot 经验，是否拆分服务根据实际需要决定。

综合项目可以选择“Java 代码库分析与问题定位 Agent”，串联代码检索、工具执行、任务状态、评估和故障分析。面试准备以可运行项目、固定评估集、失败案例和设计取舍为证据，课程完成状态与项目能力分别记录。

## 学习流程

1. 对照官方课程安排，记录本课课件、视频、阅读材料与参考资料。
2. 用自己的话整理核心概念、方法、适用条件与疑问，区分课程内容和个人理解。
3. 挑选核心论文精读，记录问题、方法、证据、局限及与本课的联系。
4. 完成一个最小实验或案例分析，保存运行方式、配置、结果与失败原因。
5. 回顾本课目标，更新完成状态和后续待办。

每课以“能够解释核心问题与方法、有核心材料阅读记录、有实验或案例分析、有结论及未解决问题”为完成参考。论文分为精读、选读和参考，不要求逐篇完整复现。

学习状态统一使用“未开始 / 进行中 / 已完成”。开始或完成一课时，同步更新该课 `README.md` 和 [课程学习索引](lessons/README.md)。目录与模板就绪不代表课程已经学完。

## 资源与实验管理

- 论文文件建议命名为 `<arxiv-id或作者年份>-<简称>.pdf`；BibTeX 条目核实后补入 `references/bibliography.bib`。阅读优先级和状态在对应课程 README 中维护，阅读笔记放在该课 `papers/`。
- 论文 PDF 统一保存在 `references/pdfs/`，与阅读记录、来源链接一起纳入 Git，提交并推送后随仓库保存。同一篇论文只保留一份，各课通过相对路径引用，记录版本和获取日期。
- 以 Python 作为代码实验的默认语言，具体依赖与运行方式随实验建立；当前尚未初始化运行环境。
- 普通实验优先共享项目环境；训练或复杂框架需要独立环境时，在对应目录说明。
- 实验应记录模型名称与版本、主要参数、数据来源、运行命令和结果；外部服务调用需说明所需环境变量。
- 密钥通过环境变量或本地 `.env` 配置，示例配置仅填写占位值。
- 实验代码和需要保留的成果纳入 Git：结果放在 `results/<实验名>/`，包括指标、图表、预测样例、配置与必要日志；最终模型放在 `models/final/<实验名>/`，包括权重或适配器、配置与加载说明。
- 下载的基础模型放在 `models/pretrained/`，临时测试模型放在 `models/test/`，可丢弃的训练检查点放在 `temporary-checkpoints/`，这些目录被忽略。原始数据集放在被忽略的根目录 `data/`。
- `outputs/`、`runs/`、`checkpoints/`、日志与模型扩展名不再统一忽略，避免漏掉需要保存的结果。临时内容应放到明确忽略的目录，成果说明应关联代码版本、运行配置和评估指标。

## 作业、项目与成果说明

三项作业当前均未开始，具体要求、截止时间与作业仓库在实现前核对 [官网作业页](https://www.cmu-agents.com/#/assignments)。每项作业开始时补充关联课程、依赖、运行方式、资源要求与验证结果。综合项目按项目建立独立目录，记录研究问题、方法与评估标准。

`results/<实验名>/` 保存指标、表格、图像、预测样例、配置与必要日志。结果说明应关联课程、代码版本、运行命令、模型和数据版本；各课 `experiments.md` 链接到实际成果并总结结论。

`models/final/<实验名>/` 保存最终权重或适配器、模型配置与加载说明。模型说明应记录基础模型及版本、训练与加载命令、评估指标，并链接对应实验结果；只保存适配器时明确恢复所需的基础权重。模型用途由目录区分，不按扩展名统一忽略。

共享组件在出现实际复用需求时提取到 `src/agent_study/`。关键行为和边界条件的测试放在 `tests/`，小型测试样例可纳入 Git。当前尚无代码实现、模型成果或实验结果。

## 当前进度

- [x] 建立项目说明、协作约定与 Git 忽略规则。
- [x] 整理官方完整日程与资源索引。
- [x] 建立 23 个授课条目的笔记、资料与代码目录。
- [x] 建立文献、共享代码、三项作业、综合项目与验证目录。
- [ ] 开始第一课学习，验证笔记与实验组织方式。
- [ ] 初始化代码环境并完成首个实验。

课程学习进度：**0 / 23**；三项作业均未开始。当前笔记与实验文件为待填写模板，尚未下载论文原文或运行实验。
