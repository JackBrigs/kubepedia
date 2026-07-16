---
id: TAG-FACTS
type: ansible_tag
title: "facts (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - facts
  - "--tags facts"
tags:
  - ansible-tag
  - bootstrap-os
sources:
  - type: code
    path: roles/kubernetes/preinstall/tasks/0020-set_facts.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/tasks/0020-set_facts.yml
    note: "run-tag facts"
relations: []
---

# facts (Ansible run-tag)

## Summary

Сквозной тег на задачах сбора фактов и вычисления переменных (set_fact, include_vars, setup) во многих ролях: bootstrap_os (подключение distro-vars), download (download_force_cache, container-facts, флаги образов, пути кэша), etcd, kubernetes/preinstall (0020-set_facts: ansible_os_family и др.), kubernetes/node, kubernetes/control-plane, kubernetes/kubeadm, network_plugin/calico, container-engine, remove-node.

## Context

- **Playbooks:** `cluster.yml`, `scale.yml`, `upgrade_cluster.yml`, `reset.yml`, `remove_node.yml`
- **Affected host groups:** `k8s_cluster`, `etcd`, `calico_rr`, `kube_control_plane`, `kube_node`
- **Roles:** `bootstrap_os`, `download`, `etcd`, `kubernetes/preinstall`, `kubernetes/node`, `kubernetes/control-plane`, `kubernetes/kubeadm`, `network_plugin/calico`, `container-engine`

## Implementation

Сквозной тег на задачах сбора фактов и вычисления переменных (set_fact, include_vars, setup) во многих ролях: bootstrap_os (подключение distro-vars), download (download_force_cache, container-facts, флаги образов, пути кэша), etcd, kubernetes/preinstall (0020-set_facts: ansible_os_family и др.), kubernetes/node, kubernetes/control-plane, kubernetes/kubeadm, network_plugin/calico, container-engine, remove-node. Не меняет состояние узлов, только формирует факты и переменные для последующих задач.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: safe.** Задачи неразрушающие (set_fact/include_vars). Обычно комбинируется с preinstall/download для получения переменных перед целевыми действиями (пример из docs: `--tags preinstall,facts`). Соответствует docs ("Gathering facts and misc check results").
 [v2.31.0] network_facts отрефакторена (вычисление IP и no_proxy); no_proxy теперь собирается фильтрами flatten+join.

## References

- `roles/kubernetes/preinstall/tasks/0020-set_facts.yml`
- `roles/download/tasks/prep_download.yml`
- `roles/download/tasks/download_container.yml`
- `roles/download/tasks/download_file.yml`
- `roles/bootstrap_os/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
