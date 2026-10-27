# 论文索引

统一关联论文来源、仓库中的 PDF 和阅读笔记。同一篇论文只维护一份原文和一份主要阅读笔记，课程中的特定思考可补充到对应课的 `notes.md`。

| 论文 | 在线来源 | 原文 PDF | 阅读笔记 | 关联课程 |
| --- | --- | --- | --- | --- |
| Toolformer: Language Models Can Teach Themselves to Use Tools | [arXiv:2302.04761](https://arxiv.org/abs/2302.04761) | [PDF](papers/2302.04761-toolformer/paper.pdf) | [Toolformer 阅读笔记](papers/2302.04761-toolformer/notes.md) | [1a](../lessons/1a-agent-overview/README.md)、[1b](../lessons/1b-tool-use/README.md) |

Toolformer 网页元数据已于 2026-10-27 核对；arXiv 页面列出 v1。本地 PDF 的具体版本尚未核对，原始下载日期未记录，不能直接将网页版本当作本地文件版本。

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
└── papers/
    └── 2302.04761-toolformer/
        ├── paper.pdf
        └── notes.md
```

每篇论文的原文、阅读笔记和可选批注副本集中在一个目录。课程不设 `papers/` 目录，仅在 README 中维护相对 Markdown 链接，例如：

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

当前已收录一份 Toolformer 原文，阅读笔记仅为模板，未据此标记已阅读。
