---
id: TAG-EXTERNAL_HCLOUD
type: ansible_tag
title: "external-hcloud (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - external-hcloud
  - "--tags external-hcloud"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/external_cloud_controller/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/external_cloud_controller/meta/main.yml
    note: "run-tag external-hcloud"
relations: []
---

# external-hcloud (Ansible run-tag)

## Summary

Разворачивает внешний Hetzner Cloud Controller Manager: генерирует манифесты (secret, service-account, role-bindings, DaemonSet — с сетями или без, в зависимости от external_hcloud_cloud.with_networks) и применяет их через kubectl (roles/kubernetes-apps/external_cloud_controller/hcloud)..

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/external_cloud_controller/hcloud`

## Implementation

Разворачивает внешний Hetzner Cloud Controller Manager: генерирует манифесты (secret, service-account, role-bindings, DaemonSet — с сетями или без, в зависимости от external_hcloud_cloud.with_networks) и применяет их через kubectl (roles/kubernetes-apps/external_cloud_controller/hcloud).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: safe.** Условие включения: cloud_provider == "external" и external_cloud_provider == "hcloud"; задачи на groups['kube_control_plane'][0]. Расхождение с docs/ansible/ansible.md: тег external-hcloud в таблице документации отсутствует — приоритет коду (v2.30.0). Требует работающий control plane.

## References

- `roles/kubernetes-apps/external_cloud_controller/meta/main.yml`
- `roles/kubernetes-apps/external_cloud_controller/hcloud/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
