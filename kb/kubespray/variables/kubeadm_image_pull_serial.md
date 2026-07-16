---
id: VARIABLE-KUBEADM_IMAGE_PULL_SERIAL
type: variable
title: kubeadm_image_pull_serial
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubeadm_image_pull_serial
tags:
  - kubeadm
  - images
  - control-plane
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Defines kubeadm_image_pull_serial: true"
relations: []
---

# kubeadm_image_pull_serial

## Summary
Controls the `imagePullSerial` setting passed to kubeadm: whether image pulling performed by kubeadm is done serially (`true`) or in parallel (`false`). Default is `true`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as:

```yaml
kubeadm_image_pull_serial: true
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number shifts: 255 in v2.29.0/v2.29.1, 262 in v2.30.0/v2.31.0).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Consumed by the kubernetes control-plane role when rendering the kubeadm configuration.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
