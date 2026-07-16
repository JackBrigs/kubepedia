---
id: TAG-ANNOTATE
type: ansible_tag
title: "annotate (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - annotate
  - "--tags annotate"
tags:
  - ansible-tag
  - network-plugin
sources:
  - type: code
    path: roles/network_plugin/kube-router/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/kube-router/tasks/main.yml
    note: "run-tag annotate"
relations: []
---

# annotate (Ansible run-tag)

## Summary

Создаёт аннотации на узлах для сетевого плагина kube-router: задача импортирует annotate.yml из роли network_plugin/kube-router (roles/network_plugin/kube-router/tasks/main.yml, import_tasks annotate.yml).

## Context

- **Playbooks:** `cluster.yml`, `scale.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `k8s_cluster`, `kube_node`
- **Roles:** `network_plugin/kube-router`

## Implementation

Создаёт аннотации на узлах для сетевого плагина kube-router: задача импортирует annotate.yml из роли network_plugin/kube-router (roles/network_plugin/kube-router/tasks/main.yml, import_tasks annotate.yml). Аннотации задают параметры BGP (subnet/ASN и пр.) для работы kube-router. Применяется только при kube_network_plugin == 'kube-router'.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Зависит от развёрнутого kube-router и выбранного kube_network_plugin == 'kube-router'; вне сетевого этапа (роль network_plugin) без установленного CNI изолированный запуск смысла не имеет. Соответствует описанию в docs/ansible/ansible.md ("Create kube-router annotation").

## References

- `roles/network_plugin/kube-router/tasks/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
