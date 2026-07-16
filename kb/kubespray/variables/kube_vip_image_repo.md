---
id: VARIABLE-KUBE_VIP_IMAGE_REPO
type: variable
title: kube_vip_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_image_repo
tags:
  - kube-vip
  - image
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines the kube-vip container image repository (computed)"
relations:
  - type: see_also
    target: COMPONENT-KUBE_VIP
---

# kube_vip_image_repo

## Summary
Container image repository for the kube-vip image. Computed from `github_image_repo`, appending the `kube-vip/kube-vip` path and an `-iptables` suffix when `kube_vip_lb_fwdmethod == 'masquerade'`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```
kube_vip_image_repo: "{{ github_image_repo }}/kube-vip/kube-vip{{ '-iptables' if kube_vip_lb_fwdmethod == 'masquerade' else '' }}"
```

The computed expression is unchanged across v2.29.0-v2.31.0; only the line number shifts (266 in v2.29.0, 268 in v2.29.1, 269 in v2.30.0, 263 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `github_image_repo`, `kube_vip_lb_fwdmethod`, `kube_vip_image_tag`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
