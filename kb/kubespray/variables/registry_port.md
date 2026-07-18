---
id: VARIABLE-REGISTRY_PORT
type: variable
title: registry_port
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - registry_port
tags:
  - kubernetes-apps
  - registry
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/registry/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/registry/defaults/main.yml
    note: "default: 5000"
relations: []
---
<!-- generated: variable-stub -->

# registry_port

## Summary

Kubespray variable `registry_port` — default `5000`. Defined in `roles/kubernetes-apps/registry/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/registry/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
registry_port: 5000
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/registry/defaults/main.yml` (Kubespray `v2.31.0`).
