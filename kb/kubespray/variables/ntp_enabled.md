---
id: VARIABLE-NTP_ENABLED
type: variable
title: ntp_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - ntp_enabled
tags:
  - ntp
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Starts and enables the ntpd/chrony service at boot; default false"
relations: []
---

# ntp_enabled

## Summary
Controls whether Kubespray installs, starts, and enables the NTP service (ntpd or chrony) at system boot. Default is `false`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as `ntp_enabled: false`. The value is unchanged across v2.29.0-v2.31.0 (line number shifts: 788 in v2.29.0/v2.29.1, 791 in v2.30.0, 810 in v2.31.0). The sample inventory `inventory/sample/group_vars/all/all.yml` carries the same default.

## Compatibility
Kubespray v2.29.0 through v2.31.0. When true, the package named by `ntp_package` is installed. Related: `ntp_package`, `ntp_manage_config`, `ntp_force_sync_immediately`, `ntp_timezone`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
