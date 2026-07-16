---
id: COMPONENT-HELM
type: component
title: helm
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: "3.18.4"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - helm
tags:
  - packaging
  - cli
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "helm_version computed from helm_archive_checksums['amd64']"
relations: []
---

# helm

## Summary
Helm is the package manager for Kubernetes; in Kubespray it is the `helm` CLI binary that can be installed on control-plane nodes to manage chart releases. It is deployed as an optional add-on: the enable flag `helm_enabled` defaults to `false`. Helm is delivered as a downloaded client binary (a release tarball), not as a running in-cluster image, so it has no `*_image_repo`/`*_image_tag` variables. Across all indexed tags (v2.29.0 through v2.31.0) the version is `3.18.4` and does not change.

## Context
This document covers Kubespray tags v2.29.0, v2.29.1, v2.30.0, and v2.31.0. Helm is opt-in: `helm_enabled` defaults to `false` (defined in both `roles/kubernetes-apps/helm/defaults/main.yml` and `roles/kubespray_defaults/defaults/main/main.yml`). When enabled, the `helm` download definition in `roles/kubespray_defaults/defaults/main/download.yml` fetches the release tarball and the `roles/kubernetes-apps/helm` role installs the `helm` binary onto the target hosts. It depends on the download subsystem (`local_release_dir`) and the per-arch checksums table.

## Implementation
The version is computed as the first (newest) key of the `amd64` entry in the Helm archive checksums map:

```yaml
helm_version: "{{ (helm_archive_checksums['amd64'] | dict2items)[0].key }}"
helm_download_url: "{{ get_helm_url }}/helm-v{{ helm_version }}-linux-{{ image_arch }}.tar.gz"
helm_archive_checksum: "{{ helm_archive_checksums[image_arch][helm_version] }}"
```

The `helm_archive_checksums` table lives in `roles/kubespray_defaults/vars/main/checksums.yml`; the first-listed `amd64` key is the resolved version.

Per-tag concrete version (first `amd64` key of `helm_archive_checksums`):

| Kubespray tag | commit  | helm_version | first amd64 key |
|---------------|---------|--------------|-----------------|
| v2.29.0       | 9991412 | 3.18.4       | 3.18.4          |
| v2.29.1       | 0c6a295 | 3.18.4       | 3.18.4          |
| v2.30.0       | f4ccdb5 | 3.18.4       | 3.18.4          |
| v2.31.0       | 1c9add4 | 3.18.4       | 3.18.4          |

Helm has no image repo/tag variables; it is a client binary downloaded from `helm_download_url` (`helm-v3.18.4-linux-<arch>.tar.gz`).

## Configuration
- Enable flag: `helm_enabled` — default `false` (`roles/kubernetes-apps/helm/defaults/main.yml` and `roles/kubespray_defaults/defaults/main/main.yml`).
- Version variable: `helm_version` — computed default = newest key of `helm_archive_checksums['amd64']` (`roles/kubespray_defaults/defaults/main/download.yml`).
- Download URL: `helm_download_url` = `{{ get_helm_url }}/helm-v{{ helm_version }}-linux-{{ image_arch }}.tar.gz` (binary; no image_repo/image_tag vars).
- Checksum: `helm_archive_checksum` = `helm_archive_checksums[image_arch][helm_version]`.

## Compatibility
| Kubespray tag | component version |
|---------------|-------------------|
| v2.29.0       | 3.18.4            |
| v2.29.1       | 3.18.4            |
| v2.30.0       | 3.18.4            |
| v2.31.0       | 3.18.4            |

Version is unchanged across the indexed range. Applicable to the Kubernetes releases supported by these Kubespray tags (approximately 1.31–1.35).

## References
- roles/kubespray_defaults/defaults/main/download.yml (helm_version, helm_download_url, helm_archive_checksum)
- roles/kubespray_defaults/vars/main/checksums.yml (helm_archive_checksums)
- roles/kubernetes-apps/helm/defaults/main.yml (helm_enabled)
- roles/kubernetes-apps/helm/tasks/main.yml (binary install)
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
