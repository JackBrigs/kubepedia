---
id: VARIABLE-KUBE_CA_CERT_VALIDITY_PERIOD
type: variable
title: kube_ca_cert_validity_period
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_ca_cert_validity_period
tags:
  - certificates
  - ca
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Validity period for Kubernetes CA certificates; default 87600h"
relations: []
---

# kube_ca_cert_validity_period

## Summary
Sets the validity period for the Kubernetes CA certificates. Default is `87600h` (10 years).

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml`:

```yaml
kube_ca_cert_validity_period: 87600h
```

The value `87600h` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0. Related to `kube_cert_validity_period` (leaf certificate validity).

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
