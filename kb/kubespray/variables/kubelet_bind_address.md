---
id: VARIABLE-KUBELET_BIND_ADDRESS
type: variable
title: kubelet_bind_address
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_bind_address
tags:
  - kubelet
  - network
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Bind address for kubelet; defaults to main_ip or :: (all interfaces)"
relations: []
---

# kubelet_bind_address

## Summary
Sets the address kubelet binds to. Per the in-code comment, set to `::` to listen on all interfaces. Defaults to the node's `main_ip`, falling back to `::` when `main_ip` is undefined.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` (line 7):

```yaml
kubelet_bind_address: "{{ main_ip | default('::') }}"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `main_ip`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
