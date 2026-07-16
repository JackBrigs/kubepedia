---
id: TAG-SNAPSHOT
type: ansible_tag
title: "snapshot (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - snapshot
  - "--tags snapshot"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/snapshots/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/snapshots/meta/main.yml
    note: "run-tag snapshot"
relations: []
---

# snapshot (Ansible run-tag)

## Summary

Создаёт VolumeSnapshotClass для Cinder CSI: копирует шаблон cinder-csi-snapshot-class.yml и применяет его через kubectl (roles/kubernetes-apps/snapshots/cinder-csi/tasks/main.yml).

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/snapshots/cinder-csi`

## Implementation

Создаёт VolumeSnapshotClass для Cinder CSI: копирует шаблон cinder-csi-snapshot-class.yml и применяет его через kubectl (roles/kubernetes-apps/snapshots/cinder-csi/tasks/main.yml). Не ставит сам контроллер снапшотов.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: safe.** Условие включения: cinder_csi_enabled (тег помечен вместе с cinder-csi-driver). Задачи ограничены groups['kube_control_plane'][0]. Отличие от snapshot-controller: snapshot = только VolumeSnapshotClass Cinder; snapshot-controller = сам контроллер; snapshots = зонтик над обоими. Практически бесполезен без snapshot-controller.

## References

- `roles/kubernetes-apps/snapshots/meta/main.yml`
- `roles/kubernetes-apps/snapshots/cinder-csi/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
