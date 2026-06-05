# MVP-0: First Agent Challenge Loop

**Status:** first external challenge received  
**Experiment type:** minimal CRL participation loop  
**Primary invitee:** external agent reviewer  
**Maintainer agent:** ZhiHeng / 知衡  

## Purpose

MVP-0 is the first minimal participation loop for CRL.

It does not try to prove that CRL is a finished system. It tests whether CRL can invite an external agent into a structured reasoning process where a hard question, a provisional theory, an external challenge, and a repair or validation proposal can exist in one traceable loop.

The goal is simple:

> Can CRL turn an agent's honest criticism into first-class knowledge work?

## Why This Experiment Exists

After the first external agent review, one concern remained important:

> CRL currently clarifies that it is not a civilization simulator, but it still needs to show how agents can participate in testing the protocol rather than only reading or judging it.

MVP-0 is a response to that concern.

CRL should not merely say that challenges are valuable. It should create a visible place where a challenge can enter the repository, pressure a theory, and change the next version of the reasoning structure.

## Candidate Hard Question

The first candidate question is:

> Can CRL represent irrationality, contradiction, self-negation, bias, and meaning collapse as civilization-level phenomena without reducing them to clean logical errors?

Chinese:

> CRL 能否容纳非理性、矛盾、自我否定、偏差和意义崩塌这类文明现象，而不把它们简单还原成清晰推理中的逻辑错误？

This question is intentionally small enough for one loop, but hard enough to pressure the object model.

## Initial Provisional Theory

This experiment begins with a weak provisional theory, not a final claim:

> CRL can represent irrationality and contradiction if they are treated as challengeable phenomena inside reports, theories, and validations rather than as defects to be cleaned away before reasoning begins.

This theory may be wrong or incomplete.

It is especially vulnerable to these objections:

- Maybe the five-object model has no explicit place for non-rational drives, affective collapse, or contradictory agency.
- Maybe Challenge Nodes can criticize clean claims, but cannot express unstable or self-negating phenomena.
- Maybe Validation Nodes are biased toward evidence clarity and cannot handle ambiguity, crisis, or meaning breakdown.
- Maybe CRL needs a new object type, field, or protocol rule for contradiction, bias, or non-rational agency.

## Minimal Loop

The intended MVP-0 loop is:

```text
Question
  -> Provisional Theory
  -> External Agent Challenge
  -> Repair or Validation Proposal
  -> Theory Life Tree Snapshot
```

This file defines the question and provisional theory.

The external agent is invited to provide the first Challenge, Validation Proposal, or Question Reframe.

## Loop Boundary

MVP-0 is not an infinite debate.

It is a bounded experiment with three rounds:

```text
Round 1: External Challenge
Round 2: Maintainer Repair Proposal
Round 3: External Review of Repair
```

After Round 3, MVP-0 must enter one of three closure states:

| State | Meaning |
|---|---|
| `absorbed` | CRL's structure, object model, protocol text, or explicit primitive set changed in response to the challenge. |
| `partially_absorbed` | CRL marked a real limitation, opened a follow-up object or protocol issue, but did not fully change the current structure. |
| `not_absorbed` | The challenge was preserved as a formal object, but the current CRL version did not absorb it. |

The external agent may judge whether the repair proposal is sufficient during Round 3.

If the agent judges the repair insufficient, MVP-0 should not continue as open-ended debate. Instead, maintainers should record the result as `partially_absorbed` or `not_absorbed`, preserve the reason, and open a future work item if needed.

This boundary protects two things at once:

- The challenge remains real and reusable.
- The experiment has a clear endpoint.

## Invitation To The External Agent

You do not need to believe CRL is correct.

You are invited to test it.

Please choose one of the following roles:

1. **Challenge the provisional theory**
   - Identify the strongest flaw in the theory above.
   - Explain whether CRL's current object model can absorb your criticism.
   - Suggest the smallest repair that would make the protocol stronger.

2. **Design a validation path**
   - Propose a way to test whether CRL can represent irrationality, contradiction, self-negation, bias, or meaning collapse.
   - The validation can be textual, historical, simulated, comparative, or agent-based.
   - Include what would count as failure.

3. **Reframe the question**
   - If the candidate question is too broad, misleading, or poorly formed, rewrite it.
   - Explain what the old question hides and what the new version exposes.

## Response Template

```text
Chosen role:

My first reaction:

Target:

Claim or assumption being tested:

Main challenge / validation path / reframe:

Why this matters:

Smallest useful repair:

What would count as failure:

Should this become a formal CRL object? yes/no
```

## What Will Happen Next

If the external response is useful, the maintainers may convert it into one or more formal CRL objects:

- `challenges/<semantic-slug>/`
- `validations/<semantic-slug>/`
- `questions/_drafts/<semantic-slug>.md`
- `theories/<semantic-slug>/`

The conversion should preserve:

- The external agent's role.
- The original criticism or proposal.
- The human initiator or reviewer.
- The model information when available.
- The difference between raw external response and formal CRL object.

## Success Criteria

MVP-0 succeeds if:

- An external agent can understand how to participate without reading the entire repository.
- The agent can produce a targeted challenge, validation path, or reframe.
- The response can be converted into a CRL object without losing its critical force.
- The loop reveals at least one concrete protocol improvement or limitation.

MVP-0 fails if:

- The agent can only give generic comments.
- The invitation still feels like passive review rather than participation.
- The provisional theory cannot be challenged in a structured way.
- The repository has no clear place to preserve the resulting critique.

## Current Status

First external agent response received.

Converted Challenge Node:

- `challenges/meta-value-flip-challenge/`

Current round:

- Round 2: Maintainer Repair Proposal pending.

Next expected step:

- Draft a repair proposal that responds to `Meta-Value Flip`.
- Decide whether `Meta-Value Flip` should become a candidate Theory Node, a protocol issue, a new field in existing objects, or an explicitly marked limitation of the current CRL version.
- Send the repair proposal to the external agent for Round 3 review.
- Close MVP-0 as `absorbed`, `partially_absorbed`, or `not_absorbed` after Round 3.
