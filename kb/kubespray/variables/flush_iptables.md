---
id: VARIABLE-FLUSH_IPTABLES
type: variable
title: flush_iptables
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - flush_iptables
tags:
  - reset
  - variable
sources:
  - type: code
    path: roles/reset/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/reset/defaults/main.yml
    note: "default: true"
relations: []
---
<!-- generated: variable-stub -->

# flush_iptables

## Summary

Kubespray variable `flush_iptables` — default `true`. Defined in `roles/reset/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/reset/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
flush_iptables: true
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/reset/defaults/main.yml` (Kubespray `v2.31.0`).
