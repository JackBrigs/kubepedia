---
id: VARIABLE-CILIUM_ENABLE_BPF_CLOCK_PROBE
type: variable
title: cilium_enable_bpf_clock_probe
status: active
kubespray_version: ">=v2.27.0 <=v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - cilium_enable_bpf_clock_probe
tags:
  - network-plugin
  - cilium
  - variable
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/network_plugin/cilium/defaults/main.yml
    note: "default: true"
relations: []
---
<!-- generated: variable-stub -->

# cilium_enable_bpf_clock_probe

## Summary

Kubespray variable `cilium_enable_bpf_clock_probe` — default `true`. Defined in `roles/network_plugin/cilium/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.30.0` of the indexed range. **Removed after `v2.30.0`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/network_plugin/cilium/defaults/main.yml` (Kubespray `v2.30.0`):

```yaml
cilium_enable_bpf_clock_probe: true
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.30.0`. **Removed after `v2.30.0`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/network_plugin/cilium/defaults/main.yml` (Kubespray `v2.30.0`).
