---
id: VARIABLE-ETCD_IMAGE_REPO
type: variable
title: etcd_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_image_repo
tags:
  - etcd
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Computes etcd_image_repo from quay_image_repo as {{ quay_image_repo }}/coreos/etcd"
relations: []
---

# etcd_image_repo

## Summary
The container image repository for etcd. Computed as `{{ quay_image_repo }}/coreos/etcd` (Quay CoreOS etcd repository by default).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
etcd_image_repo: "{{ quay_image_repo }}/coreos/etcd"
```

Referenced in the download image list of the same file and used in `roles/etcd/templates/etcd.j2`, `etcd-events.j2`, `roles/etcdctl_etcdutl/tasks/main.yml`, and the kubeadm-config / kubeadm-images templates (where the trailing `/etcd` is stripped via `regex_replace`). The computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Depends on `quay_image_repo`. Related: `etcd_image_tag`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
