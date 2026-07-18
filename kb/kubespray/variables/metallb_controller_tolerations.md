---
id: VARIABLE-METALLB_CONTROLLER_TOLERATIONS
type: variable
title: metallb_controller_tolerations
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - metallb_controller_tolerations
tags:
  - kubernetes-apps
  - metallb
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/metallb/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/metallb/defaults/main.yml
    note: "default: []"
relations: []
---
<!-- generated: variable-stub -->

# metallb_controller_tolerations

## Summary

Kubespray variable `metallb_controller_tolerations` — default `[]`. Defined in `roles/kubernetes-apps/metallb/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/metallb/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
metallb_controller_tolerations: []
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/metallb/defaults/main.yml` (Kubespray `v2.31.0`).
