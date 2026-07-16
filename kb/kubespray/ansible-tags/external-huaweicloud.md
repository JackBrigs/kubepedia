---
id: TAG-EXTERNAL_HUAWEICLOUD
type: ansible_tag
title: "external-huaweicloud (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - external-huaweicloud
  - "--tags external-huaweicloud"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/external_cloud_controller/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/external_cloud_controller/meta/main.yml
    note: "run-tag external-huaweicloud"
relations: []
---

# external-huaweicloud (Ansible run-tag)

## Summary

Разворачивает внешний Huawei Cloud Controller Manager: проверяет учётные данные (huaweicloud-credential-check.yml), читает cacert, формирует секрет cloud-config, генерирует манифесты (config-secret, roles, role-bindings, DaemonSet) и применяет их через kubectl (roles/kubernetes-apps/external_cloud_controller/huaweicloud)..

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/external_cloud_controller/huaweicloud`

## Implementation

Разворачивает внешний Huawei Cloud Controller Manager: проверяет учётные данные (huaweicloud-credential-check.yml), читает cacert, формирует секрет cloud-config, генерирует манифесты (config-secret, roles, role-bindings, DaemonSet) и применяет их через kubectl (roles/kubernetes-apps/external_cloud_controller/huaweicloud).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: safe.** Условие включения: cloud_provider == "external" и external_cloud_provider == "huaweicloud"; задачи на groups['kube_control_plane'][0]. Расхождение с docs/ansible/ansible.md: тег external-huaweicloud в документации отсутствует — приоритет коду. Требует работающий control plane и корректные учётные данные.

## References

- `roles/kubernetes-apps/external_cloud_controller/meta/main.yml`
- `roles/kubernetes-apps/external_cloud_controller/huaweicloud/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
