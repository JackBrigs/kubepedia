---
id: VARIABLE-CRIO_ARCHIVE_CHECKSUMS
type: variable
title: crio_archive_checksums
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - crio_archive_checksums
tags:
  - checksums
  - cri-o
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "SHA256 checksum table for CRI-O release archives keyed by arch then version"
relations: []
---

# crio_archive_checksums

## Summary
Static lookup table of SHA256 checksums for CRI-O (`cri-o`) release archives. It is a nested dict keyed first by CPU architecture (`arm64`, `amd64`, ...) and then by CRI-O version, used to verify the downloaded archive. It has no scalar default.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/checksums.yml`, e.g. in v2.31.0:

```yaml
crio_archive_checksums:
  arm64:
    1.35.0: sha256:e57175a4d00387b78adfbe248d087d8127bed625afb529e34b2c90d08cfdaf87
    ...
  amd64:
    1.35.0: sha256:55b6d3e9fc9a5864ab5cdf0b24d54b1dcbaf6d4919274b3b9eb37bfc4b0b8cb5
    ...
```

Present in all four tags. The table content grows over tags as new CRI-O versions and checksums are added; the defining path is unchanged, only the line offset differs (18 in v2.29.0/v2.29.1, 15 in v2.30.0/v2.31.0).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Consumed together with `crio_version`, `crio_download_url` and `crio_archive_checksum` (the per-version/arch selected value).

## References
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
