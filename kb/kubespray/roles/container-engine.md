---
id: ROLE-CONTAINER_ENGINE
type: role
title: container-engine
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - container-engine
tags:
  - role
sources:
  - type: code
    path: roles/container-engine
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/roles/container-engine
    note: "container-engine role"
relations:
  - type: see_also
    target: TAG-CONTAINER_ENGINE
---

# container-engine

## Summary

Installs and configures the container runtime selected by container_manager (containerd/crio/docker) by dispatching to the runtime sub-roles.

## Implementation

Task files under `roles/container-engine/tasks/`. Invoked from the playbooks under the
corresponding run-tag (see [[TAG-CONTAINER_ENGINE]]).

## Configuration

Driven by variables in `roles/kubespray_defaults` (see [[ROLE-KUBESPRAY_DEFAULTS]]) and the role's own `defaults/`.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.

## References

- `roles/container-engine/` (tag `v2.31.0` `1c9add4`).
