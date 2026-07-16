---
id: VARIABLE-CERT_MANAGEMENT
type: variable
title: cert_management
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cert_management
tags:
  - certificates
  - etcd
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Method used to manage cluster certificates; default script"
relations: []
---

# cert_management

## Summary
Selects the mechanism Kubespray uses to generate and manage cluster certificates. Default value is `script`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
cert_management: script
```

It sits alongside the containerized control-plane / etcd settings (near `etcd_deployment_type`). The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray `>=v2.29.0 <=v2.31.0`. Related to certificate settings such as `certificates_duration` and `certificates_key_size`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
