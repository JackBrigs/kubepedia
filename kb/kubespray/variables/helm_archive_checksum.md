---
id: VARIABLE-HELM_ARCHIVE_CHECKSUM
type: variable
title: helm_archive_checksum
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - helm_archive_checksum
tags:
  - helm
  - download
  - checksum
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Selected Helm archive checksum for the active arch and version"
relations: []
---

# helm_archive_checksum

## Summary
The checksum of the Helm release archive that Kubespray verifies after download. It is looked up from the `helm_archive_checksums` map by the active image architecture and `helm_version`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
helm_archive_checksum: "{{ helm_archive_checksums[image_arch][helm_version] }}"
```

The computed expression is unchanged across v2.29.0-v2.31.0.

## Compatibility
Kubespray v2.29.0-v2.31.0. Related: `helm_archive_checksums`, `helm_version`, `helm_download_url`, `image_arch`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
