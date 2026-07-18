---
id: CONCEPT-K8S_ORDERED_NAMESPACE_DELETION
type: concept
title: "Ordered namespace deletion — pods deleted before other resources (GA 1.34)"
status: active
kubespray_version: ">=v2.31.0 <=v2.31.0"
kubernetes_version: ">=1.33 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - OrderedNamespaceDeletion
  - namespace delete pods first
  - network policy stays until pods gone
  - kubectl delete ns ordering
tags:
  - kubernetes
  - apiserver
  - security
sources:
  - type: code
    path: keps/sig-api-machinery/5080-ordered-namespace-deletion
    url: https://github.com/kubernetes/enhancements/tree/master/keps/sig-api-machinery/5080-ordered-namespace-deletion
    note: "kep.yaml: stable/GA 1.34"
relations:
  - type: see_also
    target: CONCEPT-K8S_UPGRADE_SILENT_CHANGES
  - type: see_also
    target: CONCEPT-POD_SECURITY_STANDARDS
---

# Ordered namespace deletion — pods deleted before other resources (GA 1.34)

## Summary

When a namespace is deleted, Kubernetes now removes **pods first**, before other resources — GA in
**1.34** (`OrderedNamespaceDeletion`). Previously deletion order was effectively unordered, so a
NetworkPolicy, Secret, or RBAC object could be removed **while pods were still running**, briefly
leaving workloads without the isolation/credentials they depended on. This is a **security-relevant
behavior change** on `kubectl delete namespace`.

## Context

- Milestone (`keps/sig-api-machinery/5080-...` kep.yaml): stable/GA **1.34** (Kubespray v2.31.0).
- **What changes:** the namespace controller enforces an order — **pods terminate first**, then the
  supporting objects (NetworkPolicies, Secrets, etc.) are removed. This closes a window where, e.g., a
  NetworkPolicy protecting pods vanished before the pods did.
- **Operator impact:** namespace teardown is slightly slower (waits for pods) but **safer**; automation
  that assumed near-instant deletion of all objects should tolerate the ordered, pod-first sequence.
  Pairs with Pod Security admission ([[CONCEPT-POD_SECURITY_STANDARDS]]) in the "don't leave workloads
  unprotected" direction. No config; on from 1.34.

## References

- `keps/sig-api-machinery/5080-ordered-namespace-deletion` (kep.yaml GA 1.34). Silent changes
  [[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]]; PSA [[CONCEPT-POD_SECURITY_STANDARDS]].
