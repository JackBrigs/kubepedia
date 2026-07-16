---
id: TAG-LOCALHOST
type: ansible_tag
title: "localhost (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - localhost
  - "--tags localhost"
tags:
  - ansible-tag
  - bastion-ssh-config
sources:
  - type: code
    path: playbooks/boilerplate.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/boilerplate.yml
    note: "run-tag localhost"
relations: []
---

# localhost (Ansible run-tag)

## Summary

Специальные шаги, выполняемые на управляющем узле Ansible (localhost / download_delegate).

## Context

- **Playbooks:** `cluster.yml`, `scale.yml`, `upgrade_cluster.yml`, `reset.yml`, `remove_node.yml`
- **Affected host groups:** `bastion`, `k8s_cluster`, `etcd`, `kube_node`
- **Roles:** `bastion-ssh-config`, `download`

## Implementation

Специальные шаги, выполняемые на управляющем узле Ansible (localhost / download_delegate). Тег localhost помечает: установку bastion-ssh-config (playbooks/boilerplate.yml, на bastion[0]) и локальные задачи роли download — проверку возможности стать root и доступа к контейнерному рантайму на localhost, создание локального каталога кэша образов/файлов (prep_download.yml, download_file.yml) при download_force_cache/download_run_once.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: safe.** Операции на управляющей ноде преимущественно неразрушающие (проверки, создание каталогов кэша, ssh config). Часть задач срабатывает только при download_localhost/download_force_cache. Соответствует docs/ansible/ansible.md ("Special steps for the localhost (ansible runner)").

## References

- `playbooks/boilerplate.yml`
- `roles/download/tasks/prep_download.yml`
- `roles/download/tasks/download_file.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
