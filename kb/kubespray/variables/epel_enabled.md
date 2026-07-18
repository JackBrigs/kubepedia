---
id: VARIABLE-EPEL_ENABLED
type: variable
title: epel_enabled
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - epel_enabled
tags:
  - bootstrap-os
  - variable
sources:
  - type: code
    path: roles/bootstrap_os/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/bootstrap_os/defaults/main.yml
    note: "default: false"
relations: []
---
<!-- generated: variable-stub -->

# epel_enabled

## Summary

Kubespray variable `epel_enabled` — default `false`. Defined in `roles/bootstrap_os/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/bootstrap_os/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
epel_enabled: false
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/bootstrap_os/defaults/main.yml` (Kubespray `v2.31.0`).
