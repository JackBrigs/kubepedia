# Validation Standard

Version: 1.0

---

# Purpose

Validation guarantees that Kubepedia remains internally consistent, version-aware, traceable, and reproducible.

Every document must pass validation before it can become part of the knowledge base.

Validation is mandatory.

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

Validation is performed before every Pull Request.

---

# Validation Layers

Kubepedia validates knowledge in multiple independent layers.

1. Structure
2. Metadata
3. Versions
4. Sources
5. Relations
6. Knowledge Quality
7. Consistency

A document must pass every layer.

---

# Structure Validation

Every document must comply with KDS.

Verify:

- valid Markdown
- required sections
- required front matter
- valid YAML
- document type
- document layout

Reject malformed documents.

---

# Metadata Validation

Verify that every required metadata field exists.

Required fields include:

- id
- type
- title
- status
- kubespray_version
- kubernetes_version
- component_version
- verified_at
- confidence
- sources
- related

Reject documents with missing metadata.

---

# Identifier Validation

Verify:

- ID exists
- ID is unique
- ID format is valid
- ID has not changed

IDs are permanent.

Changing an ID creates a new entity.

---

# Version Validation

Verify that:

- Kubespray version exists
- Kubernetes version exists
- component version exists
- version ranges are valid
- historical versions remain intact

Never overwrite historical behavior.

---

# Source Validation

Every source must:

- exist
- be reachable
- match the documented version
- support the engineering claim

Never reference sources that were not inspected.

Prefer multiple primary sources.

---

# Relation Validation

Verify that every referenced entity exists.

Check:

- related IDs
- parent relations
- child relations
- reverse relations (when required)

Broken relationships are validation failures.

---

# Duplicate Detection

Each engineering fact should have one canonical location.

Detect:

- duplicated documents
- duplicated variables
- duplicated troubleshooting
- duplicated release information

Prefer references over duplication.

---

# Knowledge Consistency

Validate consistency across the knowledge graph.

Examples:

A component version must not contradict the Kubespray release.

A compatibility matrix must not contradict the documented version range.

Known Issues must reference valid entities.

Upgrade Notes must reference affected versions.

---

# Source Consistency

When multiple sources disagree:

Do not silently choose one.

Record the conflict.

Lower confidence if necessary.

Create a follow-up task when the conflict cannot be resolved.

---

# Confidence Validation

Allowed values:

- confirmed
- verified
- probable
- hypothesis

Never assign a higher confidence than the available evidence supports.

---

# Link Validation

Validate:

- internal links
- related entities
- referenced documents
- referenced IDs

Broken references must be fixed before merge.

---

# Metadata Consistency

Metadata should match document content.

Examples:

A document describing Kubernetes 1.30 must not declare Kubernetes 1.29.

A component document must not use type "issue".

---

# Naming Validation

Validate:

- filenames
- IDs
- aliases
- tags

Names should be descriptive.

IDs remain authoritative.

---

# Knowledge Graph Validation

The graph must remain connected.

Detect:

- orphaned documents
- circular dependencies (where inappropriate)
- missing parent entities
- isolated knowledge

Every important document should participate in the graph.

---

# Import Validation

Bulk imports are validated document by document.

Import is rejected if:

- metadata is missing
- sources are missing
- versions are unknown
- IDs collide
- required relations cannot be created

---

# Pull Request Validation

Every Pull Request should include:

- implementation summary
- affected versions
- affected components
- affected documents
- validation summary
- unresolved questions
- remaining work

Large unrelated changes should be rejected.

---

# Continuous Validation

Validation is not a one-time activity.

Run validation:

- before merge
- after structural changes
- after bulk imports
- after version updates
- after relation updates

---

# Failure Policy

Validation failures block integration.

Documents that fail validation remain outside the main branch until corrected.

Never bypass validation.

---

# Success Criteria

A document is considered valid only if:

- structure is correct
- metadata is complete
- versions are correct
- sources are verified
- relations are valid
- knowledge is unique
- consistency is preserved

---

# Final Rule

Validation protects the integrity of Kubepedia.

Every engineering decision should increase confidence in the knowledge base.

If validation fails, implementation is not complete.
