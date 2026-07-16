---
id: TAG-FILES
type: ansible_tag
title: "files (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - files
  - "--tags files"
tags:
  - ansible-tag
  - reset
sources:
  - type: code
    path: roles/reset/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/reset/tasks/main.yml
    note: "run-tag files"
relations: []
---

# files (Ansible run-tag)

## Summary

Разрушающее удаление файлов и каталогов, созданных Kubespray, при сбросе узла (роль reset).

## Context

- **Playbooks:** `reset.yml`, `remove_node.yml`
- **Affected host groups:** `k8s_cluster`, `etcd`, `calico_rr`
- **Roles:** `reset`

## Implementation

Разрушающее удаление файлов и каталогов, созданных Kubespray, при сбросе узла (роль reset). Тег files стоит на: массовом удалении конфигов/данных/бинарников (kube_config_dir, /var/lib/kubelet, containerd_storage_dir, etcd_data_dir, сертификаты CA, CNI, бинарники kubelet/etcd/kubectl/kubeadm/helm/crictl и др.), удалении бинарников containerd и удалении DNS-блоков из dhclient.conf. Стирает установленные компоненты и артефакты кластера с узла.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: unsafe.** Опасно запускать изолированно на рабочем узле: удаляет бинарники и конфигурацию кластера. Выполняется только в рамках сброса (reset.yml/remove_node.yml). Соответствует docs/ansible/ansible.md ("Remove files when resetting").

## References

- `roles/reset/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
