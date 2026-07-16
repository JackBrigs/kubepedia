---
id: VARIABLE-KUBE_PROXY_OOM_SCORE_ADJ
type: variable
title: kube_proxy_oom_score_adj
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_proxy_oom_score_adj
tags:
  - kube-proxy
  - control-plane
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    note: "Defines kube_proxy_oom_score_adj: -999"
relations:
  - type: see_also
    target: VARIABLE-KUBE_PROXY_MODE
---

# kube_proxy_oom_score_adj

## Summary
Sets the `oomScoreAdj` value in the kube-proxy configuration, controlling the Linux OOM killer priority of the kube-proxy process. Default is `-999`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/kube-proxy.yml`:

```yaml
kube_proxy_oom_score_adj: -999
```

Consumed by the kubeadm config templates as `oomScoreAdj: {{ kube_proxy_oom_score_adj }}` (`kubeadm-config.v1beta3.yaml.j2` / `kubeadm-config.v1beta4.yaml.j2`; v2.31.0 uses only the v1beta4 template). The default value `-999` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Part of the kube-proxy `KubeProxyConfiguration` block rendered into the kubeadm config.

## References
- roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
