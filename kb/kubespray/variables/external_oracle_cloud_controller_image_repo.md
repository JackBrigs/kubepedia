---
id: VARIABLE-EXTERNAL_ORACLE_CLOUD_CONTROLLER_IMAGE_REPO
type: variable
title: external_oracle_cloud_controller_image_repo
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - external_oracle_cloud_controller_image_repo
tags:
  - kubernetes-apps
  - external-cloud-controller
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/external_cloud_controller/oci/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/external_cloud_controller/oci/defaults/main.yml
    note: "default: ghcr.io/oracle/cloud-provider-oci"
relations: []
---
<!-- generated: variable-stub -->

# external_oracle_cloud_controller_image_repo

## Summary

Kubespray variable `external_oracle_cloud_controller_image_repo` — default `ghcr.io/oracle/cloud-provider-oci`. Defined in `roles/kubernetes-apps/external_cloud_controller/oci/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/external_cloud_controller/oci/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
external_oracle_cloud_controller_image_repo: ghcr.io/oracle/cloud-provider-oci
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/external_cloud_controller/oci/defaults/main.yml` (Kubespray `v2.31.0`).
