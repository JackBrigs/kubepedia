---
id: VARIABLE-KUBE_POD_SECURITY_DEFAULT_AUDIT
type: variable
title: kube_pod_security_default_audit
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_pod_security_default_audit
tags:
  - security
  - pod-security
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Defines kube_pod_security_default_audit default restricted"
relations: []
---

# kube_pod_security_default_audit

## Summary
Default Pod Security Admission (PSA) `audit` level applied cluster-wide when the default PSA configuration is enabled. Default is `restricted`, meaning violations of the restricted policy are audited (logged) but not blocked.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` under the PodSecurityAdmission plugin configuration:

```yaml
kube_pod_security_default_audit: restricted
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. It takes effect only when `kube_pod_security_use_default: true`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `kube_pod_security_use_default`, `kube_pod_security_default_audit_version`, `kube_pod_security_default_enforce`, `kube_pod_security_default_warn`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
