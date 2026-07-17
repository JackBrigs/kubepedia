# Design Decisions

Version: 1.0

An append-only log of architectural decisions and resolved conflicts between
standards. Never rewrite a decision; supersede it with a new one that references
the old. This log is the "record the conflict" mechanism required by `CLAUDE.md`.

Each entry: context, decision, rationale, consequences.

---

## D-001 — Single normative source-priority list

**Context.** `sources.md` and `workflow.md` each defined a source-priority
ordering, and they disagreed: `sources.md` ranked Migration Guides above Release
Notes; `workflow.md` ranked Release Notes above Migration Guides. Two orderings
for the same decision guarantees drift.

**Decision.** `sources.md` → "Source Priority" is the single normative list.
`workflow.md` references it and keeps no ordering of its own. Migration Guides
rank above Release Notes.

**Rationale.** A migration guide is the authoritative, actionable account of
required upgrade actions; release notes summarize and may be incomplete. One
source of truth removes the drift.

**Consequences.** Any future change to priority happens in `sources.md` only.

---

## D-002 — KDS section profiles per document type

**Context.** KDS 1.0 required the same ten sections in every document, while also
requiring atomic single-entity documents of 100–300 lines. For an atomic fact
(one variable) most sections were empty and the size floor forced padding.

**Decision.** Each document type declares the sections it requires (KDS →
"Section Profiles"). All types require `Summary` and `References`; the rest are
per-type. Non-required sections appear only when they carry real content; empty
stub sections are forbidden.

**Rationale.** Reconciles atomicity, size, and structure. A variable document is
now small and complete; a component document remains rich.

**Consequences.** Validation checks the profile per type, not a fixed layout.

---

## D-003 — Document size rule

**Context.** The 100-line minimum conflicted with atomicity.

**Decision.** No minimum size. Soft cap ~400 lines, hard max 500; beyond it,
split by concern, never by version.

**Rationale.** Atomic facts are often short; splitting by version would break the
one-ID-per-entity rule (D-005).

---

## D-004 — Formal ID grammar

**Context.** KDS 1.0 gave ID examples but no grammar, character set, type
mapping, or collision rule.

**Decision.** `ID = TYPE "-" SLUG`, uppercase, `SEGMENT = [A-Z0-9]+`, with a
fixed type→prefix table and `__` scope-disambiguation for name collisions
(KDS → "Stable Identifier"). Issues/PRs use the upstream number.

**Rationale.** Machine-checkable identity; stable links independent of filenames.

---

## D-005 — One ID per entity across all versions

**Context.** "ID survives new versions" (KDS) versus "never mix versions in one
document" (project/sources) left the versioning model undefined: one document
with ranges, or one document per (entity × version)?

**Decision.** One entity → one ID → one document, with version differences
expressed as version-ranged facts inside it (KDS → "Version Fields",
"Version Rules"). Split only by concern and only when the hard size cap is hit,
never by version.

**Rationale.** Keeps identity stable and the graph small; a new release usually
extends ranges on existing documents rather than cloning them. Historical
behavior is preserved as ranges, satisfying "never overwrite history".

**Consequences.** Integrating a new version edits affected documents' ranges; it
does not duplicate the entity.

---

## D-006 — Typed relations

**Context.** `related` was a flat list of IDs, but the graph needs edge meaning
(depends_on, fixed_by, replaced_by, …), and `validation.md` referenced parent/
child/reverse relations that the schema did not express.

**Decision.** Replace `related` with `relations`: a list of `{type, target}`
edges over a fixed vocabulary with defined reverse pairs (KDS → "Relations").

**Rationale.** Typed edges make the graph queryable and validation meaningful.

**Consequences.** No content exists yet, so there is nothing to migrate.

---

## D-007 — Confidence ordering and semantics

**Context.** `confirmed` vs `verified` had no defined order or meaning, so
"never assign higher confidence than evidence supports" was unenforceable.

**Decision.** Order high→low: `confirmed` (from tagged source code) > `verified`
(authoritative non-code source at the tag) > `probable` (single secondary source
or inference) > `hypothesis` (unverified). A `hypothesis` may not back an
operational recommendation (KDS → "Confidence Levels").

**Rationale.** Gives each level operational meaning tied to source strength (D-001).

---

## D-008 — Version-field nullability

**Context.** KDS required `kubespray_version`, `kubernetes_version`, and
`component_version` on every document, while `validation.md` rejected missing
metadata. Many entities have an inapplicable dimension (a pure Kubespray variable
has no component version; a feature gate has no Kubespray version).

**Decision.** All three keys are always present; each holds a value or explicit
`null`. Each type must set a non-null value for the dimension that scopes it
(KDS → "Version Fields"). Validation accepts `null` only where the type permits.

**Rationale.** Keeps a uniform schema without forcing meaningless placeholders.

---

## D-009 — Repository layout and generated index

**Context.** No standard said where documents live or how to answer "without an
LLM" at scale. A flat directory of tens of thousands of files does not scale.

**Decision.** Documents live under `kb/`, sharded by domain and entity. Machine-
readable indexes live under `index/` (`documents.jsonl`, `relations.jsonl`,
`ids.txt`), are generated from frontmatter, are never hand-edited, and are checked
by validation against a fresh recompute (KDS → "Repository Layout", "Index").

