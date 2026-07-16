---
id: TAG-EXTERNAL_VSPHERE
type: ansible_tag
title: "external-vsphere (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - external-vsphere
  - "--tags external-vsphere"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/external_cloud_controller/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/external_cloud_controller/meta/main.yml
    note: "run-tag external-vsphere"
relations: []
---

# external-vsphere (Ansible run-tag)

## Summary

Разворачивает внешний vSphere Cloud Controller Manager (CPI): проверяет учётные данные, генерирует CPI cloud-config, secret, roles, role-bindings, DaemonSet, создаёт ConfigMap cloud-config и применяет манифесты через kubectl (roles/kubernetes-apps/external_cloud_controller/vsphere)..

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/external_cloud_controller/vsphere`

## Implementation

Разворачивает внешний vSphere Cloud Controller Manager (CPI): проверяет учётные данные, генерирует CPI cloud-config, secret, roles, role-bindings, DaemonSet, создаёт ConfigMap cloud-config и применяет манифесты через kubectl (roles/kubernetes-apps/external_cloud_controller/vsphere).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: safe.** Условие включения: cloud_provider == "external" и external_cloud_provider == "vsphere"; задача на groups['kube_control_plane'][0]. Тег external-vsphere навешан на уровне роли в external_cloud_controller/meta/main.yml; сами задачи в vsphere/tasks/main.yml не имеют собственных строк tags (наследуют тег роли) — поэтому в карте тег→файл присутствует только meta/main.yml. Требует работающий control plane.

## References

- `roles/kubernetes-apps/external_cloud_controller/meta/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
