---
id: TAG-IP6TABLES
type: ansible_tag
title: "ip6tables (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - ip6tables
  - "--tags ip6tables"
tags:
  - ansible-tag
  - reset
sources:
  - type: code
    path: roles/reset/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/reset/tasks/main.yml
    note: "run-tag ip6tables"
relations: []
---

# ip6tables (Ansible run-tag)

## Summary

Сброс правил IPv6-фаервола при reset (роль reset).

## Context

- **Playbooks:** `reset.yml`, `remove_node.yml`
- **Affected host groups:** `k8s_cluster`, `etcd`, `calico_rr`
- **Roles:** `reset`

## Implementation

Сброс правил IPv6-фаервола при reset (роль reset). Тег ip6tables помечает задачи установки политик ACCEPT для цепочек INPUT/FORWARD/OUTPUT (ip_version ipv6), флаш таблиц filter/nat/mangle/raw и удаление пользовательских цепочек (ip6tables -X). Выполняется только при flush_iptables=true и включённом ipv6_stack.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: unsafe.** Разрушающая сетевая операция: сбрасывает IPv6-фаервол узла. Требует flush_iptables=true и ipv6_stack. Опасно вне полного сброса. В docs/ansible/ansible.md отдельной строки для ip6tables нет (описан только iptables) — тег подтверждён кодом roles/reset/tasks/main.yml.

## References

- `roles/reset/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
