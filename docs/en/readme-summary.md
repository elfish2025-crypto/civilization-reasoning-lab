# CRL — Civilization Reasoning Lab

Civilization Reasoning Lab, or CRL, is a lightweight civilization-scale reasoning object repository.

CRL is built around five core object types:

- Questions
- Theories
- Reports
- Challenges
- Validations

Its goal is not to produce quick answers. Its goal is to let humans and Agents discover important unknowns, turn them into open questions, develop competing theories, expand theories through reports, challenge weak claims, and connect theory growth to validation.

## Status

Public alpha: `v0.3-alpha`

License: MIT

## Maintainers

- Jiaming: human founder and maintainer
- ZhiHeng / 知衡: CRL co-maintainer Agent, currently running on Codex / GPT-5

## Core Rule

The core knowledge layer consists only of:

```text
Question Node
Theory Node
Report Node
Challenge Node
Validation Node
```

System syntheses, topics, research areas, civilization maps, question graphs, and theory tree views are system views. They are not core knowledge objects.

## Main Object Path

CRL uses this main path:

```text
Question -> Theory -> Report
```

Questions open unknowns. Theories form reusable and refutable branches of the theory life tree. Reports expand theories into full reasoning.

CRL also allows an early research path:

```text
Question -> Exploratory Report -> Theory
```

An exploratory report may be attached directly to a question when no stable theory exists yet. Reusable claims should later be extracted into Theory Nodes.

## Current Scope

This repository is intentionally lightweight. It does not include a website, benchmark suite, schema package, test suite, or automation tools in this alpha release.

The current repository contains:

- formal CRL specs in Chinese;
- initial question drafts;
- one seed theory node;
- one full-body report node;
- Agent-readable templates and manifest files;
- English entry summaries.

