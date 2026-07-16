# Kubepedia

**An AI-first, version-aware, source-driven engineering knowledge base for
Kubernetes, Kubespray, and the components Kubespray manages.**

Kubepedia is not documentation, a wiki, or a pile of Markdown notes. It is a
structured **knowledge graph** of small, atomic facts where every statement is
bound to the exact versions it applies to and traceable to the source code that
proves it.

---

## Why

Operating Kubernetes through Kubespray means answering version-specific questions:
*Which etcd version ships with Kubespray v2.31.0 for Kubernetes 1.35? What does
`--tags etcd-secrets` actually do? What changed between two releases?* Generic
docs and blog posts drift out of date and rarely pin versions. Kubepedia answers
these from the **tagged Kubespray source code**, with every fact carrying its
version range and a source reference.

The long-term goal is a personalized **Upgrade & Change Report** that compares
Kubespray versions and tells an operator exactly what changes, why, and how to
apply it safely.

---

## How knowledge is organized

Every fact is a **KDS document** (Knowledge Document Specification) — one entity
per file, with YAML front matter and a stable ID:

- **Atomic** — one component, variable, run-tag, or concept per document.
- **Version-aware** — one document per entity across all versions; per-version
  values live in tables inside it. Historical behavior is never overwritten.
- **Source-backed** — each document references the tagged source it was verified
  against; confidence is graded (`confirmed` = from code).
- **Graph-oriented** — documents link through typed relations (`depends_on`,
  `part_of`, `see_also`, …), not just folders.
- **Machine- and human-readable** — a generated index lets simple clients answer
  basic questions without an LLM; the prose stays readable for engineers.

The rules are specified in [`standards/`](standards/) and are treated as the
project contract.

---

## Repository layout

```
kb/                     Knowledge graph (KDS documents)
  kubernetes/           K8s version support, control-plane, kubeadm config
  kubespray/
    variables/          Kubespray variables (kube_version, container_manager, …)
    ansible-tags/       Ansible run-tags (etcd-secrets, control-plane, reset, …)
  components/           Managed components (etcd, containerd, Cilium, CoreDNS, …)
index/                  Generated machine-readable index (documents/relations/ids)
schema/                 KDS JSON Schema
scripts/                Validator + index generator (validate_kds.py, …)
standards/              The architecture contract (project/workflow/sources/kds/…)
knowledge-base/         Legacy 0.1.0 raw source cache (not part of the KDS graph)
BACKLOG.md              Deferred work
```

---

## Current coverage

Baseline **Kubespray v2.29.0**, extended across **v2.29.0 → v2.29.1 → v2.30.0 →
v2.31.0** (Kubernetes 1.31–1.35).

| Layer | Examples |
|-------|----------|
| Kubernetes versions | supported/default versions, control-plane component versions |
| Control plane / kubeadm | kubeadm config API version (v1beta4) |
| Components | etcd, containerd, Cilium, CoreDNS, MetalLB, kube-vip |
| Variables | `kube_version`, `container_manager`, `kube_proxy_mode`, `kube_network_plugin`, … |
| Ansible run-tags | 24 tags — `etcd`, `etcd-secrets`, `control-plane`, `download`, `network`, `reset`, upgrade flow, … |

Snapshot: 38 documents, 58 typed relations, validating clean. CNI coverage is
currently **Cilium only** by design (others are in [`BACKLOG.md`](BACKLOG.md)).

---

## Using it

**Browse** — start in [`kb/`](kb/). Each document is self-contained.

**Query without an LLM** — the index is JSON Lines:

```bash
# every component and its version range
jq -r 'select(.type=="component") | "\(.id)\t\(.component_version)"' index/documents.jsonl

# what does the base cover for v2.31.0?
jq -r 'select(.kubespray_version | test("2.31")) | .id' index/documents.jsonl
```

**Ask an AI** — the documents are designed to feed retrieval (RAG / vector /
graph) for Claude, ChatGPT, and similar, without depending on any one model.

**Validate** — before trusting or extending the base:

```bash
pip install pyyaml jsonschema
python3 scripts/generate_index.py
python3 scripts/validate_kds.py
```

---

## Status

Kubepedia is **version 0.2.0** and actively growing. The architecture is
considered stable; the knowledge base is filled in incrementally, one verified
document at a time. Contributions follow the workflow in
[`standards/workflow.md`](standards/workflow.md): research the tagged source,
write KDS-compliant documents, validate, and open a focused change.

Every fact should be reproducible from its sources. If it isn't, it doesn't
belong here.
