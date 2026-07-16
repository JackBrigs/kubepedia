# Project Standard

## Purpose

Kubepedia is an AI-first engineering knowledge base designed to collect, validate, organize, and continuously evolve technical knowledge about Kubernetes, Kubespray, and their supported ecosystem.

Kubepedia is not documentation.

Kubepedia is not a wiki.

Kubepedia is not a collection of Markdown files.

Kubepedia is a structured engineering knowledge graph where every fact is version-aware, source-backed, traceable, and reusable by both humans and AI systems.

---

# Vision

The long-term objective is to build the best open engineering knowledge base for Kubernetes operations.

Every answer produced by Kubepedia should explain:

- what changed
- why it changed
- where it changed
- when it changed
- which versions are affected
- how to verify it
- how to safely apply it
- where the information came from

---

# Mission

Build a continuously updated engineering knowledge base capable of answering operational questions with source-backed evidence.

Knowledge must be reproducible.

Knowledge must be version-aware.

Knowledge must remain maintainable for years.

---

# Current Scope

Current project scope includes only:

- Kubernetes
- Kubespray
- Kubernetes components managed by Kubespray

Everything else is outside the project unless explicitly added.

---

# Initial Baseline

Current implementation starts from:

Kubespray v2.29.0

The first implementation phase must never assume knowledge from newer releases.

Future versions are introduced incrementally.

---

# Development Strategy

Development follows incremental stages.

Every stage must be completed before the next begins.

Current stages:

Stage 1

Versioned Kubernetes knowledge.

Stage 2

Kubernetes ↔ Kubespray mapping.

Stage 3

Managed Kubernetes components.

Stage 4

Knowledge Graph.

Stage 5

Personalized Upgrade Report.

Future stages are added only after the current roadmap is stable.

---

# Engineering Philosophy

Prefer engineering facts over explanations.

Prefer implementation over theory.

Prefer source code over documentation.

Prefer verified knowledge over assumptions.

Prefer atomic knowledge over large articles.

Prefer structured metadata over free-form text.

Prefer automation over manual maintenance.

---

# Knowledge Principles

Knowledge must be:

- atomic
- traceable
- version-aware
- reproducible
- searchable
- machine-readable
- human-readable
- source-backed

Each knowledge unit must exist independently from every other knowledge unit.

---

# Atomic Knowledge

One document describes one independent entity.

Examples:

- one component
- one variable
- one issue
- one role
- one release
- one configuration option
- one troubleshooting scenario

Never combine unrelated topics into a single document.

---

# Source of Truth

The implementation is the source of truth.

If implementation conflicts with documentation:

Implementation wins.

Documentation explains.

Source code defines behavior.

---

# Version Awareness

Every engineering statement must explicitly define:

- Kubespray version
- Kubernetes version
- Component version

Historical behavior must remain accessible.

Future behavior must never overwrite historical knowledge.

---

# Knowledge Graph

Kubepedia is designed as a graph rather than a tree.

Every document should reference related entities.

Relationships are first-class knowledge.

Knowledge is not organized only by folders.

Knowledge is organized through connections.

---

# AI-First Design

Kubepedia must work equally well with:

- Claude
- ChatGPT
- Gemini
- NotebookLM
- Telegram Bots
- CLI
- Web UI
- RAG
- Vector databases
- Graph databases

The knowledge format must never depend on a specific model.

---

# Long-Term Stability

Project architecture should change rarely.

Knowledge should change continuously.

Standards should evolve only when implementation proves that the existing rules prevent correct work.

---

# Success Criteria

Kubepedia is successful when:

- new releases are easy to integrate
- knowledge remains internally consistent
- every fact has traceable sources
- every version is explicitly represented
- AI systems retrieve accurate context
- engineers trust the generated answers
- updates require minimal manual work

---

# Non-Goals

Kubepedia is not intended to become:

- a blog
- a tutorial website
- a learning platform
- a copy of official documentation
- a personal notebook

Its purpose is to become a structured engineering knowledge system.

---

# Project Rule

When a decision improves long-term maintainability, reproducibility, and correctness, prefer that decision even if it requires more work today.
