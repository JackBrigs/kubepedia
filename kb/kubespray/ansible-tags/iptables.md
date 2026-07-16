---
id: TAG-IPTABLES
type: ansible_tag
title: "iptables (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - iptables
  - "--tags iptables"
tags:
  - ansible-tag
  - reset
sources:
  - type: code
    path: roles/reset/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/reset/tasks/main.yml
    note: "run-tag iptables"
relations: []
---

# iptables (Ansible run-tag)

## Summary

Сброс правил IPv4-фаервола при reset (роль reset).

## Context

- **Playbooks:** `reset.yml`, `remove_node.yml`
- **Affected host groups:** `k8s_cluster`, `etcd`, `calico_rr`
- **Roles:** `reset`

## Implementation

Сброс правил IPv4-фаервола при reset (роль reset). Тег iptables помечает задачи установки политик ACCEPT для цепочек INPUT/FORWARD/OUTPUT, флаш таблиц filter/nat/mangle/raw и удаление пользовательских цепочек (iptables -X). Выполняется только при flush_iptables=true и включённом ipv4_stack.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: unsafe.** Разрушающая сетевая операция: сбрасывает IPv4-фаервол узла. Требует flush_iptables=true и ipv4_stack. Опасно вне полного сброса. Соответствует docs/ansible/ansible.md ("Flush and clear iptable when resetting").

## References

- `roles/reset/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
