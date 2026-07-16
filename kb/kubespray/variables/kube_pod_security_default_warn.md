---
id: VARIABLE-KUBE_POD_SECURITY_DEFAULT_WARN
type: variable
title: kube_pod_security_default_warn
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_pod_security_default_warn
tags:
  - security
  - pod-security
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Sets the warn level of the PodSecurity admission default; defaults to restricted."
relations: []
---

# kube_pod_security_default_warn

## Summary
Sets the Pod Security Standard level for the `warn` mode of the PodSecurityAdmission plugin default configuration. Defaults to `restricted`, meaning workloads violating the restricted profile trigger a user-facing warning. Only takes effect when `kube_pod_security_use_default` is enabled.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as:

```yaml
kube_pod_security_default_warn: restricted
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 119 in v2.29.x, line 122 in v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Part of the PodSecurityAdmission plugin default block; related variables include `kube_pod_security_use_default`, `kube_pod_security_default_warn_version`, `kube_pod_security_default_enforce`, and `kube_pod_security_default_audit`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
