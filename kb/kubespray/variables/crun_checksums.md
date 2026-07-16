---
id: VARIABLE-CRUN_CHECKSUMS
type: variable
title: crun_checksums
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - crun_checksums
tags:
  - checksums
  - crun
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "SHA256 checksum table for crun release binaries keyed by arch then version"
relations: []
---

# crun_checksums

## Summary
Static lookup table of SHA256 checksums for crun release binaries. It is a nested dict keyed first by CPU architecture (`arm64`, `amd64`, `ppc64le`, ...) and then by crun version, used to verify the downloaded binary. It has no scalar default.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/checksums.yml`, e.g. in v2.31.0:

```yaml
crun_checksums:
  arm64:
    '1.17': sha256:3049017b99208f5ecd15c1366f47a77dace87f42dccf317ad40a07f1a867518c
    ...
  amd64:
    '1.17': sha256:e9512a3e034e781b2396d068fd24eafcd5788e410403da886df9dc8871d504a5
    ...
```

Present in all four tags. The table content grows over tags as new crun versions and checksums are added; the defining path is unchanged, only the line offset differs (838 in v2.29.0, 926 in v2.29.1, 775 in v2.30.0, 819 in v2.31.0).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Consumed together with `crun_version`, `crun_download_url` and `crun_binary_checksum` (the per-version/arch selected value); relevant when `crun_enabled` is true.

## References
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
