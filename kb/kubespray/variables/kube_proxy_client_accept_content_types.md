---
id: VARIABLE-KUBE_PROXY_CLIENT_ACCEPT_CONTENT_TYPES
type: variable
title: kube_proxy_client_accept_content_types
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_proxy_client_accept_content_types
tags:
  - networking
  - kube-proxy
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    note: "Accept header content types kube-proxy sends to the API server; defaults to empty string."
relations: []
---

# kube_proxy_client_accept_content_types

## Summary
Sets the `acceptContentTypes` field of the kube-proxy client connection, overriding the Accept header sent when kube-proxy connects to the API server (which otherwise defaults to `application/json`). Defaults to an empty string `''`, meaning kube-proxy uses its built-in default.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/kube-proxy.yml` as:

```yaml
kube_proxy_client_accept_content_types: ''
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 8 in every tag).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Part of the kube-proxy `clientConnection` defaults; related variables include `kube_proxy_client_burst` and other `kube_proxy_client_*` tunables in the same file.

## References
- roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
