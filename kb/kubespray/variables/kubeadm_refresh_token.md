---
id: VARIABLE-KUBEADM_REFRESH_TOKEN
type: variable
title: kubeadm_refresh_token
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubeadm_refresh_token
tags:
  - kubeadm
  - token
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Whether to refresh the kubeadm bootstrap token; default true"
relations: []
---

# kubeadm_refresh_token

## Summary
Controls whether Kubespray refreshes the kubeadm bootstrap token used for joining nodes. Default is `true`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml`:

```yaml
kubeadm_refresh_token: true
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. The line number shifts between tags: line 45 in v2.29.x, line 48 in v2.30.0/v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Part of the `kubernetes/control-plane` role's kubeadm token handling.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
