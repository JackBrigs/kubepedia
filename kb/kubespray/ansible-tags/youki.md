---
id: TAG-YOUKI
type: ansible_tag
title: "youki (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - youki
  - "--tags youki"
tags:
  - ansible-tag
  - container-engine
sources:
  - type: code
    path: roles/container-engine/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/tasks/main.yml
    note: "run-tag youki"
relations: []
---

# youki (Ansible run-tag)

## Summary

Настройка OCI-рантайма youki.

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `k8s_cluster`, `etcd`, `kube_node`, `kube_control_plane`, `calico_rr`
- **Roles:** `container-engine/youki`, `kubernetes-apps/container_runtimes/youki`

## Implementation

Настройка OCI-рантайма youki. (1) container-engine: подроль container-engine/youki (при youki_enabled и container_manager=='crio') скачивает бинарник youki через download_file и копирует его в {{ youki_bin_dir }}/youki на узлах. (2) apps/container-runtimes: подроль kubernetes-apps/container_runtimes/youki (при youki_enabled и container_manager=='crio') шаблонизирует и применяет объект RuntimeClass "youki" в кластере (только на первом узле kube_control_plane).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** youki поддерживается только совместно с CRI-O (условие youki_enabled и container_manager=='crio' в обеих ролях). Установочная часть требует скачанного бинарника (download), часть RuntimeClass — готового кластера и kubectl. В scale.yml роль apps не выполняется, RuntimeClass там не создаётся.

## References

- `roles/container-engine/tasks/main.yml`
- `roles/container-engine/youki/tasks/main.yml`
- `roles/kubernetes-apps/container_runtimes/meta/main.yml`
- `roles/kubernetes-apps/container_runtimes/youki/tasks/main.yaml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
