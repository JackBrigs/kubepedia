---
id: VARIABLE-KUBELET_AUTHENTICATION_TOKEN_WEBHOOK
type: variable
title: kubelet_authentication_token_webhook
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_authentication_token_webhook
tags:
  - kubelet
  - security
  - authentication
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines kubelet_authentication_token_webhook: true"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kubelet_authentication_token_webhook

## Summary
When enabled, API bearer tokens (including service account tokens) can be used to authenticate to the kubelet's HTTPS endpoint. Default is `true`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
kubelet_authentication_token_webhook: true
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 579 in v2.29.0/v2.29.1, 580 in v2.30.0, 599 in v2.31.0).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Related variable: `kubelet_authorization_mode_webhook`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
