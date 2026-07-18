---
id: VARIABLE-INGRESS_NGINX_PUBLISH_SERVICE
type: variable
title: ingress_nginx_publish_service
status: active
kubespray_version: ">=v2.28.0 <=v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - ingress_nginx_publish_service
tags:
  - kubernetes-apps
  - ingress-controller
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/ingress_controller/ingress_nginx/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/kubernetes-apps/ingress_controller/ingress_nginx/defaults/main.yml
    note: "default: {{ ingress_nginx_namespace }}/ingress-nginx"
relations: []
---
<!-- generated: variable-stub -->

# ingress_nginx_publish_service

## Summary

Kubespray variable `ingress_nginx_publish_service` — default `{{ ingress_nginx_namespace }}/ingress-nginx`. Defined in `roles/kubernetes-apps/ingress_controller/ingress_nginx/defaults/main.yml`. Present in Kubespray
`v2.28.0`–`v2.30.0` of the indexed range. **Removed after `v2.30.0`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/ingress_controller/ingress_nginx/defaults/main.yml` (Kubespray `v2.30.0`):

```yaml
ingress_nginx_publish_service: {{ ingress_nginx_namespace }}/ingress-nginx
```

## Compatibility

Present in the Kubespray tags `v2.28.0`–`v2.30.0`. **Removed after `v2.30.0`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/ingress_controller/ingress_nginx/defaults/main.yml` (Kubespray `v2.30.0`).
