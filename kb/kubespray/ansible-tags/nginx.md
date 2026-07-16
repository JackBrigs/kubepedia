---
id: TAG-NGINX
type: ansible_tag
title: "nginx (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - nginx
  - "--tags nginx"
tags:
  - ansible-tag
  - kubernetes
sources:
  - type: code
    path: roles/kubernetes/node/tasks/loadbalancer/nginx-proxy.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/tasks/loadbalancer/nginx-proxy.yml
    note: "run-tag nginx"
relations: []
---

# nginx (Ansible run-tag)

## Summary

Разворачивает локальный nginx-proxy как балансировщик к kube-apiserver (roles/kubernetes/node/tasks/loadbalancer/nginx-proxy.yml, часть роли kubernetes/node).

## Context

- **Playbooks:** `cluster.yml`, `upgrade-cluster.yml`, `scale.yml`
- **Affected host groups:** `k8s_cluster`, `kube_node`
- **Roles:** `kubernetes/node`

## Implementation

Разворачивает локальный nginx-proxy как балансировщик к kube-apiserver (roles/kubernetes/node/tasks/loadbalancer/nginx-proxy.yml, часть роли kubernetes/node). Удаляет возможный манифест haproxy, создаёт каталог nginx_config_dir, пишет nginx.conf и статический под-манифест nginx-proxy.yml. Применяется при loadbalancer_apiserver_localhost и loadbalancer_apiserver_type == "nginx", когда узел не control plane (либо kube_apiserver_bind_address != '::').

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** В docs/ansible/ansible.md описан как "Configuring LB for kube-apiserver instances". Активен только при включённом локальном LB типа nginx; пишет статический под, требует настроенного kubelet/manifest-каталога.

## References

- `roles/kubernetes/node/tasks/loadbalancer/nginx-proxy.yml`
- `roles/kubernetes/node/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
