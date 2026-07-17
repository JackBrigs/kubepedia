---
id: TAG-CRIO
type: ansible_tag
title: "crio (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - crio
  - "--tags crio"
tags:
  - ansible-tag
  - container-engine
sources:
  - type: code
    path: roles/container-engine/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/tasks/main.yml
    note: "run-tag crio"
relations: []
---

# crio (Ansible run-tag)

## Summary

Двойное назначение.

## Context

- **Playbooks:** `cluster.yml`, `scale.yml`, `upgrade_cluster.yml`, `reset.yml`, `remove_node.yml`
- **Affected host groups:** `k8s_cluster`, `etcd`, `kube_node`, `kube_control_plane`, `calico_rr`
- **Roles:** `container-engine/cri-o`, `reset`

## Implementation

Двойное назначение. (1) Установка: в роли container-engine (meta) подроль container-engine/cri-o выполняется при container_manager=='crio' — разворачивает движок CRI-O (репозитории/пакеты или бинарники, конфигурация, systemd-сервис crio). (2) Teardown: в роли reset (roles/reset/tasks/main.yml) задачи с тегом crio останавливают cri-контейнеры через crictl, останавливают и отключают сервис crio, и при container_manager=='crio' выполняют "crio wipe -f" (полная очистка контейнеров и образов CRI-O).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Как и containerd, тег означает установку в cluster/scale/upgrade и деструктивный teardown в reset/remove_node. Не путать с тегом reset_crio, который относится к задачам удаления CRI-O внутри роли cri-o (tasks/reset.yml), вызываемым из validate-container-engine при смене движка. Установочная часть требует download и фактов preinstall.

## References

- `roles/container-engine/tasks/main.yml`
- `roles/reset/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
