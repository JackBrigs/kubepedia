---
id: TAG-NODE_WEBHOOK
type: ansible_tag
title: "node-webhook (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - node-webhook
  - "--tags node-webhook"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/cluster_roles/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/cluster_roles/tasks/main.yml
    note: "run-tag node-webhook"
relations: []
---

# node-webhook (Ansible run-tag)

## Summary

Управляет доступом на основе webhook — ClusterRole/ClusterRoleBinding system:node-webhook (roles/kubernetes-apps/cluster_roles/tasks/main.yml).

## Context

- **Playbooks:** `cluster.yml`, `upgrade-cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/cluster_roles`

## Implementation

Управляет доступом на основе webhook — ClusterRole/ClusterRoleBinding system:node-webhook (roles/kubernetes-apps/cluster_roles/tasks/main.yml). Создаёт clusterrole и clusterrolebinding system:node-webhook (и удаляет старые), предоставляя необходимые права. Выполняется в рамках play "Install the control plane" (роль kubernetes-apps/cluster_roles, тег cluster-roles) на узлах kube_control_plane.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Применяет RBAC-объекты через apiserver — требует работающего control plane. Операции идемпотентны, но зависят от доступности apiserver.

## References

- `roles/kubernetes-apps/cluster_roles/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
