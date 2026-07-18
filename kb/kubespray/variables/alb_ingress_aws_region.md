---
id: VARIABLE-ALB_INGRESS_AWS_REGION
type: variable
title: alb_ingress_aws_region
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - alb_ingress_aws_region
tags:
  - kubernetes-apps
  - ingress-controller
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/ingress_controller/alb_ingress_controller/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/ingress_controller/alb_ingress_controller/defaults/main.yml
    note: "default: us-east-1"
relations: []
---
<!-- generated: variable-stub -->

# alb_ingress_aws_region

## Summary

Kubespray variable `alb_ingress_aws_region` — default `us-east-1`. Defined in `roles/kubernetes-apps/ingress_controller/alb_ingress_controller/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/ingress_controller/alb_ingress_controller/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
alb_ingress_aws_region: us-east-1
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/ingress_controller/alb_ingress_controller/defaults/main.yml` (Kubespray `v2.31.0`).
