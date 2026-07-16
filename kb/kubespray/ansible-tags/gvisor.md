---
id: TAG-GVISOR
type: ansible_tag
title: "gvisor (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - gvisor
  - "--tags gvisor"
tags:
  - ansible-tag
  - container-engine
sources:
  - type: code
    path: roles/container-engine/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/meta/main.yml
    note: "run-tag gvisor"
relations: []
---

# gvisor (Ansible run-tag)

## Summary

Настройка песочничного рантайма gVisor (runsc).

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `k8s_cluster`, `etcd`, `kube_node`, `kube_control_plane`, `calico_rr`
- **Roles:** `container-engine/gvisor`, `kubernetes-apps/container_runtimes/gvisor`

## Implementation

Настройка песочничного рантайма gVisor (runsc). (1) container-engine: подроль container-engine/gvisor (при gvisor_enabled и container_manager in ['docker','containerd']) скачивает бинарники runsc и containerd-shim-runsc-v1 и копирует их в {{ bin_dir }} на узлах. (2) apps/container-runtimes: подроль kubernetes-apps/container_runtimes/gvisor (при gvisor_enabled) создаёт каталог addons/gvisor, шаблонизирует манифест runtimeclass-gvisor.yml и применяет объект RuntimeClass через kube (только на первом kube_control_plane).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Установка бинарников gVisor ограничена движками docker/containerd (условие в roles/container-engine/meta/main.yml). Требует скачанных артефактов (download); часть RuntimeClass требует готового кластера и kubectl.

## References

- `roles/container-engine/meta/main.yml`
- `roles/container-engine/gvisor/tasks/main.yml`
- `roles/kubernetes-apps/container_runtimes/meta/main.yml`
- `roles/kubernetes-apps/container_runtimes/gvisor/tasks/main.yaml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
