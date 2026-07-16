---
id: VARIABLE-DNSAUTOSCALER_IMAGE_REPO
type: variable
title: dnsautoscaler_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - dnsautoscaler_image_repo
tags:
  - dns
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Container image repository for the DNS cluster-proportional-autoscaler"
relations: []
---

# dnsautoscaler_image_repo

## Summary
Container image repository for the DNS cluster-proportional-autoscaler. Defaults to `{{ kube_image_repo }}/cpa/cluster-proportional-autoscaler`, i.e. derived from the configured `kube_image_repo`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
dnsautoscaler_image_repo: "{{ kube_image_repo }}/cpa/cluster-proportional-autoscaler"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `kube_image_repo`; paired with `dnsautoscaler_image_tag` and `dnsautoscaler_version`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
