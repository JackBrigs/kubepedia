---
id: VARIABLE-NODELOCALDNS_IMAGE_REPO
type: variable
title: nodelocaldns_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - nodelocaldns_image_repo
tags:
  - nodelocaldns
  - dns
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Image repository for the nodelocaldns (k8s-dns-node-cache) container"
relations:
  - type: see_also
    target: COMPONENT-NODELOCALDNS
---

# nodelocaldns_image_repo

## Summary
Container image repository for nodelocaldns (the k8s-dns-node-cache). Default: `{{ kube_image_repo }}/dns/k8s-dns-node-cache`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
nodelocaldns_image_repo: "{{ kube_image_repo }}/dns/k8s-dns-node-cache"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray range: `>=v2.29.0 <=v2.31.0`. Depends on `kube_image_repo`. Paired with `nodelocaldns_image_tag`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
