---
id: VARIABLE-SYSCTL_FILE_PATH
type: variable
title: sysctl_file_path
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - sysctl_file_path
tags:
  - sysctl
  - kernel
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Path of the sysctl config file Kubespray writes kernel parameters into"
relations: []
---

# sysctl_file_path

## Summary
Filesystem path of the sysctl configuration file that Kubespray writes kernel
parameter settings into. Default is `/etc/sysctl.d/99-sysctl.conf`.

## Implementation
Defined identically (`sysctl_file_path: "/etc/sysctl.d/99-sysctl.conf"`) in
several role defaults, including the global default in
`roles/kubespray_defaults/defaults/main/main.yml` and also in
`roles/kubernetes/node/defaults/main.yml`,
`roles/kubernetes/preinstall/defaults/main.yml`, and
`roles/network_plugin/macvlan/defaults/main.yml`.

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Used by preinstall, node, and macvlan roles
when applying sysctl settings. Related to `sysctl_ignore_unknown_keys`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- roles/kubernetes/node/defaults/main.yml
- roles/kubernetes/preinstall/defaults/main.yml
- roles/network_plugin/macvlan/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
