---
id: TAG-ARGOCD
type: ansible_tag
title: "argocd (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - argocd
  - "--tags argocd"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/meta/main.yml
    note: "run-tag argocd"
relations: []
---

# argocd (Ansible run-tag)

## Summary

Разворачивает Argo CD.

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/argocd`

## Implementation

Разворачивает Argo CD. Скачивает бинарь yq и манифесты Argo CD, создаёт namespace и применяет установочный манифест выбранной версии, затем при необходимости патчит секрет initial admin. Подключается зависимостью роли kubernetes-apps/argocd в roles/kubernetes-apps/meta/main.yml.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Включается только при argocd_enabled (по умолчанию false) и выполняется на kube_control_plane[0]. Требует работающего кластера и доступа к загрузке манифестов Argo CD (сеть/зеркало). В docs/ansible/ansible.md отдельно не описан.

## References

- `roles/kubernetes-apps/meta/main.yml`
- `roles/kubernetes-apps/argocd/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
