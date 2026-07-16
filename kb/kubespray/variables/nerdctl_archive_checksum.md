---
id: VARIABLE-NERDCTL_ARCHIVE_CHECKSUM
type: variable
title: nerdctl_archive_checksum
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - nerdctl_archive_checksum
tags:
  - nerdctl
  - download
  - checksum
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Selected nerdctl archive checksum for current arch/version"
relations:
  - type: see_also
    target: COMPONENT-NERDCTL
---

# nerdctl_archive_checksum

## Summary
Resolves the SHA256 checksum of the nerdctl release archive to download, selected from the checksum map by CPU architecture and nerdctl version.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `nerdctl_archive_checksum: "{{ nerdctl_archive_checksums[image_arch][nerdctl_version] }}"`. The expression is unchanged across v2.29.0-v2.31.0. The underlying map `nerdctl_archive_checksums` lives in `roles/kubespray_defaults/vars/main/checksums.yml`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `nerdctl_archive_checksums`, `image_arch`, and `nerdctl_version`; used to verify the download from `nerdctl_download_url`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
