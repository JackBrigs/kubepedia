---
id: VARIABLE-KUBE_CERT_VALIDITY_PERIOD
type: variable
title: kube_cert_validity_period
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_cert_validity_period
tags:
  - certificates
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Validity period for Kubernetes leaf certificates; default 8760h"
relations: []
---

# kube_cert_validity_period

## Summary
Sets the validity period for Kubernetes leaf (non-CA) certificates. Default is `8760h` (1 year).

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml`:

```yaml
kube_cert_validity_period: 8760h
```

The value `8760h` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0. Related to `kube_ca_cert_validity_period` (CA certificate validity).

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
