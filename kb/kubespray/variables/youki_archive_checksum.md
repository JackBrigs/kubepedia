---
id: VARIABLE-YOUKI_ARCHIVE_CHECKSUM
type: variable
title: youki_archive_checksum
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - youki_archive_checksum
tags:
  - youki
  - checksum
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Selects the sha256 checksum for the youki archive by arch and version."
relations: []
---

# youki_archive_checksum

## Summary
The expected checksum of the downloaded youki release archive, used to verify the download integrity. It is a computed default that looks up the value in the `youki_checksums` map by the node's image architecture and the resolved youki version.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

`youki_archive_checksum: "{{ youki_checksums[image_arch][youki_version] }}"`

The expression is unchanged across v2.29.0-v2.31.0 (line 196 in v2.29.0; line 198 in v2.29.1/v2.30.0/v2.31.0). The concrete checksum value is resolved from `youki_checksums`, keyed by `image_arch` and `youki_version`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `youki_checksums`, `youki_version`, `image_arch`, `youki_download_url`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
