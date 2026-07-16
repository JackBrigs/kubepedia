---
id: VARIABLE-KUBE_POD_SECURITY_EXEMPTIONS_NAMESPACES
type: variable
title: kube_pod_security_exemptions_namespaces
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_pod_security_exemptions_namespaces
tags:
  - security
  - pod-security
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "List of namespaces exempt from PodSecurity admission; defaults to [kube-system]."
relations: []
---

# kube_pod_security_exemptions_namespaces

## Summary
List of Kubernetes namespaces exempted from the PodSecurityAdmission plugin default configuration. Defaults to a single entry, `kube-system`, so that control-plane and system workloads are not blocked by the Pod Security Standards. Only takes effect when `kube_pod_security_use_default` is enabled.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as:

```yaml
kube_pod_security_exemptions_namespaces:
  - kube-system
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (starts at line 123 in v2.29.x, line 126 in v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Part of the PodSecurityAdmission plugin default block; related variables include `kube_pod_security_use_default`, `kube_pod_security_exemptions_usernames`, and `kube_pod_security_exemptions_runtime_class_names`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
