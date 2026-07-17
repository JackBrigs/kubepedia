---
id: CONCEPT-SECURITY_INDEX
type: concept
title: "Security posture — index of CVEs, hardening, and insecure defaults"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - security index
  - security posture
  - is my cluster secure
  - cve overview kubespray
  - hardening overview
  - security hub
tags:
  - security
  - index
sources:
  - type: docs
    path: docs/operations/hardening.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/hardening.md
    note: "authoritative hardening overlay — what to turn on; the inverse is the insecure default"
relations:
  - type: see_also
    target: CONCEPT-INSECURE_DEFAULTS
  - type: see_also
    target: PRACTICE-CLUSTER_HARDENING
  - type: see_also
    target: CONCEPT-POD_SECURITY_STANDARDS
  - type: see_also
    target: CONCEPT-SECRETS_MANAGEMENT
  - type: see_also
    target: PRACTICE-RBAC_LEAST_PRIVILEGE
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
---

# Security posture — index of CVEs, hardening, and insecure defaults

## Summary

The single entry point for the security of a Kubespray-managed cluster. It answers three operator
questions and routes each to the docs that hold the source-verified detail: **"am I exposed to a
known CVE?"** (the per-component CVE matrices), **"what's insecure out of the box?"**
([[CONCEPT-INSECURE_DEFAULTS]]), and **"how do I lock it down?"** (the hardening overlay and the
control-specific practices). Nothing here is new fact — it is the map over the security knowledge
already in the base.

## Context

**1 — Known CVEs (per component, version-bound).** Each matrix maps a component **version to the
tags that ship it** and its CVE exposure across **v2.27.0–v2.31.0**, so you can check your version
directly:

| Component | CVE matrix |
|-----------|------------|
| Kubernetes | [[TROUBLE-KUBERNETES_KNOWN_CVES]] |
| containerd | [[TROUBLE-CONTAINERD_KNOWN_CVES]] |
| runc | [[TROUBLE-RUNC_KNOWN_CVES]] |
| Cilium | [[TROUBLE-CILIUM_KNOWN_CVES]] |
| CNI plugins | [[TROUBLE-CNI_PLUGINS_KNOWN_CVES]] |
| CoreDNS | [[TROUBLE-COREDNS_KNOWN_CVES]] |
| cert-manager | [[TROUBLE-CERT_MANAGER_KNOWN_CVES]] |
| Helm | [[TROUBLE-HELM_KNOWN_CVES]] |

Upstream Kubernetes security-advisory tracking: [[CONCEPT-SECURITY_ADVISORIES]]. The
[[PRACTICE-RUNBOOK_UPGRADE_ONE_MINOR]] runbook is how you close a CVE gap (move to a fixed version).

**2 — Insecure defaults.** Kubespray ships **usable, not hardened** — most security controls are
**off by default** and enabled via the hardening overlay. The catalog of what's weak out of the box
(secrets unencrypted in etcd, audit off, PodSecurity not enforced, kubelet serving cert self-signed,
profiling on, registry open) is in [[CONCEPT-INSECURE_DEFAULTS]].

**3 — Hardening controls.** The authoritative recipe is the `hardening.yaml` overlay
([[PRACTICE-CLUSTER_HARDENING]] / [[PRACTICE-HARDENING]]) applied with `-e @hardening.yaml`. Control
areas, each with a dedicated doc:

- **Encryption at rest** — [[PRACTICE-SECRETS_ENCRYPTION_AT_REST]] / [[CONCEPT-SECRETS_MANAGEMENT]].
- **Pod Security admission** — [[CONCEPT-POD_SECURITY_STANDARDS]].
- **RBAC least privilege** — [[PRACTICE-RBAC_LEAST_PRIVILEGE]].
- **PKI / certificate rotation** — [[CONCEPT-CLUSTER_PKI]] / [[PRACTICE-RUNBOOK_CERT_ROTATION]].

**How to use this.** For an audit: walk [[CONCEPT-INSECURE_DEFAULTS]] against your inventory to find
what you left at default, check each CVE matrix against your component versions, then apply the
hardening overlay for the gaps. Roll out PodSecurity in audit/warn mode first.

## References

- `docs/operations/hardening.md` (tag `v2.31.0`). Insecure defaults
  [[CONCEPT-INSECURE_DEFAULTS]]; hardening [[PRACTICE-CLUSTER_HARDENING]]; CVE matrices above;
  advisories [[CONCEPT-SECURITY_ADVISORIES]].
