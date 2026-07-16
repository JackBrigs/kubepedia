---
id: VARIABLE-DEFAULT_KUBELET_CONFIG_DIR
type: variable
title: default_kubelet_config_dir
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - default_kubelet_config_dir
tags:
  - kubelet
  - config
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Directory used for dynamic kubelet configuration; computed from kube_config_dir."
relations: []
---

# default_kubelet_config_dir

## Summary
Sets the directory used for dynamic kubelet configuration. Default is a computed expression `{{ kube_config_dir }}/dynamic_kubelet_dir`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` and also surfaced in the sample inventory at `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`:

```yaml
default_kubelet_config_dir: "{{ kube_config_dir }}/dynamic_kubelet_dir"
```

The value (the same computed expression) is unchanged across v2.29.0-v2.31.0 in both files.

## Compatibility
Present across Kubespray v2.29.0-v2.31.0. Derives from `kube_config_dir`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
