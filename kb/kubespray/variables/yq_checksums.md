---
id: VARIABLE-YQ_CHECKSUMS
type: variable
title: yq_checksums
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - yq_checksums
tags:
  - yq
  - checksums
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "Arch- and version-keyed map of sha256 checksums for the yq binary."
relations: []
---

# yq_checksums

## Summary
A nested lookup table mapping each supported yq version to the sha256 checksum of its Linux binary, keyed first by architecture (`arm`, `arm64`, `amd64`, `ppc64le`). It is not a scalar default but the source data behind `yq_version` (the first `amd64` key) and `yq_binary_checksum` (the selected value).

## Implementation
Defined in `roles/kubespray_defaults/vars/main/checksums.yml` as `yq_checksums:` with per-architecture sub-maps of `<version>: sha256:<hash>` entries. Across the four inspected tags the top (newest) `amd64` version is `4.42.1` in every case, so the resolved `yq_version` is stable.

Example verbatim entry (v2.31.0 amd64): `4.42.1: sha256:1a95960dddd426321354d58d2beac457717f7c49a9ec0806749a5a9e400eb45e`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Consumed by `yq_version` and `yq_binary_checksum`. Related variables: `yq_download_url`, `image_arch`.

## References
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
