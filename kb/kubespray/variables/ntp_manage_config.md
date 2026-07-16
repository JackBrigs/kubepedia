---
id: VARIABLE-NTP_MANAGE_CONFIG
type: variable
title: ntp_manage_config
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - ntp_manage_config
tags:
  - ntp
  - preinstall
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/defaults/main.yml
    note: "Whether Kubespray manages the NTP configuration file; default false"
relations: []
---

# ntp_manage_config

## Summary
Controls whether Kubespray manages (writes) the NTP daemon configuration file. Default is `false`. Several other NTP variables (`ntp_servers`, `ntp_restrict`, `ntp_driftfile`, `ntp_tinker_panic`) only take effect when this is true.

## Implementation
Defined in `roles/kubernetes/preinstall/defaults/main.yml` (line 41) as `ntp_manage_config: false`. The value is unchanged across v2.29.0-v2.31.0 (same file and line in all four tags). The sample inventory `inventory/sample/group_vars/all/all.yml` carries the same default.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Gates `ntp_servers`, `ntp_restrict`, `ntp_driftfile`, and `ntp_tinker_panic`. Related: `ntp_enabled`, `ntp_package`.

## References
- roles/kubernetes/preinstall/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
