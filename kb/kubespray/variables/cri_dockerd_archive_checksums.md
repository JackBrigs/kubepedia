---
id: VARIABLE-CRI_DOCKERD_ARCHIVE_CHECKSUMS
type: variable
title: cri_dockerd_archive_checksums
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cri_dockerd_archive_checksums
tags:
  - checksums
  - cri-dockerd
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "SHA256 checksum table for cri-dockerd release archives keyed by arch then version"
relations: []
---

# cri_dockerd_archive_checksums

## Summary
Static lookup table of SHA256 checksums for cri-dockerd release archives. It is a nested dict keyed first by CPU architecture (`arm64`, `amd64`, ...) and then by cri-dockerd version, used to verify the downloaded archive. It has no scalar default.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/checksums.yml`, e.g. in v2.31.0:

```yaml
cri_dockerd_archive_checksums:
  arm64:
    0.3.24: sha256:c783a03735887c4a8fc894bd4cf7a1c0defef3ecf50a4d79ff31eed45c26b17e
    ...
  amd64:
    0.3.24: sha256:dd4b7f514c248a3aaca398f467430a4c58aae9a77ea8b96a2f5b5d6fba0948d1
    ...
```

Present in all four tags. The table content grows over tags as new cri-dockerd versions and checksums are added; the defining path is unchanged, only the line offset differs (744 in v2.29.0, 818 in v2.29.1, 663 in v2.30.0, 693 in v2.31.0).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Consumed together with `cri_dockerd_version`, `cri_dockerd_download_url` and `cri_dockerd_archive_checksum` (the per-version/arch selected value).

## References
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
