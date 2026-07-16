---
id: VARIABLE-DOCKER_DAEMON_GRAPH
type: variable
title: docker_daemon_graph
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_daemon_graph
tags:
  - docker
  - storage
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Docker data root directory (graph), default /var/lib/docker"
relations: []
---

# docker_daemon_graph

## Summary
Docker data-root directory (the "graph" / `data-root` where images and containers are stored). Defaults to `/var/lib/docker`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
docker_daemon_graph: "/var/lib/docker"
```

The same default is mirrored in `inventory/sample/group_vars/all/docker.yml`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies when the Docker container engine is selected.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/all/docker.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
