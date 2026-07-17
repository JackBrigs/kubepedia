---
id: COMPONENT-SKOPEO
type: component
title: skopeo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: "1.16.1"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - skopeo
tags:
  - container-image
  - crio
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "skopeo_version = first key of skopeo_binary_checksums['amd64']; skopeo_download_url; download enabled when container_manager == 'crio'"
relations:
  - type: see_also
    target: CONCEPT-CONTAINER_MANAGER
---

# skopeo

## Summary

skopeo is a command-line tool for working with container images and registries
(inspect, copy, push/pull) without a running daemon. Kubespray installs it as a
binary and uses it to load images when the CRI-O container engine is selected.
There is no dedicated `skopeo_enabled` flag: its download is gated on the
container manager, and it is fetched only when `container_manager == 'crio'`.
Across the covered range the installed version is `1.16.1`.

## Context

- Covers Kubespray `v2.29.0`–`v2.31.0`.
- Conditional install: the `skopeo` download entry is gated by
  `enabled: "{{ container_manager == 'crio' }}"` — so it is effectively opt-in
  via CRI-O rather than via a boolean flag; there is no `skopeo_enabled`
  variable in any covered tag.
- Distributed as a standalone binary downloaded from the
  `lework/skopeo-binary` GitHub releases; it does not depend on any image
  repo/tag (there are no `skopeo_image_repo` / `skopeo_image_tag` variables).

## Implementation

The version is derived
(`roles/kubespray_defaults/defaults/main/download.yml`):

```yaml
skopeo_version: "{{ (skopeo_binary_checksums['amd64'] | dict2items)[0].key }}"
```

The value is the **first** (newest) key of `skopeo_binary_checksums['amd64']` in
`roles/kubespray_defaults/vars/main/checksums.yml`. Concrete resolution per tag:

| Kubespray | skopeo version |
|-----------|----------------|
| v2.29.0   | 1.16.1         |
| v2.29.1   | 1.16.1         |
| v2.30.0   | 1.16.1         |
| v2.31.0   | 1.16.1         |

The value is unchanged across the range. The binary is fetched via
`skopeo_download_url`
(`{{ github_url }}/lework/skopeo-binary/releases/download/v{{ skopeo_version }}/skopeo-linux-{{ image_arch }}`),
with the checksum selected as `skopeo_binary_checksums[image_arch][skopeo_version]`.

## Configuration

- Enable condition: no boolean flag; the download entry is enabled when
  `container_manager == 'crio'` (default container manager is `containerd`, so
  skopeo is **not** installed by default).
- Version selection: `skopeo_version`, `skopeo_binary_checksums`
  (`kubespray_defaults`).
- Download URL: `skopeo_download_url`; checksum: `skopeo_binary_checksum`.
- Installed as a binary (`file: true`, `unarchive: false`) into
  `local_release_dir` for the `kube_control_plane` group; there are no image
  repo/tag variables.

## Compatibility

- Kubespray `v2.29.0`/`v2.29.1`/`v2.30.0`/`v2.31.0` → skopeo `1.16.1`
  (unchanged).
- Architecture: `skopeo_binary_checksums` provides `amd64` and `arm64`.

## References

- `roles/kubespray_defaults/defaults/main/download.yml` (`skopeo_version`, `skopeo_download_url`, download `enabled` on `container_manager == 'crio'`).
- `roles/kubespray_defaults/vars/main/checksums.yml` (`skopeo_binary_checksums`).
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
