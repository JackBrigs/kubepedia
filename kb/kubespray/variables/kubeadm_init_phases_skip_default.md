---
id: VARIABLE-KUBEADM_INIT_PHASES_SKIP_DEFAULT
type: variable
title: kubeadm_init_phases_skip_default
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubeadm_init_phases_skip_default
tags:
  - kubeadm
  - control-plane
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Base list of kubeadm init phases skipped during control plane setup; default [ \"addon/coredns\" ]"
relations:
  - type: see_also
    target: CONFIG-KUBEADM_CONFIG_API_VERSION
---

# kubeadm_init_phases_skip_default

## Summary
Base list of `kubeadm init` phases that are always skipped during control plane setup. Its default is `[ "addon/coredns" ]` (CoreDNS is deployed separately by Kubespray). This list is the starting point that `kubeadm_init_phases_skip` extends conditionally (for example adding `addon/kube-proxy` for certain CNIs).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kubeadm_init_phases_skip_default: [ "addon/coredns" ]
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number shifts, e.g. line 50 in v2.29.x/v2.30.0, line 49 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Consumed by `kubeadm_init_phases_skip`, which appends `["addon/kube-proxy"]` under conditions like kube-router service proxy, Cilium kube-proxy replacement, Calico BPF, or `kube_proxy_remove`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
