---
id: VARIABLE-KUBE_CERT_GROUP
type: variable
title: kube_cert_group
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_cert_group
tags:
  - certificates
  - permissions
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "OS group owning Kubernetes certificates; default kube-cert"
relations: []
---

# kube_cert_group

## Summary
OS group that owns the Kubernetes certificate files. Default is `kube-cert`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`, and identically in `roles/adduser/defaults/main.yml`, `roles/kubernetes/preinstall/defaults/main.yml`, and `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`:

```yaml
kube_cert_group: kube-cert
```

The value `kube-cert` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0. Related to `kube_cert_dir`; the group is created by the `adduser` role.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- roles/adduser/defaults/main.yml
- roles/kubernetes/preinstall/defaults/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
