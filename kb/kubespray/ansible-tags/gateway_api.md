---
id: TAG-GATEWAY_API
type: ansible_tag
title: "gateway_api (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - gateway_api
  - "--tags gateway_api"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/common_crds/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/common_crds/meta/main.yml
    note: "run-tag gateway_api"
relations: []
---

# gateway_api (Ansible run-tag)

## Summary

Устанавливает CRD Gateway API.

## Context

- **Playbooks:** `cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/common_crds/gateway_api`

## Implementation

Устанавливает CRD Gateway API. Скачивает YAML (downloads.gateway_api_crds), кладёт в addon-каталог и применяет через kubectl установочный манифест выбранного канала (gateway_api_channel). Подключается зависимостью роли kubernetes-apps/common_crds/gateway_api.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Включается только при gateway_api_enabled (по умолчанию false). Роль common_crds подключается в плее «Invoke kubeadm and install a CNI» (hosts: k8s_cluster), но создание каталога и применение манифеста ограничены kube_control_plane[0]; скачивание файла может затрагивать все узлы k8s_cluster. Присутствует только в cluster.yml (в upgrade_cluster.yml роль common_crds не вызывается). В docs/ansible/ansible.md отдельно не описан.

## References

- `roles/kubernetes-apps/common_crds/meta/main.yml`
- `roles/kubernetes-apps/common_crds/gateway_api/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
