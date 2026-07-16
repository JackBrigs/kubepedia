---
id: TAG-PROMETHEUS_OPERATOR_CRDS
type: ansible_tag
title: "prometheus_operator_crds (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - prometheus_operator_crds
  - "--tags prometheus_operator_crds"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/common_crds/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/common_crds/meta/main.yml
    note: "run-tag prometheus_operator_crds"
relations: []
---

# prometheus_operator_crds (Ansible run-tag)

## Summary

Устанавливает CRD Prometheus Operator.

## Context

- **Playbooks:** `cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/common_crds/prometheus_operator_crds`

## Implementation

Устанавливает CRD Prometheus Operator. Скачивает YAML (downloads.prometheus_operator_crds) и применяет его через kubectl apply. Подключается зависимостью роли kubernetes-apps/common_crds/prometheus_operator_crds.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Включается только при prometheus_operator_crds_enabled (по умолчанию false). Роль common_crds вызывается в плее «Invoke kubeadm and install a CNI» (hosts: k8s_cluster); применение манифеста ограничено kube_control_plane[0], скачивание может затрагивать узлы k8s_cluster. Есть только в cluster.yml (в upgrade_cluster.yml роль common_crds не вызывается). В docs/ansible/ansible.md отдельно не описан.

## References

- `roles/kubernetes-apps/common_crds/meta/main.yml`
- `roles/kubernetes-apps/common_crds/prometheus_operator_crds/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
