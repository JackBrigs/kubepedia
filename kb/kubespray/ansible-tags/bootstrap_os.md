---
id: TAG-BOOTSTRAP_OS
type: ansible_tag
title: "bootstrap_os (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - bootstrap_os
  - "--tags bootstrap_os"
tags:
  - ansible-tag
  - bootstrap-os
sources:
  - type: code
    path: playbooks/internal_facts.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/internal_facts.yml
    note: "run-tag bootstrap_os"
relations: []
---

# bootstrap_os (Ansible run-tag)

## Summary

Объединяет задачи первичной подготовки ОС узлов.

## Context

- **Playbooks:** `cluster.yml`, `scale.yml`, `upgrade_cluster.yml`, `reset.yml`, `remove_node.yml`
- **Affected host groups:** `k8s_cluster`, `etcd`, `calico_rr`
- **Roles:** `bootstrap_os`, `system_packages`, `kubernetes/preinstall`

## Implementation

Объединяет задачи первичной подготовки ОС узлов. Включает роль bootstrap_os (playbooks/internal_facts.yml: определение дистрибутива, подключение distro-специфичных vars/tasks, hostname, bash_completion), установку системных пакетов через роль system_packages (обновление кэша пакетов, epel-release, установка/удаление пакетов) и задачи роли kubernetes/preinstall: создание каталогов (0050), настройка resolvconf/systemd-resolved/NetworkManager DNS, системные конфигурации sysctl/SELinux/ip_forward (0080), NTP (0081) и dhclient-хуки. Меняет системные настройки, DNS-резолвинг, пакеты и sysctl на узлах.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Часть задач зависит от фактов и переменных, задаваемых задачами с тегом facts (include_vars distro-специфики в bootstrap_os, набор пакетов pkgs). При запуске только `--tags bootstrap_os` без facts часть переменных может оказаться не определена. Соответствует docs/ansible/ansible.md ("Anything related to host OS configuration").

## References

- `playbooks/internal_facts.yml`
- `roles/system_packages/tasks/main.yml`
- `roles/kubernetes/preinstall/tasks/main.yml`
- `roles/kubernetes/preinstall/tasks/0050-create_directories.yml`
- `roles/kubernetes/preinstall/tasks/0080-system-configurations.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
