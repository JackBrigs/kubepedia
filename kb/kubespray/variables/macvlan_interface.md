---
id: VARIABLE-MACVLAN_INTERFACE
type: variable
title: macvlan_interface
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - macvlan_interface
tags:
  - network-plugin
  - macvlan
  - variable
sources:
  - type: code
    path: roles/network_plugin/macvlan/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/macvlan/defaults/main.yml
    note: "default: eth0"
relations: []
---
<!-- generated: variable-stub -->

# macvlan_interface

## Summary

Kubespray variable `macvlan_interface` — default `eth0`. Defined in `roles/network_plugin/macvlan/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/network_plugin/macvlan/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
macvlan_interface: eth0
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/network_plugin/macvlan/defaults/main.yml` (Kubespray `v2.31.0`).
