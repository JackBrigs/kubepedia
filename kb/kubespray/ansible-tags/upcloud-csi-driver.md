---
id: TAG-UPCLOUD_CSI_DRIVER
type: ansible_tag
title: "upcloud-csi-driver (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - upcloud-csi-driver
  - "--tags upcloud-csi-driver"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/meta/main.yml
    note: "run-tag upcloud-csi-driver"
relations: []
---

# upcloud-csi-driver (Ansible run-tag)

## Summary

Разворачивает CSI-драйвер UpCloud (roles/kubernetes-apps/csi_driver/upcloud) и объекты хранилища через roles/kubernetes-apps/persistent_volumes/upcloud-csi (StorageClass)..

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/csi_driver/upcloud`, `kubernetes-apps/persistent_volumes/upcloud-csi`

## Implementation

Разворачивает CSI-драйвер UpCloud (roles/kubernetes-apps/csi_driver/upcloud) и объекты хранилища через roles/kubernetes-apps/persistent_volumes/upcloud-csi (StorageClass).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: safe.** Условие включения: upcloud_csi_enabled. Входит в зонтичный тег csi-driver. Расхождение с docs/ansible/ansible.md: в таблице документации тег upcloud-csi-driver не описан — приоритет отдан коду (v2.30.0). При выключенном флаге — no-op.

## References

- `roles/kubernetes-apps/meta/main.yml`
- `roles/kubernetes-apps/persistent_volumes/meta/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
