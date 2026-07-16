---
id: TAG-CONTAINER_RUNTIMES
type: ansible_tag
title: "container-runtimes (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - container-runtimes
  - "--tags container-runtimes"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/container_runtimes/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/container_runtimes/meta/main.yml
    note: "run-tag container-runtimes"
relations: []
---

# container-runtimes (Ansible run-tag)

## Summary

Тег этапа apps (роль kubernetes-apps/container_runtimes).

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/container_runtimes`, `kubernetes-apps/container_runtimes/kata_containers`, `kubernetes-apps/container_runtimes/gvisor`, `kubernetes-apps/container_runtimes/crun`, `kubernetes-apps/container_runtimes/youki`

## Implementation

Тег этапа apps (роль kubernetes-apps/container_runtimes). Не устанавливает бинарники на узлах, а создаёт в кластере объекты RuntimeClass для дополнительных рантаймов: kata-containers (если kata_containers_enabled), gvisor (если gvisor_enabled), crun (если crun_enabled), youki (если youki_enabled и container_manager=='crio'). Для каждого включённого рантайма шаблонизируется манифест runtimeclass-*.yml в {{ kube_config_dir }} и применяется через модуль kube (kubectl apply). Все задачи выполняются только на первом узле kube_control_plane (inventory_hostname == groups['kube_control_plane'][0]).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Запускается в рамках роли kubernetes-apps (тег apps) на группе kube_control_plane, но фактически действует только на первом control plane узле. Требует работающего кластера и валидного kubeconfig ({{ bin_dir }}/kubectl), поэтому изолированный запуск на неготовом кластере завершится ошибкой. Создаёт только RuntimeClass; сами рантаймы должны быть предварительно установлены тегом container-engine.

## References

- `roles/kubernetes-apps/container_runtimes/meta/main.yml`
- `roles/kubernetes-apps/meta/main.yml`
- `roles/kubernetes-apps/container_runtimes/kata_containers/tasks/main.yaml`
- `roles/kubernetes-apps/container_runtimes/gvisor/tasks/main.yaml`
- `roles/kubernetes-apps/container_runtimes/crun/tasks/main.yaml`
- `roles/kubernetes-apps/container_runtimes/youki/tasks/main.yaml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
