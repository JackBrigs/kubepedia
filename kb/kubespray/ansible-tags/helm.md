---
id: TAG-HELM
type: ansible_tag
title: "helm (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - helm
  - "--tags helm"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/meta/main.yml
    note: "run-tag helm"
relations: []
---

# helm (Ansible run-tag)

## Summary

Устанавливает и настраивает Helm: ставит зависимость PyYAML, скачивает и копирует бинарь helm в bin_dir, генерирует bash-completion.

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/helm`

## Implementation

Устанавливает и настраивает Helm: ставит зависимость PyYAML, скачивает и копирует бинарь helm в bin_dir, генерирует bash-completion. Роль kubernetes-apps/helm подключается зависимостью в kubernetes-apps/meta.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: safe.** Включается только при helm_enabled (по умолчанию false). В отличие от большинства addon'ов НЕ ограничен kube_control_plane[0] — устанавливает helm на все узлы группы kube_control_plane. Идемпотентен и относительно безопасен для изолированного запуска (ставит клиент, кластерные ресурсы не меняет), но требует доступа к загрузке бинаря helm. docs/ansible/ansible.md: «Installing and configuring Helm».

## References

- `roles/kubernetes-apps/meta/main.yml`
- `roles/kubernetes-apps/helm/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