**Rationale.** Directory sharding scales; a derived index enables no-LLM lookup
and matches the filesystem-wins invariant already used for navigation.

---

## D-010 — Knowledge-content language: English

**Context.** Standards are in English; the legacy 0.1.0 notes were in Russian.
KDS did not fix a content language.

**Decision.** KDS knowledge content is written in English. Conversational and
user-facing summaries may be in the user's language.

**Rationale.** Open engineering knowledge base; broadest reach and AI-tool
compatibility; identifiers and technical terms are English already.

**Consequences.** Reversible while no knowledge content exists; revisit before the
first content stage if the owner prefers otherwise.

---

## D-011 — Legacy 0.1.0 base as a raw source cache

**Context.** Baseline is v2.29.0, but the repository already held v2.27.0–v2.31.0
slices in the old format. No rule covered their fate.

**Decision.** Keep `knowledge-base/` (0.1.0) as a raw, pre-analyzed source cache,
separate from the KDS graph under `kb/`. Every fact must be re-verified against
the tag before it becomes a KDS document (`CLAUDE.md` → "Baseline").

**Rationale.** Preserves valuable extracted material without treating it as
trusted KDS knowledge or deleting it.

---

## D-012 — `ansible_tag` document type

**Context.** Kubespray run-tags (`--tags etcd`, `--tags etcd-secrets`, …) are a
first-class operational entity: each has its own behavior, affected roles/tasks,
host groups, playbook membership, and standalone-run safety. None of the existing
KDS types expressed this, so questions like "which tag regenerates etcd
certificates in v2.29.1" could not be answered from the KB. The 0.1.0 base already
treated run-tags as first-class.

**Decision.** Add the `ansible_tag` document type (KDS): ID prefix `TAG`, section
profile `Summary, Context, Implementation, Compatibility, References`, Kubespray
version scope. `Context` carries playbooks and affected host groups;
`Implementation` the tagged tasks/roles; `Compatibility` version coverage and
standalone-run safety.

**Rationale.** Justified architecture extension under the Final Rule: correctly
representing a run-tag was impossible with existing types, blocking a real
operational question. Kept minimal — one type, reusing the existing section
vocabulary.

**Consequences.** `kds.md` 1.2, `schema/kds.schema.json`, and `scripts/kdslib.py`
updated together. Run-tags now indexed under `kb/kubespray/ansible-tags/`.

## D-013 — Scope expansion: adjacent operator domains (2026-07-17)

**Context.** The owner explicitly requested (2026-07-17) expanding beyond the original
scope (Kubernetes + Kubespray + Kubespray-managed components) to adjacent domains that
operators run **on** Kubespray clusters: (1) observability — Prometheus/Grafana/
Alertmanager and the VictoriaMetrics stack; (2) GitOps — ArgoCD; (3) application/PV
backup & DR — Velero (complementing the existing etcd backup); (4) the secrets/DNS
ecosystem — external-dns / external-secrets / sealed-secrets; (5) the operating system —
Ubuntu 24.04+ and its relationship with Kubernetes.

**Decision.** Expand scope to these domains, but **bounded to their integration with a
Kubernetes/Kubespray cluster**: how they install on such a cluster, version/Kubernetes
compatibility, configuration ownership, operational concerns, and troubleshooting — **not**
a reproduction of each project's full upstream documentation.

**Rationale.** Permitted under the Final Rule: a separate task explicitly requires it. These
are the most common real "what next after the cluster is up" operator needs and directly
serve the troubleshooting/administration priority.

**Consequences.** Most of these are **not** Kubespray-managed, so their evidence tier is
the upstream project's docs/charts (`verified`), not tagged Kubespray code (`confirmed`) —
except the OS domain and ArgoCD (a Kubespray-managed add-on), which draw on Kubespray
source too. Version-awareness is expressed relative to the Kubernetes/Kubespray range.
New content lands under `kb/ecosystem/` (or per-domain dirs); kept bounded to integration
to avoid scope explosion.

## D-014 — Extend version range back to v2.27.0 (2026-07-17)

**Context.** The owner requested extending the KB's Kubespray coverage **backward** from
the v2.29.0 baseline to include **v2.27.0, v2.27.1, v2.28.0, v2.28.1**, so the range (and
the Upgrade-Report tool) spans **v2.27.0 – v2.31.0**.

**Decision.** Add `RELEASE-*` docs for v2.27.0/v2.27.1/v2.28.0/v2.28.1 and `UPGRADE-*` docs
extending the chain (v2.27.0→…→v2.29.0). Component versions are **code-verified** from the
fetched upstream tags (`confirmed`); notable/breaking changes from the tags' release notes
(`verified`).

**Rationale.** Owner task; extends the version envelope and makes the upgrade-report
capstone usable from v2.27.0. The v2.29.0 baseline remains the *research* baseline; this is
historical release/upgrade coverage.

**Consequences.** Note the role path changed at v2.28.0 (`kubespray-defaults` →
`kubespray_defaults`) and versions dropped the leading `v` — reflected in the per-tag docs.
