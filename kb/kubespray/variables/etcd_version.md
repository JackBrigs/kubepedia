---
id: VARIABLE-ETCD_VERSION
type: variable
title: etcd_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_version
tags:
  - etcd
  - versions
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "etcd version resolved from etcd_supported_versions[kube_major_version]"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_version

## Summary
The etcd version to download/deploy, computed as `etcd_supported_versions[kube_major_version]` — i.e. selected automatically based on the target Kubernetes minor version.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `etcd_version: "{{ etcd_supported_versions[kube_major_version] }}"` (line 130 in v2.29.0, line 132 in v2.29.1/v2.30.0/v2.31.0). The computed expression is unchanged across v2.29.0-v2.31.0; only the line number shifted. The resolved concrete etcd version varies because `etcd_supported_versions` changes between tags.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Depends on `etcd_supported_versions` and `kube_major_version`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
