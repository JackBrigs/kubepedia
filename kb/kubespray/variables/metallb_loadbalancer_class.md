---
id: VARIABLE-METALLB_LOADBALANCER_CLASS
type: variable
title: metallb_loadbalancer_class
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - metallb_loadbalancer_class
tags:
  - kubernetes-apps
  - metallb
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/metallb/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/metallb/defaults/main.yml
    note: "default: (empty)"
relations: []
---
<!-- generated: variable-stub -->

# metallb_loadbalancer_class

## Summary

Kubespray variable `metallb_loadbalancer_class` — default `(empty)`. Defined in `roles/kubernetes-apps/metallb/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/metallb/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
metallb_loadbalancer_class: (empty)
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/metallb/defaults/main.yml` (Kubespray `v2.31.0`).
