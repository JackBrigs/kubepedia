---
id: TAG-HAPROXY
type: ansible_tag
title: "haproxy (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - haproxy
  - "--tags haproxy"
tags:
  - ansible-tag
  - kubernetes
sources:
  - type: code
    path: roles/kubernetes/node/tasks/loadbalancer/haproxy.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/tasks/loadbalancer/haproxy.yml
    note: "run-tag haproxy"
relations: []
---

# haproxy (Ansible run-tag)

## Summary

Разворачивает локальный HAProxy как балансировщик к kube-apiserver (roles/kubernetes/node/tasks/loadbalancer/haproxy.yml, часть роли kubernetes/node).

## Context

- **Playbooks:** `cluster.yml`, `upgrade-cluster.yml`, `scale.yml`
- **Affected host groups:** `k8s_cluster`, `kube_node`
- **Roles:** `kubernetes/node`

## Implementation

Разворачивает локальный HAProxy как балансировщик к kube-apiserver (roles/kubernetes/node/tasks/loadbalancer/haproxy.yml, часть роли kubernetes/node). Удаляет возможный манифест nginx-proxy, создаёт каталог конфигурации, пишет haproxy.cfg и статический под-манифест haproxy.yml в kube_manifest_dir. Применяется только при loadbalancer_apiserver_localhost и loadbalancer_apiserver_type == "haproxy", и когда узел не является control plane (либо kube_apiserver_bind_address != '::').

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Задача включается через import_tasks внутри роли node. Изолированный запуск имеет смысл только при включённом локальном LB типа haproxy; иначе no-op. Пишет статический под — требует настроенного kubelet/manifest-каталога.

## References

- `roles/kubernetes/node/tasks/loadbalancer/haproxy.yml`
- `roles/kubernetes/node/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
