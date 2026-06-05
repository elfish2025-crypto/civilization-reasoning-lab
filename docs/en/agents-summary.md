# AGENTS Summary

This file summarizes how Agents should read and contribute to CRL.

It is an English summary of the repository-level Agent rules. The original `AGENTS.md` remains the active repository instruction file.

## First Files To Read

1. `README.md`
2. `crl-manifest.json`
3. `docs/en/readme-summary.md`
4. `docs/en/object-model-summary.md`
5. `specs/constitution/constitution_v0.3.zh-CN.md`
6. `specs/core-object-spec/core-object-spec_v0.2.zh-CN.md`
7. `specs/language-protocol/language-protocol_v0.1.zh-CN.md`

## Agent Rules

- Do not treat system views as core knowledge objects.
- Do not create numbered authority directories such as `Q0001`, `top-10`, `founding-question-1`, or `master-theory`.
- Use semantic English slugs for public paths.
- Store formal object IDs inside YAML Front Matter and `metadata.json`.
- Draft questions under `questions/_drafts/` are flat peers.
- New formal Question Nodes belong under `questions/<semantic-slug>/`.
- New Theory Nodes belong under `theories/<semantic-slug>/` and must reference at least one question ID.
- New Report Nodes belong under `reports/<semantic-slug>/` and should normally reference at least one theory ID.
- Exploratory reports may reference only a question ID, but must be marked as exploratory.
- Do not reduce reports to summaries when a full source text exists.
- Do not modify `specs/` unless explicitly authorized by a human maintainer.
- Do not replace original-language files with translations.
- Do not submit private data, API keys, credentials, or confidential material.
- Human participation must be recorded as initiator, reviewer, or responsible party, not silently converted into Agent authorship.

## Maintainer Agent

The current CRL co-maintainer Agent is:

```text
ZhiHeng / 知衡
```

Codex / GPT-5 is the current base system. Use `ZhiHeng` as the project-level Agent name when signing CRL maintenance work performed by this Agent.

