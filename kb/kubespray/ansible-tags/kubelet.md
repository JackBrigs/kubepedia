---
id: TAG-KUBELET
type: ansible_tag
title: "kubelet (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - kubelet
  - "--tags kubelet"
tags:
  - ansible-tag
  - kubernetes
sources:
  - type: code
    path: roles/kubernetes/node/tasks/install.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/tasks/install.yml
    note: "run-tag kubelet"
relations: []
---

# kubelet (Ansible run-tag)

## Summary

Устанавливает и конфигурирует kubelet на всех узлах k8s_cluster (роль kubernetes/node): сбор фактов, копирование бинаря kubelet (node/install.yml), запись kubelet.env, kubelet-config.yaml и systemd-юнита kubelet.service, flush_handlers и включение/запуск службы kubelet (node/kubelet.yml).

## Context

- **Playbooks:** `cluster.yml`, `upgrade-cluster.yml`, `scale.yml`
- **Affected host groups:** `k8s_cluster`, `kube_node`, `kube_control_plane`
- **Roles:** `kubernetes/node`, `kubernetes/preinstall`

## Implementation

Устанавливает и конфигурирует kubelet на всех узлах k8s_cluster (роль kubernetes/node): сбор фактов, копирование бинаря kubelet (node/install.yml), запись kubelet.env, kubelet-config.yaml и systemd-юнита kubelet.service, flush_handlers и включение/запуск службы kubelet (node/kubelet.yml). Также тег kubelet используется в preinstall (meta: зависимость adduser; создание каталога в 0050-create_directories.yml).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Перезапускает службу kubelet (через handlers) — на работающем узле это кратковременно влияет на компоненты. Требует скачанного бинаря kubelet и подготовленной конфигурации (preinstall).

## References

- `roles/kubernetes/node/tasks/install.yml`
- `roles/kubernetes/node/tasks/kubelet.yml`
- `roles/kubernetes/node/tasks/main.yml`
- `roles/kubernetes/preinstall/meta/main.yml`
- `roles/kubernetes/preinstall/tasks/0050-create_directories.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
