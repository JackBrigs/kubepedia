---
id: VARIABLE-INGRESS_PUBLISH_STATUS_ADDRESS
type: variable
title: ingress_publish_status_address
status: active
kubespray_version: ">=v2.27.0 <=v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - ingress_publish_status_address
tags:
  - kubernetes-apps
  - ingress-controller
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/ingress_controller/ingress_nginx/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/kubernetes-apps/ingress_controller/ingress_nginx/defaults/main.yml
    note: "default: (empty)"
relations: []
---
<!-- generated: variable-stub -->

# ingress_publish_status_address

## Summary

Kubespray variable `ingress_publish_status_address` — default `(empty)`. Defined in `roles/kubernetes-apps/ingress_controller/ingress_nginx/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.30.0` of the indexed range. **Removed after `v2.30.0`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/ingress_controller/ingress_nginx/defaults/main.yml` (Kubespray `v2.30.0`):

```yaml
ingress_publish_status_address: (empty)
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.30.0`. **Removed after `v2.30.0`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/ingress_controller/ingress_nginx/defaults/main.yml` (Kubespray `v2.30.0`).
