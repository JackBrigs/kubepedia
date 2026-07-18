---
id: VARIABLE-EXTERNAL_ORACLE_LOAD_BALANCER_SECURITY_LIST_MANAGEMENT_MODE
type: variable
title: external_oracle_load_balancer_security_list_management_mode
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - external_oracle_load_balancer_security_list_management_mode
tags:
  - kubernetes-apps
  - external-cloud-controller
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/external_cloud_controller/oci/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/external_cloud_controller/oci/defaults/main.yml
    note: "default: All"
relations: []
---
<!-- generated: variable-stub -->

# external_oracle_load_balancer_security_list_management_mode

## Summary

Kubespray variable `external_oracle_load_balancer_security_list_management_mode` — default `All`. Defined in `roles/kubernetes-apps/external_cloud_controller/oci/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/external_cloud_controller/oci/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
external_oracle_load_balancer_security_list_management_mode: All
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/external_cloud_controller/oci/defaults/main.yml` (Kubespray `v2.31.0`).
