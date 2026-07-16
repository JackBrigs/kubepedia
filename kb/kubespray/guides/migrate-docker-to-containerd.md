---
id: PRACTICE-MIGRATE_DOCKER_TO_CONTAINERD
type: best_practice
title: "Migrating from Docker to containerd (experimental)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - migrate-docker-to-containerd
tags:
  - operations
  - container-runtime
sources:
  - type: docs
    path: docs/upgrades/migrate_docker2containerd.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/upgrades/migrate_docker2containerd.md
    note: "digest of the tag doc"
relations:
  - type: see_also
    target: VARIABLE-CONTAINER_MANAGER
---

# Migrating from Docker to containerd (experimental)

## Summary

Switching a running cluster's container engine from Docker to containerd is **not officially supported** by Kubespray. The docs provide an experimental, manual, node-by-node procedure. containerd is the default since Kubespray 2.18.0.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0` (procedure predates but still indicative).
- High-risk operation; needs full root on every node.

## Implementation

Recommended safer path: **reset and redeploy** with containerd rather than in-place migration. If migrating in place: cordon/drain each node, manually remove Docker, then re-run `cluster.yml` (set `container_manager: containerd`) — repeat per node for minimum downtime. Expect downtime and no guarantees; do not change other cluster config mid-migration. See [[VARIABLE-CONTAINER_MANAGER]], [[COMPONENT-CONTAINERD]].

## References

- `docs/upgrades/migrate_docker2containerd.md` (tag v2.31.0 `1c9add4`).
