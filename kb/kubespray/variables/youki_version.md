---
id: VARIABLE-YOUKI_VERSION
type: variable
title: youki_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - youki_version
tags:
  - youki
  - runtime
  - version
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Computed youki version; defaults to the first key of youki_checksums['amd64']."
relations:
  - type: see_also
    target: VARIABLE-CONTAINER_MANAGER
---

# youki_version

## Summary
The youki container runtime version that will be downloaded and installed. It is not a hardcoded literal but a computed default: the first key of the `amd64` sub-map of `youki_checksums`. Because that map lists newest versions first, this resolves to the newest checksummed youki release for the tag.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

`youki_version: "{{ (youki_checksums['amd64'] | dict2items)[0].key }}"`

The expression is identical across v2.29.0-v2.31.0 (line 79 in v2.29.0; line 81 in v2.29.1/v2.30.0/v2.31.0). The resolved value depends on `youki_checksums`, so it differs by tag:

| Tag | Resolved youki_version |
|-----|------------------------|
| v2.29.0 | 0.5.5 |
| v2.29.1 | 0.5.7 |
| v2.30.0 | 0.5.7 |
| v2.31.0 | 0.5.7 |

## Compatibility
Kubespray v2.29.0 through v2.31.0. Drives `youki_download_url` and `youki_archive_checksum`. Related variables: `youki_checksums`, `youki_enabled`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
