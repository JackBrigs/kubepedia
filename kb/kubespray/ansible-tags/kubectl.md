---
id: TAG-KUBECTL
type: ansible_tag
title: "kubectl (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - kubectl
  - "--tags kubectl"
tags:
  - ansible-tag
  - kubernetes
sources:
  - type: code
    path: roles/kubernetes/control-plane/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/tasks/main.yml
    note: "run-tag kubectl"
relations: []
---

# kubectl (Ansible run-tag)

## Summary

Устанавливает kubectl и bash-автодополнение на control plane узлах (roles/kubernetes/control-plane/tasks/main.yml): копирует бинарь kubectl из download-каталога в bin_dir, генерирует /etc/bash_completion.d/kubectl.sh, задаёт alias (kubectl_alias) и права на файл.

## Context

- **Playbooks:** `cluster.yml`, `upgrade-cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes/control-plane`

## Implementation

Устанавливает kubectl и bash-автодополнение на control plane узлах (roles/kubernetes/control-plane/tasks/main.yml): копирует бинарь kubectl из download-каталога в bin_dir, генерирует /etc/bash_completion.d/kubectl.sh, задаёт alias (kubectl_alias) и права на файл. Ряд этих задач дополнительно помечен тегом upgrade.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: safe.** Неразрушающие операции (копирование бинаря и настройка completion). Требует, чтобы бинарь kubectl был предварительно скачан (роль download / downloads.kubectl).

## References

- `roles/kubernetes/control-plane/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
