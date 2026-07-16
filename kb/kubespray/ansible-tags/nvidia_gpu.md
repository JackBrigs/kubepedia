---
id: TAG-NVIDIA_GPU
type: ansible_tag
title: "nvidia_gpu (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - nvidia_gpu
  - "--tags nvidia_gpu"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/container_engine_accelerator/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/container_engine_accelerator/meta/main.yml
    note: "run-tag nvidia_gpu"
relations: []
---

# nvidia_gpu (Ansible run-tag)

## Summary

Тег подроли kubernetes-apps/container_engine_accelerator/nvidia_gpu (включается при nvidia_accelerator_enabled).

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/container_engine_accelerator/nvidia_gpu`

## Implementation

Тег подроли kubernetes-apps/container_engine_accelerator/nvidia_gpu (включается при nvidia_accelerator_enabled). Загружает ОС-специфичные переменные, вычисляет URL драйвера NVIDIA (flavor tesla/gtx), создаёт каталог addons/container_engine_accelerator, шаблонизирует манифесты nvidia-driver-install-daemonset.yml и k8s-device-plugin-nvidia-daemonset.yml и применяет их через модуль kube. Создание манифестов — при nvidia_driver_install_container, применение — дополнительно при nvidia_driver_install_supported; всё только на первом узле kube_control_plane.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** По содержанию задач эквивалентен тегу container_engine_accelerator (оба ведут к подроли nvidia_gpu). Требует готового кластера и kubectl; изолированный запуск на неготовом кластере невозможен.

## References

- `roles/kubernetes-apps/container_engine_accelerator/meta/main.yml`
- `roles/kubernetes-apps/container_engine_accelerator/nvidia_gpu/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
