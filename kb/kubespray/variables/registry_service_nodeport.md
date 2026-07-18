---
id: VARIABLE-REGISTRY_SERVICE_NODEPORT
type: variable
title: registry_service_nodeport
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - registry_service_nodeport
tags:
  - kubernetes-apps
  - registry
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/registry/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/registry/defaults/main.yml
    note: "default: (empty)"
relations: []
---
<!-- generated: variable-stub -->

# registry_service_nodeport

## Summary

Kubespray variable `registry_service_nodeport` — default `(empty)`. Defined in `roles/kubernetes-apps/registry/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/registry/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
registry_service_nodeport: (empty)
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/registry/defaults/main.yml` (Kubespray `v2.31.0`).
