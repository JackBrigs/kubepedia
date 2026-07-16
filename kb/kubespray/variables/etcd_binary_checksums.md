---
id: VARIABLE-ETCD_BINARY_CHECKSUMS
type: variable
title: etcd_binary_checksums
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_binary_checksums
tags:
  - etcd
  - checksums
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "Per-arch, per-etcd-version sha256 checksums for the etcd binary tarball"
relations: []
---

# etcd_binary_checksums

## Summary
Nested mapping of sha256 checksums for the etcd release tarball, keyed by CPU architecture (`arm64`, `amd64`, ...) and then by etcd version. Used to verify the downloaded etcd binary against `etcd_download_url`.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/checksums.yml` (v2.29.0 line 425, v2.29.1 line 477, v2.30.0 line 353, v2.31.0 line 333). The value is a large architecture/version checksum map, e.g. in v2.31.0 the `arm64` block starts with `3.6.10: sha256:e40dc34b...`.

The map content **differs between tags**: entries (etcd versions and their checksums) are added/removed as the set of supported etcd versions changes. The variable name and structure are unchanged across v2.29.0-v2.31.0; only the enumerated versions/checksums differ.

## Compatibility
Kubespray v2.29.0-v2.31.0. The consumed checksum is selected by `image_arch` and `etcd_version` (`etcd_version: "{{ etcd_supported_versions[kube_major_version] }}"`). Related: `etcd_download_url`, `etcd_version`.

## References
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
