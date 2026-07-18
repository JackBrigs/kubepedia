---
id: VARIABLE-FLANNEL_CPU_LIMIT
type: variable
title: flannel_cpu_limit
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - flannel_cpu_limit
tags:
  - network-plugin
  - flannel
  - variable
sources:
  - type: code
    path: roles/network_plugin/flannel/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/flannel/defaults/main.yml
    note: "default: 300m"
relations: []
---
<!-- generated: variable-stub -->

# flannel_cpu_limit

## Summary

Kubespray variable `flannel_cpu_limit` — default `300m`. Defined in `roles/network_plugin/flannel/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/network_plugin/flannel/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
flannel_cpu_limit: 300m
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/network_plugin/flannel/defaults/main.yml` (Kubespray `v2.31.0`).
