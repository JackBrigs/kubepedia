---
id: TAG-CERT_MANAGER
type: ansible_tag
title: "cert-manager (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - cert-manager
  - "--tags cert-manager"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/ingress_controller/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/ingress_controller/meta/main.yml
    note: "run-tag cert-manager"
relations: []
---

# cert-manager (Ansible run-tag)

## Summary

Разворачивает cert-manager.

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/ingress_controller/cert_manager`

## Implementation

Разворачивает cert-manager. Удаляет устаревшие каталог/namespace прежней установки (задачи с тегом upgrade), создаёт addon-каталог, рендерит и применяет манифесты cert-manager. Подключается зависимостью роли kubernetes-apps/ingress_controller/cert_manager.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Включается только при cert_manager_enabled (по умолчанию false), выполняется на kube_control_plane[0]. Метка идёт в связке с apps и ingress-controller. Часть задач помечена дополнительным тегом upgrade (очистка legacy-ресурсов). docs/ansible/ansible.md: «Configuring certificate manager for K8s».
## References

- `roles/kubernetes-apps/ingress_controller/meta/main.yml`
- `roles/kubernetes-apps/ingress_controller/cert_manager/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
