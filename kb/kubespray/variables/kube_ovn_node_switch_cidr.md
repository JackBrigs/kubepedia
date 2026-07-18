---
id: VARIABLE-KUBE_OVN_NODE_SWITCH_CIDR
type: variable
title: kube_ovn_node_switch_cidr
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - kube_ovn_node_switch_cidr
tags:
  - network-plugin
  - kube-ovn
  - variable
sources:
  - type: code
    path: roles/network_plugin/kube-ovn/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/kube-ovn/defaults/main.yml
    note: "default: 100.64.0.0/16"
relations: []
---
<!-- generated: variable-stub -->

# kube_ovn_node_switch_cidr

## Summary

Kubespray variable `kube_ovn_node_switch_cidr` — default `100.64.0.0/16`. Defined in `roles/network_plugin/kube-ovn/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/network_plugin/kube-ovn/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
kube_ovn_node_switch_cidr: 100.64.0.0/16
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/network_plugin/kube-ovn/defaults/main.yml` (Kubespray `v2.31.0`).
