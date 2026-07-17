---
id: TROUBLE-NAMESPACE_STUCK_TERMINATING
type: troubleshooting
title: "Namespace stuck in Terminating"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - namespace stuck terminating
  - namespace won't delete
  - namespace terminating forever
  - finalizers blocking namespace
  - apiservice unavailable namespace
tags:
  - troubleshooting
  - namespace
  - finalizers
  - api
sources:
  - type: docs
    path: Kubernetes namespaces / finalizers
    url: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/
    note: "namespace deletion blocks while contained resources have finalizers or an APIService is unavailable"
relations:
  - type: see_also
    target: TROUBLE-POD_STUCK_TERMINATING
  - type: see_also
    target: CONCEPT-TROUBLESHOOTING_MAP
---

# Namespace stuck in Terminating

## Summary

A namespace stays `Terminating` because Kubernetes can't finish removing everything inside
it. Two usual causes: a **resource with a finalizer** that never gets cleared (its
controller/operator is gone), or an **unavailable APIService** (an aggregated/CRD API the
namespace-controller can't list, so it won't declare the namespace empty). Find the
blocker rather than force-removing the finalizer blindly.

## Problem

`kubectl get ns` shows a namespace `Terminating` indefinitely; `kubectl delete ns` hangs
or returns but the namespace never disappears.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- The namespace controller deletes all contained objects, then removes the namespace's own
  `kubernetes` finalizer. It won't finish while (a) an object still has a **finalizer**
  pending, or (b) it **cannot list** a resource type because that API is down.

## Diagnostics

- **What's blocking:** `kubectl get ns <ns> -o yaml` — read `status.conditions`; modern
  Kubernetes reports `NamespaceDeletionContentFailure` /
  `NamespaceDeletionDiscoveryFailure` / `…GroupVersionParsingFailure` with the exact
  offending API group/resource.
- **Leftover objects:** `kubectl api-resources --verbs=list --namespaced -o name | xargs
  -n1 kubectl get -n <ns> --ignore-not-found` — lists anything still in the namespace.
- **APIService health:** `kubectl get apiservices | grep -v True` — an aggregated API
  (e.g. `v1beta1.metrics.k8s.io`, a webhook-backed API) that is `False`/unavailable blocks
  discovery for the whole cluster's namespace GC.
- **Finalizers:** `kubectl get <resource> -n <ns> -o json | jq '.items[].metadata |
  {name, finalizers}'` — which objects still hold finalizers.

## Known Issues

Fix the **cause**, not the symptom:

- **Unavailable APIService** — restore or **delete** the broken APIService
  (`kubectl delete apiservice <name>`). A stale metrics-server / webhook API left
  registered after the backend is gone is the classic case; once discovery succeeds the
  namespace finishes on its own.
- **Stuck finalizer on an object** — the owning controller/operator is gone, so the
  finalizer is never cleared. Restore the controller, or remove the finalizer from that
  **object** (`kubectl patch <res> <name> -n <ns> -p '{"metadata":{"finalizers":[]}}'
  --type=merge`) so the object (and then the namespace) can delete.
- **Last resort — namespace `spec.finalizers`:** removing the namespace's own
  `kubernetes` finalizer via the `finalize` subresource forces it gone, but **orphans**
  whatever was still inside (objects in etcd with no namespace). Prefer clearing the actual
  blocker; use this only when you accept the leak.

**Gotchas:**

- Force-removing the namespace finalizer is widely copy-pasted but **hides** the real
  problem (a broken API/operator) and leaves orphaned objects — diagnose the condition
  first.
- Distinct from a **pod** stuck Terminating (node/kubelet/finalizer at the pod level) —
  [[TROUBLE-POD_STUCK_TERMINATING]].

## References

- Kubernetes namespaces/finalizers. Pod-level analogue: [[TROUBLE-POD_STUCK_TERMINATING]];
  symptom map: [[CONCEPT-TROUBLESHOOTING_MAP]].
