---
id: TAG-CHECK
type: ansible_tag
title: "check (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - check
  - "--tags check"
tags:
  - ansible-tag
  - kubespray
sources:
  - type: code
    path: playbooks/ansible_version.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/ansible_version.yml
    note: "run-tag check"
relations: []
---

# check (Ansible run-tag)

## Summary

Помечает три assert-проверки окружения запуска в playbooks/ansible_version.yml: версия Ansible в диапазоне minimal_ansible_version (2.17.3) <= x < maximal_ansible_version (2.18.0), наличие python-netaddr (ansible.utils.ipaddr) и достаточно свежая версия Jinja.

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`, `scale.yml`, `reset.yml`, `remove_node.yml`
- **Affected host groups:** `all`
- **Roles:** n/a

## Implementation

Помечает три assert-проверки окружения запуска в playbooks/ansible_version.yml: версия Ansible в диапазоне minimal_ansible_version (2.17.3) <= x < maximal_ansible_version (2.18.0), наличие python-netaddr (ansible.utils.ipaddr) и достаточно свежая версия Jinja. Выполняются один раз (run_once) на хостах группы all, ничего не меняют.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: safe.** Play ansible_version.yml помечен тегом always, поэтому эти проверки и так выполняются при каждом запуске; тег check позволяет адресно прогнать только их. Задачи неразрушающие. В docs/ansible/ansible.md тег check отдельно не описан.

## References

- `playbooks/ansible_version.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
