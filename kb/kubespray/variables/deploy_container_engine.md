---
id: VARIABLE-DEPLOY_CONTAINER_ENGINE
type: variable
title: deploy_container_engine
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - deploy_container_engine
tags:
  - container-runtime
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    lines: "335 (v2.31.0)"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "deploy_container_engine computed from group membership and etcd_deployment_type"
relations:
  - type: see_also
    target: TAG-CONTAINER_ENGINE
  - type: see_also
    target: VARIABLE-ETCD_DEPLOYMENT_TYPE
---

# deploy_container_engine

## Summary

`deploy_container_engine` decides whether Kubespray installs a container runtime
on a host. It is computed, not a plain boolean: true for cluster nodes and for
etcd nodes that run etcd in Docker.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
deploy_container_engine: "{{ 'k8s_cluster' in group_names or etcd_deployment_type == 'docker' }}"
```

So a host gets the container engine when it is in `k8s_cluster`, or when it is an
etcd node using `etcd_deployment_type: docker` (see
[[VARIABLE-ETCD_DEPLOYMENT_TYPE]]). It gates the `container-engine` role
(`when: deploy_container_engine`, see [[TAG-CONTAINER_ENGINE]]).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: the computed expression is unchanged.
- A standalone etcd node with `etcd_deployment_type: host` (the default) does
  **not** get a container engine, because it is neither in `k8s_cluster` nor using
  Docker for etcd.

## References

- `roles/kubespray_defaults/defaults/main/main.yml` — expression (line shifts by
  tag: L322 in v2.29.0/v2.29.1, L323 in v2.30.0, L335 in v2.31.0).
- Tags: v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
