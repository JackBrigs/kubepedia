---
id: COMPONENT-KATA_CONTAINERS
type: component
title: kata-containers
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: "3.7.0"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kata-containers
tags:
  - container-runtime
  - sandbox
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "kata_containers_version / download binary"
relations: []
---

# kata-containers

## Summary
Kata Containers is a sandboxed container runtime that runs each pod inside a lightweight virtual machine to provide stronger workload isolation than standard OCI runtimes. In Kubespray it is an opt-in RuntimeClass integrated with containerd or CRI-O. It is installed from the upstream `kata-static` release tarball (a binary distribution), not as a container image. It is disabled by default and, across all four indexed tags, is pinned to version `3.7.0`.

## Context
Covers v2.29.0-v2.31.0. Kata Containers is gated by the opt-in boolean `kata_containers_enabled`, whose default is `false` (`roles/kubespray_defaults/defaults/main/main.yml`). It is only supported with the `containerd` or `crio` container managers; the `validate_inventory` role stops the run if `kata_containers_enabled` is set while `container_manager` is `docker`. It depends on a supported container runtime being present.

## Implementation
The version is not a plain literal; it is computed as the newest key of the amd64 checksums table:

```yaml
kata_containers_version: "{{ (kata_containers_binary_checksums['amd64'] | dict2items)[0].key }}"
```

The concrete value resolves from `kata_containers_binary_checksums` in `roles/kubespray_defaults/vars/main/checksums.yml` (first amd64 key):

| Tag | Commit | kata_containers_version |
|-----|--------|-------------------------|
| v2.29.0 | 9991412 | 3.7.0 |
| v2.29.1 | 0c6a295 | 3.7.0 |
| v2.30.0 | f4ccdb5 | 3.7.0 |
| v2.31.0 | 1c9add4 | 3.7.0 |

There is no image repo/tag: kata is downloaded as a static tarball from
`{{ github_url }}/kata-containers/kata-containers/releases/download/{{ kata_containers_version }}/kata-static-{{ kata_containers_version }}-{{ image_arch }}.tar.xz`
(`kata_containers_download_url`) and installed by the `container-engine/kata-containers` role.

## Configuration
- Enable flag: `kata_containers_enabled` (default `false`).
- Version variable: `kata_containers_version` (computed from `kata_containers_binary_checksums['amd64']`).
- Image variables: none (binary install; controlled by `kata_containers_download_url` / `kata_containers_binary_checksum`).
- Constraint: supported only with `container_manager` in `containerd` or `crio`; enforced by `roles/validate_inventory/tasks/main.yml`.

## Compatibility
- v2.29.0: 3.7.0
- v2.29.1: 3.7.0
- v2.30.0: 3.7.0
- v2.31.0: 3.7.0

The version is unchanged (3.7.0) across all four tags. Applies to the Kubernetes releases shipped by these Kubespray tags (approximately k8s 1.31-1.35). Only relevant when explicitly enabled and using the containerd or CRI-O runtime.

## References
- roles/kubespray_defaults/defaults/main/download.yml (kata_containers_version, kata_containers_download_url, download enabled condition)
- roles/kubespray_defaults/vars/main/checksums.yml (kata_containers_binary_checksums)
- roles/kubespray_defaults/defaults/main/main.yml (kata_containers_enabled default)
- roles/validate_inventory/tasks/main.yml (container_manager constraint)
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
