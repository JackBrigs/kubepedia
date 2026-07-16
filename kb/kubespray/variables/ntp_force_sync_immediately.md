---
id: VARIABLE-NTP_FORCE_SYNC_IMMEDIATELY
type: variable
title: ntp_force_sync_immediately
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - ntp_force_sync_immediately
tags:
  - ntp
  - preinstall
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/defaults/main.yml
    note: "Force an immediate time sync after NTP install; default false"
relations: []
---

# ntp_force_sync_immediately

## Summary
When true, forces an immediate time synchronization right after the NTP package is installed, which is useful on freshly provisioned systems. Default is `false`.

## Implementation
Defined in `roles/kubernetes/preinstall/defaults/main.yml` (line 74) as `ntp_force_sync_immediately: false`. The value is unchanged across v2.29.0-v2.31.0 (same file and line in all four tags).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant when NTP is being installed (`ntp_enabled: true`). Related: `ntp_enabled`, `ntp_manage_config`.

## References
- roles/kubernetes/preinstall/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
