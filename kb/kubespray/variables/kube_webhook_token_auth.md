---
id: VARIABLE-KUBE_WEBHOOK_TOKEN_AUTH
type: variable
title: kube_webhook_token_auth
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_webhook_token_auth
tags:
  - authentication
  - webhook
  - apiserver
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Defines the default value false"
relations: []
---

# kube_webhook_token_auth

## Summary
Enables webhook token authentication for the kube-apiserver. Default: `false` (webhook token auth disabled). When enabled, the apiserver validates bearer tokens against an external webhook service.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as:

```yaml
kube_webhook_token_auth: false
```

The value is `false` and unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 147 in v2.29.0/v2.29.1, line 150 in v2.30.0/v2.31.0). It is also set to `false` in `inventory/sample/group_vars/all/all.yml` and shown as a commented sample in `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Related: `kube_webhook_token_auth_url`, `kube_webhook_token_auth_url_skip_tls_verify`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- inventory/sample/group_vars/all/all.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
