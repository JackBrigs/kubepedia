---
project: kubespray
kubespray_version: v2.28.1
git_commit: a20891a
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/12565
retrieved_at: 2026-07-15
topics:
  - etcd
  - cilium
  - certificates
affected_versions:
  - v2.28.0
  - v2.28.1
fixed_versions:
  - v2.29.0
reliability: confirmed
---

# etcd: лишняя попытка извлечь etcd-сертификаты на worker при Cilium с `identity_allocation_mode: crd` (исправлено в v2.29.0)

## Симптом

На не-control-plane-узлах Kubespray пытался извлечь сертификаты etcd, даже когда Cilium работает
в режиме `cilium_identity_allocation_mode: crd` и доступ к etcd с worker-узлов не требуется. Это
приводило к лишним/сбойным задачам извлечения сертификатов.

## Корневая причина

В `roles/kubernetes/kubeadm/tasks/main.yml` задача «Extract etcd certs from control plane if
using etcd kubeadm mode» включалась для CNI из списка `["calico", "flannel", "cilium"]` без учёта
того, что Cilium с identity-режимом `crd` не хранит identity в etcd/kvstore и сертификаты etcd на
worker ему не нужны.

## Проверка по коду тега v2.28.1

`roles/kubernetes/kubeadm/tasks/main.yml` (v2.28.1), условие задачи извлечения:

```yaml
when:
  - etcd_deployment_type == "kubeadm"
  - inventory_hostname not in groups['kube_control_plane']
  - kube_network_plugin in ["calico", "flannel", "cilium"] or cilium_deploy_additionally
  - kube_network_plugin != "calico" or calico_datastore == "etcd"
```

Дополнительного условия по `cilium_identity_allocation_mode` в v2.28.0/v2.28.1 нет; оно добавлено в v2.29.0.

## Решение

PR [#12565](https://github.com/kubernetes-sigs/kubespray/pull/12565) «bugfix: skip etcd cert
extraction if cilium identity uses crd» (master, commit `e39e00530`, вошёл в v2.29.0) добавляет
условие:

```yaml
  - kube_network_plugin != "cilium" or cilium_identity_allocation_mode != 'crd'
```

**Бэкпорта в release-2.28 нет.**

## Версии

- **Затронуто:** v2.28.0, v2.28.1 (Cilium + `identity_allocation_mode: crd` + etcd kubeadm).
- **Исправлено:** v2.29.0 (#12565).

## Связанное

[[versions/v2.28.1/variables/etcd|Переменные etcd]] · [[versions/v2.28.1/variables/cni|Переменные CNI (Cilium)]]
