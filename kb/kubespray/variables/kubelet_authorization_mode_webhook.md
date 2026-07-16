---
id: VARIABLE-KUBELET_AUTHORIZATION_MODE_WEBHOOK
type: variable
title: kubelet_authorization_mode_webhook
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_authorization_mode_webhook
tags:
  - kubelet
  - security
  - authorization
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines kubelet_authorization_mode_webhook: true"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kubelet_authorization_mode_webhook

## Summary
When enabled, access to the kubelet API requires authorization by delegation to the API server (webhook mode). Default is `true`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
kubelet_authorization_mode_webhook: true
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 582 in v2.29.0/v2.29.1, 583 in v2.30.0, 602 in v2.31.0).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Related variable: `kubelet_authentication_token_webhook`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
