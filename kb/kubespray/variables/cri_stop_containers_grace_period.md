---
id: VARIABLE-CRI_STOP_CONTAINERS_GRACE_PERIOD
type: variable
title: cri_stop_containers_grace_period
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - cri_stop_containers_grace_period
tags:
  - reset
  - variable
sources:
  - type: code
    path: roles/reset/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/reset/defaults/main.yml
    note: "default: 0"
relations: []
---
<!-- generated: variable-stub -->

# cri_stop_containers_grace_period

## Summary

Kubespray variable `cri_stop_containers_grace_period` — default `0`. Defined in `roles/reset/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/reset/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
cri_stop_containers_grace_period: 0
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/reset/defaults/main.yml` (Kubespray `v2.31.0`).
