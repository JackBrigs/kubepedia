---
id: VARIABLE-UBUNTU_STOP_UNATTENDED_UPGRADES
type: variable
title: ubuntu_stop_unattended_upgrades
status: active
kubespray_version: ">=v2.28.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - ubuntu_stop_unattended_upgrades
tags:
  - bootstrap-os
  - variable
sources:
  - type: code
    path: roles/bootstrap_os/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/bootstrap_os/defaults/main.yml
    note: "default: false"
relations: []
---
<!-- generated: variable-stub -->

# ubuntu_stop_unattended_upgrades

## Summary

Kubespray variable `ubuntu_stop_unattended_upgrades` — default `false`. Defined in `roles/bootstrap_os/defaults/main.yml`. Present in Kubespray
`v2.28.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/bootstrap_os/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
ubuntu_stop_unattended_upgrades: false
```

## Compatibility

Present in the Kubespray tags `v2.28.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/bootstrap_os/defaults/main.yml` (Kubespray `v2.31.0`).
