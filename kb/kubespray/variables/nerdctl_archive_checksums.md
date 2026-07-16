---
id: VARIABLE-NERDCTL_ARCHIVE_CHECKSUMS
type: variable
title: nerdctl_archive_checksums
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - nerdctl_archive_checksums
tags:
  - nerdctl
  - download
  - checksum
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "Map of nerdctl archive SHA256 checksums by arch and version"
relations:
  - type: see_also
    target: COMPONENT-NERDCTL
---

# nerdctl_archive_checksums

## Summary
A nested map of SHA256 checksums for nerdctl release archives, keyed first by CPU architecture (e.g. `arm`, `amd64`, `arm64`) and then by nerdctl version. It is the lookup table consumed by `nerdctl_archive_checksum`.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/checksums.yml` as `nerdctl_archive_checksums:` followed by per-architecture, per-version `sha256:` entries. The variable exists in all four tags; the concrete set of versions/checksums it lists is updated per release (the map is refreshed as new nerdctl versions are added).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Consumed by `nerdctl_archive_checksum` via `nerdctl_archive_checksums[image_arch][nerdctl_version]`.

## References
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
