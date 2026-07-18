---
id: VARIABLE-CALICO_KUBECONFIG_WAIT_TIMEOUT
type: variable
title: calico_kubeconfig_wait_timeout
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - calico_kubeconfig_wait_timeout
tags:
  - network-plugin
  - calico-defaults
  - variable
sources:
  - type: code
    path: roles/network_plugin/calico_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/calico_defaults/defaults/main.yml
    note: "default: 300"
relations: []
---
<!-- generated: variable-stub -->

# calico_kubeconfig_wait_timeout

## Summary

Kubespray variable `calico_kubeconfig_wait_timeout` — default `300`. Defined in `roles/network_plugin/calico_defaults/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/network_plugin/calico_defaults/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
calico_kubeconfig_wait_timeout: 300
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/network_plugin/calico_defaults/defaults/main.yml` (Kubespray `v2.31.0`).
