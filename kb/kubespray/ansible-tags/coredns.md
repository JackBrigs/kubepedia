---
id: TAG-COREDNS
type: ansible_tag
title: "coredns (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - coredns
  - "--tags coredns"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/ansible/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/ansible/tasks/main.yml
    note: "run-tag coredns"
relations: []
---

# coredns (Ansible run-tag)

## Summary

Разворачивает и настраивает DNS-развёртывание CoreDNS.

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/ansible`

## Implementation

Разворачивает и настраивает DNS-развёртывание CoreDNS. Задачи в роли kubernetes-apps/ansible (delegate_to control-plane[0], run_once): применение манифестов CoreDNS (coredns_manifests) при dns_mode in ['coredns','coredns_dual'] и deploy_coredns; при dns_mode == 'coredns_dual' — второй (secondary) экземпляр с skydns_server_secondary. Тег coredns также назначен задаче nodelocalDNS (вместе с тегом nodelocaldns), поэтому запуск --tags coredns затрагивает и nodelocaldns при enable_nodelocaldns.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Применяется через kubectl на первом control-plane (run_once). Тег coredns пересекается с nodelocaldns (общая задача nodelocalDNS помечена обоими тегами). Требует рабочего apiserver.
 [v2.31.0] Задачи CoreDNS/nodelocaldns сохранены; из той же роли ansible удалены netchecker и dashboard.

## References

- `roles/kubernetes-apps/ansible/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
