---
id: TAG-LOCAL_VOLUME_PROVISIONER
type: ansible_tag
title: "local-volume-provisioner (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - local-volume-provisioner
  - "--tags local-volume-provisioner"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/external_provisioner/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/external_provisioner/meta/main.yml
    note: "run-tag local-volume-provisioner"
relations: []
---

# local-volume-provisioner (Ansible run-tag)

## Summary

Разворачивает sig-storage local-volume-provisioner (roles/kubernetes-apps/external_provisioner/local_volume_provisioner): генерирует манифесты (namespace/RBAC/StorageClass/DaemonSet) и применяет их через kubectl..

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/external_provisioner/local_volume_provisioner`

## Implementation

Разворачивает sig-storage local-volume-provisioner (roles/kubernetes-apps/external_provisioner/local_volume_provisioner): генерирует манифесты (namespace/RBAC/StorageClass/DaemonSet) и применяет их через kubectl.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: safe.** Условие включения: local_volume_provisioner_enabled; роль выполняется только на groups['kube_control_plane'][0]. Помечена также тегами apps и external-provisioner. При выключенном флаге — no-op. Требует работающий control plane.

## References

- `roles/kubernetes-apps/external_provisioner/meta/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
