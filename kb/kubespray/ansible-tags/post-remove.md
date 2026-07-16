---
id: TAG-POST_REMOVE
type: ansible_tag
title: "post-remove (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - post-remove
  - "--tags post-remove"
tags:
  - ansible-tag
  - remove-node
sources:
  - type: code
    path: roles/remove-node/post-remove/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/remove-node/post-remove/tasks/main.yml
    note: "run-tag post-remove"
relations: []
---

# post-remove (Ansible run-tag)

## Summary

Финальный этап удаления узла (роль remove-node/post-remove в playbooks/remove_node.yml).

## Context

- **Playbooks:** `remove-node.yml`
- **Affected host groups:** `kube_node`, `kube_control_plane`, `etcd`
- **Roles:** `remove-node/post-remove`

## Implementation

Финальный этап удаления узла (роль remove-node/post-remove в playbooks/remove_node.yml). Выполняет kubectl delete node для удаляемого узла с делегированием на первый control plane узел, с ретраями. Запускается на хостах, указанных в переменной node.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: unsafe.** Разрушающая операция (удаление узла из кластера). Зависит от переменной nodes, регистрируемой на этапе pre-remove (список узлов кластера), поэтому не может корректно выполняться в изоляции от pre-remove. Первый control plane/etcd узел удалять нельзя (ограничение remove_node.yml).

## References

- `roles/remove-node/post-remove/tasks/main.yml`
- `playbooks/remove_node.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
