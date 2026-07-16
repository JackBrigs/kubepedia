---
id: VARIABLE-DOCKER_ORPHAN_CLEAN_UP
type: variable
title: docker_orphan_clean_up
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_orphan_clean_up
tags:
  - docker
  - cleanup
sources:
  - type: code
    path: roles/container-engine/docker/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/docker/defaults/main.yml
    note: "Flag to enable/disable Docker orphan cleanup; default false"
relations:
  - type: see_also
    target: VARIABLE-CONTAINER_MANAGER
---

# docker_orphan_clean_up

## Summary
Flag enabling cleanup of orphaned Docker resources. Defaults to `false` (cleanup disabled). Documented in the source as "flag to enable/disable docker cleanup".

## Implementation
Defined in `roles/container-engine/docker/defaults/main.yml`:

```yaml
docker_orphan_clean_up: false
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies when Docker is the selected container engine.

## References
- roles/container-engine/docker/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
