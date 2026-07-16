---
id: TAG-SCHEDULER_PLUGINS
type: ansible_tag
title: "scheduler_plugins (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - scheduler_plugins
  - "--tags scheduler_plugins"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/meta/main.yml
    note: "run-tag scheduler_plugins"
relations: []
---

# scheduler_plugins (Ansible run-tag)

## Summary

Разворачивает проект scheduler-plugins (SIG Scheduling): создаёт каталог, рендерит и применяет CRD (appgroups, networktopologies, elasticquotas, podgroups, noderesourcetopologies), namespace, SA, RBAC, ConfigMap и deployment контроллера/шедулера, ожидает готовности подов.

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/scheduler_plugins`

## Implementation

Разворачивает проект scheduler-plugins (SIG Scheduling): создаёт каталог, рендерит и применяет CRD (appgroups, networktopologies, elasticquotas, podgroups, noderesourcetopologies), namespace, SA, RBAC, ConfigMap и deployment контроллера/шедулера, ожидает готовности подов. Роль kubernetes-apps/scheduler_plugins.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** ВАЖНО. Условие подключения роли в roles/kubernetes-apps/meta/main.yml: scheduler_plugins_enabled (по умолчанию false) И kube_major_version is version('1.29', '<') И kube_control_plane[0]. kube_major_version вычисляется из kube_version (roles/kubespray_defaults/ vars/main/main.yml: "{{ (kube_version | split('.'))[:-1] | join('.') }}"), а kube_version по умолчанию в v2.30.0 = 1.34.x, то есть kube_major_version = "1.34". Проверка "1.34" < "1.29" ложна, поэтому при дефолтной версии Kubernetes роль scheduler_plugins НЕ разворачивается даже при scheduler_plugins_enabled=true — addon фактически инертен для K8s >= 1.29. Развернуть его можно только на кластере с kube_version < 1.29. Это отличие от предыдущих версий следует учитывать: тег присутствует, но при штатной установке v2.30.0 ничего не делает.

## References

- `roles/kubernetes-apps/meta/main.yml`
- `roles/kubernetes-apps/scheduler_plugins/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
