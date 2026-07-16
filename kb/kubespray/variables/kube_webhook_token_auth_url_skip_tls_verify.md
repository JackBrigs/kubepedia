---
id: VARIABLE-KUBE_WEBHOOK_TOKEN_AUTH_URL_SKIP_TLS_VERIFY
type: variable
title: kube_webhook_token_auth_url_skip_tls_verify
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_webhook_token_auth_url_skip_tls_verify
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

# kube_webhook_token_auth_url_skip_tls_verify

## Summary
Controls whether TLS certificate verification is skipped when the kube-apiserver contacts the webhook token authentication endpoint. Default: `false` (TLS verification is enforced). Relevant only when `kube_webhook_token_auth` is enabled.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as:

```yaml
kube_webhook_token_auth_url_skip_tls_verify: false
```

The value is `false` and unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 148 in v2.29.0/v2.29.1, line 151 in v2.30.0/v2.31.0). It is also set in `inventory/sample/group_vars/all/all.yml` and shown as a commented sample in `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Related: `kube_webhook_token_auth`, `kube_webhook_token_auth_url`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- inventory/sample/group_vars/all/all.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
