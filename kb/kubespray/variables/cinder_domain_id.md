---
id: VARIABLE-CINDER_DOMAIN_ID
type: variable
title: cinder_domain_id
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - cinder_domain_id
tags:
  - kubernetes-apps
  - csi-driver
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/csi_driver/cinder/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/csi_driver/cinder/defaults/main.yml
    note: "default: {{ lookup('env', 'OS_USER_DOMAIN_ID') }}"
relations: []
---
<!-- generated: variable-stub -->

# cinder_domain_id

## Summary

Kubespray variable `cinder_domain_id` — default `{{ lookup('env', 'OS_USER_DOMAIN_ID') }}`. Defined in `roles/kubernetes-apps/csi_driver/cinder/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/csi_driver/cinder/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
cinder_domain_id: {{ lookup('env', 'OS_USER_DOMAIN_ID') }}
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/csi_driver/cinder/defaults/main.yml` (Kubespray `v2.31.0`).
