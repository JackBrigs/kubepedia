---
id: VARIABLE-KUBE_POD_SECURITY_EXEMPTIONS_RUNTIME_CLASS_NAMES
type: variable
title: kube_pod_security_exemptions_runtime_class_names
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_pod_security_exemptions_runtime_class_names
tags:
  - security
  - pod-security
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "List of RuntimeClass names exempt from PodSecurity admission; defaults to []."
relations: []
---

# kube_pod_security_exemptions_runtime_class_names

## Summary
List of RuntimeClass names exempted from the PodSecurityAdmission plugin default configuration. Defaults to an empty list `[]`, so no RuntimeClass is exempt by default. Only takes effect when `kube_pod_security_use_default` is enabled.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as:

```yaml
kube_pod_security_exemptions_runtime_class_names: []
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 122 in v2.29.x, line 125 in v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Part of the PodSecurityAdmission plugin default block; related variables include `kube_pod_security_use_default`, `kube_pod_security_exemptions_namespaces`, and `kube_pod_security_exemptions_usernames`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
