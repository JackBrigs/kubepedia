---
id: TAG-CRUN
type: ansible_tag
title: "crun (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - crun
  - "--tags crun"
tags:
  - ansible-tag
  - container-engine
sources:
  - type: code
    path: roles/container-engine/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/meta/main.yml
    note: "run-tag crun"
relations: []
---

# crun (Ansible run-tag)

## Summary

Настройка низкоуровневого OCI-рантайма crun.

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `k8s_cluster`, `etcd`, `kube_node`, `kube_control_plane`, `calico_rr`
- **Roles:** `container-engine/crun`, `kubernetes-apps/container_runtimes/crun`

## Implementation

Настройка низкоуровневого OCI-рантайма crun. Проявляется в двух местах. (1) container-engine: подроль container-engine/crun (при crun_enabled) скачивает бинарник crun через download_file и копирует его в {{ bin_dir }}/crun на узлах. (2) apps/container-runtimes: подроль kubernetes-apps/container_runtimes/crun (при crun_enabled) шаблонизирует и применяет объект RuntimeClass "crun" в кластере (только на первом узле kube_control_plane).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Условие включения — crun_enabled (без ограничения по container_manager на этапе container-engine). Установочная часть требует скачанного бинарника (download), часть RuntimeClass требует готового кластера и kubectl. В scale.yml роль apps не выполняется, поэтому RuntimeClass там не создаётся.

## References

- `roles/container-engine/meta/main.yml`
- `roles/container-engine/crun/tasks/main.yml`
- `roles/kubernetes-apps/container_runtimes/meta/main.yml`
- `roles/kubernetes-apps/container_runtimes/crun/tasks/main.yaml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
