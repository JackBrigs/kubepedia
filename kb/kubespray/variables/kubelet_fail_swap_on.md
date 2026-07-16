---
id: VARIABLE-KUBELET_FAIL_SWAP_ON
type: variable
title: kubelet_fail_swap_on
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_fail_swap_on
tags:
  - kubelet
  - swap
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Controls kubelet failSwapOn; defaults to true"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kubelet_fail_swap_on

## Summary
Controls whether kubelet refuses to start when swap is enabled on the node (kubelet `failSwapOn`). Defaults to `true`, matching upstream kubelet behavior of failing on active swap.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kubelet_fail_swap_on: true
```

The default is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 21 in v2.29.0, line 24 in v2.31.0). Some CI test inventories under `tests/files/` set it to `false`, but the role default remains `true`.

## Compatibility
Kubespray v2.29.0 through v2.31.0.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
