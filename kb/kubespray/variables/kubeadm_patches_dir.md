---
id: VARIABLE-KUBEADM_PATCHES_DIR
type: variable
title: kubeadm_patches_dir
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - kubeadm_patches_dir
tags:
  - kubernetes
  - kubeadm-common
  - variable
sources:
  - type: code
    path: roles/kubernetes/kubeadm_common/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/kubeadm_common/defaults/main.yml
    note: "default: {{ kube_config_dir }}/patches"
relations: []
---
<!-- generated: variable-stub -->

# kubeadm_patches_dir

## Summary

Kubespray variable `kubeadm_patches_dir` — default `{{ kube_config_dir }}/patches`. Defined in `roles/kubernetes/kubeadm_common/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes/kubeadm_common/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
kubeadm_patches_dir: {{ kube_config_dir }}/patches
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes/kubeadm_common/defaults/main.yml` (Kubespray `v2.31.0`).
