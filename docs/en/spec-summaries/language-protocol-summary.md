# CRL Language Protocol v0.1 — English Summary

Source: `specs/language-protocol/language-protocol_v0.1.zh-CN.md`

Status: summary, not replacement.

## Purpose

The Language Protocol defines how CRL handles natural languages, language tags, translations, human views, Agent views, machine-readable metadata, and cross-language references.

It does not prescribe writing style or require a single submission language.

## Core Principle

CRL does not unify natural language. It unifies knowledge structure.

Content may exist in different languages, but object types, fields, relationships, metadata, and IDs must remain consistent.

## Language Freedom

Formal submissions may be written in any natural language.

Language is not a knowledge access barrier.

## Original Language First

Each object must preserve its original submission language.

The original version is the primary authority for that object. Translations are derived views and must not overwrite the original.

## Traceable Translation

Translations must record:

- source object;
- translation Agent;
- model used;
- date;
- version;
- translation status.

Translation is a knowledge operation and must be traceable.

## Human View and Agent View

Each formal object should support:

- Human View: readable Markdown with YAML Front Matter;
- Agent View: structured metadata, JSON, JSON-LD, graph relationships, and machine summaries.

## No Language-Based Object Duplication

Different languages should not create duplicate questions, theories, or reports if they express the same object.

New objects are justified only when the meaning materially differs.

## Machine Summary

Machine summaries should be short, clear, searchable, and free of rhetoric.

They are for indexing and Agent reading. They do not replace full object content.

## Cross-Language Theory Trees

Theory trees should use object IDs as the stable core.

Titles, summaries, and translations may vary by language, but the underlying object graph should remain stable.

