---
id: TAG-SNAPSHOTS
type: ansible_tag
title: "snapshots (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - snapshots
  - "--tags snapshots"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/meta/main.yml
    note: "run-tag snapshots"
relations: []
---

# snapshots (Ansible run-tag)

## Summary

Зонтичный тег подсистемы снапшотов.

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/snapshots`, `kubernetes-apps/snapshots/snapshot-controller`, `kubernetes-apps/snapshots/cinder-csi`

## Implementation

Зонтичный тег подсистемы снапшотов. Запускает роль roles/kubernetes-apps/snapshots, которая через зависимости ставит snapshot-controller (при cinder_csi_enabled or csi_snapshot_controller_enabled) и VolumeSnapshotClass Cinder (при cinder_csi_enabled). Роль выполняется на groups['kube_control_plane'][0].

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: safe.** В roles/kubernetes-apps/meta/main.yml роль snapshots помечена тегами snapshots и csi-driver и выполняется только на первом control plane узле (без флага включения на уровне роли; конкретные зависимости имеют свои условия). Отличие от родственных тегов: snapshots — зонтик; snapshot-controller — только контроллер снапшотов; snapshot — только VolumeSnapshotClass Cinder. Требует работающий control plane.

## References

- `roles/kubernetes-apps/meta/main.yml`
- `roles/kubernetes-apps/snapshots/meta/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
