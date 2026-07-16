---
id: VARIABLE-KUBE_CERT_DIR
type: variable
title: kube_cert_dir
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_cert_dir
tags:
  - certificates
  - paths
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Directory for Kubernetes SSL certificates; computed as {{ kube_config_dir }}/ssl"
relations: []
---

# kube_cert_dir

## Summary
Directory holding Kubernetes SSL certificates. Computed as `{{ kube_config_dir }}/ssl` (i.e. `/etc/kubernetes/ssl` by default).

## Implementation
Defined as a computed expression in `roles/kubespray_defaults/defaults/main/main.yml`, and identically in `roles/kubernetes/preinstall/defaults/main.yml` and `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`:

```yaml
kube_cert_dir: "{{ kube_config_dir }}/ssl"
```

The expression `{{ kube_config_dir }}/ssl` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0. Derived from `kube_config_dir`; related to `kube_cert_compat_dir` and `kube_cert_group`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- roles/kubernetes/preinstall/defaults/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
