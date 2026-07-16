---
id: TAG-PERSISTENT_VOLUMES
type: ansible_tag
title: "persistent_volumes (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - persistent_volumes
  - "--tags persistent_volumes"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/meta/main.yml
    note: "run-tag persistent_volumes"
relations: []
---

# persistent_volumes (Ansible run-tag)

## Summary

Запускает роль roles/kubernetes-apps/persistent_volumes, которая через свои зависимости создаёт объекты хранилища (StorageClass/PV) для включённых CSI: cinder, aws-ebs, azuredisk, gcp-pd, upcloud.

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`, `scale.yml`
- **Affected host groups:** `kube_control_plane`, `k8s_cluster`
- **Roles:** `kubernetes-apps/persistent_volumes`, `kubernetes/preinstall`

## Implementation

Запускает роль roles/kubernetes-apps/persistent_volumes, которая через свои зависимости создаёт объекты хранилища (StorageClass/PV) для включённых CSI: cinder, aws-ebs, azuredisk, gcp-pd, upcloud. Дополнительно этим же тегом помечена задача создания директорий под локальное хранилище в preinstall (roles/kubernetes/preinstall/tasks/0050-create_directories.yml).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: safe.** Условие включения роли persistent_volumes: persistent_volumes_enabled, и она выполняется только на groups['kube_control_plane'][0]. Реально созданные объекты зависят от включённых *_csi_enabled (см. persistent_volumes_* под-теги). Задача создания директорий в preinstall (тег persistent_volumes) выполняется на группе k8s_cluster и попадает также в scale.yml (через роль preinstall). Требует работающий control plane для применения манифестов.

## References

- `roles/kubernetes-apps/meta/main.yml`
- `roles/kubernetes-apps/persistent_volumes/meta/main.yml`
- `roles/kubernetes/preinstall/tasks/0050-create_directories.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
