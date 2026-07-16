---
id: VARIABLE-GATEWAY_API_VERSION
type: variable
title: gateway_api_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - gateway_api_version
tags:
  - gateway-api
  - crds
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Version of the Gateway API CRDs to install; literal in v2.29.x, computed from checksums in v2.30.0+."
relations: []
---

# gateway_api_version

## Summary
Version of the Gateway API CRDs that Kubespray downloads and installs. In v2.29.x it is a literal `1.2.1`; from v2.30.0 it is computed as the highest (first) key of `gateway_api_standard_crds_checksums.no_arch`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`. The definition changes between tags:

| Tag | Definition | Effective value |
|-----|-----------|-----------------|
| v2.29.0 | `gateway_api_version: "1.2.1"` | 1.2.1 |
| v2.29.1 | `gateway_api_version: "1.2.1"` | 1.2.1 |
| v2.30.0 | `gateway_api_version: "{{ (gateway_api_standard_crds_checksums.no_arch \| dict2items)[0].key }}"` | 1.4.1 |
| v2.31.0 | `gateway_api_version: "{{ (gateway_api_standard_crds_checksums.no_arch \| dict2items)[0].key }}"` | 1.5.1 |

In v2.29.0/v2.29.1 the variable is also set literally to `1.2.1` in `roles/kubernetes-apps/common_crds/gateway_api/defaults/main.yml`; from v2.30.0 that role default was removed and `download.yml` is the sole definition.

## Compatibility
Kubespray v2.29.0 through v2.31.0. From v2.30.0 the effective value is driven by `gateway_api_standard_crds_checksums`. Related variables: `gateway_api_standard_crds_checksums`, `gateway_api_experimental_crds_checksums`, `gateway_api_enabled`, `gateway_api_channel`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- roles/kubernetes-apps/common_crds/gateway_api/defaults/main.yml (v2.29.0, v2.29.1)
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
