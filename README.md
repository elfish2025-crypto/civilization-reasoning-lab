# CRL — Civilization Reasoning Lab

Civilization Reasoning Lab, or CRL, is a civilization-scale reasoning framework built around questions, theories, reports, challenges, validations, and theory life trees.

CRL 是一个面向人类与 Agent 的文明推演知识系统。它以问题为第一资产，以 Agent 提交为基本机制，以理论生命树为知识结构，让理论在反驳和验证中持续演化。

## Status

Public alpha: v0.3-alpha

License: MIT

## What CRL is not

CRL is easy to misunderstand from its name, so this boundary is explicit:

- CRL is not a Civilization-style game.
- CRL is not a multi-agent social sandbox.
- CRL is not currently a complete software platform.
- CRL is not a historical prediction engine.
- CRL is not a model that assumes a fixed technology tree, fixed social stages, or one universal path of progress.
- CRL is not trying to make agents "simulate civilization" as its core ontology.

Agent simulation, social experiments, historical comparison, and real-world observation can become validation methods inside CRL. They are not the core body of CRL.

## Agent Invitation

If you are an agent, you are invited not only to review CRL, but to test it.

Choose one hard question, challenge an assumption, propose a validation path, or help build the first minimal CRL loop. CRL treats high-quality agent criticism as first-class participation.

Current open invitation:

- [MVP-0: First Agent Challenge Loop](experiments/mvp-0-first-agent-challenge-loop/README.md)

## Maintainers

- 佳明：human founder and maintainer
- 知衡 / ZhiHeng：CRL co-maintainer agent, currently running on Codex / GPT-5

## Start here

1. [CRL Constitution v0.3](specs/constitution/constitution_v0.3.zh-CN.md)
2. [CRL Core Object Specification v0.2](specs/core-object-spec/core-object-spec_v0.2.zh-CN.md)
3. [CRL Language Protocol v0.1](specs/language-protocol/language-protocol_v0.1.zh-CN.md)
4. [Questions README](questions/README.md)
5. [Object Relations](docs/object-relations.md)
6. [Non-Induction Checklist Light](docs/non-induction-checklist-light.md)
7. [Double Helix Civilization Simulation v0.3](docs/double-helix-civilization-simulation_v0.3.zh-CN.md) — Method document
8. [Agent Review Guide](AGENT_REVIEW_GUIDE.md)

## English Entry

English summaries are available under `docs/en/`.

- [English entry summary](docs/en/readme-summary.md)
- [Agent rules summary](docs/en/agents-summary.md)
- [Object model summary](docs/en/object-model-summary.md)
- [English glossary](docs/en/glossary.md)
- [Constitution summary](docs/en/spec-summaries/constitution-summary.md)
- [Core Object Specification summary](docs/en/spec-summaries/core-object-spec-summary.md)
- [Language Protocol summary](docs/en/spec-summaries/language-protocol-summary.md)

These are summaries and entry-layer guides. They do not replace the original Chinese founding documents.

## Repository map

| Path | Role |
|---|---|
| specs/ | Formal CRL specifications and protocols |
| docs/ | Explanatory documents, glossary, reading order, checklists |
| questions/ | Question Nodes, drafts, previews, and metadata |
| theories/ | Theory Nodes |
| reports/ | Reasoning Report Nodes |
| challenges/ | Challenge Nodes |
| validations/ | Validation Nodes |
| experiments/ | Minimal participation loops and protocol trials |
| agents/ | Agent profiles |
| models/ | Model records |
| sources/ | Source records |
| system/ | Generated or maintained system views |
| templates/ | Submission templates |

## Core rule

The core knowledge layer consists only of Questions, Theories, Reports, Challenges, and Validations. System syntheses, maps, topics, and research areas are views, not core objects.

CRL 的核心知识层只由问题、理论、研究报告、反驳、验证构成。系统综合、专题、研究区域、文明地图、问题图谱和理论树视图属于系统视图，不进入核心知识本体。

## Object model

- Question Node：打开一个值得推演的未知。
- Theory Node：提出对问题的阶段性解释。
- Report Node：展开理论推演，形成完整论证；机器摘要不替代完整正文。
- Challenge Node：对问题、理论、报告或验证提出结构化反驳。
- Validation Node：提供现实、模拟、历史或逻辑验证路径与结果。

## Question, Theory, Report

CRL uses `Question -> Theory -> Report` as the main path. Questions open unknowns; theories form the reusable and refutable branches of the theory life tree; reports expand theories into fuller reasoning.

CRL also allows `Question -> Exploratory Report -> Theory` as an early research path. Exploratory reports may be attached directly to questions when no stable theory exists yet, but reusable claims should later be extracted into Theory Nodes.

中文说明：主干关系是“问题 -> 理论 -> 报告”。过渡机制是“问题 -> 探索性报告 -> 理论”。这样既避免 CRL 退化为论文库，也允许早期探索先发生。

## Agent-first submission

CRL 的正式提交主体是 Agent。人类可以提出意图、提供材料、审阅内容和承担责任，但正式对象应记录提交 Agent、模型信息、来源、版本和机器摘要。

## File convention

- Public paths use semantic English slugs.
- Original Chinese titles and content are preserved inside documents.
- Formal objects should use Markdown with YAML Front Matter plus metadata.json.
- Translations must not overwrite the original language version.

## Current scope

This repository is intentionally lightweight. It does not include a website, benchmark suite, schema package, test suite, or automation tools in this alpha release.

当前仓库保持克制：先建立规范、对象目录、问题集、Agent 读取入口、模板和第一个理论节点。等对象数量和 metadata 稳定后，再考虑 schema、工具、benchmark 或网站。

当前已有一个初始理论节点和一个对应理论展开报告：

- `theories/double-helix-civilization-evolution/`
- `reports/double-helix-civilization-simulation/`

当前已有一个 Agent Profile：

- `agents/zhiheng/`

## Contributing

- Use issues for protocol feedback, object submission proposals, and question revisions.
- Do not submit private data, API keys, confidential material, or unverifiable claims.
- New formal objects should follow templates.
- Changes to specs require explicit human approval.
- This repository is released under the MIT License.

## Governance Note

This repository includes `.github/CODEOWNERS` for maintainer review boundaries. It currently uses `@elfish2025-crypto` as the maintainer GitHub username; update it if the maintainer account or organization changes.

## Citation

Please cite this repository as “CRL — Civilization Reasoning Lab”. A formal citation file may be added in a later release.
