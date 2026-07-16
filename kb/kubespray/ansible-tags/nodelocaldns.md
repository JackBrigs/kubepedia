---
id: TAG-NODELOCALDNS
type: ansible_tag
title: "nodelocaldns (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - nodelocaldns
  - "--tags nodelocaldns"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/ansible/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/ansible/tasks/main.yml
    note: "run-tag nodelocaldns"
relations: []
---

# nodelocaldns (Ansible run-tag)

## Summary

Разворачивает DaemonSet nodelocaldns (локальный кэш DNS на узлах).

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/ansible`

## Implementation

Разворачивает DaemonSet nodelocaldns (локальный кэш DNS на узлах). Задача "Kubernetes Apps | nodelocalDNS" в роли kubernetes-apps/ansible применяет манифесты nodelocaldns_manifests при enable_nodelocaldns (delegate_to control-plane[0], run_once). Формирует адреса upstream/forward на основе dns_mode, skydns_server(_secondary), manual_dns_server и upstream_dns_servers. Задача помечена и тегом coredns.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Выполняется только при enable_nodelocaldns. Манифест применяется через kubectl на первом control-plane. Требует рабочего apiserver и корректных переменных DNS.
 [v2.31.0] Без изменений поведения; в роли ansible удалены соседние задачи netchecker/dashboard.

## References

- `roles/kubernetes-apps/ansible/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
