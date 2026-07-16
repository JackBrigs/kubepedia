---
id: TAG-VALIDATE_CONTAINER_ENGINE
type: ansible_tag
title: "validate-container-engine (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - validate-container-engine
  - "--tags validate-container-engine"
tags:
  - ansible-tag
  - container-engine
sources:
  - type: code
    path: roles/container-engine/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/meta/main.yml
    note: "run-tag validate-container-engine"
relations: []
---

# validate-container-engine (Ansible run-tag)

## Summary

Первая (валидирующая) подроль роли container-engine (container-engine/validate-container-engine).

## Context

- **Playbooks:** `cluster.yml`, `scale.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `k8s_cluster`, `etcd`, `kube_node`, `kube_control_plane`, `calico_rr`
- **Roles:** `container-engine/validate-container-engine`, `remove_node/pre_remove`, `container-engine/containerd`, `container-engine/docker`, `container-engine/cri-o`

## Implementation

Первая (валидирующая) подроль роли container-engine (container-engine/validate-container-engine). Определяет is_ostree, наличие systemd-юнита kubelet, собирает service_facts и ищет установленные сервисы containerd/docker/crio. Если обнаружен запущенный движок, отличный от текущего container_manager (и это не ostree/Flatcar), выполняет удаление старого движка: при необходимости drain узла (роль remove_node/pre_remove, тег pre-remove), остановку kubelet и import_role соответствующей reset-логики (container-engine/containerd|docker|cri-o, tasks_from=reset). Обеспечивает корректный переход между container runtimes.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Выполняется как часть роли container-engine (навешан тег container-engine и validate-container-engine). Потенциально деструктивен: при смене движка может вызвать drain узла, остановку kubelet и полное удаление ранее установленного контейнерного движка. Опирается на факты (service_facts, is_ostree). Изолированный запуск безопасен только если движок не менялся; иначе способен нарушить работу узла.

## References

- `roles/container-engine/meta/main.yml`
- `roles/container-engine/validate-container-engine/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
