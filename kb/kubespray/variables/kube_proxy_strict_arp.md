---
id: VARIABLE-KUBE_PROXY_STRICT_ARP
type: variable
title: kube_proxy_strict_arp
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_proxy_strict_arp
tags:
  - kube-proxy
  - ipvs
  - metallb
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    note: "Defines kube_proxy_strict_arp: false"
relations: []
---

# kube_proxy_strict_arp

## Summary
Sets the `ipvs.strictARP` field in the kube-proxy configuration. Default is `false`. Must be set to `true` for MetalLB when kube-proxy runs in IPVS mode.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/kube-proxy.yml`:

```yaml
kube_proxy_strict_arp: false
```

Also surfaced in the sample inventory (`inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`, same value `false`). Rendered as `strictARP: {{ kube_proxy_strict_arp }}` in the kubeadm templates. The MetalLB role (`roles/kubernetes-apps/metallb/tasks/main.yml`) asserts a failure when `kube_proxy_mode == 'ipvs' and not kube_proxy_strict_arp`. The default `false` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related: `kube_proxy_mode`, MetalLB deployment.

## References
- roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
- roles/kubernetes-apps/metallb/tasks/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
