---
id: TAG-PRE_REMOVE
type: ansible_tag
title: "pre-remove (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - pre-remove
  - "--tags pre-remove"
tags:
  - ansible-tag
  - remove-node
sources:
  - type: code
    path: roles/remove_node/pre_remove/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/remove_node/pre_remove/tasks/main.yml
    note: "run-tag pre-remove"
relations: []
---

# pre-remove (Ansible run-tag)

## Summary

Подготовка узла к удалению (роль remove_node/pre_remove в playbooks/remove_node.yml).

## Context

- **Playbooks:** `remove-node.yml`
- **Affected host groups:** `kube_node`, `kube_control_plane`, `etcd`
- **Roles:** `remove_node/pre_remove`

## Implementation

Подготовка узла к удалению (роль remove_node/pre_remove в playbooks/remove_node.yml). Получает список узлов кластера (kubectl get nodes, сохраняется в факт nodes), выполняет kubectl drain удаляемого узла (--ignore-daemonsets, --delete-emptydir-data, с ретраями и учётом allow_ungraceful_removal) и дожидается отсоединения томов (volumeattachments) от узла. Все kubectl-операции делегируются на первый control plane узел.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Выполняет drain узла (эвакуация подов) — влияет на рабочие нагрузки. Требует работающего control plane. Регистрирует факт nodes, который затем использует этап post-remove. Файл roles/container-engine/validate-container-engine/tasks/main.yml, попавший в карту тегов для pre-remove, содержит только задачи с тегом facts (meta-зависимость), собственных задач тега pre-remove не имеет.

## References

- `roles/remove_node/pre_remove/tasks/main.yml`
- `playbooks/remove_node.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
