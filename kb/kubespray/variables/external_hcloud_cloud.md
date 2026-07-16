---
id: VARIABLE-EXTERNAL_HCLOUD_CLOUD
type: variable
title: external_hcloud_cloud
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - external_hcloud_cloud
tags:
  - cloud-provider
  - hcloud
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Configuration map for the Hetzner Cloud (hcloud) external cloud controller manager"
relations: []
---

# external_hcloud_cloud

## Summary
Configuration map for the Hetzner Cloud (hcloud) external cloud controller manager, used when `external_cloud_provider` is `hcloud`. Holds the API token, secret name, service account, controller image tag, and extra controller args.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` (line 502 in v2.29.0/v2.29.1, line 503 in v2.30.0, line 510 in v2.31.0) with default sub-keys: `hcloud_api_token: ""`, `token_secret_name: hcloud`, `service_account_name: cloud-controller-manager`, `controller_image_tag: "latest"`, `controller_extra_args: {}`. The same default map is also defined in the role `roles/kubernetes-apps/external_cloud_controller/hcloud/defaults/main.yml`. The map contents are unchanged across v2.29.0-v2.31.0; only line numbers shifted.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Effective when `cloud_provider` is `external` and `external_cloud_provider` is `hcloud`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- roles/kubernetes-apps/external_cloud_controller/hcloud/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
