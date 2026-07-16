---
id: TAG-METALLB
type: ansible_tag
title: "metallb (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - metallb
  - "--tags metallb"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/meta/main.yml
    note: "run-tag metallb"
relations: []
---

# metallb (Ansible run-tag)

## Summary

Разворачивает MetalLB (балансировщик L2/BGP для bare-metal).

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/metallb`

## Implementation

Разворачивает MetalLB (балансировщик L2/BGP для bare-metal). Проверяет требования (для kube_proxy_mode ipvs обязателен kube_proxy_strict_arp), рендерит metallb.yaml и применяет его, дожидается готовности контроллера. Роль kubernetes-apps/metallb подключается в kubernetes-apps/meta.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Включается только при metallb_enabled (по умолчанию false), выполняется на kube_control_plane[0]. Есть проверка устаревшей переменной matallb_auto_assign (задача fail). Требует работающего apiserver. docs/ansible/ansible.md: «Installing and configuring metallb».

## References

- `roles/kubernetes-apps/meta/main.yml`
- `roles/kubernetes-apps/metallb/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
