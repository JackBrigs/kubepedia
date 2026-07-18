---
id: VARIABLE-PKG_INSTALL_RETRIES
type: variable
title: pkg_install_retries
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - pkg_install_retries
tags:
  - system-packages
  - variable
sources:
  - type: code
    path: roles/system_packages/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/system_packages/defaults/main.yml
    note: "default: 4"
relations: []
---
<!-- generated: variable-stub -->

# pkg_install_retries

## Summary

Kubespray variable `pkg_install_retries` — default `4`. Defined in `roles/system_packages/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/system_packages/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
pkg_install_retries: 4
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/system_packages/defaults/main.yml` (Kubespray `v2.31.0`).
