---
id: VARIABLE-AUTO_RENEW_CERTIFICATES
type: variable
title: auto_renew_certificates
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - auto_renew_certificates
tags:
  - certificates
  - control-plane
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Toggles automatic monthly renewal of control plane certificates, default false"
relations: []
---

# auto_renew_certificates

## Summary
Enables automatic renewal of Kubernetes control plane certificates on the first Monday of each month via a systemd timer. Default: `false`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as:

```yaml
auto_renew_certificates: false
```

The same default (`false`) is also exposed in `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. When enabled, the schedule is controlled by `auto_renew_certificates_systemd_calendar`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
