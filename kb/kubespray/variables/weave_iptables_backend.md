---
id: VARIABLE-WEAVE_IPTABLES_BACKEND
type: variable
title: weave_iptables_backend
status: active
kubespray_version: ">=v2.27.0 <=v2.28.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - weave_iptables_backend
tags:
  - network-plugin
  - weave
  - variable
sources:
  - type: code
    path: roles/network_plugin/weave/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.28.1/roles/network_plugin/weave/defaults/main.yml
    note: "default: ~"
relations: []
---
<!-- generated: variable-stub -->

# weave_iptables_backend

## Summary

Kubespray variable `weave_iptables_backend` — default `~`. Defined in `roles/network_plugin/weave/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.28.1` of the indexed range. **Removed after `v2.28.1`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/network_plugin/weave/defaults/main.yml` (Kubespray `v2.28.1`):

```yaml
weave_iptables_backend: ~
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.28.1`. **Removed after `v2.28.1`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/network_plugin/weave/defaults/main.yml` (Kubespray `v2.28.1`).
