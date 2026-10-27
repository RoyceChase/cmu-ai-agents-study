# 参考资料索引

统一关联资料来源、仓库中的 PDF 和阅读笔记。学术论文放在 `papers/`，工程文章放在 `articles/`；每份资料的原文和笔记放在一起，课程只引用。课程中的特定思考可补充到对应课的 `notes.md`。

[官网完整资料清单与个人阅读建议](reading-guide.md)：按课程列出论文、技术报告及其他参考资源，并区分适合当前目标的阅读优先级。此清单不表示已下载或已阅读。

## 学术论文

| 论文 | 在线来源 | 原文 PDF | 阅读笔记 | 关联课程 |
| --- | --- | --- | --- | --- |
| Toolformer: Language Models Can Teach Themselves to Use Tools | [arXiv:2302.04761](https://arxiv.org/abs/2302.04761) | [PDF](papers/2302.04761-toolformer/paper.pdf) | [Toolformer 阅读笔记](papers/2302.04761-toolformer/notes.md) | [1a](../lessons/1a-agent-overview/README.md)、[1b](../lessons/1b-tool-use/README.md) |
| ReAct: Synergizing Reasoning and Acting in Language Models | [arXiv:2210.03629](https://arxiv.org/abs/2210.03629) | [PDF](papers/2210.03629-ReAct/paper.pdf) | [ReAct 阅读笔记](papers/2210.03629-ReAct/notes.md) | [1a](../lessons/1a-agent-overview/README.md)、[4a](../lessons/4a-computer-use-agents/README.md) |
| Executable Code Actions Elicit Better LLM Agents | [arXiv:2402.01030v4](https://arxiv.org/abs/2402.01030v4) | [PDF](papers/2402.01030-codeact/paper.pdf) | [CodeAct 阅读笔记](papers/2402.01030-codeact/notes.md) | [1b](../lessons/1b-tool-use/README.md) |
| MemGPT: Towards LLMs as Operating Systems | [arXiv:2310.08560v2](https://arxiv.org/abs/2310.08560v2) | [PDF](papers/2310.08560-memgpt/paper.pdf) | [MemGPT 阅读笔记](papers/2310.08560-memgpt/notes.md) | [2a](../lessons/2a-context-management/README.md)、[2b](../lessons/2b-skills-and-memory/README.md) |
| Reflexion: Language Agents with Verbal Reinforcement Learning | [arXiv:2303.11366v4](https://arxiv.org/abs/2303.11366v4) | [PDF](papers/2303.11366-reflexion/paper.pdf) | [Reflexion 阅读笔记](papers/2303.11366-reflexion/notes.md) | [2b](../lessons/2b-skills-and-memory/README.md) |
| SWE-bench: Can Language Models Resolve Real-World GitHub Issues? | [arXiv:2310.06770v3](https://arxiv.org/abs/2310.06770v3) | [PDF](papers/2310.06770-swe-bench/paper.pdf) | [SWE-bench 阅读笔记](papers/2310.06770-swe-bench/notes.md) | [3b](../lessons/3b-coding-agents/README.md)、[7b](../lessons/7b-openhands/README.md) |
| Agentless: Demystifying LLM-based Software Engineering Agents | [arXiv:2407.01489v2](https://arxiv.org/abs/2407.01489v2) | [PDF](papers/2407.01489-agentless/paper.pdf) | [Agentless 阅读笔记](papers/2407.01489-agentless/notes.md) | [3b](../lessons/3b-coding-agents/README.md) |
| AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents | [arXiv:2406.13352v3](https://arxiv.org/abs/2406.13352v3) | [PDF](papers/2406.13352-agentdojo/paper.pdf) | [AgentDojo 阅读笔记](papers/2406.13352-agentdojo/notes.md) | [7a](../lessons/7a-agent-safety/README.md) |

Toolformer 网页元数据已于 2026-10-27 核对；arXiv 页面列出 v1。本地 PDF 的具体版本尚未核对，原始下载日期未记录，不能直接将网页版本当作本地文件版本。

## 技术文章

| 文章 | 在线来源 | 本地 PDF | 阅读笔记 | 关联课程 |
| --- | --- | --- | --- | --- |
| Building effective agents · Anthropic | [官方网页](https://www.anthropic.com/engineering/building-effective-agents) | [PDF](articles/anthropic-building-effective-agents/article.pdf) | [阅读笔记](articles/anthropic-building-effective-agents/notes.md) | [3a](../lessons/3a-planning-and-coordination/README.md)、[9a](../lessons/9a-orchestration-and-monitoring/README.md) |
| Writing effective tools for AI agents · Anthropic | [官方网页](https://www.anthropic.com/engineering/writing-tools-for-agents) | [PDF](articles/anthropic-writing-effective-tools/article.pdf) | [阅读笔记](articles/anthropic-writing-effective-tools/notes.md) | [1b](../lessons/1b-tool-use/README.md)（个人补充） |
| Effective context engineering for AI agents · Anthropic | [官方网页](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | [PDF](articles/anthropic-effective-context-engineering/article.pdf) | [阅读笔记](articles/anthropic-effective-context-engineering/notes.md) | [2a](../lessons/2a-context-management/README.md)（个人补充） |
| How to Create Effective Agent Skills · OpenHands | [官方网页](https://www.openhands.dev/blog/20260227-creating-effective-agent-skills) | [PDF](articles/openhands-effective-agent-skills/article.pdf) | [阅读笔记](articles/openhands-effective-agent-skills/notes.md) | [2b](../lessons/2b-skills-and-memory/README.md) |
| Don't Sleep on Single-agent Systems · OpenHands | [官方网页](https://www.openhands.dev/blog/dont-sleep-on-single-agent-systems) | [PDF](articles/openhands-single-agent-systems/article.pdf) | [阅读笔记](articles/openhands-single-agent-systems/notes.md) | [3a](../lessons/3a-planning-and-coordination/README.md)、[7b](../lessons/7b-openhands/README.md)、[9a](../lessons/9a-orchestration-and-monitoring/README.md) |
| Diagnosing a performance regression on Terminal-Bench with Docent · Transluce / The Docent Team | [官方网页](https://transluce.org/docent/blog/terminal-bench) | [PDF](articles/transluce-terminal-bench-regression/article.pdf) | [阅读笔记](articles/transluce-terminal-bench-regression/notes.md) | [9a](../lessons/9a-orchestration-and-monitoring/README.md) |

技术文章使用 `articles/<机构>-<主题>/`，网页导出原文保存为 `article.pdf`，阅读笔记保存为 `notes.md`。记录来源、发布日期、快照日期与阅读状态；不额外创建分类索引或单篇 README。网页保存为 PDF 不改变原资料的类型。

当前 BibTeX 脚本只同步索引中具有 arXiv 链接的论文行，技术文章不参与自动同步。

## 新增论文

1. 创建 `papers/<论文ID>-<简称>/`，将原文保存为 `paper.pdf`，主要阅读笔记保存为同目录下的 `notes.md`。例如 `papers/2302.04761-toolformer/`。
2. 在上表新增一行，关联来源页、实际 PDF、阅读笔记和相关课程。来源链接使用干净的 URL，不附带标点。
3. 在统一的 `notes.md` 中记录原文链接、文件版本、获取日期和阅读状态；不确定的信息标为待核对。
4. 在相关课程 README 的论文条目中添加相对 Markdown 链接，指向统一论文目录、PDF 和阅读笔记。例如 `[论文目录](../../references/papers/2302.04761-toolformer/)`。多课共用同一份资料。
5. 运行下面的脚本，从 arXiv 获取元数据并更新 [bibliography.bib](bibliography.bib)。有实际文件后删除所在目录的 `.gitkeep`。
6. 检查链接并将 PDF、索引和笔记一起提交。阅读状态以主要阅读笔记为准；课程完成状态单独维护。

## 目录与课程引用

```text
references/
├── README.md
├── bibliography.bib
├── articles/
│   ├── anthropic-building-effective-agents/
│   │   ├── article.pdf
│   │   └── notes.md
│   ├── anthropic-effective-context-engineering/
│   │   ├── article.pdf
│   │   └── notes.md
│   ├── anthropic-writing-effective-tools/
│   │   ├── article.pdf
│   │   └── notes.md
│   ├── openhands-effective-agent-skills/
│   │   ├── article.pdf
│   │   └── notes.md
│   ├── openhands-single-agent-systems/
│   │   ├── article.pdf
│   │   └── notes.md
│   └── transluce-terminal-bench-regression/
│       ├── article.pdf
│       └── notes.md
└── papers/
    ├── 2210.03629-ReAct/
    │   ├── paper.pdf
    │   └── notes.md
    ├── 2302.04761-toolformer/
    │   ├── paper.pdf
    │   └── notes.md
    ├── 2303.11366-reflexion/
    │   ├── paper.pdf
    │   └── notes.md
    ├── 2310.06770-swe-bench/
    │   ├── paper.pdf
    │   └── notes.md
    ├── 2310.08560-memgpt/
    │   ├── paper.pdf
    │   └── notes.md
    ├── 2402.01030-codeact/
    │   ├── paper.pdf
    │   └── notes.md
    ├── 2406.13352-agentdojo/
    │   ├── paper.pdf
    │   └── notes.md
    └── 2407.01489-agentless/
        ├── paper.pdf
        └── notes.md
```

每篇论文或技术文章的原文、阅读笔记和可选批注副本集中在一个目录。课程不设 `papers/` 目录，仅在 README 中维护相对 Markdown 链接，例如：

```markdown
[论文目录](../../references/papers/2302.04761-toolformer/)
[PDF](../../references/papers/2302.04761-toolformer/paper.pdf)
[阅读笔记](../../references/papers/2302.04761-toolformer/notes.md)
```

链接路径相对于课程 README，无需操作系统符号链接权限或特殊 Git 设置。尚未收录的论文先保留在线来源，添加实际资料后再补本地链接。

## 自动维护 bibliography.bib

在仓库根目录运行，仅需要 Python 3.10 或更新版本，无第三方依赖或 AI 接口：

```shell
python scripts/update_bibliography.py --dry-run
python scripts/update_bibliography.py
```

脚本读取本 README 表格，每一行必须包含一个 arXiv 链接和一个实际存在的本地 PDF 链接，支持带空格或 URL 编码的路径。PDF 路径相对于本 README；正文和代码块中的示例不参与提取。同一论文的重复相同行会去重，多个 PDF 或版本对应同一论文时会报错，避免错误配对。

标题、作者、年份、分类来自 [arXiv Atom API](https://info.arxiv.org/help/api/user-manual.html)，PDF 路径写入 BibTeX 的 `file` 字段，相对于输出 `.bib` 文件。此操作只建立路径关联，不读取或修改 PDF，也不能据此确认本地 PDF 版本。链接含版本号时按该版本获取，未指定时获取当前元数据。

已有条目按 `eprint` 或 arXiv `url` 匹配，保留引用键和自定义字段，更新标准元数据与 PDF 路径；新条目使用基于 arXiv ID 的稳定引用键。未在索引中的旧条目保留，不自动删除。再次运行不会重复添加。仅支持花括号包围的 BibTeX 条目；遇到不支持的语法或重复条目时报错。请勿手改脚本管理的标准字段，人工补充可使用 `note` 等字段。

默认需要网络。也可使用从 arXiv API 保存的 Atom XML 离线更新：

```shell
python scripts/update_bibliography.py --metadata-file .cache/arxiv.xml
```

可用 `--readme <路径>` 和 `--output <路径>` 指定其他索引或输出位置。脚本在所有输入与元数据校验成功后才替换输出文件；网络、文件路径或解析失败时不会写入部分结果。它只维护 `.bib`，论文索引与阅读笔记仍由你维护，不会自动提交或推送。

## 笔记与 PDF 批注

- 原始 PDF 保持原样，便于引用与比较版本。
- Markdown 是主要阅读记录，便于 Git 比较修改、搜索、复习和关联代码。记录结论时注明章节或页码，并说明是 PDF 文件页码还是论文印刷页码。
- 高亮和页边注释用于阅读过程中的定位。需要持久保存时，另存为同一论文目录中的 `paper-annotated.pdf`，并在对应笔记中添加链接；批注副本也可纳入 Git。
- 关键理解、疑问和结论应整理进 Markdown，不只留在高亮中。PDF 是二进制文件，不便查看逐行差异或合并多人修改，因此不必每次高亮后都单独提交副本。

当前已收录优先清单中的 8 篇论文原文和 6 篇技术文章。新下载的 6 篇使用明确的版本链接；原有两篇的本地版本仍待核对。各篇阅读状态以对应笔记为准，新增笔记模板不代表已阅读。
