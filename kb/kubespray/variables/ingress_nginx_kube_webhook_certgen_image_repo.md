---
id: VARIABLE-INGRESS_NGINX_KUBE_WEBHOOK_CERTGEN_IMAGE_REPO
type: variable
title: ingress_nginx_kube_webhook_certgen_image_repo
status: active
kubespray_version: ">=v2.27.0 <=v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - ingress_nginx_kube_webhook_certgen_image_repo
tags:
  - kubespray-defaults
  - variable
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "default: {{ kube_image_repo }}/ingress-nginx/kube-webhook-certgen"
relations: []
---
<!-- generated: variable-stub -->

# ingress_nginx_kube_webhook_certgen_image_repo

## Summary

Kubespray variable `ingress_nginx_kube_webhook_certgen_image_repo` — default `{{ kube_image_repo }}/ingress-nginx/kube-webhook-certgen`. Defined in `roles/kubespray_defaults/defaults/main/download.yml`. Present in Kubespray
`v2.27.0`–`v2.30.0` of the indexed range. **Removed after `v2.30.0`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/download.yml` (Kubespray `v2.30.0`):

```yaml
ingress_nginx_kube_webhook_certgen_image_repo: {{ kube_image_repo }}/ingress-nginx/kube-webhook-certgen
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.30.0`. **Removed after `v2.30.0`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubespray_defaults/defaults/main/download.yml` (Kubespray `v2.30.0`).
