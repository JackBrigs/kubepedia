---
id: VARIABLE-ETCD_SUPPORTED_VERSIONS
type: variable
title: etcd_supported_versions
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_supported_versions
tags:
  - etcd
  - versions
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/main.yml
    note: "Map of Kubernetes minor version to the etcd version selected for it"
relations: []
---

# etcd_supported_versions

## Summary
A mapping from Kubernetes minor version (`kube_major_version`) to the etcd version to use, computed from `etcd_binary_checksums`. It is consumed by `etcd_version`. The set of supported Kubernetes keys changes between tags.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/main.yml` (line 14). Each entry selects an etcd version via a Jinja expression over `etcd_binary_checksums['amd64'].keys()`. The key set and selectors differ between tags:

| Tag | Entries |
|-----|---------|
| v2.29.0 / v2.29.1 | `'1.31'`, `'1.32'`, `'1.33'` all `select('version', '3.6', '<')[0]` |
| v2.30.0 | `'1.32'`, `'1.33'`, `'1.34'` all `select('version', '3.6', '<')[0]` |
| v2.31.0 | `'1.33'` `<3.6`, `'1.34'` `<3.6`, `'1.35'` `select('version', '3.7', '<')[0]` |

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Consumed by `etcd_version` via `etcd_supported_versions[kube_major_version]`.

## References
- roles/kubespray_defaults/vars/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
