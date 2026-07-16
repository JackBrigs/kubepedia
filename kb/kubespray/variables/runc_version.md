---
id: VARIABLE-RUNC_VERSION
type: variable
title: runc_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - runc_version
tags:
  - runc
  - version
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Derives runc version from the first key of amd64 checksums"
relations: []
---

# runc_version

## Summary
The runc version Kubespray installs. Instead of a hardcoded literal, it is derived from the first key of the `amd64` entry in `runc_checksums`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:
`runc_version: "{{ (runc_checksums['amd64'] | dict2items)[0].key }}"`.
The computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0; the concrete version it resolves to depends on the contents of `runc_checksums` in each tag.

## Compatibility
Present in Kubespray >=v2.29.0 <=v2.31.0. Depends on `runc_checksums`; consumed by `runc_download_url` and `runc_binary_checksum`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
