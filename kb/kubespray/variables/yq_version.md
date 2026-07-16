---
id: VARIABLE-YQ_VERSION
type: variable
title: yq_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - yq_version
tags:
  - yq
  - download
  - version
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Computed yq version; defaults to the first key of yq_checksums['amd64']."
relations: []
---

# yq_version

## Summary
The version of the yq YAML processor binary that Kubespray downloads. It is a computed default: the first key of the `amd64` sub-map of `yq_checksums`, which lists newest versions first, so it resolves to the newest checksummed yq release for the tag.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

`yq_version: "{{ (yq_checksums['amd64'] | dict2items)[0].key }}"`

The expression is identical across v2.29.0-v2.31.0 (line 141 in v2.29.0; line 143 in v2.29.1/v2.30.0/v2.31.0). The resolved value is `4.42.1` in every inspected tag (the top `amd64` key of `yq_checksums` did not change).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Drives `yq_download_url` and `yq_binary_checksum`. Related variables: `yq_checksums`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
