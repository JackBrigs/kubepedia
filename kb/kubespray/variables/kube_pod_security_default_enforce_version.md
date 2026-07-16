---
id: VARIABLE-KUBE_POD_SECURITY_DEFAULT_ENFORCE_VERSION
type: variable
title: kube_pod_security_default_enforce_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_pod_security_default_enforce_version
tags:
  - security
  - pod-security
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Sets the enforce-version pin for the PodSecurity admission default; defaults to v{{ kube_major_version }}."
relations: []
---

# kube_pod_security_default_enforce_version

## Summary
Pins the Pod Security Standard version used for the `enforce` mode of the PodSecurityAdmission plugin default configuration. Defaults to `"v{{ kube_major_version }}"`, i.e. the cluster's Kubernetes minor version (e.g. `v1.31`). Only takes effect when `kube_pod_security_use_default` is enabled.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as:

```yaml
kube_pod_security_default_enforce_version: "v{{ kube_major_version }}"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number shifts: line 116 in v2.29.x, line 119 in v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Part of the PodSecurityAdmission plugin default block; related variables include `kube_pod_security_use_default`, `kube_pod_security_default_enforce`, `kube_pod_security_default_warn_version`, and `kube_pod_security_default_audit_version`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
