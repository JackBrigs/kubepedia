---
id: VARIABLE-CNI_BIN_OWNER
type: variable
title: cni_bin_owner
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - cni_bin_owner
tags:
  - network-plugin
  - cni
  - variable
sources:
  - type: code
    path: roles/network_plugin/cni/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cni/defaults/main.yml
    note: "default: {{ kube_owner }}"
relations: []
---
<!-- generated: variable-stub -->

# cni_bin_owner

## Summary

Kubespray variable `cni_bin_owner` — default `{{ kube_owner }}`. Defined in `roles/network_plugin/cni/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/network_plugin/cni/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
cni_bin_owner: {{ kube_owner }}
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/network_plugin/cni/defaults/main.yml` (Kubespray `v2.31.0`).
