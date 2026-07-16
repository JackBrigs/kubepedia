---
id: TAG-SYSTEM_UPGRADE_YUM
type: ansible_tag
title: "system-upgrade-yum (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - system-upgrade-yum
  - "--tags system-upgrade-yum"
tags:
  - ansible-tag
  - upgrade
sources:
  - type: code
    path: roles/upgrade/system-upgrade/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/upgrade/system-upgrade/tasks/main.yml
    note: "run-tag system-upgrade-yum"
relations: []
---

# system-upgrade-yum (Ansible run-tag)

## Summary

Подтег системного обновления для RedHat-семейства (роль upgrade/system-upgrade).

## Context

- **Playbooks:** `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`, `kube_node`, `calico_rr`
- **Roles:** `upgrade/system-upgrade`

## Implementation

Подтег системного обновления для RedHat-семейства (роль upgrade/system-upgrade). Включает yum.yml при system_upgrade=true, ansible_os_family == 'RedHat' и не Fedora CoreOS. Выполняет обновление пакетов через YUM/DNF в рамках апгрейда кластера.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Условия: system_upgrade=true, RedHat и не Fedora CoreOS. Изолированный запуск обновляет системные пакеты и может требовать перезагрузки. Доступен только в upgrade_cluster.yml. В docs/ansible/ansible.md не описан — подтверждено кодом.

## References

- `roles/upgrade/system-upgrade/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
