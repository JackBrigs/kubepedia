---
id: VARIABLE-ETCD_CERT_DIR_MODE
type: variable
title: etcd_cert_dir_mode
status: active
kubespray_version: ">=v2.27.0 <=v2.29.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - etcd_cert_dir_mode
tags:
  - etcd-defaults
  - variable
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.1/roles/etcd_defaults/defaults/main.yml
    note: "default: 0700"
relations: []
---
<!-- generated: variable-stub -->

# etcd_cert_dir_mode

## Summary

Kubespray variable `etcd_cert_dir_mode` — default `0700`. Defined in `roles/etcd_defaults/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.29.1` of the indexed range. **Removed after `v2.29.1`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/etcd_defaults/defaults/main.yml` (Kubespray `v2.29.1`):

```yaml
etcd_cert_dir_mode: 0700
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.29.1`. **Removed after `v2.29.1`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/etcd_defaults/defaults/main.yml` (Kubespray `v2.29.1`).
