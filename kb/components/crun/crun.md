---
id: COMPONENT-CRUN
type: component
title: crun
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: "1.17"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - crun
tags:
  - container-runtime
  - oci
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "crun_version = first key of crun_checksums['amd64']; crun_enabled; crun_download_url"
relations: []
---

# crun

## Summary

crun is a fast, low-memory OCI container runtime written in C, usable as an
alternative to runc under CRI-O or containerd. Kubespray installs it as a
binary (not a container image). It is opt-in and **disabled by default**
(`crun_enabled: false`). Across the covered range the installed version is
`1.17`.

## Context

- Covers Kubespray `v2.29.0`–`v2.31.0`.
- Opt-in: the `crun` download entry is gated by `enabled: "{{ crun_enabled }}"`,
  and `crun_enabled` defaults to `false` in every covered tag.
- Distributed as a standalone binary downloaded from the crun GitHub releases;
  it does not depend on any image repo/tag (there are no `crun_image_repo` /
  `crun_image_tag` variables).

## Implementation

The version is derived
(`roles/kubespray_defaults/defaults/main/download.yml`):

```yaml
crun_version: "{{ (crun_checksums['amd64'] | dict2items)[0].key }}"
```

The value is the **first** (newest) key of `crun_checksums['amd64']` in
`roles/kubespray_defaults/vars/main/checksums.yml`. Concrete resolution per tag:

| Kubespray | crun version |
|-----------|--------------|
| v2.29.0   | 1.17         |
| v2.29.1   | 1.17         |
| v2.30.0   | 1.17         |
| v2.31.0   | 1.17         |

The value is unchanged across the range. The binary is fetched via
`crun_download_url`
(`{{ github_url }}/containers/crun/releases/download/{{ crun_version }}/crun-{{ crun_version }}-linux-{{ image_arch }}`),
with the checksum selected as `crun_checksums[image_arch][crun_version]`.

## Configuration

- Enable flag: `crun_enabled` — default **`false`**.
- Version selection: `crun_version`, `crun_checksums` (`kubespray_defaults`).
- Download URL: `crun_download_url`; checksum: `crun_binary_checksum`.
- Installed as a binary (`file: true`, `unarchive: false`) into
  `local_release_dir` for the `k8s_cluster` group; there are no image
  repo/tag variables.

## Compatibility

- Kubespray `v2.29.0`/`v2.29.1`/`v2.30.0`/`v2.31.0` → crun `1.17` (unchanged).
- Architecture: `crun_checksums` provides `amd64` and `arm64`.

## References

- `roles/kubespray_defaults/defaults/main/download.yml` (`crun_version`, `crun_enabled`, `crun_download_url`).
- `roles/kubespray_defaults/vars/main/checksums.yml` (`crun_checksums`).
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
