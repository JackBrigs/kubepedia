---
id: TAG-DOCKER
type: ansible_tag
title: "docker (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - docker
  - "--tags docker"
tags:
  - ansible-tag
  - container-engine
sources:
  - type: code
    path: roles/container-engine/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/tasks/main.yml
    note: "run-tag docker"
relations: []
---

# docker (Ansible run-tag)

## Summary

Двойное назначение.

## Context

- **Playbooks:** `cluster.yml`, `scale.yml`, `upgrade_cluster.yml`, `reset.yml`, `remove_node.yml`
- **Affected host groups:** `k8s_cluster`, `etcd`, `kube_node`, `kube_control_plane`, `calico_rr`
- **Roles:** `container-engine/cri-dockerd`, `container-engine/docker`, `reset`

## Implementation

Двойное назначение. (1) Установка: в роли container-engine (meta) при container_manager=='docker' выполняется подроль container-engine/cri-dockerd, которая скачивает и устанавливает бинарник cri-dockerd, генерирует systemd-юниты cri-dockerd.service и cri-dockerd.socket и запускает/включает их (сам Docker CE ставится связанными задачами роли docker). (2) Teardown: в роли reset (roles/reset/tasks/main.yml) задача "Reset | Remove Docker" при container_manager=='docker' подключает container-engine/docker tasks_from: reset — останавливает контейнеры, удаляет пакеты docker/containerd, репозитории и конфигурацию (/var/lib/docker, /etc/docker и т.д.).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** В meta-роли container-engine тег docker навешан на подроль cri-dockerd (shim, необходимый для работы kubelet с Docker). Teardown в reset деструктивен: удаляет пакеты docker-ce/containerd и все данные Docker. Изолированный запуск требует учёта контекста плейбука и предварительно скачанных артефактов.

## References

- `roles/container-engine/tasks/main.yml`
- `roles/reset/tasks/main.yml`
- `roles/container-engine/cri-dockerd/tasks/main.yml`
- `roles/container-engine/docker/tasks/reset.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
