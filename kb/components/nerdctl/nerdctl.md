---
id: COMPONENT-NERDCTL
type: component
title: nerdctl
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: ">=2.1.6 <=2.2.2"
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - nerdctl
tags:
  - container-runtime
  - nerdctl
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    lines: "128,174"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "nerdctl_version = first key of nerdctl_archive_checksums['amd64']; nerdctl_download_url"
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "nerdctl_archive_checksums — installable nerdctl archives per tag"
relations:
  - type: part_of
    target: COMPONENT-CONTAINERD
---

# nerdctl

## Summary

nerdctl is the Docker-compatible CLI for containerd. Kubespray installs it with
the containerd runtime (it is the `image_command_tool` used when
`container_manager: containerd`, see [[COMPONENT-CONTAINERD]]). Its version is
derived from the per-release checksums table.

## Context

- Covers Kubespray `v2.29.0`–`v2.31.0`.
- Installed with the containerd container engine.

## Implementation

The version is derived
(`roles/kubespray_defaults/defaults/main/download.yml:128`):

```yaml
nerdctl_version: "{{ (nerdctl_archive_checksums['amd64'] | dict2items)[0].key }}"
```

The value is the **first** (newest) key of `nerdctl_archive_checksums['amd64']`;
the archive is fetched from GitHub (`nerdctl_download_url`, line 174). Concrete
resolution per tag:

| Kubespray | nerdctl version |
|-----------|-----------------|
| v2.29.0   | 2.1.6           |
| v2.29.1   | 2.1.6           |
| v2.30.0   | 2.2.1           |
| v2.31.0   | 2.2.2           |

## Configuration

- Version selection: `nerdctl_version`, `nerdctl_archive_checksums`
  (`kubespray_defaults`).
- Download: `nerdctl_download_url` (GitHub release archive), checksum by
  `image_arch`.

## Compatibility

- Kubespray `v2.29.0`/`v2.29.1` → nerdctl `2.1.6`; `v2.30.0` → `2.2.1`; `v2.31.0`
  → `2.2.2`.
- Architecture: `nerdctl_archive_checksums` provides `amd64` and `arm64`.

## References

- `roles/kubespray_defaults/defaults/main/download.yml:128,174`
  (`nerdctl_version`, `nerdctl_download_url`).
- `roles/kubespray_defaults/vars/main/checksums.yml` (`nerdctl_archive_checksums`).
- Tags: v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
