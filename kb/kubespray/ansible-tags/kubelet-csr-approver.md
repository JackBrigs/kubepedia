---
id: TAG-KUBELET_CSR_APPROVER
type: ansible_tag
title: "kubelet-csr-approver (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - kubelet-csr-approver
  - "--tags kubelet-csr-approver"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/meta/main.yml
    note: "run-tag kubelet-csr-approver"
relations: []
---

# kubelet-csr-approver (Ansible run-tag)

## Summary

Устанавливает kubelet-csr-approver (postfinance) через Helm.

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/kubelet-csr-approver`, `helm-apps`

## Implementation

Устанавливает kubelet-csr-approver (postfinance) через Helm. Роль kubernetes-apps/kubelet-csr-approver подключает роль helm-apps, добавляет Helm-репозиторий и разворачивает релиз в namespace kube-system. Компонент автоматически подтверждает CSR-запросы на серверные сертификаты kubelet.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Включается при kubelet_csr_approver_enabled, которое по умолчанию равно kubelet_rotate_server_certificates (обычно false); выполняется на kube_control_plane[0]. В upgrade_cluster.yml роль вызывается отдельно (hosts: kube_control_plane) с этим же тегом, в cluster.yml — через kubernetes-apps/meta. Требует Helm и сетевого доступа к чарт-репозиторию postfinance. В docs/ansible/ansible.md отдельно не описан.

## References

- `roles/kubernetes-apps/meta/main.yml`
- `roles/kubernetes-apps/kubelet-csr-approver/meta/main.yml`
- `roles/kubernetes-apps/kubelet-csr-approver/defaults/main.yml`
- `playbooks/upgrade_cluster.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
