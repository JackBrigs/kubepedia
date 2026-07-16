---
id: VARIABLE-CNI_BINARY_CHECKSUMS
type: variable
title: cni_binary_checksums
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cni_binary_checksums
tags:
  - cni
  - checksums
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "Per-architecture map of CNI plugins version to sha256 checksum"
relations: []
---

# cni_binary_checksums

## Summary
Nested map providing sha256 checksums for the CNI plugins binary archive,
keyed by CPU architecture (`arm`, `arm64`, `amd64`, ...) and then by CNI
plugins version. Used to verify the downloaded CNI plugins tarball.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/checksums.yml` as
`cni_binary_checksums:` with an architecture-first structure, e.g.:

```yaml
cni_binary_checksums:
  arm64:
    1.9.1: sha256:56171987d3947707c3563db2f4001bccaf50fd63468611b9f3cbecb1375ee7ec
    ...
```

The variable and its structure exist in all four tags, but the concrete set of
listed versions and their checksum values differ between tags (newer CNI
plugins versions are added and older ones removed release to release). Line
locations: v2.29.0 L483, v2.29.1 L541, v2.30.0 L420, v2.31.0 L442.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Consumed by the download role for the CNI
plugins; the selected key is driven by the target architecture and the pinned
CNI plugins version.

## References
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
