---
id: TROUBLE-RBAC_FORBIDDEN
type: troubleshooting
title: "Error from server (Forbidden) — RBAC denies the request"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - forbidden
  - RBAC denied
  - cannot list resource
  - user cannot get
  - is forbidden User
  - serviceaccount forbidden
  - access denied kubernetes
tags:
  - troubleshooting
  - rbac
  - authorization
  - security
sources:
  - type: docs
    path: Kubernetes RBAC authorization
    url: https://kubernetes.io/docs/reference/access-authn-authz/rbac/
    note: "Forbidden = the (user|group|serviceaccount) has no Role/ClusterRole binding granting the verb on the resource"
relations:
  - type: see_also
    target: PRACTICE-CLUSTER_ACCESS
  - type: see_also
    target: PRACTICE-CLUSTER_HARDENING
  - type: see_also
    target: CONCEPT-TROUBLESHOOTING_MAP
---

# Error from server (Forbidden) — RBAC denies the request

## Summary

`Error from server (Forbidden): <subject> cannot <verb> resource "<res>" …` means
**RBAC** allowed authentication but not **authorization**: the identity making the call
has no `(Cluster)RoleBinding` granting that verb on that resource (in that namespace).
The error text names exactly **who**, **what verb**, and **which resource** — the fix is
to grant it, scoped as tightly as possible.

## Problem

`kubectl` (or an app using a ServiceAccount) returns
`… is forbidden: User "…" cannot list resource "pods" in API group "" in the namespace
"x"` — authentication worked (you're identified) but the action is denied.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`; `authorization_modes` is `['Node','RBAC']`
  (hardened) — RBAC is the effective authorizer ([[PRACTICE-CLUSTER_HARDENING]]).
- Authorization is **additive-deny-by-default**: nothing is allowed unless a Role/
  ClusterRole grants it and a binding attaches it to the subject.

## Diagnostics

- **Read the message** — it states `User/Group/ServiceAccount`, the **verb**
  (`get`/`list`/`create`/…), the **resource** and **apiGroup**, and the **namespace**.
- **`kubectl auth can-i <verb> <resource> [-n ns]`** — check your own access;
  `kubectl auth can-i --list` dumps everything you can do.
- **Impersonate to test a subject:** `kubectl auth can-i list pods -n x
  --as=system:serviceaccount:x:myapp` (as an admin) — confirms what *that* SA can do.
- **Find existing grants:** `kubectl get rolebindings,clusterrolebindings -A -o wide |
  grep <subject>`.

## Known Issues

Grant the missing access — **least privilege first**:

- **A user/group needs access** — bind an appropriate (Cluster)Role:
  `kubectl create rolebinding dev-view --clusterrole=view --user=<u> -n <ns>` (namespaced),
  or a ClusterRoleBinding for cluster-wide. Prefer the built-in `view`/`edit`/`admin`
  ClusterRoles over `cluster-admin`.
- **A ServiceAccount (app) needs access** — create a Role/ClusterRole with the exact
  verbs+resources and bind it to `system:serviceaccount:<ns>:<sa>`. Apps should use their
  own SA, not `default`.
- **Wrong scope** — a `RoleBinding` only grants in its namespace; for cross-namespace or
  cluster resources you need a `ClusterRoleBinding`. A common mistake is binding a
  ClusterRole with a RoleBinding and expecting cluster-wide effect (it stays namespaced).
- **apiGroup mismatch** — the Role's `apiGroups`/`resources` must match the request
  (e.g. `apps` for deployments, `""` for pods/services). The Forbidden message gives the
  exact group.

**Gotchas:**

- **Forbidden ≠ Unauthorized.** `Forbidden` (403) = authenticated but not permitted (RBAC);
  `Unauthorized` (401) = authentication failed (bad/expired cert/token —
  [[PRACTICE-CLUSTER_ACCESS]], [[CONCEPT-CLUSTER_PKI]]).
- **Don't reach for `cluster-admin`** — the CNCF-cited anti-pattern is granting everyone
  cluster-admin. Bind the narrowest built-in role that works.
- A controller/operator SA hitting Forbidden after an upgrade often lost a grant its chart
  used to create — reconcile the operator's RBAC, don't hand-widen it.
- `system:anonymous`/`system:unauthenticated` Forbidden means no credentials reached the
  API (kubeconfig not loaded), not an RBAC gap.

## References

- Kubernetes RBAC reference. Access/kubeconfig: [[PRACTICE-CLUSTER_ACCESS]]; auth modes:
  [[PRACTICE-CLUSTER_HARDENING]]; symptom map: [[CONCEPT-TROUBLESHOOTING_MAP]].
