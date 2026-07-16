---
id: TAG-SERVICES
type: ansible_tag
title: "services (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - services
  - "--tags services"
tags:
  - ansible-tag
  - reset
sources:
  - type: code
    path: roles/reset/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/reset/tasks/main.yml
    note: "run-tag services"
relations: []
---

# services (Ansible run-tag)

## Summary

Остановка и удаление systemd-сервисов при сбросе узла (роль reset).

## Context

- **Playbooks:** `reset.yml`, `remove_node.yml`
- **Affected host groups:** `k8s_cluster`, `etcd`, `calico_rr`
- **Roles:** `reset`

## Implementation

Остановка и удаление systemd-сервисов при сбросе узла (роль reset). Тег services помечает: остановку/отключение kubelet, cri-dockerd, containerd, etcd, etcd-events; удаление unit-файлов этих сервисов (а также calico-node, k8s-certs-renew, http-proxy drop-in), и рестарт сетевых сервисов (NetworkManager/systemd-networkd/networking) после сброса. Останавливает компоненты кластера на узле.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: unsafe.** Разрушающая операция: останавливает kubelet/containerd/etcd и удаляет их unit-файлы. Опасно на рабочем узле вне полного сброса. Соответствует docs/ansible/ansible.md ("Remove services (etcd, kubelet etc...) when resetting").

## References

- `roles/reset/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
