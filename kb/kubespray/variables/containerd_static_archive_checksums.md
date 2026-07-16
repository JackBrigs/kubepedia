---
id: VARIABLE-CONTAINERD_STATIC_ARCHIVE_CHECKSUMS
type: variable
title: containerd_static_archive_checksums
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_static_archive_checksums
tags:
  - containerd
  - checksums
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "Per-arch, per-version SHA256 checksums of the containerd static release archives"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd_static_archive_checksums

## Summary
A nested lookup table of SHA256 checksums for the containerd static release archives, keyed by CPU architecture (`arm64`, `amd64`, etc.) and then by containerd version. Used to verify the downloaded containerd archive integrity.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/checksums.yml` as a nested mapping `arch -> version -> sha256:<hash>`. The consuming variable `containerd_static_archive_checksum` in `roles/kubespray_defaults/defaults/main/download.yml` looks it up:

```yaml
containerd_static_archive_checksum: "{{ containerd_static_archive_checksums[image_arch][containerd_version] }}"
```

The definition line number shifts between tags (v2.29.0 line 1406, v2.29.1 line 1543, v2.30.0 line 1179, v2.31.0 line 1278) and the concrete checksum entries differ per tag as new containerd versions are added/removed. The structure (arch -> version -> checksum) is unchanged across v2.29.0–v2.31.0.

## Compatibility
Present in v2.29.0–v2.31.0. The set of listed containerd versions and their checksums is tag-specific. Related: `containerd_static_archive_checksum`, `containerd_version`, `image_arch`.

## References
- roles/kubespray_defaults/vars/main/checksums.yml
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
