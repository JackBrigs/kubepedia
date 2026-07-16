---
id: VARIABLE-KUBE_CONFIG_DIR
type: variable
title: kube_config_dir
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_config_dir
tags:
  - paths
  - configuration
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Base directory for Kubernetes configuration; default /etc/kubernetes"
relations: []
---

# kube_config_dir

## Summary
Base directory holding the Kubernetes configuration on nodes. Default is `/etc/kubernetes`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`, and identically in `roles/kubernetes/client/defaults/main.yml` (quoted `"/etc/kubernetes"`), `roles/kubernetes/preinstall/defaults/main.yml`, and `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`:

```yaml
kube_config_dir: /etc/kubernetes
```

The value `/etc/kubernetes` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0. Used as the base for derived paths such as `kube_cert_dir` (`{{ kube_config_dir }}/ssl`).

## References
- roles/kubespray_defaults/defaults/main/main.yml
- roles/kubernetes/client/defaults/main.yml
- roles/kubernetes/preinstall/defaults/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
