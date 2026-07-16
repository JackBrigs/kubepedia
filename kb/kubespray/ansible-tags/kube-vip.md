---
id: TAG-KUBE_VIP
type: ansible_tag
title: "kube-vip (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - kube-vip
  - "--tags kube-vip"
tags:
  - ansible-tag
  - kubernetes
sources:
  - type: code
    path: roles/kubernetes/node/tasks/loadbalancer/kube-vip.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/tasks/loadbalancer/kube-vip.yml
    note: "run-tag kube-vip"
relations: []
---

# kube-vip (Ansible run-tag)

## Summary

Устанавливает и настраивает kube-vip как статический под для виртуального IP apiserver (roles/kubernetes/node/tasks/loadbalancer/kube-vip.yml, часть роли kubernetes/node).

## Context

- **Playbooks:** `cluster.yml`, `upgrade-cluster.yml`, `scale.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes/node`

## Implementation

Устанавливает и настраивает kube-vip как статический под для виртуального IP apiserver (roles/kubernetes/node/tasks/loadbalancer/kube-vip.yml, часть роли kubernetes/node). Проверяет требование kube_proxy_strict_arp при ipvs+ARP, выбирает admin.conf/super-admin.conf, пишет манифест kube-vip.yml в kube_manifest_dir. Выполняется только на узлах kube_control_plane при kube_vip_enabled.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Активен только при kube_vip_enabled и на control plane узлах. Пишет статический под — требует настроенного kubelet/manifest-каталога.

## References

- `roles/kubernetes/node/tasks/loadbalancer/kube-vip.yml`
- `roles/kubernetes/node/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
