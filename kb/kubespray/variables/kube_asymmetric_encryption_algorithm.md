---
id: VARIABLE-KUBE_ASYMMETRIC_ENCRYPTION_ALGORITHM
type: variable
title: kube_asymmetric_encryption_algorithm
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_asymmetric_encryption_algorithm
tags:
  - certificates
  - encryption
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Asymmetric algorithm used for Kubernetes certificates/keys; default RSA-2048"
relations: []
---

# kube_asymmetric_encryption_algorithm

## Summary
Selects the asymmetric algorithm used to generate Kubernetes certificate keys. Default is `"RSA-2048"`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml`:

```yaml
kube_asymmetric_encryption_algorithm: "RSA-2048"
```

The value `"RSA-2048"` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0. Related to certificate validity variables such as `kube_cert_validity_period` and `kube_ca_cert_validity_period`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
