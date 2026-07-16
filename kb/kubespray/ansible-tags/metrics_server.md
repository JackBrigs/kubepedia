---
id: TAG-METRICS_SERVER
type: ansible_tag
title: "metrics_server (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - metrics_server
  - "--tags metrics_server"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/meta/main.yml
    note: "run-tag metrics_server"
relations: []
---

# metrics_server (Ansible run-tag)

## Summary

Разворачивает Kubernetes Metrics Server: удаляет прежний addon-каталог (задача с тегом upgrade), создаёт каталог заново, рендерит манифесты (SA, Deployment, Service, APIService, ClusterRole/RoleBinding) и применяет их.

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/metrics_server`

## Implementation

Разворачивает Kubernetes Metrics Server: удаляет прежний addon-каталог (задача с тегом upgrade), создаёт каталог заново, рендерит манифесты (SA, Deployment, Service, APIService, ClusterRole/RoleBinding) и применяет их. Роль kubernetes-apps/metrics_server подключается в kubernetes-apps/meta.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Включается только при metrics_server_enabled (по умолчанию false), выполняется на kube_control_plane[0]. Часть задач помечена дополнительным тегом upgrade (пересоздание манифестов при обновлении). Требует apiserver. docs/ansible/ansible.md: «Configuring metrics_server».

## References

- `roles/kubernetes-apps/meta/main.yml`
- `roles/kubernetes-apps/metrics_server/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
