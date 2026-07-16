---
id: TAG-NODE_FEATURE_DISCOVERY
type: ansible_tag
title: "node_feature_discovery (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - node_feature_discovery
  - "--tags node_feature_discovery"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/meta/main.yml
    note: "run-tag node_feature_discovery"
relations: []
---

# node_feature_discovery (Ansible run-tag)

## Summary

Разворачивает Node Feature Discovery (NFD): создаёт addon-каталог, рендерит манифесты (namespace, CRD, SA, Role/ClusterRole и binding'и, ConfigMap'ы master/worker/topologyupdater, deployment'ы nfd-master и nfd-gc, DaemonSet nfd-worker, Service) и применяет их.

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/node_feature_discovery`

## Implementation

Разворачивает Node Feature Discovery (NFD): создаёт addon-каталог, рендерит манифесты (namespace, CRD, SA, Role/ClusterRole и binding'и, ConfigMap'ы master/worker/topologyupdater, deployment'ы nfd-master и nfd-gc, DaemonSet nfd-worker, Service) и применяет их. Роль kubernetes-apps/node_feature_discovery подключается в kubernetes-apps/meta.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Включается только при node_feature_discovery_enabled (по умолчанию false), выполняется на kube_control_plane[0]. Требует apiserver. В docs/ansible/ansible.md отдельно не описан.

## References

- `roles/kubernetes-apps/meta/main.yml`
- `roles/kubernetes-apps/node_feature_discovery/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
