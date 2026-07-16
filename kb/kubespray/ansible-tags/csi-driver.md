---
id: TAG-CSI_DRIVER
type: ansible_tag
title: "csi-driver (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - csi-driver
  - "--tags csi-driver"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/meta/main.yml
    note: "run-tag csi-driver"
relations: []
---

# csi-driver (Ansible run-tag)

## Summary

Зонтичный тег для всей подсистемы CSI-драйверов.

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/csi_driver/csi_crd`, `kubernetes-apps/csi_driver/cinder`, `kubernetes-apps/csi_driver/aws_ebs`, `kubernetes-apps/csi_driver/azuredisk`, `kubernetes-apps/csi_driver/gcp_pd`, `kubernetes-apps/csi_driver/upcloud`, `kubernetes-apps/csi_driver/vsphere`, `kubernetes-apps/snapshots`

## Implementation

Зонтичный тег для всей подсистемы CSI-драйверов. Включает установку CSI CRD (roles/kubernetes-apps/csi_driver/csi_crd) и всех включённых CSI-драйверов: cinder, aws_ebs, azuredisk, gcp_pd, upcloud, vsphere, а также подсистему снапшотов (roles/kubernetes-apps/snapshots). Каждая зависимость выполняется только при своём флаге (*_csi_enabled). Драйверы генерируют манифесты (Deployment/DaemonSet/RBAC/StorageClass) и применяют их через kubectl к работающему кластеру.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: safe.** В upgrade_cluster.yml тег csi-driver навешан отдельно на роль kubernetes-apps (строка 63) — это выделенный проход апгрейда CSI. Реально выполняется только то, для чего включён соответствующий флаг: cinder_csi_enabled, aws_ebs_csi_enabled, azure_csi_enabled, gcp_pd_csi_enabled, upcloud_csi_enabled, vsphere_csi_enabled; CSI CRD и snapshot-controller ставятся при (cinder_csi_enabled or csi_snapshot_controller_enabled). Если ни один флаг не включён — тег ничего не делает (no-op). Требует работающего control plane (задачи применяют манифесты через kubectl). Изолированный запуск на уже развёрнутом кластере безопасен; в offline-сценарии образы должны быть заранее скачаны (--tags download).

## References

- `roles/kubernetes-apps/meta/main.yml`
- `playbooks/upgrade_cluster.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
