---
id: TAG-KUBE_CONTROLLER_MANAGER
type: ansible_tag
title: "kube-controller-manager (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - kube-controller-manager
  - "--tags kube-controller-manager"
tags:
  - ansible-tag
  - kubernetes
sources:
  - type: code
    path: roles/kubernetes/preinstall/tasks/0050-create_directories.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/tasks/0050-create_directories.yml
    note: "run-tag kube-controller-manager"
relations: []
---

# kube-controller-manager (Ansible run-tag)

## Summary

В v2.30.0 тег kube-controller-manager встречается ТОЛЬКО в roles/kubernetes/preinstall/tasks/0050-create_directories.yml и покрывает создание служебного каталога для kube-controller-manager.

## Context

- **Playbooks:** `cluster.yml`, `upgrade-cluster.yml`, `scale.yml`
- **Affected host groups:** `k8s_cluster`
- **Roles:** `kubernetes/preinstall`

## Implementation

В v2.30.0 тег kube-controller-manager встречается ТОЛЬКО в roles/kubernetes/preinstall/tasks/0050-create_directories.yml и покрывает создание служебного каталога для kube-controller-manager. Сам статический под kube-controller-manager разворачивается kubeadm, а не задачами этого тега.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: safe.** Фактически тег ограничен созданием каталога (idempotent, безопасно). Описание в docs/ansible/ansible.md ("Configuring static pod kube-controller-manager") шире реального объёма кода этого тега в данной версии — приоритет коду.

## References

- `roles/kubernetes/preinstall/tasks/0050-create_directories.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
