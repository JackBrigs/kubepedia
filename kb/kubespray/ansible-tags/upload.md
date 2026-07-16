---
id: TAG-UPLOAD
type: ansible_tag
title: "upload (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - upload
  - "--tags upload"
tags:
  - ansible-tag
  - download
sources:
  - type: code
    path: roles/download/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/download/tasks/main.yml
    note: "run-tag upload"
relations: []
---

# upload (Ansible run-tag)

## Summary

В v2.30.0 тег upload помечает в roles/download/tasks/main.yml две подготовительные задачи роли download: подготовку рабочих каталогов и переменных (import prep_download.yml) и получение бинарника kubeadm со списком требуемых образов (include prep_kubeadm_images.yml).

## Context

- **Playbooks:** `cluster.yml`, `scale.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `k8s_cluster`, `etcd`, `kube_node`, `kube_control_plane`
- **Roles:** `download`

## Implementation

В v2.30.0 тег upload помечает в roles/download/tasks/main.yml две подготовительные задачи роли download: подготовку рабочих каталогов и переменных (import prep_download.yml) и получение бинарника kubeadm со списком требуемых образов (include prep_kubeadm_images.yml). Обе задачи имеют оба тега (download и upload).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Важное расхождение с docs/ansible/ansible.md: документация описывает upload как "Distributing images/binaries across hosts", однако фактически в коде тег upload навешен только на подготовительные задачи (prep_download, prep_kubeadm_images), а сама раздача образов/файлов на узлы (synchronize push в download_container.yml/download_file.yml) идёт под тегом download, не upload. В примере docs upload обычно исключают (`--skip-tags upload`) при локальной подготовке образов. Приоритет у кода.

## References

- `roles/download/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
