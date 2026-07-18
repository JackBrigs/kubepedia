---
id: VARIABLE-MULTUS_CONF_FILE
type: variable
title: multus_conf_file
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - multus_conf_file
tags:
  - network-plugin
  - multus
  - variable
sources:
  - type: code
    path: roles/network_plugin/multus/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/multus/defaults/main.yml
    note: "default: auto"
relations: []
---
<!-- generated: variable-stub -->

# multus_conf_file

## Summary

Kubespray variable `multus_conf_file` — default `auto`. Defined in `roles/network_plugin/multus/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/network_plugin/multus/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
multus_conf_file: auto
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/network_plugin/multus/defaults/main.yml` (Kubespray `v2.31.0`).
