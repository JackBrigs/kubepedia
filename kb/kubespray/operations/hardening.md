---
id: PRACTICE-HARDENING
type: best_practice
title: Cluster hardening (CIS-aligned)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-21
confidence: verified
aliases:
  - hardening
  - cis benchmark
tags:
  - security
  - hardening
  - operations
sources:
  - type: docs
    path: docs/operations/hardening.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/hardening.md
    note: "CIS-aligned hardening.yaml example (apiserver, audit, PodSecurity, kubelet)"
  - type: code
    path: roles/kubernetes/control-plane/handlers/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/handlers/main.yml
    note: "'Control plane | Restart apiserver' — the restart the hardening overlay triggers"
relations:
  - type: see_also
    target: PRACTICE-CLUSTER_HARDENING
  - type: see_also
    target: VARIABLE-KUBERNETES_AUDIT
  - type: see_also
    target: VARIABLE-KUBE_POD_SECURITY_USE_DEFAULT
  - type: see_also
    target: VARIABLE-KUBE_ENCRYPT_SECRET_DATA
---

# Cluster hardening (CIS-aligned)

## Summary

Kubespray ships a documented hardening configuration to move a cluster toward CIS
Benchmark compliance. It is applied as an extra-vars file (e.g. `hardening.yaml`)
layered on top of the inventory; most controls are **off by default** and turned
on here.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- Minimum Kubernetes `v1.23.6` for all referenced features (PodSecurity admission,
  etc.) — comfortably met by the indexed range (`>=1.31`).
- Ensure no other inventory settings override these values.

## Implementation

The `hardening.yaml` example sets, among others:

- **kube-apiserver**: `authorization_modes: ['Node','RBAC']`,
  `kube_apiserver_request_timeout: 120s`,
  `kube_apiserver_service_account_lookup: true`.
- **Audit logging**: [[VARIABLE-KUBERNETES_AUDIT]] `true`, with
  `audit_log_path`, `audit_log_maxage/maxbackups/maxsize`.
- **Pod Security**: enable the `PodSecurity` admission plugin and a default policy
  ([[VARIABLE-KUBE_POD_SECURITY_USE_DEFAULT]] and
  [[VARIABLE-KUBE_APISERVER_ENABLE_ADMISSION_PLUGINS]]).
- **Secrets at rest**: [[VARIABLE-KUBE_ENCRYPT_SECRET_DATA]].
- **kubelet**: disable the read-only port ([[VARIABLE-KUBE_READ_ONLY_PORT]] `0`),
  restrict anonymous auth, and related kubelet flags.

Apply by passing the file as extra vars to `cluster.yml`.

## Compatibility

- Verified against `v2.31.0` docs; the hardening guidance is stable across the
  indexed range. Roll out PodSecurity in audit/warn mode first to avoid rejecting
  workloads.

## Service impact

Applying the overlay to a **running** cluster is disruptive: the apiserver config changes
notify `Control plane | Restart apiserver` (pod sandbox removed) and the kubelet flags
notify `Node | restart kubelet`, so the API plane bounces and every node goes briefly
`NotReady`; `cluster.yml`'s control-plane play has no `serial`, so the control-plane
restart is parallel by default. Running workloads survive, but `PodSecurity` enforce
`restricted` starts **rejecting new pods** cluster-wide, which surfaces on the next
rollout or drain. The per-setting breakdown, the encryption-key caveat and the backout
path are in [[PRACTICE-CLUSTER_HARDENING]].

## References

- `docs/operations/hardening.md` (tag `v2.31.0` `1c9add4`). Full settings list and
  disruption breakdown: [[PRACTICE-CLUSTER_HARDENING]].
