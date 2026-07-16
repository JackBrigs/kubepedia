---
id: TAG-AWS_EBS_CSI_DRIVER
type: ansible_tag
title: "aws-ebs-csi-driver (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - aws-ebs-csi-driver
  - "--tags aws-ebs-csi-driver"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/meta/main.yml
    note: "run-tag aws-ebs-csi-driver"
relations: []
---

# aws-ebs-csi-driver (Ansible run-tag)

## Summary

Разворачивает CSI-драйвер AWS EBS (roles/kubernetes-apps/csi_driver/aws_ebs) и связанные объекты хранилища через roles/kubernetes-apps/persistent_volumes/aws-ebs-csi (StorageClass).

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/csi_driver/aws_ebs`, `kubernetes-apps/persistent_volumes/aws-ebs-csi`

## Implementation

Разворачивает CSI-драйвер AWS EBS (roles/kubernetes-apps/csi_driver/aws_ebs) и связанные объекты хранилища через roles/kubernetes-apps/persistent_volumes/aws-ebs-csi (StorageClass). Генерирует манифесты драйвера и StorageClass и применяет их к кластеру kubectl-ом.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: safe.** Условие включения: aws_ebs_csi_enabled. Является частью зонтичного тега csi-driver (навешан вместе с ним в roles/kubernetes-apps/meta/main.yml). Ставит и сам драйвер, и StorageClass (через persistent_volumes/aws-ebs-csi). При выключенном флаге — no-op. Требует работающий control plane.

## References

- `roles/kubernetes-apps/meta/main.yml`
- `roles/kubernetes-apps/persistent_volumes/meta/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
