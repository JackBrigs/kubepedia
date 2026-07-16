---
id: VARIABLE-CONTAINERD_VERSION
type: variable
title: containerd_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_version
tags:
  - containerd
  - version
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Default containerd version derived from the first key of the amd64 checksum map"
relations: []
---

# containerd_version

## Summary
The containerd version to install. By default it is computed as the first (newest) key of the `amd64` entry in `containerd_archive_checksums`, so the effective default differs per Kubespray tag.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
containerd_version: "{{ (containerd_archive_checksums['amd64'] | dict2items)[0].key }}"
```

The expression is unchanged across all four tags, but the resolved default differs because the checksum map (`roles/kubespray_defaults/vars/main/checksums.yml`) changes:

| Tag | Default containerd_version |
|-----|----------------------------|
| v2.29.0 | 2.1.4 |
| v2.29.1 | 2.1.5 |
| v2.30.0 | 2.2.1 |
| v2.31.0 | 2.2.3 |

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related: `containerd_archive_checksums`, `containerd_download_url`, `containerd_checksum`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
