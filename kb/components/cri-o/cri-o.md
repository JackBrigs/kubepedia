---
id: COMPONENT-CRI_O
type: component
title: cri-o
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: ">=1.33.5 <=1.35.0"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cri-o
tags:
  - container-runtime
  - crio
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "crio_version derived from crio_archive_checksums table"
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "crio_archive_checksums — installable cri-o archives per tag"
  - type: code
    path: roles/container-engine/cri-o
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/roles/container-engine/cri-o
    note: "cri-o role: archive install and /etc/crio configuration"
relations:
  - type: see_also
    target: CONCEPT-CONTAINER_MANAGER
---

# cri-o

## Summary

cri-o is one of the container runtimes Kubespray can install as an alternative
to the default containerd. It is an opt-in choice: cri-o is only deployed when
`container_manager` is set to `crio` (the default `container_manager` is
`containerd`). The runtime is installed from a release archive whose version is
derived from the per-release checksums table, so it moves with the Kubespray
release. Across the covered tags the resolved version ranges from `1.33.5` to
`1.35.0`.

## Context

- Covers Kubespray `v2.29.0`–`v2.31.0`.
- Not a default: enabled only by selecting `container_manager: crio`.
- Installed and configured by the `roles/container-engine/cri-o` role. cri-o is
  fetched as a tarball (`crio_download_url`), not run as a container image, so it
  has no `_image_repo` / `_image_tag` variables.
- The chosen version tracks the cluster's target Kubernetes minor: it is the
  newest cri-o archive whose minor is below `kube_major_next_version`.

## Implementation

The version is derived, not pinned
(`roles/kubespray_defaults/defaults/main/download.yml`):

```yaml
crio_version: "{{ (crio_archive_checksums['amd64'].keys() | select('version', kube_major_next_version, '<'))[0] }}"
```

The value is the first (newest) key of `crio_archive_checksums['amd64']` whose
version is strictly less than `kube_major_next_version` (one minor above the
default `kube_version`). Resolving this per tag:

| Tag | commit | default kube_version | kube_major_next_version | resolved crio_version |
|-----|--------|----------------------|-------------------------|-----------------------|
| v2.29.0 | 9991412 | 1.33.5 | 1.34 | 1.33.5 |
| v2.29.1 | 0c6a295 | 1.33.7 | 1.34 | 1.33.7 |
| v2.30.0 | f4ccdb5 | 1.34.3 | 1.35 | 1.34.4 |
| v2.31.0 | 1c9add4 | 1.35.4 | 1.36 | 1.35.0 |

The version changes between tags as the checksums table and default Kubernetes
version advance. cri-o is delivered from
`{{ storage_googleapis_url }}/cri-o/artifacts/cri-o.{{ image_arch }}.v{{ crio_version }}.tar.gz`
and there is no container image for the runtime itself.

## Configuration

- Enable: no dedicated `crio_enabled` flag; cri-o is activated by setting
  `container_manager: crio` (default is `containerd`,
  `roles/kubespray_defaults/defaults/main/main.yml`).
- Version var: `crio_version` (derived, see above).
- Install source: `crio_download_url`, checksum `crio_archive_checksum`
  (`crio_archive_checksums[image_arch][crio_version]`).
- Config template: `roles/container-engine/cri-o/templates/crio.conf.j2`
  (e.g. NRI is enabled when `nri_enabled and crio_version >= 1.26.0`).
- No image repo/tag variables (installed from archive, not an image).

## Compatibility

- Per-tag versions: v2.29.0 → 1.33.5, v2.29.1 → 1.33.7, v2.30.0 → 1.34.4,
  v2.31.0 → 1.35.0.
- Applicable to the Kubernetes versions shipped by these tags (default
  `kube_version` 1.33–1.35); the selected cri-o minor follows the target
  Kubernetes minor.

## References

- roles/kubespray_defaults/defaults/main/download.yml (crio_version)
- roles/kubespray_defaults/vars/main/checksums.yml (crio_archive_checksums)
- roles/container-engine/cri-o (install and configuration)
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
