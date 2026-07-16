---
id: TAG-RESET_CONTAINERD
type: ansible_tag
title: "reset_containerd (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - reset_containerd
  - "--tags reset_containerd"
tags:
  - ansible-tag
  - container-engine
sources:
  - type: code
    path: roles/container-engine/containerd/tasks/reset.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/tasks/reset.yml
    note: "run-tag reset_containerd"
relations: []
---

# reset_containerd (Ansible run-tag)

## Summary

Teardown-тег внутри роли container-engine/containerd (tasks/reset.yml).

## Context

- **Playbooks:** n/a
- **Affected host groups:** `k8s_cluster`, `etcd`, `kube_node`, `kube_control_plane`
- **Roles:** `container-engine/containerd`, `container-engine/validate-container-engine`

## Implementation

Teardown-тег внутри роли container-engine/containerd (tasks/reset.yml). Все задачи файла reset.yml помечены этим тегом: остановка и отключение сервиса containerd, удаление конфигурационных файлов и каталогов (/etc/systemd/system/containerd.service, containerd_systemd_dir, containerd_cfg_dir, containerd_storage_dir, containerd_state_dir). Задачи выполняются, когда reset.yml роли containerd подключается извне.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: unsafe.** Тег reset_containerd не задан ни в одном плейбуке напрямую и в docs/ansible/ansible.md не описан. Задачи reset.yml роли containerd достигаются через validate-container-engine (блок "Uninstall containerd"), который вызывает import_role container-engine/containerd tasks_from=reset при обнаружении иного (не containerd) container_manager и запущенного containerd. Изолированный запуск только с --tags reset_containerd небезопасен: пропускаются задачи сбора фактов (service_facts, is_ostree) и охранные условия блока, из-за чего логика удаления выполнится вне ожидаемого контекста. Использовать осознанно.

## References

- `roles/container-engine/containerd/tasks/reset.yml`
- `roles/container-engine/validate-container-engine/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
