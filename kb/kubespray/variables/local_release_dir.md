---
id: VARIABLE-LOCAL_RELEASE_DIR
type: variable
title: local_release_dir
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - local_release_dir
tags:
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines local_release_dir with default /tmp/releases"
relations: []
---

# local_release_dir

## Summary
Directory on the target nodes where downloaded binaries and release artifacts are staged. Default is `/tmp/releases`.

## Implementation
Default is `/tmp/releases`, set consistently in:

- `roles/kubespray_defaults/defaults/main/download.yml` (`local_release_dir: /tmp/releases`)
- `roles/kubespray_defaults/defaults/main/main.yml` (`local_release_dir: "/tmp/releases"`)
- `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml` (`local_release_dir: "/tmp/releases"`)

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Used throughout the download role for staging artifacts.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
