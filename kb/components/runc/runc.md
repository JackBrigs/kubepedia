---
id: COMPONENT-RUNC
type: component
title: runc
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: ">=1.3.2 <=1.4.2"
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - runc
tags:
  - container-runtime
  - runc
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    lines: "79"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "runc_version = first key of runc_checksums['amd64']"
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "runc_checksums — installable runc binaries per tag"
relations:
  - type: part_of
    target: COMPONENT-CONTAINERD
---

# runc

## Summary

runc is the OCI runtime that containerd uses to run containers. Kubespray
installs it alongside [[COMPONENT-CONTAINERD]]; its version is derived from the
per-release checksums table, so it moves with the Kubespray release.

## Context

- Covers Kubespray `v2.29.0`–`v2.31.0`.
- Installed with the containerd container engine (see
  [[VARIABLE-CONTAINER_MANAGER]]).

## Implementation

The version is derived
(`roles/kubespray_defaults/defaults/main/download.yml:79`):

```yaml
runc_version: "{{ (runc_checksums['amd64'] | dict2items)[0].key }}"
```

The value is the **first** (newest) key of `runc_checksums['amd64']`. Concrete
resolution per tag:

| Kubespray | runc version |
|-----------|--------------|
| v2.29.0   | 1.3.2        |
| v2.29.1   | 1.3.4        |
| v2.30.0   | 1.3.4        |
| v2.31.0   | 1.4.2        |

Note the `1.3 → 1.4` bump in `v2.31.0`.

## Configuration

- Version selection: `runc_version`, `runc_checksums` (`kubespray_defaults`).
- Installed as a binary; the checksum is selected by `image_arch`.

## Compatibility

- Kubespray `v2.29.0` → runc `1.3.2`; `v2.29.1`/`v2.30.0` → `1.3.4`; `v2.31.0` →
  `1.4.2`.
- Architecture: `runc_checksums` provides `amd64` and `arm64`.

## References

- `roles/kubespray_defaults/defaults/main/download.yml:79` (`runc_version`).
- `roles/kubespray_defaults/vars/main/checksums.yml` (`runc_checksums`).
- Tags: v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
