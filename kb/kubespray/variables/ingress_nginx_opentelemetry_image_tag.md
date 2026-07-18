---
id: VARIABLE-INGRESS_NGINX_OPENTELEMETRY_IMAGE_TAG
type: variable
title: ingress_nginx_opentelemetry_image_tag
status: active
kubespray_version: ">=v2.27.0 <=v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - ingress_nginx_opentelemetry_image_tag
tags:
  - kubespray-defaults
  - variable
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "default: v20230721-3e2062ee5"
relations: []
---
<!-- generated: variable-stub -->

# ingress_nginx_opentelemetry_image_tag

## Summary

Kubespray variable `ingress_nginx_opentelemetry_image_tag` — default `v20230721-3e2062ee5`. Defined in `roles/kubespray_defaults/defaults/main/download.yml`. Present in Kubespray
`v2.27.0`–`v2.30.0` of the indexed range. **Removed after `v2.30.0`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/download.yml` (Kubespray `v2.30.0`):

```yaml
ingress_nginx_opentelemetry_image_tag: v20230721-3e2062ee5
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.30.0`. **Removed after `v2.30.0`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubespray_defaults/defaults/main/download.yml` (Kubespray `v2.30.0`).
