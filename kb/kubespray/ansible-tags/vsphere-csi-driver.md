---
id: TAG-VSPHERE_CSI_DRIVER
type: ansible_tag
title: "vsphere-csi-driver (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - vsphere-csi-driver
  - "--tags vsphere-csi-driver"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/meta/main.yml
    note: "run-tag vsphere-csi-driver"
relations: []
---

# vsphere-csi-driver (Ansible run-tag)

## Summary

Разворачивает CSI-драйвер vSphere (roles/kubernetes-apps/csi_driver/vsphere): генерирует и применяет манифесты драйвера/RBAC/StorageClass.

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/csi_driver/vsphere`

## Implementation

Разворачивает CSI-драйвер vSphere (roles/kubernetes-apps/csi_driver/vsphere): генерирует и применяет манифесты драйвера/RBAC/StorageClass. В отличие от остальных *-csi-driver, отдельной под-роли в persistent_volumes нет — объекты создаются внутри самой роли csi_driver/vsphere.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: safe.** Условие включения: vsphere_csi_enabled. Входит в зонтичный тег csi-driver. В persistent_volumes/meta/main.yml под-роли vsphere нет (в отличие от cinder/aws-ebs/azure/gcp/upcloud), поэтому нет парного тега persistent_volumes_vsphere_csi. При выключенном флаге — no-op.

## References

- `roles/kubernetes-apps/meta/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
