---
id: VARIABLE-KUBEADM_SCALE_DOWN_COREDNS_ENABLED
type: variable
title: kubeadm_scale_down_coredns_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubeadm_scale_down_coredns_enabled
tags:
  - kubeadm
  - coredns
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Whether kubeadm scales down the CoreDNS deployment; default true"
relations:
  - type: see_also
    target: CONFIG-KUBEADM_CONFIG_API_VERSION
---

# kubeadm_scale_down_coredns_enabled

## Summary
Controls whether the CoreDNS deployment is scaled down during control-plane setup (Kubespray manages CoreDNS separately from kubeadm's addon). Default is `true`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml`:

```yaml
kubeadm_scale_down_coredns_enabled: true
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. Line number shifts: line 48 in v2.29.x, line 51 in v2.30.0/v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Part of the `kubernetes/control-plane` role.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
