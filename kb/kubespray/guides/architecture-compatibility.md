---
id: PRACTICE-ARCHITECTURE_COMPATIBILITY
type: best_practice
title: "CPU architecture (amd64/arm64) feature compatibility"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - architecture-compatibility
tags:
  - operations
  - arch
sources:
  - type: docs
    path: docs/advanced/arch.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/advanced/arch.md
    note: "digest of the tag doc"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# CPU architecture (amd64/arm64) feature compatibility

## Summary

The node CPU architecture (amd64, arm64, or mixed) constrains which CNI plugins and features are usable. Cilium works on amd64 and arm64 but **not** on a mixed amd64+arm64 cluster; only Calico supports mixed clusters among CNIs.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- Matters when planning heterogeneous (mixed-arch) clusters or arm64 deployments.

## Implementation

Per the compatibility table: Cilium (our indexed CNI) is supported on pure amd64 and pure arm64, but **not** on amd64+arm64 mixed. Flannel/Canal/kube-router are amd64-only. If you need a mixed-arch cluster with Cilium, that combination is unsupported — use a single architecture, or Calico for mixed. Verify image availability for the target arch.

## References

- `docs/advanced/arch.md` (tag v2.31.0 `1c9add4`).
