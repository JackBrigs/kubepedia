---
id: TAG-CNI
type: ansible_tag
title: "cni (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - cni
  - "--tags cni"
tags:
  - ansible-tag
  - win-nodes
sources:
  - type: code
    path: roles/win_nodes/kubernetes_patch/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/win_nodes/kubernetes_patch/tasks/main.yml
    note: "run-tag cni"
relations: []
---

# cni (Ansible run-tag)

## Summary

ВНИМАНИЕ: в v2.30.0 Ansible-тег cni назначен только одной задаче — "Ensure that user manifests directory exists" в роли win_nodes/kubernetes_patch (tags: [init, cni]), выполняемой в play "Patch Kubernetes for Windows" на хосте kube_control_plane[0].

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `win_nodes/kubernetes_patch`

## Implementation

ВНИМАНИЕ: в v2.30.0 Ansible-тег cni назначен только одной задаче — "Ensure that user manifests directory exists" в роли win_nodes/kubernetes_patch (tags: [init, cni]), выполняемой в play "Patch Kubernetes for Windows" на хосте kube_control_plane[0]. Эта задача создаёт каталог пользовательских манифестов. Установка CNI-плагинов (бинарники в /opt/cni/bin роли network_plugin/cni) под тег cni НЕ помечена — она идёт под тегом network.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: safe.** Расхождение с docs/ansible/ansible.md: документация описывает cni как "CNI plugins for Network Plugins", но фактически (приоритет кода, раздел 6.2 CLAUDE.md) тег cni в v2.30.0 привязан лишь к созданию каталога манифестов в win_nodes-патче. Для реальной установки CNI используйте тег network.

## References

- `roles/win_nodes/kubernetes_patch/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
