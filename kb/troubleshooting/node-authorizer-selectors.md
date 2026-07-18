---
id: TROUBLE-K8S_NODE_AUTHORIZER_SELECTORS
type: troubleshooting
title: "Controller using node credentials gets Forbidden — Node authorizer tightened with selectors (GA 1.34)"
status: active
kubespray_version: ">=v2.31.0 <=v2.31.0"
kubernetes_version: ">=1.34 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - AuthorizeNodeWithSelectors forbidden
  - node authorizer restricted
  - kubelet credentials forbidden after 1.34
  - node cannot list all secrets
  - node authorization selectors
tags:
  - kubernetes
  - troubleshooting
  - auth
  - node
sources:
  - type: code
    path: keps/sig-auth/4601-authorize-with-selectors
    url: https://github.com/kubernetes/enhancements/tree/master/keps/sig-auth/4601-authorize-with-selectors
    note: "kep.yaml: AuthorizeWithSelectors/AuthorizeNodeWithSelectors alpha 1.31, beta 1.32, stable 1.34"
relations:
  - type: see_also
    target: CONCEPT-K8S_UPGRADE_SILENT_CHANGES
  - type: see_also
    target: PRACTICE-RBAC_LEAST_PRIVILEGE
  - type: see_also
    target: CONCEPT-K8S_FEATURE_GATES
---

# Controller using node credentials gets Forbidden — Node authorizer tightened with selectors (GA 1.34)

## Summary

The **Node authorizer** (which scopes what a kubelet can read/write) was tightened by
`AuthorizeNodeWithSelectors` (**GA in K8s 1.34**): a node's kubelet credentials are now restricted to
objects **related to that node** via label/field selectors, rather than being able to list broadly.
Custom controllers, DaemonSets, or tooling that (mis)use **node/kubelet credentials** to list cluster-
wide objects can start getting `Forbidden` after a cluster reaches 1.34 (Kubespray v2.31.0).

## Problem

- After upgrading to K8s 1.34 (Kubespray v2.31.0), a workload authenticating as a **node identity**
  (`system:node:<name>`, group `system:nodes`) gets `Forbidden` on LIST/GET it previously could do.
- A controller running under a node's kubelet credentials can no longer enumerate Secrets/ConfigMaps/
  Pods it doesn't "own".

## Context

- Milestone (`keps/sig-auth/4601-...` kep.yaml): alpha **1.31**, beta **1.32**, stable **1.34**. The
  restriction becomes fully enforced at GA.
- Intent: a compromised node should only reach **its own** objects (the pods scheduled to it and their
  Secrets/ConfigMaps), not the whole cluster — a real security hardening.
- The break is only for things **abusing node credentials**; normal kubelet operation is unaffected
  (kubelet already accesses only node-related objects).

## Diagnostics

- Identify the identity: check the failing request's user in an **audit log** entry — is it
  `system:node:*` / group `system:nodes`? If a controller authenticates as a node, that's the cause.
- `kubectl auth can-i list secrets --as=system:node:<node> --as-group=system:nodes` — compare before/
  after the upgrade expectation.

## Known Issues

- **Fix (correct):** give the controller its **own ServiceAccount + RBAC** with exactly the access it
  needs ([[PRACTICE-RBAC_LEAST_PRIVILEGE]]) — do not run workloads under node/kubelet credentials.
- **Do not** try to broaden the Node authorizer; it is intentionally selector-scoped. The gate
  (`AuthorizeNodeWithSelectors`) exists transitionally ([[CONCEPT-K8S_FEATURE_GATES]]) but the
  hardening is the intended end state.
- **Pre-upgrade audit:** before v2.31.0, grep audit logs for `system:node:` performing broad
  LIST/GET and migrate those consumers to dedicated ServiceAccounts
  ([[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]]).

## References

- `keps/sig-auth/4601-authorize-with-selectors` (kep.yaml stable 1.34). Silent changes
  [[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]]; RBAC [[PRACTICE-RBAC_LEAST_PRIVILEGE]]; gates
  [[CONCEPT-K8S_FEATURE_GATES]].
