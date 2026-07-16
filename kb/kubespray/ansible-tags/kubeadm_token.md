---
id: TAG-KUBEADM_TOKEN
type: ansible_tag
title: "kubeadm_token (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - kubeadm_token
  - "--tags kubeadm_token"
tags:
  - ansible-tag
  - kubernetes
sources:
  - type: code
    path: roles/kubernetes/control-plane/tasks/kubeadm-setup.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/tasks/kubeadm-setup.yml
    note: "run-tag kubeadm_token"
relations: []
---

# kubeadm_token (Ansible run-tag)

## Summary

Управление bootstrap-токенами kubeadm для присоединения узлов (roles/kubernetes/control-plane/tasks/kubeadm-setup.yml).

## Context

- **Playbooks:** `cluster.yml`, `upgrade-cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes/control-plane`

## Implementation

Управление bootstrap-токенами kubeadm для присоединения узлов (roles/kubernetes/control-plane/tasks/kubeadm-setup.yml). Создаёт заранее заданный (hardcoded) токен при kubeadm_refresh_token, либо генерирует токен с сроком 24ч (kubeadm token create), затем сохраняет его в факт kubeadm_token. Выполняется на первом control plane узле (first_kube_control_plane).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: safe.** Только генерация/пересоздание токена — операция относительно безопасна, но требует уже инициализированного kubeadm (наличия admin.conf) на первом control plane узле.

## References

- `roles/kubernetes/control-plane/tasks/kubeadm-setup.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
