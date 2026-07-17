---
id: TROUBLE-KUBELET_IMAGE_GC
type: troubleshooting
title: "kubelet: image GC can't reclaim disk — 'freed 0 bytes'"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - failed to garbage collect required amount of images
  - freed 0 bytes
  - imageGCHighThresholdPercent
  - node disk pressure images in use
tags:
  - troubleshooting
  - kubelet
  - disk
  - nodes
sources:
  - type: docs
    path: image GC 'freed 0 bytes' issue
    url: https://github.com/kubernetes/kubernetes/issues/71869
    note: "GC only deletes unreferenced images"
relations:
  - type: see_also
    target: TROUBLE-DISK_PRESSURE_EVICTION
  - type: see_also
    target: CONCEPT-TROUBLESHOOTING_MAP
---

# kubelet: image GC can't reclaim disk — 'freed 0 bytes'

## Summary

The node is under disk pressure but image GC recovers nothing: `failed to garbage collect
required amount of images. Wanted to free N bytes, but freed 0 bytes`. Image GC only deletes
**unreferenced** images — if everything is in use, or the real consumer isn't images, it frees
nothing.

## Problem

- kubelet: `failed to garbage collect required amount of images. Wanted to free … bytes, but
  freed 0 bytes`; node stays under `nodefs` pressure; DiskPressure taint/evictions
  ([[TROUBLE-DISK_PRESSURE_EVICTION]]).

## Context

- Applies to Kubernetes **1.29–1.35**. Governed by `imageGCHighThresholdPercent` /
  `imageGCLowThresholdPercent` (defaults **85 / 80**).

## Diagnostics

- **Why nothing is freed:** image GC only removes images **not referenced by any container**.
  When all pulled images are in use, GC has nothing eligible.
- **Find the real consumer** — it's usually **not** images: **writable container layers**,
  **logs** (`/var/log`), **emptyDir**, or a runaway app. Check `du -sh` on the runtime data root
  and `/var/log`.
- **Prune dangling images:** `crictl rmi --prune`.
- **Tune:** lower `imageGCHighThresholdPercent` so GC starts **earlier**, or add disk. Raising
  disk is the real fix when images genuinely dominate.

## Known Issues

- `freed 0 bytes` is a **symptom of misattribution** — chasing image GC when logs/emptyDir are
  the culprit wastes time. Measure first.

## References

- k8s issue #71869, PR #132578 (above); eviction: [[TROUBLE-DISK_PRESSURE_EVICTION]].
