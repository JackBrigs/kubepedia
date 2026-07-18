---
id: VARIABLE-INGRESS_NGINX_SECURE_PORT
type: variable
title: ingress_nginx_secure_port
status: active
kubespray_version: ">=v2.27.0 <=v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - ingress_nginx_secure_port
tags:
  - kubernetes-apps
  - ingress-controller
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/ingress_controller/ingress_nginx/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/kubernetes-apps/ingress_controller/ingress_nginx/defaults/main.yml
    note: "default: 443"
relations: []
---
<!-- generated: variable-stub -->

# ingress_nginx_secure_port

## Summary

Kubespray variable `ingress_nginx_secure_port` — default `443`. Defined in `roles/kubernetes-apps/ingress_controller/ingress_nginx/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.30.0` of the indexed range. **Removed after `v2.30.0`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/ingress_controller/ingress_nginx/defaults/main.yml` (Kubespray `v2.30.0`):

```yaml
ingress_nginx_secure_port: 443
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.30.0`. **Removed after `v2.30.0`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/ingress_controller/ingress_nginx/defaults/main.yml` (Kubespray `v2.30.0`).
