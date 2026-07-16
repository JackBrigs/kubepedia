---
id: TAG-KATA_CONTAINERS
type: ansible_tag
title: "kata-containers (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - kata-containers
  - "--tags kata-containers"
tags:
  - ansible-tag
  - container-engine
sources:
  - type: code
    path: roles/container-engine/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/meta/main.yml
    note: "run-tag kata-containers"
relations: []
---

# kata-containers (Ansible run-tag)

## Summary

Настройка рантайма Kata Containers.

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `k8s_cluster`, `etcd`, `kube_node`, `kube_control_plane`, `calico_rr`
- **Roles:** `container-engine/kata-containers`, `kubernetes-apps/container_runtimes/kata_containers`

## Implementation

Настройка рантайма Kata Containers. (1) container-engine: подроль container-engine/kata-containers (при kata_containers_enabled) скачивает и распаковывает бинарники kata в корень, создаёт каталог конфигурации, шаблонизирует configuration-qemu.toml и containerd-shim-kata-qemu-v2, загружает и закрепляет модули ядра vhost_vsock и vhost_net (/etc/modules-load.d/kubespray-kata-containers.conf). (2) apps/container-runtimes: подроль kubernetes-apps/container_runtimes/kata_containers (при kata_containers_enabled) создаёт addons/kata_containers, шаблонизирует runtimeclass-kata-qemu.yml и применяет RuntimeClass через kube (только на первом kube_control_plane).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** В meta container-engine подроль kata-containers включается только при kata_containers_enabled (без ограничения по container_manager). Загружает модули ядра vhost на узлах. Требует скачанных артефактов; RuntimeClass — готового кластера и kubectl.

## References

- `roles/container-engine/meta/main.yml`
- `roles/container-engine/kata-containers/tasks/main.yml`
- `roles/kubernetes-apps/container_runtimes/meta/main.yml`
- `roles/kubernetes-apps/container_runtimes/kata_containers/tasks/main.yaml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
