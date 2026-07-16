---
id: VARIABLE-ALB_INGRESS_IMAGE_REPO
type: variable
title: alb_ingress_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - alb_ingress_image_repo
tags:
  - aws
  - ingress
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines the container image repository for the AWS ALB ingress controller"
relations: []
---

# alb_ingress_image_repo

## Summary
Container image repository for the AWS ALB (Application Load Balancer) ingress controller. Default is `{{ docker_image_repo }}/amazon/aws-alb-ingress-controller`, derived from the configured `docker_image_repo`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:
```yaml
alb_ingress_image_repo: "{{ docker_image_repo }}/amazon/aws-alb-ingress-controller"
```
The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number varies).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `docker_image_repo`; paired with `alb_ingress_image_tag`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
