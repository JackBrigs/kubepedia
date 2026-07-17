---
id: COMPONENT-REGISTRY
type: component
title: registry
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: "2.8.1"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - registry
tags:
  - registry
  - addon
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "registry_version / registry_image_repo / registry_image_tag"
relations:
  - type: see_also
    target: CONFIG-PROXY
---

# registry

## Summary
`registry` is the Docker/OCI Distribution image registry (`library/registry`, the reference "Docker Registry v2" implementation) that Kubespray can optionally deploy as an in-cluster addon to store and serve container images. It is disabled by default (`registry_enabled: false`) and, across the indexed range, is pinned to version `2.8.1`.

## Context
This document covers Kubespray tags v2.29.0 through v2.31.0. The registry addon is opt-in: the enable flag `registry_enabled` defaults to `false` in every indexed tag, so nothing is deployed unless the operator sets it to `true`. When enabled it runs as an in-cluster deployment and provides an image registry endpoint for the cluster.

## Implementation
The version is defined as a plain literal in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
registry_version: "2.8.1"
registry_image_repo: "{{ docker_image_repo }}/library/registry"
registry_image_tag: "{{ registry_version }}"
```

The image tag is derived directly from `registry_version`, so the effective image tag is `2.8.1` in all four tags.

| Tag | Commit | registry_version |
|-----|--------|------------------|
| v2.29.0 | 9991412 | 2.8.1 |
| v2.29.1 | 0c6a295 | 2.8.1 |
| v2.30.0 | f4ccdb5 | 2.8.1 |
| v2.31.0 | 1c9add4 | 2.8.1 |

The version is unchanged across the entire indexed range.

## Configuration
- Enable flag: `registry_enabled` — default `false` (`roles/kubespray_defaults/defaults/main/main.yml`).
- Version var: `registry_version` — default `2.8.1`.
- Image repo: `registry_image_repo` = `{{ docker_image_repo }}/library/registry`.
- Image tag: `registry_image_tag` = `{{ registry_version }}` (resolves to `2.8.1`).

## Compatibility
| Tag | Version |
|-----|---------|
| v2.29.0 | 2.8.1 |
| v2.29.1 | 2.8.1 |
| v2.30.0 | 2.8.1 |
| v2.31.0 | 2.8.1 |

Applicable to the Kubernetes versions shipped by these Kubespray tags (roughly 1.31–1.35).

## References
- roles/kubespray_defaults/defaults/main/download.yml (registry_version, registry_image_repo, registry_image_tag)
- roles/kubespray_defaults/defaults/main/main.yml (registry_enabled)
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
