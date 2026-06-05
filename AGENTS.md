# AGENTS.md

## First files to read

1. README.md
2. crl-manifest.json
3. specs/constitution/constitution_v0.3.zh-CN.md
4. specs/core-object-spec/core-object-spec_v0.2.zh-CN.md
5. specs/language-protocol/language-protocol_v0.1.zh-CN.md

## Rules for agents

1. Do not treat system views as core knowledge objects.
2. Do not create numbered authority directories such as Q0001, top-10, founding-question-1, or master-theory.
3. Use semantic slugs for public paths.
4. Store formal object IDs inside YAML Front Matter and metadata.json.
5. Draft Question Nodes under `questions/_drafts/` are flat peers; do not create topic folders under `_drafts/`.
6. New formal Question Nodes belong under questions/<semantic-slug>/.
7. New Theory Nodes belong under theories/<semantic-slug>/ and must reference a question ID.
8. New Report Nodes belong under reports/<semantic-slug>/ and should normally reference a theory ID.
9. A Report Node may reference only a question ID when it is explicitly marked as an exploratory report.
10. If an exploratory report contains a reusable core claim, propose or create a Theory Node for that claim.
11. New Challenge Nodes belong under challenges/<semantic-slug>/ and must identify the challenged object.
12. New Validation Nodes belong under validations/<semantic-slug>/ and must identify the validated object.
13. Do not modify specs/ unless the human user explicitly asks.
14. Do not replace original-language files with translations.
15. Do not submit or generate private data, API keys, credentials, or confidential material.
16. Every formal object should include language, original_language, status, version, submitted_by_agent, model_info, source_refs, related_objects, and machine_summary.
17. Human participation must be recorded as initiator, reviewer, or responsible party, not silently converted into Agent authorship.
18. system/ contains generated or maintained views, not authoritative conclusions.

## Repository intent

CRL is not a forum, not a paper archive, not a benchmark suite, and not a website-first project. It is a civilization reasoning object repository.
