---
id: TAG-REGISTRY
type: ansible_tag
title: "registry (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - registry
  - "--tags registry"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/meta/main.yml
    note: "run-tag registry"
relations: []
---

# registry (Ansible run-tag)

## Summary

Разворачивает внутрикластерный docker registry: валидирует registry_service_type и связанные переменные, создаёт addon-каталог, рендерит манифесты (namespace, SA, ...) и применяет их.

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/registry`

## Implementation

Разворачивает внутрикластерный docker registry: валидирует registry_service_type и связанные переменные, создаёт addon-каталог, рендерит манифесты (namespace, SA, ...) и применяет их. Роль kubernetes-apps/registry подключается в kubernetes-apps/meta.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Включается только при registry_enabled (по умолчанию false) и на kube_control_plane[0]. Начинается с набора проверок совместимости registry_service_type (ClusterIP/LoadBalancer/NodePort) — при конфликте конфигурации задачи fail останавливают выполнение. Требует apiserver. docs/ansible/ansible.md: «Configuring local docker registry».

## References

- `roles/kubernetes-apps/meta/main.yml`
- `roles/kubernetes-apps/registry/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
