---
id: VARIABLE-CINDER_PASSWORD
type: variable
title: cinder_password
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - cinder_password
tags:
  - kubernetes-apps
  - csi-driver
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/csi_driver/cinder/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/csi_driver/cinder/defaults/main.yml
    note: "default: {{ lookup('env', 'OS_PASSWORD') }}"
relations: []
---
<!-- generated: variable-stub -->

# cinder_password

## Summary

Kubespray variable `cinder_password` — default `{{ lookup('env', 'OS_PASSWORD') }}`. Defined in `roles/kubernetes-apps/csi_driver/cinder/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/csi_driver/cinder/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
cinder_password: {{ lookup('env', 'OS_PASSWORD') }}
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/csi_driver/cinder/defaults/main.yml` (Kubespray `v2.31.0`).
