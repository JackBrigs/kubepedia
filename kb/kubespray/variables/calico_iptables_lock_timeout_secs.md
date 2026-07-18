---
id: VARIABLE-CALICO_IPTABLES_LOCK_TIMEOUT_SECS
type: variable
title: calico_iptables_lock_timeout_secs
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - calico_iptables_lock_timeout_secs
tags:
  - network-plugin
  - calico-defaults
  - variable
sources:
  - type: code
    path: roles/network_plugin/calico_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/calico_defaults/defaults/main.yml
    note: "default: 10"
relations: []
---
<!-- generated: variable-stub -->

# calico_iptables_lock_timeout_secs

## Summary

Kubespray variable `calico_iptables_lock_timeout_secs` — default `10`. Defined in `roles/network_plugin/calico_defaults/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/network_plugin/calico_defaults/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
calico_iptables_lock_timeout_secs: 10
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/network_plugin/calico_defaults/defaults/main.yml` (Kubespray `v2.31.0`).
