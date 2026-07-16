---
id: TAG-SYSTEM_PACKAGES
type: ansible_tag
title: "system-packages (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - system-packages
  - "--tags system-packages"
tags:
  - ansible-tag
  - bootstrap-os
sources:
  - type: code
    path: roles/bootstrap_os/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/bootstrap_os/tasks/main.yml
    note: "run-tag system-packages"
relations: []
---

# system-packages (Ansible run-tag)

## Summary

Установка системных пакетов через пакетный менеджер ОС (роль bootstrap_os → import роли system_packages).

## Context

- **Playbooks:** `cluster.yml`, `scale.yml`, `upgrade_cluster.yml`, `reset.yml`, `remove_node.yml`
- **Affected host groups:** `k8s_cluster`, `etcd`, `calico_rr`
- **Roles:** `bootstrap_os`, `system_packages`

## Implementation

Установка системных пакетов через пакетный менеджер ОС (роль bootstrap_os → import роли system_packages). Обновляет кэш пакетов (zypper/apt/dnf), удаляет устаревший файл репозитория docker, ставит epel-release на RHEL-производных и выполняет установку/удаление пакетов из наборов pkgs и pkgs_to_remove. Пропускается на Flatcar и Fedora CoreOS.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Роль system_packages вызывается из bootstrap_os, где distro-специфичные vars (в т.ч. наборы пакетов) подключаются задачами с тегом facts. При запуске только `--tags system-packages` без facts переменные pkgs могут быть не определены. Соответствует docs/ansible/ansible.md ("Install packages using OS package manager").

## References

- `roles/bootstrap_os/tasks/main.yml`
- `roles/system_packages/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
