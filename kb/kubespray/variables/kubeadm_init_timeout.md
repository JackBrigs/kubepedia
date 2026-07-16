---
id: VARIABLE-KUBEADM_INIT_TIMEOUT
type: variable
title: kubeadm_init_timeout
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubeadm_init_timeout
tags:
  - kubeadm
  - control-plane
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Timeout for the first control-plane kubeadm init; default 300s"
relations: []
---

# kubeadm_init_timeout

## Summary
Timeout applied when initializing the first control-plane node with `kubeadm init`. Default value is `300s`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kubeadm_init_timeout: 300s
```

Preceded by the comment `## The timeout for init first control-plane`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 42 in v2.29.x/v2.30.0, line 41 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Governs how long Kubespray waits for the first control-plane `kubeadm init` to complete.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
