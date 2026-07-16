---
id: TAG-INGRESS_ALB
type: ansible_tag
title: "ingress_alb (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - ingress_alb
  - "--tags ingress_alb"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/ingress_controller/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/ingress_controller/meta/main.yml
    note: "run-tag ingress_alb"
relations: []
---

# ingress_alb (Ansible run-tag)

## Summary

Разворачивает AWS ALB Ingress Controller: создаёт addon-каталог, рендерит манифесты (ClusterRole/binding, namespace, ServiceAccount, deployment) и применяет их.

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/ingress_controller/alb_ingress_controller`

## Implementation

Разворачивает AWS ALB Ingress Controller: создаёт addon-каталог, рендерит манифесты (ClusterRole/binding, namespace, ServiceAccount, deployment) и применяет их. Подключается зависимостью роли kubernetes-apps/ingress_controller/alb_ingress_controller.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Включается только при ingress_alb_enabled (по умолчанию false); применение манифестов ограничено kube_control_plane[0]. Предназначен для кластеров в AWS. docs/ansible/ansible.md: «AWS ALB Ingress Controller».

## References

- `roles/kubernetes-apps/ingress_controller/meta/main.yml`
- `roles/kubernetes-apps/ingress_controller/alb_ingress_controller/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
