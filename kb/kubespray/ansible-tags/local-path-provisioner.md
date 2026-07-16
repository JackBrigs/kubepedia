---
id: TAG-LOCAL_PATH_PROVISIONER
type: ansible_tag
title: "local-path-provisioner (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - local-path-provisioner
  - "--tags local-path-provisioner"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/external_provisioner/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/external_provisioner/meta/main.yml
    note: "run-tag local-path-provisioner"
relations: []
---

# local-path-provisioner (Ansible run-tag)

## Summary

Разворачивает Rancher local-path-provisioner (roles/kubernetes-apps/external_provisioner/local_path_provisioner): генерирует манифесты (namespace/RBAC/ConfigMap/Deployment/StorageClass) и применяет их через kubectl..

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/external_provisioner/local_path_provisioner`

## Implementation

Разворачивает Rancher local-path-provisioner (roles/kubernetes-apps/external_provisioner/local_path_provisioner): генерирует манифесты (namespace/RBAC/ConfigMap/Deployment/StorageClass) и применяет их через kubectl.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: safe.** Условие включения: local_path_provisioner_enabled. В отличие от local-volume-provisioner, роль не ограничена узлом [0] и подключается на всех kube_control_plane (внутри задач применение манифестов обычно всё равно выполняется только на первом узле). Помечена также тегами apps и external-provisioner. При выключенном флаге — no-op.

## References

- `roles/kubernetes-apps/external_provisioner/meta/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
