---
id: VARIABLE-RUNC_ENABLED
type: variable
title: runc_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - runc_enabled
tags:
  - runc
  - container-runtime
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Toggle for the runc runtime, default false"
relations: []
---

# runc_enabled

## Summary
Boolean toggle that controls whether the runc container runtime is enabled/installed. Default is `false`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as `runc_enabled: false`. The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (the line number shifts between tags but the value does not).

## Compatibility
Present in Kubespray >=v2.29.0 <=v2.31.0. Related runc variables: `runc_version`, `runc_bin_dir`, `runc_package_name`, `runc_download_url`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
