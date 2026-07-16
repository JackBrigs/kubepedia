---
id: VARIABLE-ALB_INGRESS_IMAGE_TAG
type: variable
title: alb_ingress_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - alb_ingress_image_tag
tags:
  - aws
  - ingress
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines the image tag for the AWS ALB ingress controller (v1.1.9)"
relations: []
---

# alb_ingress_image_tag

## Summary
Container image tag for the AWS ALB ingress controller. Default is `v1.1.9`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:
```yaml
alb_ingress_image_tag: "v1.1.9"
```
The default value `v1.1.9` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number varies).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Paired with `alb_ingress_image_repo`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
