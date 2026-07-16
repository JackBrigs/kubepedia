---
id: VARIABLE-KUBELET_SWAP_BEHAVIOR
type: variable
title: kubelet_swap_behavior
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_swap_behavior
tags:
  - kubelet
  - swap
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Kubelet swap behavior when swap is enabled; default LimitedSwap"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kubelet_swap_behavior

## Summary
Controls kubelet swap behavior (memory swap `swapBehavior`) when swap is used on nodes. Default is `LimitedSwap`. Sits alongside `kubelet_fail_swap_on` in the swap settings block.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kubelet_swap_behavior: LimitedSwap
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 22 in v2.29.0/v2.29.1/v2.30.0, line 25 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related to `kubelet_fail_swap_on` (default true), which must be disabled for swap to be used.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
