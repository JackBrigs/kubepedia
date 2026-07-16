---
id: TAG-K8S_PRE_UPGRADE
type: ansible_tag
title: "k8s-pre-upgrade (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - k8s-pre-upgrade
  - "--tags k8s-pre-upgrade"
tags:
  - ansible-tag
  - kubernetes
sources:
  - type: code
    path: roles/kubernetes/control-plane/tasks/pre-upgrade.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/tasks/pre-upgrade.yml
    note: "run-tag k8s-pre-upgrade"
relations: []
---

# k8s-pre-upgrade (Ansible run-tag)

## Summary

Предапгрейдовая подготовка control plane (roles/kubernetes/control-plane/tasks/pre-upgrade.yml).

## Context

- **Playbooks:** `cluster.yml`, `upgrade-cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes/control-plane`

## Implementation

Предапгрейдовая подготовка control plane (roles/kubernetes/control-plane/tasks/pre-upgrade.yml). При изменении etcd-секретов (etcd_secret_changed) удаляет статические манифесты kube-apiserver, kube-controller-manager, kube-scheduler из /etc/kubernetes/manifests и, если манифесты были удалены, принудительно удаляет соответствующие docker-контейнеры control plane. Импортируется в начале roles/kubernetes/control-plane/tasks/main.yml.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: unsafe.** Потенциально разрушительная логика: удаляет манифесты и контейнеры control plane (срабатывает лишь при etcd_secret_changed). Осмысленна только как часть полного прогона роли control-plane; изолированный запуск не рекомендуется. Docker-ветка актуальна лишь для container_manager == docker.

## References

- `roles/kubernetes/control-plane/tasks/pre-upgrade.yml`
- `roles/kubernetes/control-plane/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
