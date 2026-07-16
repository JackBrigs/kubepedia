---
id: VARIABLE-ETCD_IMAGE_TAG
type: variable
title: etcd_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_image_tag
tags:
  - etcd
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Computes etcd_image_tag as v{{ etcd_version }}"
relations: []
---

# etcd_image_tag

## Summary
The container image tag for etcd, derived from the etcd version. Computed as `v{{ etcd_version }}`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
etcd_image_tag: "v{{ etcd_version }}"
```

Used by `netcheck_etcd_image_tag` and the download image list in the same file, and consumed in `roles/etcd/templates/etcd.j2`, `etcd-events.j2`, `roles/etcdctl_etcdutl/tasks/main.yml`, `roles/etcd/tasks/install_docker.yml`, and the kubeadm-config / kubeadm-images templates. The computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (the underlying `etcd_version` differs per release).

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Depends on `etcd_version`. Related: `etcd_image_repo`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
