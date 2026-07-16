---
id: TAG-ETCDUTL
type: ansible_tag
title: "etcdutl (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - etcdutl
  - "--tags etcdutl"
tags:
  - ansible-tag
  - etcd
sources:
  - type: code
    path: roles/etcd/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd/tasks/main.yml
    note: "run-tag etcdutl"
relations: []
---

# etcdutl (Ansible run-tag)

## Summary

Устанавливает бинари etcdutl и etcdctl через роль etcdctl_etcdutl (тот же набор задач, что и у тега etcdctl).

## Context

- **Playbooks:** `cluster.yml`, `upgrade-cluster.yml`, `scale.yml`
- **Affected host groups:** `etcd`, `kube_control_plane`
- **Roles:** `etcd`, `etcdctl_etcdutl`, `kubernetes/control-plane`

## Implementation

Устанавливает бинари etcdutl и etcdctl через роль etcdctl_etcdutl (тот же набор задач, что и у тега etcdctl). etcdutl — офлайн-утилита обслуживания данных etcd (снапшоты, дефрагментация, миграция). Вызывается из roles/etcd/tasks/main.yml (группа etcd, etcd_cluster_setup) и из control-plane/kubeadm-etcd.yml (etcd_deployment_type == kubeadm).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: safe.** Тег etcdutl неотделим от etcdctl: оба навешаны на одну задачу import_role, установка бинарей происходит совместно. Отдельного набора задач только для etcdutl нет.

## References

- `roles/etcd/tasks/main.yml`
- `roles/kubernetes/control-plane/tasks/kubeadm-etcd.yml`
- `roles/etcdctl_etcdutl/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
