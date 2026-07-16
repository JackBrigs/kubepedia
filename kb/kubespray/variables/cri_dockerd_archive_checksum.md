---
id: VARIABLE-CRI_DOCKERD_ARCHIVE_CHECKSUM
type: variable
title: cri_dockerd_archive_checksum
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cri_dockerd_archive_checksum
tags:
  - cri-dockerd
  - checksum
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Checksum for the cri-dockerd archive, looked up by arch and version"
relations: []
---

# cri_dockerd_archive_checksum

## Summary
The expected checksum of the downloaded cri-dockerd archive, used to verify the
download. It is computed by indexing the `cri_dockerd_archive_checksums` map by
the target architecture and cri-dockerd version.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as the same
computed expression across all four tags:

```yaml
cri_dockerd_archive_checksum: "{{ cri_dockerd_archive_checksums[image_arch][cri_dockerd_version] }}"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. The
resolved checksum values live in the `cri_dockerd_archive_checksums` map in
`roles/kubespray_defaults/vars/main/checksums.yml`.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Depends on `image_arch`,
`cri_dockerd_version`, and the `cri_dockerd_archive_checksums` map. Relevant when
`container_manager` is `docker` (cri-dockerd).

## References
- roles/kubespray_defaults/defaults/main/download.yml
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
