---
id: VARIABLE-KUBE_PROXY_CLIENT_CONTENT_TYPE
type: variable
title: kube_proxy_client_content_type
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_proxy_client_content_type
tags:
  - kube-proxy
  - networking
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    note: "Defines clientConnection.contentType for kube-proxy; default application/vnd.kubernetes.protobuf"
relations:
  - type: see_also
    target: VARIABLE-KUBE_PROXY_MODE
---

# kube_proxy_client_content_type

## Summary
Content type used when kube-proxy sends data to the API server (the `clientConnection.contentType` field of the KubeProxyConfiguration). Default is `application/vnd.kubernetes.protobuf`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/kube-proxy.yml`:

```yaml
kube_proxy_client_content_type: application/vnd.kubernetes.protobuf
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (same file, line 14 in each tag).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Part of the kube-proxy `clientConnection` block alongside `kube_proxy_client_kubeconfig` and `kube_proxy_client_qps`.

## References
- roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
