---
id: VARIABLE-NTP_FILTER_INTERFACE
type: variable
title: ntp_filter_interface
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - ntp_filter_interface
tags:
  - ntp
  - preinstall
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/defaults/main.yml
    note: "Whether to filter NTP listening interfaces; default false"
relations: []
---

# ntp_filter_interface

## Summary
Controls whether the managed NTP configuration restricts the interfaces the daemon listens on (via the companion `ntp_interfaces` list). Default is `false`.

## Implementation
Defined in `roles/kubernetes/preinstall/defaults/main.yml` (line 55) as `ntp_filter_interface: false`. The value is unchanged across v2.29.0-v2.31.0 (same file and line in all four tags).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Only takes effect when `ntp_manage_config: true`; when enabled it uses the `ntp_interfaces` list. Related: `ntp_manage_config`, `ntp_interfaces`.

## References
- roles/kubernetes/preinstall/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
