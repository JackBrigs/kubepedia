---
id: VARIABLE-KUBE_WEBHOOK_AUTHORIZATION
type: variable
title: kube_webhook_authorization
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_webhook_authorization
tags:
  - authorization
  - apiserver
  - webhook
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Enables webhook authorization mode for the API server, default false"
relations: []
---

# kube_webhook_authorization

## Summary
Enables the webhook authorization mode for the Kubernetes API server. Default is `false`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as `kube_webhook_authorization: false`. The value is unchanged across v2.29.0-v2.31.0; only the line number shifts (line 155 in v2.29.0/v2.29.1, line 158 in v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `kube_webhook_authorization_url_skip_tls_verify`, `authorization_modes`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
