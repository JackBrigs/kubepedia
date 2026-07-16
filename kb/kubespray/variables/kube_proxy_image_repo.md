---
id: VARIABLE-KUBE_PROXY_IMAGE_REPO
type: variable
title: kube_proxy_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_proxy_image_repo
tags:
  - kube-proxy
  - image
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines kube_proxy_image_repo as {{ kube_image_repo }}/kube-proxy"
relations:
  - type: see_also
    target: VARIABLE-KUBE_PROXY_MODE
---

# kube_proxy_image_repo

## Summary
Container image repository for the kube-proxy image. Computed from `kube_image_repo` with the `/kube-proxy` suffix, i.e. `"{{ kube_image_repo }}/kube-proxy"`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
kube_proxy_image_repo: "{{ kube_image_repo }}/kube-proxy"
```

The computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 214 in v2.29.0; line 216 in v2.29.1/v2.30.0/v2.31.0).

## Compatibility
Applies to Kubespray v2.29.0–v2.31.0. Derived from `kube_image_repo`; overriding that base repo (e.g. for mirrors/offline installs) changes this value.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
