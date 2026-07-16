---
id: TAG-SNAPSHOT_CONTROLLER
type: ansible_tag
title: "snapshot-controller (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - snapshot-controller
  - "--tags snapshot-controller"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/snapshots/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/snapshots/meta/main.yml
    note: "run-tag snapshot-controller"
relations: []
---

# snapshot-controller (Ansible run-tag)

## Summary

Разворачивает CSI Snapshot Controller: проверяет наличие namespace, генерирует и применяет манифесты snapshot-ns, rbac-snapshot-controller, snapshot-controller (roles/kubernetes-apps/snapshots/snapshot-controller/tasks/main.yml).

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/snapshots/snapshot-controller`

## Implementation

Разворачивает CSI Snapshot Controller: проверяет наличие namespace, генерирует и применяет манифесты snapshot-ns, rbac-snapshot-controller, snapshot-controller (roles/kubernetes-apps/snapshots/snapshot-controller/tasks/main.yml). Ставит сам контроллер снапшотов и его RBAC, но не VolumeSnapshotClass.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: safe.** Условие включения: cinder_csi_enabled or csi_snapshot_controller_enabled. Все задачи ограничены groups['kube_control_plane'][0]. Отличие от тега snapshot: этот ставит контроллер и RBAC, а snapshot создаёт только VolumeSnapshotClass Cinder. Требует работающий control plane.

## References

- `roles/kubernetes-apps/snapshots/meta/main.yml`
- `roles/kubernetes-apps/snapshots/snapshot-controller/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
