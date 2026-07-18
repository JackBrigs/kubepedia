---
id: VARIABLE-CILIUM_REMOVE_OLD_RESOURCES
type: variable
title: cilium_remove_old_resources
status: active
kubespray_version: ">=v2.28.1 <=v2.29.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - cilium_remove_old_resources
tags:
  - network-plugin
  - cilium
  - variable
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.1/roles/network_plugin/cilium/defaults/main.yml
    note: "default: false"
relations: []
---
<!-- generated: variable-stub -->

# cilium_remove_old_resources

## Summary

Kubespray variable `cilium_remove_old_resources` — default `false`. Defined in `roles/network_plugin/cilium/defaults/main.yml`. Present in Kubespray
`v2.28.1`–`v2.29.1` of the indexed range. **Removed after `v2.29.1`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/network_plugin/cilium/defaults/main.yml` (Kubespray `v2.29.1`):

```yaml
cilium_remove_old_resources: false
```

## Compatibility

Present in the Kubespray tags `v2.28.1`–`v2.29.1`. **Removed after `v2.29.1`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/network_plugin/cilium/defaults/main.yml` (Kubespray `v2.29.1`).
