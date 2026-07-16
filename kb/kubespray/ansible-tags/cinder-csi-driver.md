---
id: TAG-CINDER_CSI_DRIVER
type: ansible_tag
title: "cinder-csi-driver (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - cinder-csi-driver
  - "--tags cinder-csi-driver"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/meta/main.yml
    note: "run-tag cinder-csi-driver"
relations: []
---

# cinder-csi-driver (Ansible run-tag)

## Summary

Разворачивает CSI-драйвер OpenStack Cinder (roles/kubernetes-apps/csi_driver/cinder), создаёт объекты хранилища (roles/kubernetes-apps/persistent_volumes/cinder-csi, StorageClass) и дополнительно VolumeSnapshotClass для Cinder (roles/kubernetes-apps/snapshots/cinder-csi).

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/csi_driver/cinder`, `kubernetes-apps/persistent_volumes/cinder-csi`, `kubernetes-apps/snapshots/cinder-csi`

## Implementation

Разворачивает CSI-драйвер OpenStack Cinder (roles/kubernetes-apps/csi_driver/cinder), создаёт объекты хранилища (roles/kubernetes-apps/persistent_volumes/cinder-csi, StorageClass) и дополнительно VolumeSnapshotClass для Cinder (roles/kubernetes-apps/snapshots/cinder-csi). Отличие от остальных *-csi-driver: единственный, который затрагивает и подсистему снапшотов.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: safe.** Условие включения: cinder_csi_enabled. Помимо драйвера и StorageClass создаёт VolumeSnapshotClass Cinder (snapshots/cinder-csi). Значение cinder_csi_enabled также включает установку CSI CRD и snapshot-controller (см. теги csi-driver, snapshot-controller). Требует работающий control plane.

## References

- `roles/kubernetes-apps/meta/main.yml`
- `roles/kubernetes-apps/persistent_volumes/meta/main.yml`
- `roles/kubernetes-apps/snapshots/meta/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
