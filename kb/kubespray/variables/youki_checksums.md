---
id: VARIABLE-YOUKI_CHECKSUMS
type: variable
title: youki_checksums
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - youki_checksums
tags:
  - youki
  - checksums
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "Arch- and version-keyed map of sha256 checksums for youki archives."
relations: []
---

# youki_checksums

## Summary
A nested lookup table mapping each supported youki version to the sha256 checksum of its release archive, keyed first by architecture (`amd64`, `arm64`). It is not a scalar default but the source data behind `youki_version` (the first `amd64` key) and `youki_archive_checksum` (the selected value).

## Implementation
Defined in `roles/kubespray_defaults/vars/main/checksums.yml` as `youki_checksums:` with `amd64:` and `arm64:` sub-maps of `<version>: sha256:<hash>` entries. The set of listed versions grows between tags; the leading (newest) entry determines the resolved `youki_version`:

| Tag | Top amd64 version listed |
|-----|--------------------------|
| v2.29.0 | 0.5.5 |
| v2.29.1 | 0.5.7 |
| v2.30.0 | 0.5.7 |
| v2.31.0 | 0.5.7 |

Example verbatim entry (v2.31.0 amd64): `0.5.7: sha256:10077b1a4f013990a416acf15e6b397cf64b5d62008516a9711abc22730d8203`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Consumed by `youki_version` and `youki_archive_checksum`. Related variables: `youki_download_url`, `youki_enabled`, `image_arch`.

## References
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
