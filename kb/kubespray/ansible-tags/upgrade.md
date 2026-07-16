---
id: TAG-UPGRADE
type: ansible_tag
title: "upgrade (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - upgrade
  - "--tags upgrade"
tags:
  - ansible-tag
  - etcd
sources:
  - type: code
    path: roles/etcd/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd/tasks/main.yml
    note: "run-tag upgrade"
relations: []
---

# upgrade (Ansible run-tag)

## Summary

Сквозной тег, помечающий отдельные задачи обновления бинарей и addon-ов в разных ролях (не является отдельной ролью).

## Context

- **Playbooks:** `cluster.yml`, `upgrade-cluster.yml`
- **Affected host groups:** `etcd`, `kube_control_plane`, `k8s_cluster`, `kube_node`
- **Roles:** `etcd`, `kubernetes/control-plane`, `kubernetes/node`, `kubernetes-apps/ingress_controller/cert_manager`, `kubernetes-apps/metrics_server`

## Implementation

Сквозной тег, помечающий отдельные задачи обновления бинарей и addon-ов в разных ролях (не является отдельной ролью). Покрывает: установку etcdctl/etcdutl и установку бинаря etcd (roles/etcd/tasks/main.yml), копирование kubectl и настройку completion (roles/kubernetes/control-plane/tasks/main.yml), копирование бинаря kubelet (roles/kubernetes/node/tasks/install.yml), переустановку cert-manager (ingress_controller/cert_manager) и metrics_server. Позволяет прицельно перезапустить задачи, связанные с обновлением компонентов.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Не самостоятельный сценарий, а набор точечных задач в нескольких ролях. Изолированный запуск затрагивает разрозненные операции (копирование бинарей, переустановка addon-ов) и требует, чтобы соответствующие download/образа были доступны, а кластер работал. Тег upgrade отсутствует в справочной таблице docs/ansible/ansible.md — подтверждён только по коду.

## References

- `roles/etcd/tasks/main.yml`
- `roles/kubernetes/control-plane/tasks/main.yml`
- `roles/kubernetes/node/tasks/install.yml`
- `roles/kubernetes-apps/ingress_controller/cert_manager/tasks/main.yml`
- `roles/kubernetes-apps/metrics_server/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
