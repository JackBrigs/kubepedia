---
id: TAG-CONTAINER_ENGINE_ACCELERATOR
type: ansible_tag
title: "container_engine_accelerator (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - container_engine_accelerator
  - "--tags container_engine_accelerator"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/container_engine_accelerator/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/container_engine_accelerator/meta/main.yml
    note: "run-tag container_engine_accelerator"
relations: []
---

# container_engine_accelerator (Ansible run-tag)

## Summary

Тег этапа apps (роль kubernetes-apps/container_engine_accelerator).

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/container_engine_accelerator`, `kubernetes-apps/container_engine_accelerator/nvidia_gpu`

## Implementation

Тег этапа apps (роль kubernetes-apps/container_engine_accelerator). Включает поддержку GPU-ускорителей. Через meta-зависимость подключает подроль nvidia_gpu при nvidia_accelerator_enabled. Загружает ОС-специфичные переменные, формирует URL драйвера NVIDIA (flavor tesla/gtx), создаёт каталог addons и шаблонизирует манифесты nvidia-driver-install-daemonset.yml и k8s-device-plugin-nvidia-daemonset.yml, затем применяет их через модуль kube. Действия по созданию/применению манифестов выполняются только на первом узле kube_control_plane и только при nvidia_driver_install_container (и nvidia_driver_install_supported для apply).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** В roles/kubernetes-apps/meta/main.yml роль включается по условию nvidia_accelerator_enabled. По содержанию задач тег container_engine_accelerator и тег nvidia_gpu в v2.30.0 практически эквивалентны (обе ведут к подроли nvidia_gpu). Требует готового кластера и kubectl; изолированный запуск на неготовом кластере невозможен.

## References

- `roles/kubernetes-apps/container_engine_accelerator/meta/main.yml`
- `roles/kubernetes-apps/meta/main.yml`
- `roles/kubernetes-apps/container_engine_accelerator/nvidia_gpu/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
