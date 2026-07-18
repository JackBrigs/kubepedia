---
id: VARIABLE-CERT_MANAGER_NAMESPACE
type: variable
title: cert_manager_namespace
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - cert_manager_namespace
tags:
  - kubernetes-apps
  - ingress-controller
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/ingress_controller/cert_manager/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/ingress_controller/cert_manager/defaults/main.yml
    note: "default: cert-manager"
relations: []
---
<!-- generated: variable-stub -->

# cert_manager_namespace

## Summary

Kubespray variable `cert_manager_namespace` — default `cert-manager`. Defined in `roles/kubernetes-apps/ingress_controller/cert_manager/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/ingress_controller/cert_manager/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
cert_manager_namespace: cert-manager
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/ingress_controller/cert_manager/defaults/main.yml` (Kubespray `v2.31.0`).
