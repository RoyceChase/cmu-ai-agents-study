# 7a · Safety 1: Agent Safety

- 官方日期：2026 · Tue, Oct 6（沿用官网日期）
- 课程分组：Agent Safety
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
- [课件：Lecture 13 slides](https://www.cmu-agents.com/slides/lecture-13-agent-safety.pdf)
- 视频：官网暂未提供，后续核对。

## 论文与参考资料

来源：[官方课表](https://www.cmu-agents.com/#/schedule)，核对日期：2026-10-27。资料可能包含论文、技术文档、博客和代码仓库；阅读优先级是本项目的初始建议。

| 资料 | 官网分类 | 阅读优先级 | 状态 |
| --- | --- | --- | --- |
| [OpenClaw incident report](https://x.com/summeryue0/status/2025774069124399363) | References | 参考 | 未阅读 |
| [PocketOS database-deletion incident](https://thenewstack.io/ai-agents-credential-crisis) | References | 参考 | 未阅读 |
| [Microsoft advisory: CVE-2025-32711](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32711) | References | 参考 | 未阅读 |
| [Cline supply-chain compromise postmortem](https://cline.bot/blog/post-mortem-unauthorized-cline-cli-npm) | References | 参考 | 未阅读 |
| [Gambit Security: AI agents targeting online retailers](https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company) | References | 参考 | 未阅读 |
| [AgentDojo](https://arxiv.org/abs/2406.13352v3) · [论文目录](../../references/papers/2406.13352-agentdojo/) · [PDF](../../references/papers/2406.13352-agentdojo/paper.pdf) · [阅读笔记](../../references/papers/2406.13352-agentdojo/notes.md) | References | 参考 | [以阅读笔记为准](../../references/papers/2406.13352-agentdojo/notes.md) |
| [ToolEmu](https://arxiv.org/abs/2309.15817v2) | References | 参考 | 未阅读 |
| [Introducing Docent](https://transluce.org/docent/blog/introducing-docent) | References | 参考 | 未阅读 |
| [Gray Swan Arena: Agent Red-Teaming Challenge](https://app.grayswan.ai/arena/challenge/agent-red-teaming/leaderboard) | References | 参考 | 未阅读 |
| [Security Challenges in AI Agent Deployment: Insights from a Large Scale Public Competition](https://arxiv.org/abs/2507.20526) | References | 参考 | 未阅读 |
| [Jailbreaking Black Box Large Language Models in Twenty Queries (PAIR)](https://arxiv.org/abs/2310.08419) | References | 参考 | 未阅读 |
| [Nemotron 3 Super technical report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf) | References | 参考 | 未阅读 |
| [Docker Engine security](https://docs.docker.com/engine/security/) | References | 参考 | 未阅读 |
| [Modal sandbox networking and security](https://modal.com/docs/guide/sandbox-networking) | References | 参考 | 未阅读 |
| [OpenShell architecture (pinned revision)](https://github.com/NVIDIA/OpenShell/blob/ec49209da25be39840742df29b64ec694d159c2f/docs/about/architecture.mdx) | References | 参考 | 未阅读 |
| [Modal sandboxes](https://modal.com/docs/guide/sandboxes) | References | 参考 | 未阅读 |
| [E2B sandbox persistence](https://docs.e2b.dev/sandbox/persistence) | References | 参考 | 未阅读 |
| [Apptainer quick start](https://apptainer.org/docs/user/main/quick_start.html) | References | 参考 | 未阅读 |
| [QEMU system emulation](https://www.qemu.org/docs/master/system/introduction.html) | References | 参考 | 未阅读 |
| [E2B sandbox lifecycle](https://docs.e2b.dev/sandbox) | References | 参考 | 未阅读 |
| [GitHub personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) | References | 参考 | 未阅读 |
| [RFC 8693: OAuth 2.0 Token Exchange](https://www.rfc-editor.org/rfc/rfc8693.html) | References | 参考 | 未阅读 |
| [GitHub App installation access tokens](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-an-installation-access-token-for-a-github-app) | References | 参考 | 未阅读 |
| [AI Control: Improving Safety Despite Intentional Subversion](https://arxiv.org/abs/2312.06942v5) | References | 参考 | 未阅读 |
| [OpenTelemetry generative AI attributes](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/) | References | 参考 | 未阅读 |
| [Docent](https://transluce.org/docent) | References | 参考 | 未阅读 |
| [Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation](https://arxiv.org/abs/2503.11926) | References | 参考 | 未阅读 |
| [AgentHarm](https://arxiv.org/abs/2410.09024) | References | 参考 | 未阅读 |
| [OpenAgentSafety](https://arxiv.org/abs/2507.06134v2) | References | 参考 | 未阅读 |
| [Monitoring Monitorability](https://arxiv.org/abs/2512.18311) | References | 参考 | 未阅读 |

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
