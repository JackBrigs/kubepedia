---
id: VARIABLE-CALICO_IPIP_MODE_IPV6
type: variable
title: calico_ipip_mode_ipv6
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - calico_ipip_mode_ipv6
tags:
  - network-plugin
  - calico-defaults
  - variable
sources:
  - type: code
    path: roles/network_plugin/calico_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/calico_defaults/defaults/main.yml
    note: "default: Never"
relations: []
---
<!-- generated: variable-stub -->

# calico_ipip_mode_ipv6

## Summary

Kubespray variable `calico_ipip_mode_ipv6` — default `Never`. Defined in `roles/network_plugin/calico_defaults/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/network_plugin/calico_defaults/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
calico_ipip_mode_ipv6: Never
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/network_plugin/calico_defaults/defaults/main.yml` (Kubespray `v2.31.0`).
