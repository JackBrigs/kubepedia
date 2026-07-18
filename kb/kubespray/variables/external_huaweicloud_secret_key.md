---
id: VARIABLE-EXTERNAL_HUAWEICLOUD_SECRET_KEY
type: variable
title: external_huaweicloud_secret_key
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - external_huaweicloud_secret_key
tags:
  - kubernetes-apps
  - external-cloud-controller
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/external_cloud_controller/huaweicloud/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/external_cloud_controller/huaweicloud/defaults/main.yml
    note: "default: {{ lookup('env', 'OS_SECRET_KEY') }}"
relations: []
---
<!-- generated: variable-stub -->

# external_huaweicloud_secret_key

## Summary

Kubespray variable `external_huaweicloud_secret_key` — default `{{ lookup('env', 'OS_SECRET_KEY') }}`. Defined in `roles/kubernetes-apps/external_cloud_controller/huaweicloud/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/external_cloud_controller/huaweicloud/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
external_huaweicloud_secret_key: {{ lookup('env', 'OS_SECRET_KEY') }}
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/external_cloud_controller/huaweicloud/defaults/main.yml` (Kubespray `v2.31.0`).
