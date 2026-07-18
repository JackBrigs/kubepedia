---
id: VARIABLE-METALLB_LOG_LEVEL
type: variable
title: metallb_log_level
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - metallb_log_level
tags:
  - kubernetes-apps
  - metallb
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/metallb/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/metallb/defaults/main.yml
    note: "default: info"
relations: []
---
<!-- generated: variable-stub -->

# metallb_log_level

## Summary

Kubespray variable `metallb_log_level` — default `info`. Defined in `roles/kubernetes-apps/metallb/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/metallb/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
metallb_log_level: info
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/metallb/defaults/main.yml` (Kubespray `v2.31.0`).
