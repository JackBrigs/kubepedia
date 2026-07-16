---
id: VARIABLE-KUBE_PROXY_PORT_RANGE
type: variable
title: kube_proxy_port_range
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_proxy_port_range
tags:
  - kube-proxy
  - control-plane
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    note: "Defines kube_proxy_port_range: '' (empty by default)"
relations: []
---

# kube_proxy_port_range

## Summary
Sets the `portRange` field in the kube-proxy configuration, defining the range of host ports that may be consumed for proxying service traffic. Default is an empty string (kube-proxy default range applies).

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/kube-proxy.yml`:

```yaml
kube_proxy_port_range: ''
```

Rendered by the kubeadm config templates as `portRange: {{ kube_proxy_port_range }}` (`kubeadm-config.v1beta3.yaml.j2` / `kubeadm-config.v1beta4.yaml.j2`; v2.31.0 uses only the v1beta4 template). The empty-string default is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Part of the kube-proxy `KubeProxyConfiguration` block.

## References
- roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
