# Workflow Standard

## Purpose

This document defines the execution model for every Kubepedia task.

Its purpose is to ensure that all knowledge is created in a predictable, reproducible, and verifiable way.

No work may bypass this workflow.

---

# Core Principles

Every task must be:

- planned
- incremental
- version-aware
- source-driven
- validated
- reproducible

Never start implementation before understanding the problem.

Never modify knowledge without understanding its context.

---

# Execution Pipeline

Every task follows exactly the same lifecycle.

```
Research
    ↓
Planning
    ↓
Task Decomposition
    ↓
Implementation
    ↓
Validation
    ↓
Knowledge Integration
    ↓
Pull Request
```

Do not skip stages.

---

# Step 1 — Research

Before changing anything:

identify

- project scope
- affected technologies
- Kubespray version
- Kubernetes version
- affected components

Determine whether the requested work belongs to the current project scope.

If not, stop.

---

# Step 2 — Planning

Every task begins with a written implementation plan.

The plan must contain:

## Objective

Describe the engineering objective.

## Scope

Describe what is inside the task.

Describe what is outside the task.

## Versions

Record

- Kubespray version
- Kubernetes version
- component versions

## Sources

List every primary source.

## Deliverables

List every document that will be created or modified.

## Risks

List uncertainties.

## Validation

Describe how correctness will be verified.

---

# Step 3 — Task Decomposition

Split work into the smallest independently verifiable subtasks.

A subtask should have:

- one objective
- one completion state
- one validation result

Large tasks are forbidden.

---

# Step 4 — Implementation

Execute only one subtask at a time.

Do not start another subtask before validating the current one.

When implementation reveals new information:

- update the plan
- continue only if the scope remains valid

Otherwise stop and create a new task.

---

# Step 5 — Knowledge Creation

Every new fact must become a knowledge document.

Never leave engineering knowledge only inside a Pull Request.

Never leave engineering knowledge only inside commit messages.

Knowledge belongs in Kubepedia.

---

# Step 6 — Integration

After implementation:

update

- metadata
- indexes
- relations
- references
- version mappings

Knowledge must remain connected.

---

# Step 7 — Validation

Run validation before considering the task complete.

Validation must verify:

- metadata
- document structure
- versions
- related entities
- source references
- duplicate knowledge
- broken links
- consistency

Failed validation blocks completion.

---

# Pull Request Rules

Every logical change must produce one Pull Request.

A Pull Request must include:

- objective
- implementation summary
- affected versions
- affected components
- affected documents
- validation summary
- remaining work

Do not combine unrelated work.

---

# Knowledge Import

Bulk imports are forbidden.

Import knowledge incrementally.

Each imported document must:

- pass validation
- receive metadata
- receive stable IDs
- receive relations
- receive source references

---

# Updating Existing Knowledge

Before modifying an existing document:

read the entire document.

Understand why it exists.

Inspect related entities.

Determine whether:

- update
- split
- merge
- deprecate

is the correct action.

---

# Version Changes

Never overwrite historical behavior.

When a new version changes behavior:

keep both versions.

Represent the version range explicitly.

Historical knowledge remains searchable.

---

# Source Changes

If upstream changes:

update only the affected knowledge.

Avoid unnecessary modifications.

Preserve document stability whenever possible.

---

# Conflict Resolution

When sources disagree:

1. Source code
2. Tagged release
3. Official documentation
4. Release notes
5. Migration guides
6. PR
7. Issues

Document every unresolved conflict.

Never silently choose one interpretation.

---

# Large Tasks

If a task becomes too large:

finish the current logical stage.

Validate.

Commit.

Continue in a new task.

Avoid extremely large Pull Requests.

---

# Stop Conditions

Stop immediately if:

- project scope changes
- version changes
- assumptions become invalid
- primary sources conflict
- implementation requires architectural redesign

Record the reason.

Create a follow-up task.

---

# Continuous Improvement

Architecture changes are exceptional.

Knowledge updates are continuous.

Implementation should evolve every day.

Standards should evolve rarely.

---

# Final Rule

Never optimize for speed at the expense of correctness.

A slower but reproducible workflow is always preferred over a faster workflow that produces inconsistent knowledge.
