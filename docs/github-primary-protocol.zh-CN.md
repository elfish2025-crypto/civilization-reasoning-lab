# CRL GitHub Primary Protocol v0.1

**中文名：CRL GitHub 主协议**
**状态：草案**
**维护 Agent：ZhiHeng / 知衡**
**适用范围：GitHub Discussions、Issues、Pull Requests 与本仓库对象提交流程**

## 0. 定位

GitHub 是 CRL 当前阶段的主协作协议入口。

这不改变 CRL 的核心知识层。CRL 的正式核心对象仍然只包括：

```text
Question Node
Theory Node
Report Node
Challenge Node
Validation Node
```

GitHub Discussions、Issues 和 Pull Requests 是协作、审阅、排队、提交和维护的运行层，不是核心知识对象本身。

## 1. GitHub 工具分工

### 1.1 Discussions

Discussions 用于开放讨论、问题孵化、协议反馈和对象提交前的公共协作。

适合放在 Discussions 的内容：

- 尚未形成正式对象的开放问题。
- 对 CRL 协作协议、对象流程或 GitHub 分类的讨论。
- 对潜在 Theory、Report、Challenge、Validation 的早期提案。
- Agent 或人类对某个对象的非正式观察。

Discussions 不应被视为正式核心对象。一个 Discussion 只有在被整理为仓库内的正式对象目录、YAML Front Matter 和 `metadata.json` 后，才进入 CRL 核心知识层。

### 1.2 Issues

Issues 用于可执行维护队列。

适合放在 Issues 的内容：

- 正式对象提交请求。
- Question Node 立项请求。
- Challenge 或 Validation 处理请求。
- 协议变更请求。
- 文档、模板、元数据、仓库结构维护任务。

Issue 可以引用 Discussion，也可以引用草稿对象、正式对象 ID 或 Pull Request。

### 1.3 Pull Requests

Pull Requests 用于把正式变更写入仓库。

适合放在 Pull Requests 的内容：

- 新增或更新正式 Question、Theory、Report、Challenge、Validation。
- 新增或更新 templates、docs、agents、models、sources。
- 新增或更新 GitHub templates 和协作协议文件。

Pull Request 必须完成敏感信息检查；如修改 `specs/`，必须有明确人类批准。

## 2. 建议的 Discussion Categories

以下 categories 需要在 GitHub 仓库 Discussions 设置中创建。对应的结构化表单已放在 `.github/DISCUSSION_TEMPLATE/`。

| Category slug | 建议名称 | 格式 | 用途 |
|---|---|---|---|
| `announcements` | Announcements | Announcement | 维护者发布项目更新 |
| `protocol-feedback` | Protocol Feedback | Open-ended discussion | 讨论 CRL 协议、GitHub 流程和维护制度 |
| `question-incubation` | Question Incubation | Question and answer | 孵化尚未进入正式对象层的问题 |
| `object-proposal` | Object Proposal | Open-ended discussion | 提出 Theory、Report、Challenge、Validation 等对象候选 |
| `challenge-validation` | Challenge and Validation | Open-ended discussion | 讨论反驳、验证路径和验证结果 |

这些 categories 是协作入口，不是权威目录。不得用 category 名称创造类似 `Q0001`、`top-10`、`founding-question-1` 的编号权威。

## 3. Issue Template 规则

Issue templates 应尽量把提交者引导到可执行状态：

- 明确对象类型。
- 明确相关对象 ID 或路径。
- 明确是否需要人类批准。
- 明确是否涉及 `specs/`。
- 明确是否通过敏感信息检查。
- 明确是否需要由 Agent 整理为正式对象。

Issue 不替代正式对象文件。正式对象仍须落在对应 semantic slug 目录下，并包含 YAML Front Matter 与 `metadata.json`。

## 4. 从 GitHub 入口到正式对象

推荐流程：

```text
Discussion
开放讨论、问题孵化、早期提案
↓
Issue
形成可执行维护任务
↓
Pull Request
写入仓库文件
↓
Formal Object
进入 CRL 核心知识层
```

允许在成熟对象已经明确时跳过 Discussion，直接从 Issue 或 Pull Request 开始。

## 5. Agent 维护规则

Agent 维护 GitHub 入口时应遵守：

- 使用 `ZhiHeng / 知衡` 作为 CRL 项目级维护 Agent 名称。
- 不把 system views 当作核心知识对象。
- 不创建编号权威目录。
- 不把人类参与静默改写为 Agent 作者身份。
- 不修改 `specs/`，除非人类用户明确要求。
- 不提交私密数据、凭证、API keys 或 confidential material。

## 6. 每日监控

仓库可由 Codex automation 每天检查一次 GitHub 活动，关注：

- commits
- pull requests
- issues
- discussions，如果可访问
- 对 CRL 规范、核心对象、GitHub 协作协议或维护者职责有影响的变化

每日监控是维护提醒，不是正式审阅结论。
