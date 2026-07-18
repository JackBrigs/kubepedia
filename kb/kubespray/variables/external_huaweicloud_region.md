---
id: VARIABLE-EXTERNAL_HUAWEICLOUD_REGION
type: variable
title: external_huaweicloud_region
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - external_huaweicloud_region
tags:
  - kubernetes-apps
  - external-cloud-controller
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/external_cloud_controller/huaweicloud/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/external_cloud_controller/huaweicloud/defaults/main.yml
    note: "default: {{ lookup('env', 'OS_REGION_NAME') }}"
relations: []
---
<!-- generated: variable-stub -->

# external_huaweicloud_region

## Summary

Kubespray variable `external_huaweicloud_region` — default `{{ lookup('env', 'OS_REGION_NAME') }}`. Defined in `roles/kubernetes-apps/external_cloud_controller/huaweicloud/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/external_cloud_controller/huaweicloud/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
external_huaweicloud_region: {{ lookup('env', 'OS_REGION_NAME') }}
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/external_cloud_controller/huaweicloud/defaults/main.yml` (Kubespray `v2.31.0`).
