---
id: VARIABLE-KUBE_CERT_COMPAT_DIR
type: variable
title: kube_cert_compat_dir
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_cert_compat_dir
tags:
  - certificates
  - paths
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Compatibility PKI directory path; default /etc/kubernetes/pki"
relations: []
---

# kube_cert_compat_dir

## Summary
Compatibility directory for the Kubernetes PKI (a stable `/etc/kubernetes/pki` path). Default is `/etc/kubernetes/pki`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as `"/etc/kubernetes/pki"`, and also in `roles/kubernetes/preinstall/defaults/main.yml` as `/etc/kubernetes/pki` (same value, unquoted).

```yaml
kube_cert_compat_dir: "/etc/kubernetes/pki"
```

The value `/etc/kubernetes/pki` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0. Related to `kube_cert_dir` and `kube_config_dir`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- roles/kubernetes/preinstall/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
