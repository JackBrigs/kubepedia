---
id: TAG-EXTERNAL_OCI
type: ansible_tag
title: "external-oci (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - external-oci
  - "--tags external-oci"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/external_cloud_controller/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/external_cloud_controller/meta/main.yml
    note: "run-tag external-oci"
relations: []
---

# external-oci (Ansible run-tag)

## Summary

Разворачивает внешний Oracle OCI Cloud Controller Manager: проверяет учётные данные и настройки (assert), формирует секрет cloud-config, генерирует манифесты (config-secret, RBAC, cloud-controller-manager) и применяет их через kubectl (roles/kubernetes-apps/external_cloud_controller/oci)..

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/external_cloud_controller/oci`

## Implementation

Разворачивает внешний Oracle OCI Cloud Controller Manager: проверяет учётные данные и настройки (assert), формирует секрет cloud-config, генерирует манифесты (config-secret, RBAC, cloud-controller-manager) и применяет их через kubectl (roles/kubernetes-apps/external_cloud_controller/oci).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: safe.** Условие включения: cloud_provider == "external" и external_cloud_provider == "oci"; секрет и манифесты на groups['kube_control_plane'][0]. Задачи assert (проверка external_oracle_* и настроек LB) выполняются без ограничения по хосту и без тега external-oci — при изолированном запуске по тегу они пропускаются, а применяются только помеченные задачи. Расхождение с docs/ansible/ansible.md: тег external-oci в документации отсутствует (есть лишь общий "oci") — приоритет коду.

## References

- `roles/kubernetes-apps/external_cloud_controller/meta/main.yml`
- `roles/kubernetes-apps/external_cloud_controller/oci/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
