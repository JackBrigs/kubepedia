---
id: VARIABLE-KUBE_MANIFEST_DIR
type: variable
title: kube_manifest_dir
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_manifest_dir
tags:
  - paths
  - manifests
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Directory for Kubernetes manifests; default {{ kube_config_dir }}/manifests"
relations: []
---

# kube_manifest_dir

## Summary
Directory on nodes where Kubernetes manifests are placed. Default: `{{ kube_config_dir }}/manifests`.

## Implementation
Defined as the role default in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kube_manifest_dir: "{{ kube_config_dir }}/manifests"
```

Also present in the sample inventory `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml` with the identical value. The role default takes precedence per project rules; both agree here. Unchanged across v2.29.0–v2.31.0.

## Compatibility
Kubespray v2.29.0–v2.31.0. Depends on `kube_config_dir`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
