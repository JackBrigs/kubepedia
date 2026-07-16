---
id: TAG-ETCD_METRICS
type: ansible_tag
title: "etcd_metrics (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - etcd_metrics
  - "--tags etcd_metrics"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/ansible/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/ansible/tasks/main.yml
    note: "run-tag etcd_metrics"
relations: []
---

# etcd_metrics (Ansible run-tag)

## Summary

Применяет манифесты Endpoints и Service для экспонирования метрик etcd в кластере (roles/kubernetes-apps/ansible/tasks/main.yml): kubectl apply шаблонов etcd_metrics-endpoints.yml.j2 и etcd_metrics-service.yml.j2.

## Context

- **Playbooks:** `cluster.yml`, `upgrade-cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/ansible`

## Implementation

Применяет манифесты Endpoints и Service для экспонирования метрик etcd в кластере (roles/kubernetes-apps/ansible/tasks/main.yml): kubectl apply шаблонов etcd_metrics-endpoints.yml.j2 и etcd_metrics-service.yml.j2. Выполняется только когда определены etcd_metrics_port и etcd_metrics_service_labels; delegate на kube_control_plane[0], run_once.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Часть этапа установки kube-apps (play "Install Kubernetes apps", hosts kube_control_plane). Требует работающего apiserver. Без заданных etcd_metrics_port/labels задача пропускается (no-op).

## References

- `roles/kubernetes-apps/ansible/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
