---
id: COMPONENT-YOUKI
type: component
title: youki
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: ">=0.5.5 <=0.5.7"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - youki
tags:
  - container-runtime
  - oci
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "youki_version = first key of youki_checksums['amd64']; youki_enabled; youki_download_url"
relations:
  - type: see_also
    target: CONCEPT-CONTAINER_RUNTIMES
---

# youki

## Summary

youki is an OCI container runtime implemented in Rust, usable as an alternative
low-level runtime. Kubespray installs it as a binary archive (not a container
image). It is opt-in and **disabled by default** (`youki_enabled: false`).
Across the covered range the installed version moves from `0.5.5` to `0.5.7`.

## Context

- Covers Kubespray `v2.29.0`–`v2.31.0`.
- Opt-in: the `youki` download entry is gated by
  `enabled: "{{ youki_enabled }}"`, and `youki_enabled` defaults to `false` in
  every covered tag.
- Distributed as a gzip tarball downloaded from the youki GitHub releases and
  unarchived; it does not depend on any image repo/tag (there are no
  `youki_image_repo` / `youki_image_tag` variables).

## Implementation

The version is derived
(`roles/kubespray_defaults/defaults/main/download.yml`):

```yaml
youki_version: "{{ (youki_checksums['amd64'] | dict2items)[0].key }}"
```

The value is the **first** (newest) key of `youki_checksums['amd64']` in
`roles/kubespray_defaults/vars/main/checksums.yml`. Concrete resolution per tag:

| Kubespray | youki version |
|-----------|---------------|
| v2.29.0   | 0.5.5         |
| v2.29.1   | 0.5.7         |
| v2.30.0   | 0.5.7         |
| v2.31.0   | 0.5.7         |

Note the `0.5.5 → 0.5.7` bump in `v2.29.1`. The archive is fetched via
`youki_download_url`
(`{{ github_url }}/youki-dev/youki/releases/download/v{{ youki_version }}/youki-{{ youki_version }}-{{ ansible_architecture }}-gnu.tar.gz`).

## Configuration

- Enable flag: `youki_enabled` — default **`false`**.
- Version selection: `youki_version`, `youki_checksums` (`kubespray_defaults`).
- Download URL: `youki_download_url`; checksum: `youki_archive_checksum`.
- Install directory: `youki_bin_dir` (defaults to `bin_dir`).
- Installed as an archive (`file: true`, `unarchive: true`) for the
  `k8s_cluster` group; there are no image repo/tag variables.

## Compatibility

- Kubespray `v2.29.0` → youki `0.5.5`; `v2.29.1`/`v2.30.0`/`v2.31.0` → `0.5.7`.
- Architecture: `youki_checksums` provides `amd64` and `arm64`.

## References

- `roles/kubespray_defaults/defaults/main/download.yml` (`youki_version`, `youki_enabled`, `youki_download_url`).
- `roles/kubespray_defaults/vars/main/checksums.yml` (`youki_checksums`).
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
