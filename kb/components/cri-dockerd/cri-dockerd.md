---
id: COMPONENT-CRI_DOCKERD
type: component
title: cri-dockerd
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: ">=0.3.20 <=0.3.24"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cri-dockerd
tags:
  - container-runtime
  - docker
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "cri_dockerd_version / download binary"
relations:
  - type: see_also
    target: CONCEPT-CONTAINER_MANAGER
---

# cri-dockerd

## Summary
cri-dockerd is Mirantis' CRI (Container Runtime Interface) shim for the Docker Engine. It lets Kubernetes' kubelet talk to Docker via CRI after the in-tree dockershim was removed from Kubernetes. In Kubespray it is used only when the container runtime is Docker (`container_manager: docker`). It is installed as a downloaded binary, not as a container image. Since the default `container_manager` is `containerd`, cri-dockerd is not deployed by default. Across the indexed tags the version ranges from `0.3.20` (v2.29.0) to `0.3.24` (v2.31.0).

## Context
Covers v2.29.0-v2.31.0. cri-dockerd is not gated by a dedicated `cri_dockerd_enabled` boolean; instead the `container-engine/cri-dockerd` role runs only `when: container_manager == 'docker'`, and its download is `enabled: "{{ container_manager == 'docker' }}"`. The default `container_manager` is `containerd` (`roles/kubespray_defaults/defaults/main/main.yml`), so cri-dockerd stays off unless the user selects the Docker runtime. It depends on Docker Engine being installed on the node.

## Implementation
The version is not a plain literal; it is computed as the newest key of the amd64 checksums table:

```yaml
cri_dockerd_version: "{{ (cri_dockerd_archive_checksums['amd64'] | dict2items)[0].key }}"
```

The concrete value resolves from `cri_dockerd_archive_checksums` in `roles/kubespray_defaults/vars/main/checksums.yml` (first amd64 key):

| Tag | Commit | cri_dockerd_version |
|-----|--------|---------------------|
| v2.29.0 | 9991412 | 0.3.20 |
| v2.29.1 | 0c6a295 | 0.3.21 |
| v2.30.0 | f4ccdb5 | 0.3.23 |
| v2.31.0 | 1c9add4 | 0.3.24 |

There is no image repo/tag: cri-dockerd is downloaded as a tarball from
`{{ github_url }}/Mirantis/cri-dockerd/releases/download/v{{ cri_dockerd_version }}/cri-dockerd-{{ cri_dockerd_version }}.{{ image_arch }}.tgz`
(`cri_dockerd_download_url`) and installed by the `container-engine/cri-dockerd` role.

## Configuration
- Enable condition: `container_manager == 'docker'` (no `cri_dockerd_enabled` flag; default runtime is `containerd`, so cri-dockerd is disabled by default).
- Version variable: `cri_dockerd_version` (computed from `cri_dockerd_archive_checksums['amd64']`).
- Image variables: none (binary install; controlled by `cri_dockerd_download_url` / `cri_dockerd_archive_checksum`).
- Other options: `cri_dockerd_log_level` (default `"info"`, from `roles/container-engine/cri-dockerd/defaults/main.yml`).

## Compatibility
- v2.29.0: 0.3.20
- v2.29.1: 0.3.21
- v2.30.0: 0.3.23
- v2.31.0: 0.3.24

The version changes between tags (0.3.20 -> 0.3.24). Applies to the Kubernetes releases shipped by these Kubespray tags (approximately k8s 1.31-1.35). Only relevant when Docker is chosen as the container runtime.

## References
- roles/kubespray_defaults/defaults/main/download.yml (cri_dockerd_version, cri_dockerd_download_url, download enabled condition)
- roles/kubespray_defaults/vars/main/checksums.yml (cri_dockerd_archive_checksums)
- roles/kubespray_defaults/defaults/main/main.yml (container_manager default)
- roles/container-engine/tasks/main.yml / roles/container-engine/tasks/main.yml (cri-dockerd role gating)
- roles/container-engine/cri-dockerd/defaults/main.yml (cri_dockerd_log_level)
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
