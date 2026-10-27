# CMU AI Agents 学习项目

围绕 [CMU 11-768 · AI Agents](https://www.cmu-agents.com/) 的个人学习仓库，按课组织笔记、论文阅读与代码实验，逐步完成综合作业和个人项目。

- [课程安排](https://www.cmu-agents.com/#/schedule)
- [课程作业](https://www.cmu-agents.com/#/assignments)
- [课程说明与政策](https://www.cmu-agents.com/#/syllabus)

## 学习导航

- [课程学习索引](lessons/README.md)：23 个授课条目的笔记、资料与实验入口。
- [官方完整日程](course/README.md)：30 个日程项，包括休课、项目时间与海报展示。
- [从第一课开始](lessons/1a-agent-overview/README.md)。
- [论文索引与维护方法](references/README.md)、[文献目录](references/bibliography.bib)与[论文与笔记](references/papers/)。
- 综合作业：[Harness](assignments/harness/)、[Eval](assignments/eval/)、[Training](assignments/training/)。
- [共享代码](src/agent_study/)、[综合项目](projects/)、[代码验证](tests/)。

课程资源核对日期：2026-10-27，学期：Fall 2026。已同步官网提供的课件、视频与阅读资料链接；官网尚未提供的资源在对应课程中标明。日期沿用官网，不进行时区换算。

## 项目结构

每节课对应一个学习目录，使用官方课次编号与英文主题命名，例如 `1a-agent-overview`、`1b-tool-use`。跨课复用的代码集中维护，综合作业独立组织。

以下目录已建立。每课使用一致的笔记、资料与实验模板，内容随学习进度补充：

```text
cmu-ai-agents-study/
├── README.md                     # 项目介绍、导航与维护约定
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
│   ├── README.md                 # 论文来源、PDF 与阅读笔记的统一索引
│   ├── bibliography.bib          # 统一文献目录
│   └── papers/                   # 统一论文资料，纳入 Git
│       └── 2302.04761-toolformer/
│           ├── paper.pdf         # 原始论文
│           └── notes.md          # 共用阅读笔记
├── src/
│   └── agent_study/              # 跨课共用代码
├── assignments/
│   ├── harness/
│   ├── eval/
│   └── training/
├── projects/                     # 综合项目
├── tests/                        # 关键行为验证
└── scripts/
    └── update_bibliography.py     # 从论文索引同步 arXiv 元数据和 PDF 路径
```

每个课程目录均已包含以下结构；作业和综合项目也可沿用这套记录方式：

```text
<课次>-<英文主题>/
├── README.md                     # 目标、资源、论文引用与导航
├── notes.md                      # 概念、方法、证据与个人理解
├── experiments/                  # 按实验组织完整内容
└── experiments.md                # 实验链接与一句话结论
```

每个实验开始时再建子目录，示例如下（尚未创建具体实验）：

```text
experiments/basic-tool-call/
├── main.py                       # 实验代码，可按需要增加模块
├── config.json                   # 可复现的配置，不含密钥
├── notes.md                      # 目标、运行方式、结果解读与疑问
├── results/                      # 指标、图表、样例与必要日志
└── models/                       # 仅需要模型文件时建立
    ├── final/                    # 需要保留的最终模型，纳入 Git
    ├── pretrained/               # 下载的基础模型，忽略
    └── test/                     # 临时测试模型，忽略
```

一个学习对象的内容放在一起：论文包含原文与阅读笔记；课程包含课程笔记与实验；每个实验包含代码、配置和成果。作业与综合项目也在各自目录中维护完整内容。仅真正共用的组件提取到 `src/agent_study/`。

空目录用 `.gitkeep` 保留，添加实际文件后删除对应占位文件。新增或调整目录时同步维护本节结构。

README 集中保留在根目录、课程索引、完整日程、统一论文索引和每课目录。每课的论文列表与运行说明统一写在该课 README；作业和综合项目实际开始、有独立说明需求时再添加 README。

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

课程学习状态只在 [课程学习索引](lessons/README.md) 维护，使用“未开始 / 进行中 / 已完成”；每课完成检查用于自查，官方日程只记录课程安排与资源。目录与模板就绪不代表课程已经学完。

## 资源与实验管理

- 每篇论文建立 `references/papers/<论文ID>-<简称>/`，将原文 `paper.pdf` 与主要阅读笔记 `notes.md` 放在一起。阅读优先级在课程 README 中维护，阅读状态以统一笔记为准。
- 论文 PDF、阅读笔记与来源索引一起纳入 Git。各课程仅在 README 中使用相对 Markdown 链接引用统一论文目录、PDF 和笔记，维护方法见 [论文索引](references/README.md#目录与课程引用)。
- 以 Python 作为代码实验的默认语言，具体依赖与运行方式随实验建立；当前尚未初始化运行环境。
- 普通实验优先共享项目环境；训练或复杂框架需要独立环境时，在对应目录说明。
- 实验应记录模型名称与版本、主要参数、数据来源、运行命令和结果；外部服务调用需说明所需环境变量。
- 密钥通过环境变量或本地 `.env` 配置，示例配置仅填写占位值。
- 实验代码和成果一起纳入 Git：在所属实验、作业或项目目录下，用 `results/` 保存指标、图表、预测样例和必要日志，用 `models/final/` 保存需要保留的权重或适配器、配置与加载说明。
- 下载的基础模型与临时测试模型分别放在所属对象的 `models/pretrained/`、`models/test/`，可丢弃的训练检查点放在 `temporary-checkpoints/`，缓存放在 `.cache/`；这些目录被忽略。原始数据放在所属对象的 `data/raw/`，小型测试样例可以纳入 Git。
- `outputs/`、`runs/`、`checkpoints/`、日志与模型扩展名不再统一忽略，避免漏掉需要保存的结果。临时内容应放到明确忽略的目录，成果说明应关联代码版本、运行配置和评估指标。

论文新增流程和 PDF 批注约定见 [论文索引](references/README.md)。原始 PDF 保持原样，主要理解与结论写入 Markdown；需要保留高亮时另存批注副本并由笔记关联。

新增论文索引后，在仓库根目录运行 `python scripts/update_bibliography.py` 更新 BibTeX；可先加 `--dry-run` 预览。脚本使用 Python 标准库，通过 arXiv API 获取元数据，保留已有引用键与自定义字段，无需 AI。

## 作业、项目与成果说明

三项作业当前均未开始，具体要求、截止时间与作业仓库在实现前核对 [官网作业页](https://www.cmu-agents.com/#/assignments)。每项作业开始时补充关联课程、依赖、运行方式、资源要求与验证结果。综合项目按项目建立独立目录，记录研究问题、方法与评估标准。

课程的 `experiments.md` 只记录实验入口和简要结论，详细实验过程统一写在 `experiments/<实验名>/notes.md`。运行记录应关联代码版本、运行命令、依赖、模型和数据版本；区分预期结果与实际观察。

需要保留的最终模型与实验结果一起放在所属对象目录中。只保存适配器时，说明恢复所需的基础权重和版本，不必复制可重新下载的基础模型。

共享组件在出现实际复用需求时提取到 `src/agent_study/`。维护脚本和共享代码的测试放在 `tests/`，实验自身的测试随实验保存。当前已有文献维护脚本及测试，尚未实现课程实验或产生模型成果。

## 当前进度

- [x] 建立项目说明、协作约定与 Git 忽略规则。
- [x] 整理官方完整日程与资源索引。
- [x] 建立 23 个授课条目的笔记、资源入口与实验目录。
- [x] 建立文献、共享代码、三项作业、综合项目与验证目录。
- [ ] 开始第一课学习，验证笔记与实验组织方式。
- [ ] 初始化代码环境并完成首个实验。

课程学习状态见 [课程索引](lessons/README.md)。已收录 Toolformer PDF 和阅读笔记模板；阅读状态见该论文笔记，实际作业与项目开始时再补充内容。
