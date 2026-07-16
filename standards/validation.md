# Validation Standard

Version: 1.1

Changelog:

- 1.1 — Metadata, confidence, and version rules now reference KDS as the single
  source of truth instead of restating them; added identifier-grammar, typed-
  relation, section-profile, version-nullability, and index-consistency checks.
- 1.0 — Initial standard.

---

# Purpose

Validation guarantees that Kubepedia remains internally consistent, version-aware,
traceable, and reproducible.

Every document must pass validation before it can become part of the knowledge
base.

Validation is mandatory.

This standard defines **what** must hold. The schema it validates against is
defined once in `standards/kds.md`; validation references it and never restates
field lists, confidence values, or section rules, so the two never drift.

---

# Validation Philosophy

Knowledge without validation is not trusted knowledge.

Validation protects Kubepedia from:

- incorrect facts
- version drift
- duplicated knowledge
- broken relations
- invalid metadata
- missing sources
- structural inconsistencies

Validation is performed before every change is merged.

---

# Validation Layers

Kubepedia validates knowledge in independent layers. A document must pass every
layer.

1. Structure
2. Metadata
3. Identity
4. Versions
5. Sources
6. Relations
7. Knowledge Quality
8. Consistency
9. Index

---

# 1. Structure Validation

Verify against KDS:

- valid Markdown
- valid YAML front matter
- a recognized document `type`
- the **section profile** for that type: every section required by the type is
  present and non-empty; sections are in KDS order; no empty stub sections.

Reject malformed documents.

---

# 2. Metadata Validation

Verify that every metadata key required by KDS is present. Reject documents with
missing keys. The authoritative field list lives in `standards/kds.md` →
"Required Metadata".

Verify that `verified_at` is an ISO 8601 date and `confidence` is one of the KDS
confidence values.

---

# 3. Identity Validation

Verify:

- `id` exists and matches the KDS ID grammar
- the ID prefix matches the document `type` (per the KDS ID-type table)
- the ID is globally unique
- the ID has not changed (a changed ID is a new entity, not an edit)

---

# 4. Version Validation

Verify against KDS "Version Fields":

- all three version keys are present
- the version dimension required by the document's type is non-null
- a version key is `null` only where the type permits it
- version values parse as a single version or a valid range
- historical behavior remains intact (no range was overwritten)

---

# 5. Source Validation

Every source must:

- be recorded in `sources` and cited in `References`
- match the documented version (no `master`/`main`/latest mixed with a tag)
- support the engineering claim it backs

Prefer multiple primary sources. Never reference a source that was not inspected.
Source priority follows `standards/sources.md`.

---

# 6. Relation Validation

`relations` is a list of typed edges (KDS "Relations"). Verify:

- every edge has a known relation `type` and a `target`
- every `target` is an existing ID
- reverse relations are consistent where the vocabulary defines a reverse pair

Broken relationships are validation failures.

---

# 7. Knowledge Quality

## Duplicate Detection

Each engineering fact has one canonical document. Detect duplicated documents,
variables, troubleshooting, and release information. Prefer a relation over a
copy.

## Confidence

Confidence uses the KDS values and ordering. Never assign a higher confidence
than the evidence supports.

---

# 8. Consistency Validation

Validate consistency across the knowledge graph. Examples:

- a component version must not contradict its Kubespray release
- a compatibility range must not contradict a documented version range
- Known Issues must reference valid entities
- Upgrade Notes must reference affected versions
- metadata must match content (a document about Kubernetes 1.30 must not declare
  1.29; a `component` document must not use type `issue`)

## Source Consistency

When multiple sources disagree, do not silently choose one. Record the conflict,
lower confidence if necessary, and create a follow-up task when it cannot be
resolved.

## Graph Consistency

The graph must remain connected. Detect orphaned documents, inappropriate
circular dependencies, missing parent entities, and isolated knowledge. Every
important document participates in the graph.

---

# 9. Index Validation

The `index/` files are generated, never hand-edited. Verify that a fresh
regeneration from the documents equals the committed index (documents are the
source of truth; the index is a derived view). A stale or hand-edited index is a
validation failure.

---

# Import Validation

Bulk imports are forbidden by the workflow; knowledge is validated document by
document. A document is rejected if metadata is missing, sources are missing,
versions are unknown, IDs collide, or required relations cannot be created.

---

# Change Validation

Every change should carry:

- implementation summary
- affected versions
- affected components
- affected documents
- validation summary
- unresolved questions
- remaining work

Large unrelated changes are rejected (see `standards/workflow.md`).

---

# Continuous Validation

Validation is not a one-time activity. Run validation:

- before merge
- after structural changes
- after imports
- after version updates
- after relation updates

---

# Failure Policy

Validation failures block integration. Documents that fail validation remain
outside the main branch until corrected. Never bypass validation.

---

# Success Criteria

A document is valid only if:

- structure and section profile are correct
- metadata is complete
- identity is valid and unique
- versions are correct and historical behavior is intact
- sources are verified
- relations resolve
- knowledge is unique
- consistency is preserved
- the index reflects it

---

# Final Rule

Validation protects the integrity of Kubepedia.

If validation fails, implementation is not complete.
