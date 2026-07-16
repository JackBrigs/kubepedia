---
id: TAG-KUBE_APISERVER
type: ansible_tag
title: "kube-apiserver (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - kube-apiserver
  - "--tags kube-apiserver"
tags:
  - ansible-tag
  - kubernetes
sources:
  - type: code
    path: roles/kubernetes/control-plane/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/tasks/main.yml
    note: "run-tag kube-apiserver"
relations: []
---

# kube-apiserver (Ansible run-tag)

## Summary

В роли kubernetes/control-plane тегом kube-apiserver помечён импорт encrypt-at-rest.yml (конфигурация шифрования secret-данных в etcd, когда kube_encrypt_secret_data).

## Context

- **Playbooks:** `cluster.yml`, `upgrade-cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes/control-plane`, `kubernetes/preinstall`

## Implementation

В роли kubernetes/control-plane тегом kube-apiserver помечён импорт encrypt-at-rest.yml (конфигурация шифрования secret-данных в etcd, когда kube_encrypt_secret_data). Дополнительно в preinstall (0050-create_directories.yml) под этим тегом создаётся служебный каталог. Сам статический под kube-apiserver в этой версии формируется kubeadm (kubeadm-setup), а не отдельными задачами данного тега.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Несмотря на имя, тег покрывает узкий набор задач (encrypt-at-rest + создание каталога), а не полную настройку apiserver. Изолированный запуск возможен только на готовом control plane.

## References

- `roles/kubernetes/control-plane/tasks/main.yml`
- `roles/kubernetes/preinstall/tasks/0050-create_directories.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
