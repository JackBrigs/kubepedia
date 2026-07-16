---
id: COMPONENT-DOCKER
type: component
title: docker
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: "28.3"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker
tags:
  - container-runtime
  - docker
sources:
  - type: code
    path: roles/container-engine/docker/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/docker/defaults/main.yml
    note: "docker_version literal default"
  - type: code
    path: roles/container-engine/docker
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/roles/container-engine/docker
    note: "docker role: package install and per-distro version maps"
relations: []
---

# docker

## Summary

docker is a container-engine option Kubespray can install. It is opt-in: docker
is only deployed when `container_manager` is set to `docker` (the default
`container_manager` is `containerd`). Unlike the archive/image-based runtimes,
docker is installed as a distribution package, so its version is a literal
package version rather than an image tag. The default `docker_version` is `28.3`
and is unchanged across all covered tags.

## Context

- Covers Kubespray `v2.29.0`–`v2.31.0`.
- Not a default: enabled only by selecting `container_manager: docker`.
- Installed by the `roles/container-engine/docker` role, which maps
  `docker_version` to concrete distro packages via `docker_versioned_pkg`.
- docker is a package, not a container image, so it has no `_image_repo` /
  `_image_tag` for the engine itself.

## Implementation

The version is a literal default
(`roles/container-engine/docker/defaults/main.yml`):

```yaml
docker_version: '28.3'
docker_cli_version: "{{ docker_version }}"
```

Per-tag concrete value:

| Tag | commit | docker_version |
|-----|--------|----------------|
| v2.29.0 | 9991412 | 28.3 |
| v2.29.1 | 0c6a295 | 28.3 |
| v2.30.0 | f4ccdb5 | 28.3 |
| v2.31.0 | 1c9add4 | 28.3 |

The value is identical in all four tags. Some distributions override it in the
role's `vars/` files (e.g. `vars/kylin.yml` uses `26.1`, `vars/amazon.yml` uses
`latest`); the cross-distro default is `28.3`. The engine has no image variables;
`docker_image_repo: "docker.io"`
(`roles/kubespray_defaults/defaults/main/download.yml`) is the default registry
prefix used to pull other images, not the docker engine itself.

## Configuration

- Enable: no dedicated `docker_enabled` flag; docker is activated by setting
  `container_manager: docker` (default is `containerd`,
  `roles/kubespray_defaults/defaults/main/main.yml`).
- Version var: `docker_version` (default `'28.3'`); `docker_cli_version` follows
  `docker_version`.
- Package mapping: `docker_versioned_pkg[docker_version]` per distro
  (`roles/container-engine/docker/vars/*.yml`).
- No image repo/tag variables for the engine (installed as an OS package).

## Compatibility

- Per-tag version: `28.3` for v2.29.0, v2.29.1, v2.30.0, and v2.31.0.
- Applicable to the Kubernetes versions shipped by these tags (default
  `kube_version` 1.33–1.35). Note that dockershim was removed from Kubernetes
  upstream; docker here is an OS-level container engine option managed by the
  role, distinct from the Kubernetes CRI selection.

## References

- roles/container-engine/docker/defaults/main.yml (docker_version)
- roles/container-engine/docker/vars/*.yml (per-distro package maps)
- roles/kubespray_defaults/defaults/main/main.yml (container_manager default)
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
