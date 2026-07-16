---
id: TAG-WIN_NODES
type: ansible_tag
title: "win_nodes (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - win_nodes
  - "--tags win_nodes"
tags:
  - ansible-tag
  - win-nodes
sources:
  - type: code
    path: roles/win_nodes/kubernetes_patch/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/win_nodes/kubernetes_patch/tasks/main.yml
    note: "run-tag win_nodes"
relations: []
---

# win_nodes (Ansible run-tag)

## Summary

Специфичные для Windows задачи (роль win_nodes/kubernetes_patch), выполняются на первом узле control plane.

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `win_nodes/kubernetes_patch`

## Implementation

Специфичные для Windows задачи (роль win_nodes/kubernetes_patch), выполняются на первом узле control plane. Создают каталог пользовательских манифестов и патчат DaemonSet kube-proxy nodeSelector'ом kubernetes.io/os=linux, чтобы системные компоненты не планировались на Windows-узлы. Роль подключается с тегами [control-plane, win_nodes].

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Требует работающего API-сервера и kubectl (patch kube-proxy), выполняется на kube_control_plane[0]. В изоляции без поднятого кластера завершится ошибкой. Соответствует docs/ansible/ansible.md ("Running windows specific tasks").

## References

- `roles/win_nodes/kubernetes_patch/tasks/main.yml`
- `playbooks/cluster.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
