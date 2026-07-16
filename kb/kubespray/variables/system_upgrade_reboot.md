---
id: VARIABLE-SYSTEM_UPGRADE_REBOOT
type: variable
title: system_upgrade_reboot
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - system_upgrade_reboot
tags:
  - upgrade
  - reboot
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Controls node reboot behavior on OS upgrade: on-upgrade"
relations: []
---

# system_upgrade_reboot

## Summary
Controls whether nodes reboot in connection with an OS package upgrade. Default is `on-upgrade`; the in-code comment documents the alternatives `never` and `always`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as `system_upgrade_reboot: on-upgrade  # never, always`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0; only its line number shifts (781 in v2.29.0/v2.29.1, 784 in v2.30.0, 803 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Accepted values per the code comment: `on-upgrade` (default), `never`, `always`. Related to `system_upgrade`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
