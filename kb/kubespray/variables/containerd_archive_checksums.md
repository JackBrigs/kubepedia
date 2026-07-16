---
id: VARIABLE-CONTAINERD_ARCHIVE_CHECKSUMS
type: variable
title: containerd_archive_checksums
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_archive_checksums
tags:
  - containerd
  - checksums
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "Per-architecture map of containerd version to sha256 checksum"
relations: []
---

# containerd_archive_checksums

## Summary
Nested map providing sha256 checksums for the containerd release archive,
keyed by CPU architecture (`arm64`, `amd64`, ...) and then by containerd
version. Used to verify the downloaded containerd tarball.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/checksums.yml` as
`containerd_archive_checksums:` with an architecture-first structure, e.g.:

```yaml
containerd_archive_checksums:
  arm64:
    2.2.3: sha256:2942d72435b18610f7b69c1ddb74f99cef5c549425ff80d3e74f04e5e80db6a4
    ...
```

The variable and its structure exist in all four tags, but the concrete set of
listed containerd versions and their checksum values differ between tags (newer
containerd releases are added release to release). Line locations: v2.29.0
L1204, v2.29.1 L1332, v2.30.0 L1031, v2.31.0 L1115.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Consumed by the download role for
containerd; the selected key is driven by the target architecture and the
pinned containerd version.

## References
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
