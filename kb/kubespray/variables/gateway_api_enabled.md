---
id: VARIABLE-GATEWAY_API_ENABLED
type: variable
title: gateway_api_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - gateway_api_enabled
tags:
  - gateway-api
  - addons
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Toggles installation of the Gateway API CRDs; default false"
relations: []
---

# gateway_api_enabled

## Summary
Toggles whether the Gateway API CRDs are installed in the cluster. Default: `false`.

## Implementation
Defined with identical value in three places: `roles/kubespray_defaults/defaults/main/main.yml`, `roles/kubernetes-apps/common_crds/gateway_api/defaults/main.yml`, and the sample inventory `inventory/sample/group_vars/k8s_cluster/addons.yml`:

```yaml
gateway_api_enabled: false
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0–v2.31.0. When enabled, drives use of `gateway_api_channel`, `gateway_api_version`, and `gateway_api_crds_download_url`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- roles/kubernetes-apps/common_crds/gateway_api/defaults/main.yml
- inventory/sample/group_vars/k8s_cluster/addons.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
