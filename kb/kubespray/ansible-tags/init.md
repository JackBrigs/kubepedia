---
id: TAG-INIT
type: ansible_tag
title: "init (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - init
  - "--tags init"
tags:
  - ansible-tag
  - win-nodes
sources:
  - type: code
    path: roles/win_nodes/kubernetes_patch/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/win_nodes/kubernetes_patch/tasks/main.yml
    note: "run-tag init"
relations: []
---

# init (Ansible run-tag)

## Summary

Задачи инициализации для поддержки Windows-узлов (роль win_nodes/kubernetes_patch).

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `win_nodes/kubernetes_patch`

## Implementation

Задачи инициализации для поддержки Windows-узлов (роль win_nodes/kubernetes_patch). Тег init стоит на создании каталога пользовательских манифестов (kubernetes_user_manifests_path/kubernetes) и на применении nodeSelector (kubernetes.io/os=linux) к DaemonSet kube-proxy через kubectl patch, чтобы kube-proxy не планировался на Windows-узлы. Выполняется на первом узле control plane.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Требует работающего API-сервера и kubectl (patch DaemonSet), выполняется на kube_control_plane[0]; в изоляции без поднятого кластера завершится ошибкой. В docs/ansible/ansible.md ("Windows kubernetes init nodes").

## References

- `roles/win_nodes/kubernetes_patch/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
