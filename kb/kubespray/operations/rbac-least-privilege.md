---
id: PRACTICE-RBAC_LEAST_PRIVILEGE
type: best_practice
title: "RBAC least privilege (and don't mix SSH + API trust)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - rbac least privilege
  - no blanket cluster-admin
  - kubespray admin.conf security
  - ssh vs api trust boundary
tags:
  - best-practice
  - rbac
  - security
  - kubespray
sources:
  - type: docs
    path: Kubernetes RBAC
    url: https://kubernetes.io/docs/reference/access-authn-authz/rbac/
    note: "Roles/ClusterRoles, least privilege"
relations:
  - type: see_also
    target: TROUBLE-RBAC_FORBIDDEN
  - type: see_also
    target: CONCEPT-K8S_1_29_CHANGES
  - type: see_also
    target: PRACTICE-HARDENING
---

# RBAC least privilege (and don't mix SSH + API trust)

## Summary

Grant the **minimum** RBAC needed, and keep two trust boundaries separate: **SSH/host access**
(how Kubespray operates the nodes) and **Kubernetes API access** (what a user/workload can do).
A blanket `cluster-admin` collapses both and is the most common over-privilege mistake.

## Context

- Applies to Kubespray **v2.29.0–v2.31.0** / Kubernetes **1.29–1.35**. Kubespray produces an
  **`admin.conf`** kubeconfig on control-plane nodes — it is effectively cluster-admin; treat it
  like root ([[CONCEPT-K8S_1_29_CHANGES]] split `admin.conf` from break-glass `super-admin.conf`).

## Implementation

- **No blanket `cluster-admin`** for humans or CI: bind narrow `Role`/`ClusterRole`s scoped to
  the namespaces/verbs actually needed. Use groups (OIDC — [[CONCEPT-ADDON_DEX]]) rather than
  per-user bindings.
- **Workloads:** each app gets its own **ServiceAccount** with a minimal Role; never mount the
  `default` SA token if the pod doesn't call the API (`automountServiceAccountToken: false`).
  Prefer **bound/projected** tokens over static Secret tokens
  ([[TROUBLE-KCM_SA_TOKEN_CLEANUP]]).
- **Separate SSH from API:** node SSH/sudo (Kubespray's operational path) is a **different**
  trust boundary than API RBAC — a user with `kubectl` access should not automatically have SSH,
  and vice-versa. Don't hand out `admin.conf` as "read access".
- **Guard the credentials:** `admin.conf`/`super-admin.conf`, the Talos/etcd PKI, and CI kube
  configs are cluster-admin equivalents — store them in a secret manager, rotate, and audit use.
- **Audit:** enable audit logging to see who does what ([[TROUBLE-APISERVER_REQUEST_LATENCY]] for
  the performance trade-offs); review ClusterRoleBindings for stray `cluster-admin`.

## References

- Kubernetes RBAC docs (above); forbidden triage: [[TROUBLE-RBAC_FORBIDDEN]]; hardening:
  [[PRACTICE-HARDENING]]; admin split: [[CONCEPT-K8S_1_29_CHANGES]].
