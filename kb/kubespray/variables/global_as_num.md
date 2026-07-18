---
id: VARIABLE-GLOBAL_AS_NUM
type: variable
title: global_as_num
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - global_as_num
tags:
  - network-plugin
  - calico
  - variable
sources:
  - type: code
    path: roles/network_plugin/calico/rr/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/calico/rr/defaults/main.yml
    note: "default: 64512"
relations: []
---
<!-- generated: variable-stub -->

# global_as_num

## Summary

Kubespray variable `global_as_num` — default `64512`. Defined in `roles/network_plugin/calico/rr/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/network_plugin/calico/rr/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
global_as_num: 64512
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/network_plugin/calico/rr/defaults/main.yml` (Kubespray `v2.31.0`).
