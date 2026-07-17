---
id: TROUBLE-KCM_RECONCILE_STALLS
type: troubleshooting
title: "controller-manager: GC stuck (foregroundDeletion) / quota monitor not synced"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - foregroundDeletion finalizer stuck
  - garbage collection stalls
  - quota monitor not synced
  - exceeded quota but usage stale
  - PartialObjectMetadata operation not supported
tags:
  - troubleshooting
  - controller-manager
  - garbage-collection
  - resource-quota
sources:
  - type: docs
    path: GC foregroundDeletion stuck issue
    url: https://github.com/kubernetes/kubernetes/issues/77081
    note: "deletingDependents stays false if GC misses first update"
  - type: docs
    path: quota monitor not synced issue
    url: https://github.com/kubernetes/kubernetes/issues/133737
    note: "one bad aggregated API/CRD blocks the quota controller"
relations:
  - type: see_also
    target: CONCEPT-TROUBLESHOOTING_MAP
  - type: see_also
    target: TROUBLE-NAMESPACE_STUCK_TERMINATING
---

# controller-manager: GC stuck (foregroundDeletion) / quota monitor not synced

## Summary

Two kube-controller-manager reconcile stalls with the same shape — an informer/monitor that
never syncs, so a subsystem wedges: **garbage collection** stuck on a `foregroundDeletion`
finalizer, and the **ResourceQuota** monitor not syncing so usage goes stale.

## Problem

- An object deleted with `propagationPolicy=Foreground` keeps `finalizers: [foregroundDeletion]`
  + `deletionTimestamp` forever; dependents not collected.
- `ResourceQuota.status.used` stops updating → admission wrongly blocks (`exceeded quota`) or
  wrongly admits. Logs: `timed out waiting for quota monitor sync`, `quota monitor not synced`,
  `Failed to watch *v1.PartialObjectMetadata: ... operation not supported`.

## Context

- Applies to Kubernetes **1.29–1.35**. Namespace-stuck-Terminating is a related finalizer/GC
  class ([[TROUBLE-NAMESPACE_STUCK_TERMINATING]]).

## Diagnostics

- **GC foregroundDeletion stuck:** if the GC controller misses the first update event,
  `deletingDependents` stays false and it never proceeds. **Restart kube-controller-manager** to
  re-trigger GC (documented workaround), or strip the finalizer:
  `kubectl patch <obj> --type=merge -p '{"metadata":{"finalizers":[]}}'` (issues #77081/#115570).
- **Quota monitor not synced:** a **single aggregated API / CRD that doesn't support
  `PartialObjectMetadata` List/Watch blocks the entire quota controller**, so all quota counts
  freeze. Find the offending API (`operation not supported` in the log), fix or remove it, then
  restart kcm / force a leader change to recover counts (issues #133737/#65107).
- **General pattern:** "monitor/informer not synced" → the whole controller loop is stalled;
  a kcm restart reseeds informers and is the standard unblock.

## Known Issues

- Stripping a finalizer manually skips the intended cleanup — only do it when the owner/GC is
  genuinely wedged.

## References

- kcm issues #77081/#115570 (GC), #133737/#65107 (quota) (above); namespaces:
  [[TROUBLE-NAMESPACE_STUCK_TERMINATING]].
