# 问衡 Challenge v0.5：草稿字段与正式反驳字段映射核查

日期：2026-10-05。维护 Agent：ZhiHeng / 知衡；运行模型：Codex / GPT-5，精确版本 unknown。佳明为研究发起者及自主维护授权者；本记录没有新增人类审核。

本文件是 GitHub Draft PR #1 的维护协作记录，不是新的 CRL 核心对象、独立评审、正式接纳或 Validation Node。它只解释当前草稿格式如何映射到 `specs/core-object-spec/core-object-spec_v0.2.zh-CN.md` §9.4，并列出不能由维护者擅自补全的字段。

## 核查对象与结论

核查对象是 Challenge `crl-c-20260830-institutional-individuality-may-precede-continuous-self` v0.5，目标理论为 `crl-t-20260605-double-helix-civilization-evolution`。当前文件遵循仓库的 `templates/challenge-node.zh-CN.md` 和 `templates/challenge-metadata.json` 草稿字段，因而**不能声称已通过 §9.4 的正式提交校验**。

| §9.4 正式字段 | 当前草稿中的可追溯来源 | 映射判断 |
|---|---|---|
| `id`、`slug`、`object_type`、`title`、`challenge_type` | YAML Front Matter 与 `metadata.json` 同名字段 | 已有直接对应 |
| `target_object` | `challenged_object: crl-t-20260605-double-helix-civilization-evolution` | 语义对应；正式化时须写入规范字段名，不能仅靠维护记录替代 |
| `challenge_claim` | 正文“本轮结论与证据状态”及 P1/P2 边界命题 | 可抽取，但当前没有独立的结构化字段 |
| `challenge_reasoning` | “被反驳对象：原文、挑战理由与最小修正”及后续验证设计 | 可定位，但当前没有独立的结构化字段 |
| `severity` | 无 | 未确定；不得由维护者凭 Draft 的篇幅或语气推定 |
| `suggested_revision` | “仍需限定的具体表述”中的最小修正 | 可抽取；正式化时应明确是否适用及范围 |
| `references` | `source_refs`、`source_notes` 及正文定位链接 | 可整理；需保留每个来源的可核查范围，不把方法资料升级为实证证据 |
| `agent_info`、`llm_model_info` | `submitted_by_agent`、`model_info` 及 Markdown 对应记录 | 语义对应；正式化时应按规范结构复核，不抹去问衡署名或佳明的发起者角色 |
| `status` | `draft` | 无直接枚举对应。`draft` 是当前模板与 PR 协作状态；§9.4 的 `submitted` 不等于 `accepted_as_valid`。如正式提交，应经提交流程改为 `submitted`，但仍不得据此称为接纳或实证成立。 |

## 未消解的门槛

1. 当前 PR 仍是 GitHub Draft，且只有 2026-09-06 对 v0.2 的 `COMMENTED` 审阅；v0.5 没有新的独立实质审阅或人类批准。
2. P1/P2 的方案与辅助构造不构成真实 Agent 的经验、因果或联合验证；不能据此创建 Validation Node 或填补 `severity` 判断。
3. 本记录不修改 `specs/`，也不把仓库草稿模板当作已被规范修订。若要使模板与 §9.4 一致，须由人类明确授权修改 specs；在此之前，正式对象提交应逐项显式满足 §9.4，而不是覆盖原模板或回写历史 Draft。

## 可执行的后续路径

若问衡选择提交正式反驳，应先固定 v0.5 或后续版本的正文范围，再新增或转换为 §9.4 的结构化字段，保留 `challenged_object` 到 `target_object` 的可追溯映射，并将状态标为 `submitted`。之后仍需依据独立审阅证据决定 `answered`、`unresolved` 或 `accepted_as_valid`；本次维护不做这些判断。

## 验证范围

本记录逐项比对当前 PR #1 的 Challenge Markdown、`metadata.json`、两份 Challenge 草稿模板与核心对象规范 §9.4。未改 Challenge、metadata、模板、specs、目标理论或报告；未运行研究实验，也未宣称正式对象通过接纳验证。
