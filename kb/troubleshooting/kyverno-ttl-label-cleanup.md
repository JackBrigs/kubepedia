---
id: TROUBLE-KYVERNO_TTL_CLEANUP
type: troubleshooting
title: "Kyverno silently deletes any resource labeled cleanup.kyverno.io/ttl"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.18.2"
verified_at: "2026-07-18"
confidence: verified
aliases:
  - cleanup.kyverno.io/ttl
  - kyverno ttl deletes resource
  - kyverno resources disappearing
  - kyverno label based cleanup
  - LabelCleanupTtl
tags:
  - kyverno
  - troubleshooting
  - cleanup
  - data-loss
sources:
  - type: code
    path: api/kyverno/constants.go
    url: https://github.com/kyverno/kyverno/blob/v1.18.2/api/kyverno/constants.go
    note: "LabelCleanupTtl = cleanup.kyverno.io/ttl (L9); propagation-policy label (L20)"
  - type: code
    path: pkg/controllers/ttl/controller.go
    url: https://github.com/kyverno/kyverno/blob/v1.18.2/pkg/controllers/ttl/controller.go
    note: "watches every resource for the ttl label; value = Go duration / ISO-8601 datetime / date (L140-149); reconcile 1m"
relations:
  - type: see_also
    target: CONCEPT-KYVERNO_CONTROLLERS
  - type: see_also
    target: CONCEPT-ADDON_KYVERNO
---

# Kyverno silently deletes any resource labeled cleanup.kyverno.io/ttl

## Summary

Independent of any CleanupPolicy object, Kyverno's **TTL controller watches *every* resource** for the
label **`cleanup.kyverno.io/ttl`** and **deletes** it once the value elapses. A label copied from a
template, or propagated onto generated resources, makes objects **vanish with no policy referencing
them** — a nasty "where did my resource go?" that an audit of CleanupPolicies won't explain.

## Problem

- Resources disappear on a schedule with no CleanupPolicy pointing at them.
- A label accidentally carried by a manifest template / Helm chart / a Kyverno `generate` rule causes
  unexpected deletions.
- Deletion cascades (or doesn't) unexpectedly depending on the propagation label.

## Context

- Applies to Kyverno **1.18.x** ([[CONCEPT-ADDON_KYVERNO]]); the TTL controller is a distinct component
  ([[CONCEPT-KYVERNO_CONTROLLERS]]).
- The trigger is purely the label **`cleanup.kyverno.io/ttl`** (`LabelCleanupTtl`,
  `api/kyverno/constants.go`@v1.18.2 L9) — **no CleanupPolicy needed**.
- The value parses as a **Go duration** (`24h`), an **ISO-8601 datetime**, or a **date**
  (`pkg/controllers/ttl/controller.go`@v1.18.2 L140-149; utils L54-63). Reconcile interval
  `ttlController.reconciliationInterval: 1m`.
- Deletion propagation is controlled by the label `cleanup.kyverno.io/propagation-policy`
  (`constants.go`@v1.18.2 L20).

## Diagnostics

- On a vanished resource's kind: `kubectl get <kind> -A -l cleanup.kyverno.io/ttl -o wide` — anything
  still carrying the label is on a countdown.
- Check for the label in your manifests/Helm templates and in any Kyverno `generate` rule's
  `synchronize`/labels (generated children may inherit it).
- Kyverno **cleanup controller** logs show the deletions.

## Known Issues

- **Fix:** remove the `cleanup.kyverno.io/ttl` label from anything that shouldn't auto-delete; audit
  templates and generate rules that might propagate it.
- **Intended use:** set it deliberately (e.g. on ephemeral test resources) with a clear duration and
  a `propagation-policy` label if children should go too.
- **Distinct from CleanupPolicy:** scheduled deletion via `CleanupPolicy`/`DeletingPolicy` objects is a
  separate mechanism; this one fires with **no object to find** — check the label first when resources
  vanish.

## References

- Kyverno `api/kyverno/constants.go`, `pkg/controllers/ttl/` (@v1.18.2). Controller map
  [[CONCEPT-KYVERNO_CONTROLLERS]]; addon [[CONCEPT-ADDON_KYVERNO]].
