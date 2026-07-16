---
id: CONCEPT-POD_SECURITY_STANDARDS
type: concept
title: "Pod Security Standards in Kubespray (enforce/audit/warn)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - PodSecurity
  - Pod Security Standards
  - PSS
  - kube_pod_security_use_default
  - baseline restricted privileged
  - pod security admission
tags:
  - kubernetes
  - security
  - podsecurity
  - admission
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "kube_pod_security_* defaults (tag v2.31.0)"
relations:
  - type: see_also
    target: PRACTICE-CLUSTER_HARDENING
  - type: see_also
    target: CONFIG-APISERVER_AUDIT
---

# Pod Security Standards in Kubespray (enforce/audit/warn)

## Summary

The built-in **PodSecurity** admission controller enforces the three Pod Security
Standards — `privileged`, `baseline`, `restricted` — cluster-wide via a default policy.
Kubespray can install that default (`kube_pod_security_use_default`), off by default.
Note the **stock default enforces `baseline`** (auditing/warning at `restricted`), while
the **hardening overlay raises enforce to `restricted`** — so what you get depends on
which you enable.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`. PodSecurity is the successor to the removed
  PodSecurityPolicy.
- Defaults (`kube_pod_security_*`):
  - `kube_pod_security_use_default: false` — master switch for the cluster-wide default
    admission config.
  - `kube_pod_security_default_enforce: baseline` — **enforced** level (blocks violations).
  - `kube_pod_security_default_audit: restricted` — audited level (logs violations).
  - `kube_pod_security_default_warn: restricted` — warned level (user-facing warnings).
  - `*_version: v{{ kube_major_version }}` — pin each level to the running K8s minor.
  - `kube_pod_security_exemptions_usernames: []` — users exempt from enforcement.

## Implementation

- The three modes are independent: you can **audit/warn** at `restricted` while only
  **enforcing** `baseline` — a common rollout path (see what would break before
  enforcing).
- `kube-system` is exempt by default (so cluster add-ons keep running).
- Per-namespace overrides use the standard labels
  (`pod-security.kubernetes.io/enforce|audit|warn` = `privileged|baseline|restricted`,
  plus `…-version`), independent of the cluster default.
- **Hardening path:** `PRACTICE-CLUSTER_HARDENING` sets `kube_pod_security_use_default:
  true` **and** `kube_pod_security_default_enforce: restricted` — the strict posture.

## Compatibility

- **Stock vs hardening differ:** plain `kube_pod_security_use_default: true` enforces
  `baseline`; only the hardening overlay enforces `restricted`. Don't assume `restricted`
  unless you set it.
- Enforcing `restricted` cluster-wide will reject many off-the-shelf workloads
  (runAsNonRoot, seccomp, dropped capabilities required) — roll out via audit/warn first,
  exempt namespaces that legitimately need `privileged` (e.g. some CSI/CNI system pods).
- Pinning `*_version` to `v{kube_major_version}` keeps the policy semantics stable across
  a K8s upgrade until you bump it deliberately.

## References

- `kube_pod_security_*` defaults at tag `v2.31.0`. Hardening: [[PRACTICE-CLUSTER_HARDENING]];
  audit logging: [[CONFIG-APISERVER_AUDIT]].
