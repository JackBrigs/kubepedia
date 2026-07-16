---
id: VARIABLE-RUNC_PACKAGE_NAME
type: variable
title: runc_package_name
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - runc_package_name
tags:
  - runc
  - container-runtime
sources:
  - type: code
    path: roles/container-engine/runc/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/runc/defaults/main.yml
    note: "OS package name for runc, default runc"
relations:
  - type: see_also
    target: COMPONENT-RUNC
---

# runc_package_name

## Summary
The OS package name used when installing runc via the system package manager. Default is `runc`.

## Implementation
Defined in `roles/container-engine/runc/defaults/main.yml` as `runc_package_name: runc`. The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Present in Kubespray >=v2.29.0 <=v2.31.0. Related runc variables: `runc_bin_dir`, `runc_enabled`.

## References
- roles/container-engine/runc/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
