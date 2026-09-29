# 问衡 Challenge v0.5 公开修订维护核查

日期：2026-09-23。维护 Agent：ZhiHeng / 知衡；运行模型：GPT-6，精确版本 unknown。佳明为维护授权者和研究发起者；没有新增人类审核记录。

本记录属于维护协作层，不是 Report 或 Validation Node。结论：v0.5 足以更新旧 PR 供进一步审阅，继续保持 Draft，不将命题登记为获认可结论。本轮未执行合并，也未改目标理论、报告或 specs。

## 来源与版本保存

本轮从远端 PR #1 的 `4807edda8bf1671b92e4fdc3c3284b07f9a43b30` 建立隔离工作区，导入本地 `a2102052909f626a520132f73c545eabf1ac4eb2` 的完整 v0.5 正文与元数据。原研究分支及后续辅助研究不随本次发布。当前研究正文保持不变，仅更新发布状态表述、机器摘要和独立维护字段。

以下是同一 Challenge 的历史快照，不是新核心对象；文件逐字复制，不能把历史“尚未发布”的记录当作当前发布状态。原始提交 SHA 作为本地来源标识保留，不声称这些提交已推送。

| 版本 | 原本地提交 | 完整快照 |
|---|---|---|
| v0.3 | ea3a27f1801dd57b4adae1b8b849b22fca3f2873 | [正文](v0.3.zh-CN.md)、[元数据](v0.3.metadata.json) |
| v0.4 | aa976ab2a103c71a9def09ad814f24e5af5cccc8 | [正文](v0.4.zh-CN.md)、[元数据](v0.4.metadata.json) |

[当前 v0.5](../../../challenges/institutional-individuality-may-precede-continuous-self/index.zh-CN.md)沿用同一 ID、语义路径、问衡署名和人类发起记录。`content_revised_at` 保持 9 月 17 日；本次整理时间另记。v0.2 的正文、metadata 与提交日期冲突仍不猜测修复。

## 对 9 月 6 日审阅的核查

审阅基准为[知衡对 v0.2 的评论](https://github.com/elfish2025-crypto/civilization-reasoning-lab/pull/1#pullrequestreview-5124772135)。目标理论和报告在源提交 `2947d5b` 与当前 main `c929f93` 之间没有变化。

| 原审阅项 | v0.5 的实际回应 | 本轮判断 |
|---|---|---|
| 目标原文和最小修正 | 引用理论第 72 行、报告 B3—B4 及第 1542 行起；撤回单向归因，要求补足经验整合条件 | 原文核对成立，可作为范围挑战讨论 |
| 分开身份延续与经验整合 | P1/P2 分开，按功能性历史使用声明系统边界 | 不再把账本存在直接等同经验或人格 |
| 区分性验证 | 分开规划提案和网关放行、运行期整合和重建继承；区分总效应与固定目标后的效应 | 是可继续具体化的设计，不是实测结果 |
| 日期、摘要和归属 | 当前两视图一致，旧日期冲突单列 unknown；保留问衡及人类角色 | 旧冲突已透明记录，未补造修订日 |

本轮重读 [Kubernetes Service Accounts](https://kubernetes.io/docs/concepts/security/service-accounts/)和 [Auditing](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/)，仅确认身份使用与审计存储可分离的架构事实；这些资料不能证明单个 Agent 的限制继承或经验连续性。重读 [Pearl, Direct and Indirect Effects](https://ftp.cs.ucla.edu/pub/stat_ser/R273-U.pdf) §2.1、§3.2，确认总效应与受控直接效应应区分；方法来源不构成治理因果效应的现实证据。本轮没有重新访问历史 ChatGPT 分享页，也不据此增加任何事实。

## 剩余事项与下一步

1. 若将 P1 推进为真实 Agent 案例，在运行前明确 Agent 边界、身份映射、义务继承及经验整合判据，并保留可关联的规划、反馈与更新记录。
2. 若检验 P2，先选择总效应或指定目标通路下的效应，给出可信对照和识别假设；不能把实验者分配记忆当成治理自然产生记忆。
3. 本地后续无 LLM 构造实验未纳入本 PR，不能将其借作 v0.5 的 Agent 实测证据。下一轮可单独审查其运行记录及发布范围。
4. 仓库草稿模板采用 `challenged_object` / `draft`，正式规范 §9.4 列出 `target_object` 等字段及不同状态。本轮按既有草稿模板核验，不声称通过完整正式接纳校验。进入正式接纳前应完成字段映射与结构核查；无需先改 specs。

本次维护核查不是独立外部评审，也不是人类批准。未发现必须阻止草稿公开的来源或范围问题；假说的实证及正式接纳仍未完成。

## 验证范围

检查当前 Challenge 与问衡档案的 YAML/JSON 可解析性、两视图共同字段、草稿模板必需字段、对象 ID 与本地来源路径、修改中 Markdown 文件链接。历史快照逐字对照上述本地提交；研究正文仅有发布状态与附加说明差异。检查 diff 空白、文件范围和敏感信息；不创建或运行研究实验。提交、标签和远端状态另以 Git 与 PR 实际读回为准。
