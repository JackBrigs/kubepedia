---
id: VARIABLE-CINDER_TENANT_ID
type: variable
title: cinder_tenant_id
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - cinder_tenant_id
tags:
  - kubernetes-apps
  - csi-driver
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/csi_driver/cinder/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/csi_driver/cinder/defaults/main.yml
    note: "default: {{ lookup('env', 'OS_TENANT_ID') | default(lookup('env', 'OS_PROJEC…"
relations: []
---
<!-- generated: variable-stub -->

# cinder_tenant_id

## Summary

Kubespray variable `cinder_tenant_id` — default `{{ lookup('env', 'OS_TENANT_ID') | default(lookup('env', 'OS_PROJEC…`. Defined in `roles/kubernetes-apps/csi_driver/cinder/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/csi_driver/cinder/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
cinder_tenant_id: {{ lookup('env', 'OS_TENANT_ID') | default(lookup('env', 'OS_PROJEC…
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/csi_driver/cinder/defaults/main.yml` (Kubespray `v2.31.0`).
