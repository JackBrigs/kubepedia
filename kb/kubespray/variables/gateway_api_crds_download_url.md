---
id: VARIABLE-GATEWAY_API_CRDS_DOWNLOAD_URL
type: variable
title: gateway_api_crds_download_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - gateway_api_crds_download_url
tags:
  - gateway-api
  - crds
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Computed download URL for the Gateway API CRDs install manifest"
relations: []
---

# gateway_api_crds_download_url

## Summary
Computed URL from which the Gateway API CRDs install manifest is downloaded, built from the GitHub URL, the Gateway API version, and the selected channel.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
gateway_api_crds_download_url: "{{ github_url }}/kubernetes-sigs/gateway-api/releases/download/v{{ gateway_api_version }}/{{ gateway_api_channel }}-install.yaml"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 178 in v2.29.0, line 180 in the others).

## Compatibility
Kubespray v2.29.0–v2.31.0. Depends on `github_url`, `gateway_api_version`, and `gateway_api_channel`. Related: `gateway_api_enabled`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
