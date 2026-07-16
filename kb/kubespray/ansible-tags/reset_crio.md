---
id: TAG-RESET_CRIO
type: ansible_tag
title: "reset_crio (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - reset_crio
  - "--tags reset_crio"
tags:
  - ansible-tag
  - container-engine
sources:
  - type: code
    path: roles/container-engine/cri-o/tasks/reset.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/cri-o/tasks/reset.yml
    note: "run-tag reset_crio"
relations: []
---

# reset_crio (Ansible run-tag)

## Summary

Teardown-тег внутри роли container-engine/cri-o (tasks/reset.yml).

## Context

- **Playbooks:** n/a
- **Affected host groups:** `k8s_cluster`, `etcd`, `kube_node`, `kube_control_plane`
- **Roles:** `container-engine/cri-o`, `container-engine/validate-container-engine`

## Implementation

Teardown-тег внутри роли container-engine/cri-o (tasks/reset.yml). Все задачи файла помечены этим тегом: удаление apt/yum-репозиториев Kubic/CRI-O, очистка метаданных yum, удаление crictl и /etc/crictl.yaml, остановка и отключение сервиса crio, удаление конфигурации CRI-O (/etc/crio, /etc/containers, /etc/systemd/system/crio.service.d) и удаление бинарников/libexec CRI-O (crio_bin_files, crio_libexec_files).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: unsafe.** Тег reset_crio не задан ни в одном плейбуке напрямую и в docs/ansible/ansible.md не описан. Задачи reset.yml роли cri-o достигаются через validate-container-engine (блок "Uninstall crio"), который вызывает import_role container-engine/cri-o tasks_from=reset при обнаружении иного (не crio) container_manager и запущенного crio. Изолированный запуск только с этим тегом небезопасен: пропускаются задачи сбора фактов и охранные условия блока.

## References

- `roles/container-engine/cri-o/tasks/reset.yml`
- `roles/container-engine/validate-container-engine/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
