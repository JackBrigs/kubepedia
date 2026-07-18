---
id: VARIABLE-CILIUM_TOFQDNS_ENABLE_POLLER
type: variable
title: cilium_tofqdns_enable_poller
status: active
kubespray_version: ">=v2.27.0 <=v2.27.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - cilium_tofqdns_enable_poller
tags:
  - network-plugin
  - cilium
  - variable
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.27.1/roles/network_plugin/cilium/defaults/main.yml
    note: "default: false"
relations: []
---
<!-- generated: variable-stub -->

# cilium_tofqdns_enable_poller

## Summary

Kubespray variable `cilium_tofqdns_enable_poller` — default `false`. Defined in `roles/network_plugin/cilium/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.27.1` of the indexed range. **Removed after `v2.27.1`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/network_plugin/cilium/defaults/main.yml` (Kubespray `v2.27.1`):

```yaml
cilium_tofqdns_enable_poller: false
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.27.1`. **Removed after `v2.27.1`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/network_plugin/cilium/defaults/main.yml` (Kubespray `v2.27.1`).
