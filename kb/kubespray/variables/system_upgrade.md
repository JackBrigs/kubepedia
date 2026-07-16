---
id: VARIABLE-SYSTEM_UPGRADE
type: variable
title: system_upgrade
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - system_upgrade
tags:
  - upgrade
  - os
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Toggles upgrading OS packages during the run: false"
relations: []
---

# system_upgrade

## Summary
Boolean toggle controlling whether Kubespray upgrades operating-system packages on nodes during a run. Default is `false` (no OS package upgrade).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as `system_upgrade: false`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0; only its line number shifts (780 in v2.29.0/v2.29.1, 783 in v2.30.0, 802 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Paired with `system_upgrade_reboot`, which governs reboot behavior after an OS upgrade.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
