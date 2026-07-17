---
id: TAG-CONTAINERD
type: ansible_tag
title: "containerd (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - containerd
  - "--tags containerd"
tags:
  - ansible-tag
  - container-engine
sources:
  - type: code
    path: roles/container-engine/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/tasks/main.yml
    note: "run-tag containerd"
relations: []
---

# containerd (Ansible run-tag)

## Summary

Двойное назначение в зависимости от плейбука.

## Context

- **Playbooks:** `cluster.yml`, `scale.yml`, `upgrade_cluster.yml`, `reset.yml`, `remove_node.yml`
- **Affected host groups:** `k8s_cluster`, `etcd`, `kube_node`, `kube_control_plane`, `calico_rr`
- **Roles:** `container-engine/containerd`, `reset`

## Implementation

Двойное назначение в зависимости от плейбука. (1) Установка: в роли container-engine (meta) подроль container-engine/containerd выполняется при container_manager=='containerd' — скачивает и распаковывает архив containerd в containerd_bin_dir, генерирует systemd-юнит containerd.service, создаёт каталоги и конфиги (config.toml или config-v1.toml по версии), пишет http-proxy drop-in, настраивает base_runtime_spec и зеркала реестров (certs.d/hosts.toml), запускает и включает сервис containerd. (2) Teardown: в роли reset (roles/reset/tasks/main.yml) задачи с тегом containerd останавливают cri-контейнеры/поды через crictl, останавливают и удаляют containerd.service, удаляют бинарники containerd (containerd, ctr, runc, crictl и т.д.) при container_manager=='containerd'.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Тег обозначает разные операции в разных плейбуках: в cluster.yml/scale.yml/ upgrade_cluster.yml — установка/настройка containerd; в reset.yml/remove_node.yml — остановка и удаление containerd, его контейнеров/подов и бинарников. Установочная часть требует скачанных артефактов (download) и фактов preinstall. Teardown-часть в reset деструктивна. Изолированный запуск требует понимания контекста плейбука.

## References

- `roles/container-engine/tasks/main.yml`
- `roles/reset/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
