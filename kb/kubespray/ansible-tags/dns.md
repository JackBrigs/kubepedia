---
id: TAG-DNS
type: ansible_tag
title: "dns (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - dns
  - "--tags dns"
tags:
  - ansible-tag
  - reset
sources:
  - type: code
    path: roles/reset/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/reset/tasks/main.yml
    note: "run-tag dns"
relations: []
---

# dns (Ansible run-tag)

## Summary

Задачи очистки DNS-настроек при сбросе узла (роль reset).

## Context

- **Playbooks:** `reset.yml`, `remove_node.yml`
- **Affected host groups:** `k8s_cluster`, `etcd`, `calico_rr`
- **Roles:** `reset`

## Implementation

Задачи очистки DNS-настроек при сбросе узла (роль reset). В v2.30.0 тег dns стоит на задаче удаления добавленных Ansible блоков из /etc/dhclient.conf и /etc/dhcp/dhclient.conf (blockinfile state=absent). Убирает DNS-записи, внесённые Kubespray в конфигурацию dhclient.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Разрушающая операция сброса (удаление конфигурации), но узкая по охвату. Выполняется в составе роли reset (playbooks reset.yml/remove_node.yml). Соответствует docs/ansible/ansible.md ("Remove dns entries when resetting").
 [v2.31.0] Без изменений (reset-тег DNS).

## References

- `roles/reset/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
