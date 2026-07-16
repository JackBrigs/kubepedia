---
id: VARIABLE-EXTERNAL_CLOUD_PROVIDER
type: variable
title: external_cloud_provider
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - external_cloud_provider
tags:
  - cloud-provider
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Selects which external cloud controller manager to install; default empty string"
relations: []
---

# external_cloud_provider

## Summary
Selects which external cloud controller manager to install when `cloud_provider` is `external`. Default is an empty string `""`. Supported values per the in-code comment are `openstack`, `vsphere`, `oci`, `huaweicloud`, `hcloud`, and `manual`; any other value fails validation.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as `external_cloud_provider: ""` (line 319 in v2.29.0/v2.29.1, line 320 in v2.30.0, line 332 in v2.31.0). The value `""` is unchanged across v2.29.0-v2.31.0; only the line number shifted.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Effective only when `cloud_provider` is set to `external`. Related: `external_hcloud_cloud` for the hcloud-specific configuration.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
