---
id: VARIABLE-KUBE_POD_SECURITY_DEFAULT_AUDIT_VERSION
type: variable
title: kube_pod_security_default_audit_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_pod_security_default_audit_version
tags:
  - security
  - pod-security
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Defines kube_pod_security_default_audit_version pinned to the cluster Kubernetes minor version"
relations: []
---

# kube_pod_security_default_audit_version

## Summary
Kubernetes version against which the default Pod Security Admission `audit` level is evaluated. Defaults to `v{{ kube_major_version }}`, pinning the audit policy to the cluster's Kubernetes minor version.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml`:

```yaml
kube_pod_security_default_audit_version: "v{{ kube_major_version }}"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. It takes effect only when `kube_pod_security_use_default: true` and pairs with `kube_pod_security_default_audit`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `kube_major_version`. Related variables: `kube_pod_security_default_audit`, `kube_pod_security_default_enforce_version`, `kube_pod_security_default_warn_version`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
