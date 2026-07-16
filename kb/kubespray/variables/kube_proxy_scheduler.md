---
id: VARIABLE-KUBE_PROXY_SCHEDULER
type: variable
title: kube_proxy_scheduler
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_proxy_scheduler
tags:
  - kube-proxy
  - ipvs
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    note: "Defines kube_proxy_scheduler: rr"
relations: []
---

# kube_proxy_scheduler

## Summary
Sets the IPVS scheduler algorithm used by kube-proxy in IPVS mode (`ipvs.scheduler`). Default is `rr` (round-robin).

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/kube-proxy.yml`:

```yaml
kube_proxy_scheduler: rr
```

Rendered inside the IPVS section of the kube-proxy config via the kubeadm templates as `scheduler: {{ kube_proxy_scheduler }}` (`kubeadm-config.v1beta3.yaml.j2` / `kubeadm-config.v1beta4.yaml.j2`; v2.31.0 uses only the v1beta4 template). The default `rr` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant only when kube-proxy runs in IPVS mode.

## References
- roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
