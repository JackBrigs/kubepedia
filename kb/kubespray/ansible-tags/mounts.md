---
id: TAG-MOUNTS
type: ansible_tag
title: "mounts (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - mounts
  - "--tags mounts"
tags:
  - ansible-tag
  - reset
sources:
  - type: code
    path: roles/reset/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/reset/tasks/main.yml
    note: "run-tag mounts"
relations: []
---

# mounts (Ansible run-tag)

## Summary

Отмонтирование каталогов kubelet при сбросе узла (роль reset).

## Context

- **Playbooks:** `reset.yml`, `remove_node.yml`
- **Affected host groups:** `k8s_cluster`, `etcd`, `calico_rr`
- **Roles:** `reset`

## Implementation

Отмонтирование каталогов kubelet при сбросе узла (роль reset). Тег mounts помечает задачу сбора смонтированных путей внутри /var/lib/kubelet/ (mount | grep | awk) и задачу их размонтирования (umount -f) с повторными попытками. Освобождает точки монтирования перед удалением данных kubelet.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Разрушающая операция сброса (принудительный umount каталогов kubelet). Выполняется в составе reset.yml/remove_node.yml. Соответствует docs/ansible/ansible.md ("Umount kubelet dirs when resetting").

## References

- `roles/reset/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
