---
id: VARIABLE-ETCD_SCRIPT_DIR
type: variable
title: etcd_script_dir
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_script_dir
tags:
  - etcd
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Directory for etcd helper scripts; default {{ bin_dir }}/etcd-scripts"
relations: []
---

# etcd_script_dir

## Summary
Directory where etcd helper scripts are placed. Defaults to `{{ bin_dir }}/etcd-scripts`.

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml` as `etcd_script_dir: "{{ bin_dir }}/etcd-scripts"` (line 32 in v2.29.0/v2.29.1, line 31 in v2.30.0/v2.31.0). The computed expression is unchanged across v2.29.0-v2.31.0; only the line number shifted.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Depends on `bin_dir` for the resolved path.

## References
- roles/etcd_defaults/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
