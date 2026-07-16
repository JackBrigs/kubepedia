---
id: VARIABLE-CRI_DOCKERD_VERSION
type: variable
title: cri_dockerd_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cri_dockerd_version
tags:
  - cri-dockerd
  - versions
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "cri-dockerd version, derived from the first key of the amd64 checksums map"
relations: []
---

# cri_dockerd_version

## Summary
The cri-dockerd version Kubespray installs. It is not a fixed literal but the
first (newest) key of the `amd64` section of the `cri_dockerd_archive_checksums`
map, so the effective value tracks that map's newest entry.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as the same
computed expression across all four tags:

```yaml
cri_dockerd_version: "{{ (cri_dockerd_archive_checksums['amd64'] | dict2items)[0].key }}"
```

The expression is unchanged, but the effective value differs per tag because the
`cri_dockerd_archive_checksums` map (in
`roles/kubespray_defaults/vars/main/checksums.yml`) evolves:

| Tag | Effective cri_dockerd_version |
|-----|-------------------------------|
| v2.29.0 | 0.3.20 |
| v2.29.1 | 0.3.21 |
| v2.30.0 | 0.3.23 |
| v2.31.0 | 0.3.24 |

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Depends on the
`cri_dockerd_archive_checksums` map. Relevant when `container_manager` is
`docker` (cri-dockerd).

## References
- roles/kubespray_defaults/defaults/main/download.yml
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
