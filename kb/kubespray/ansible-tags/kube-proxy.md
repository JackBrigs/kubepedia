---
id: TAG-KUBE_PROXY
type: ansible_tag
title: "kube-proxy (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - kube-proxy
  - "--tags kube-proxy"
tags:
  - ansible-tag
  - kubernetes
sources:
  - type: code
    path: roles/kubernetes/node/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/tasks/main.yml
    note: "run-tag kube-proxy"
relations: []
---

# kube-proxy (Ansible run-tag)

## Summary

Настраивает kube-proxy (в кластере kube-proxy — статический под, разворачиваемый kubeadm).

## Context

- **Playbooks:** `cluster.yml`, `scale.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `k8s_cluster`, `kube_control_plane`
- **Roles:** `kubernetes/node`, `kubernetes/kubeadm`

## Implementation

Настраивает kube-proxy (в кластере kube-proxy — статический под, разворачиваемый kubeadm). Фактические задачи под тегом kube-proxy: В роли kubernetes/node (hosts: k8s_cluster): резервирование диапазона nodePort через sysctl net.ipv4.ip_local_reserved_ports; загрузка модулей ядра IPVS (kube_proxy_ipvs_modules) и nf_conntrack при kube_proxy_mode == 'ipvs'; загрузка модуля nf_tables при kube_proxy_mode == 'nftables'. В роли kubernetes/kubeadm: чтение resourceVersion configmap kube-proxy; правка поля server в kubeconfig kube-proxy (варианты localhost и внешний LB); перезапуск подов kube-proxy при изменении configmap — всё при kube_proxy_deployed, выполняется run_once с delegate_to первого control-plane.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Тег не устанавливает kube-proxy как таковой (это делает kubeadm), а настраивает узлы под выбранный kube_proxy_mode (ipvs/nftables) и правит kubeconfig/configmap kube-proxy. Задачи правки configmap выполняются только при kube_proxy_deployed и на control-plane[0].

## References

- `roles/kubernetes/node/tasks/main.yml`
- `roles/kubernetes/kubeadm/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
