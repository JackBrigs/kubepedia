---
id: VARIABLE-FLANNEL_VXLAN_VNI
type: variable
title: flannel_vxlan_vni
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - flannel_vxlan_vni
tags:
  - network-plugin
  - flannel
  - variable
sources:
  - type: code
    path: roles/network_plugin/flannel/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/flannel/defaults/main.yml
    note: "default: 1"
relations: []
---
<!-- generated: variable-stub -->

# flannel_vxlan_vni

## Summary

Kubespray variable `flannel_vxlan_vni` — default `1`. Defined in `roles/network_plugin/flannel/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/network_plugin/flannel/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
flannel_vxlan_vni: 1
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/network_plugin/flannel/defaults/main.yml` (Kubespray `v2.31.0`).
