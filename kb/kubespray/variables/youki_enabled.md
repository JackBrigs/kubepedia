---
id: VARIABLE-YOUKI_ENABLED
type: variable
title: youki_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - youki_enabled
tags:
  - youki
  - runtime
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Toggles installation of the youki container runtime; default false."
relations:
  - type: see_also
    target: VARIABLE-CONTAINER_MANAGER
---

# youki_enabled

## Summary
Boolean toggle that controls whether the youki OCI container runtime is installed and configured. The default is `false`, so youki is not deployed unless explicitly enabled. When set to `true`, Kubespray downloads and installs the youki runtime for use with containerd.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

`youki_enabled: false`

The default is unchanged across v2.29.0-v2.31.0 (line number shifts: 348 in v2.29.0/v2.29.1, 349 in v2.30.0, 361 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. When enabled, drives the youki download logic. Related variables: `youki_version`, `youki_download_url`, `youki_archive_checksum`, `youki_checksums`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
