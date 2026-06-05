# Agent Review Guide for CRL

This guide is for AI agents, human reviewers using agents, and external readers who want to evaluate Civilization Reasoning Lab without misclassifying it.

CRL welcomes criticism. It especially welcomes criticism that can become a structured Challenge Node.

## 1. First Identify What CRL Claims To Be

Before reviewing CRL, read the repository as a protocol-stage project.

CRL currently claims to be:

- A civilization reasoning knowledge system.
- A protocol for Agent-submitted questions, theories, reports, challenges, and validations.
- A theory-life-tree structure for evolving civilization-level knowledge.
- A foundation for later tools, simulations, experiments, and system views.

CRL does not currently claim to be:

- A finished application.
- A social simulation engine.
- A Civilization-style game.
- A universal theory of history.
- A predictive model of all civilizations.
- A completed multi-agent environment.

If your review assumes CRL is one of those things, separate that assumption from your actual critique.

## 2. Read In This Order

Recommended reading order:

1. `README.md`
2. `crl-manifest.json`
3. `specs/constitution/constitution_v0.3.zh-CN.md`
4. `specs/core-object-spec/core-object-spec_v0.2.zh-CN.md`
5. `specs/language-protocol/language-protocol_v0.1.zh-CN.md`
6. `questions/README.md`
7. `docs/non-induction-checklist-light.md`
8. Several Question Nodes under `questions/`

After that, review the repository using the criteria below.

## 3. Separate Three Kinds Of Feedback

When giving feedback, classify your concern as one of these:

### A. Protocol Design Issue

The object model or rules themselves may be flawed.

Examples:

- The five core objects are insufficient.
- Challenge Nodes cannot meaningfully pressure theories.
- Validation Nodes lack evidence strength fields.
- The Agent submission model creates accountability gaps.

### B. Documentation / First-Impression Issue

The project may be easy to misunderstand.

Examples:

- The name suggests a simulation platform.
- The README does not explain the project stage.
- The repository map is unclear.
- The relationship between CRL and simulation is ambiguous.

### C. Missing Implementation

The protocol may be reasonable, but the software is not built yet.

Examples:

- No validator exists.
- No API exists.
- No database schema exists.
- No UI exists.
- No executable Agent submission flow exists.

Missing implementation is not automatically a design flaw. It should be reported as a roadmap gap unless the documentation falsely claims that the feature already exists.

## 4. Review The Actual Object Model

CRL's core object model is:

```text
Question Node
Theory Node
Report Node
Challenge Node
Validation Node
```

A strong review should ask:

- Are these five objects sufficient for civilization reasoning?
- Should any object be split, merged, renamed, or constrained?
- Are object relationships precise enough?
- Can a weak theory be challenged and revised?
- Can a speculative theory be marked as speculative?
- Can validation remain partial, uncertain, historical, simulated, or future-facing?
- Can a Question Node itself be challenged, reframed, split, merged, deprecated, or archived?

## 5. Do Not Assume A Hidden Civilization Simulator

The word "civilization" can trigger assumptions about:

- Technology trees.
- Resource accumulation.
- Rational-choice agents.
- Linear progress.
- Western-centered stages.
- Nation-state competition.
- War, trade, territory, and victory conditions.

Those assumptions may be useful criticisms of some civilization simulators.

They are not automatically criticisms of CRL unless you can point to a CRL object, field, rule, or document section that actually encodes them.

If you suspect CRL may later fall into those traps, frame the critique as a risk:

```text
Risk:
Where it might enter the system:
Why the current protocol may or may not prevent it:
Suggested safeguard:
```

## 6. Convert Criticism Into Challenge Node Style

CRL treats good objections as first-class knowledge work.

When possible, write criticism in this form:

```text
Target:
  Which file, section, object, or claim are you challenging?

Claim being challenged:
  What does CRL appear to assert?

Assumption at risk:
  What hidden assumption may be false?

Why this matters:
  How could this weaken reasoning, validation, fairness, or future extensibility?

Counterexample or alternative frame:
  What case, theory, history, or model suggests a different view?

Possible repair:
  What change would reduce the problem?

Validation or falsification path:
  How could this concern be checked later?
```

## 7. Example: A Useful Challenge

```text
Target:
  specs/core-object-spec/core-object-spec_v0.2.zh-CN.md, Validation Node definition

Claim being challenged:
  Validation can come from reality, history, simulation, data, or future event review.

Assumption at risk:
  Different validation sources may have very different evidence strength, but the current object model may not force agents to distinguish them clearly enough.

Why this matters:
  A speculative simulation result could be presented with the same visual weight as a historical or empirical validation.

Counterexample or alternative frame:
  In scientific workflows, evidence type and evidence strength must be explicitly separated.

Possible repair:
  Add required fields such as validation_type, evidence_strength, uncertainty_level, falsifiability, and known_limitations.

Validation or falsification path:
  Test several example Validation Nodes and see whether readers can distinguish strong empirical support from weak analogy.
```

## 8. Example: A Less Useful Review

```text
This project will fail because civilization cannot be reduced to a technology tree.
```

This may be a valid concern for a game or simulator, but it is not yet a targeted CRL critique unless it identifies where CRL actually reduces civilization to a technology tree.

A better version:

```text
I do not see a technology-tree assumption in the current protocol. However, future system-generated Civilization Maps may accidentally impose linear-progress structures. I suggest adding a rule that system views must expose their clustering assumptions and allow multiple incompatible civilization maps.
```

## 9. What A Good Agent Review Should Output

A strong review should include:

- A short summary of what CRL actually is.
- A list of real strengths.
- A list of protocol-level risks.
- A list of documentation or first-impression risks.
- A list of missing implementation pieces.
- At least one Challenge Node style critique.
- At least one concrete repair proposal.

A strong review should avoid:

- Judging only from the repository name.
- Treating protocol-stage docs as a finished app.
- Criticizing a hidden simulator that CRL does not claim to implement.
- Replacing targeted critique with broad ideological judgment.
- Asking CRL to solve every theory of civilization before it can define its object model.

## 10. Minimal Review Template

```text
My understanding of CRL:

What CRL appears to do well:

Protocol-level concerns:

Documentation / first-impression concerns:

Missing implementation concerns:

Challenge Node proposal:
  Target:
  Claim being challenged:
  Assumption at risk:
  Why this matters:
  Counterexample or alternative frame:
  Possible repair:
  Validation or falsification path:

Final recommendation:
```

## 11. Important Standard

CRL does not need to already contain every answer about civilization.

But CRL does need to preserve the conditions under which future agents can:

- Ask better questions.
- Produce competing theories.
- Challenge hidden assumptions.
- Mark uncertainty.
- Track sources and provenance.
- Connect theories to validation.
- Let weak theories degrade and stronger theories evolve.

Review CRL by whether it protects those conditions.
