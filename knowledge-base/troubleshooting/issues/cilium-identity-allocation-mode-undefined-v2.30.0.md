---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/13121
retrieved_at: 2026-07-14
topics:
  - cilium
  - kubeadm
  - etcd
affected_versions:
  - v2.29.0
  - v2.29.1
  - v2.30.0
fixed_versions:
  - v2.31.0
reliability: confirmed
---

# kubeadm: падение задачи при неопределённой `cilium_identity_allocation_mode` (затрагивает v2.30.0)

## Симптом

Задача в роли `kubernetes/kubeadm` падает с ошибкой `'cilium_identity_allocation_mode' is undefined`. Проявляется, когда выбран **не Cilium** (`kube_network_plugin != cilium`) и/или при частичном прогоне ролей (`--tags`), при котором defaults роли Cilium не загружаются.

## Корневая причина

Условие пропуска извлечения etcd-сертификатов в `roles/kubernetes/kubeadm/tasks/main.yml` (введено PR #12565) безусловно читает `cilium_identity_allocation_mode`, но эта переменная определена **только** в `roles/network_plugin/cilium/defaults/main.yml`, а не в общих defaults. При невыбранном Cilium переменная не определена, и вычисление условия падает.

## Проверка по коду тега v2.30.0

- `roles/kubernetes/kubeadm/tasks/main.yml:211`: `kube_network_plugin != "cilium" or cilium_identity_allocation_mode != 'crd'` — читает переменную без guard.
- `cilium_identity_allocation_mode` отсутствует в `roles/kubespray_defaults/defaults/main/main.yml`; определена только в `roles/network_plugin/cilium/defaults/main.yml:30` (`cilium_identity_allocation_mode: crd`).

Условие вычисляется в порядке `or`: при `kube_network_plugin != "cilium"` первый операнд истинен, но Ansible/Jinja всё равно вычисляет второй операнд и падает на undefined.

## Решение

PR [#13121](https://github.com/kubernetes-sigs/kubespray/pull/13121) (master → v2.31.0) переносит дефолт `cilium_identity_allocation_mode: crd` в `roles/kubespray_defaults/defaults/main/main.yml`, где он доступен всегда.

**Обходной путь на v2.30.0:** явно задать `cilium_identity_allocation_mode: crd` в `group_vars` (даже если CNI не Cilium).

## Версии

- **Затронуто:** v2.29.0, v2.29.1, **v2.30.0** (условие присутствует с PR #12565, вошедшего в v2.29.0).
- **Исправлено:** v2.31.0.

## Связанное

[[versions/v2.30.0/variables/cni|Переменные CNI (cilium_identity_allocation_mode)]] · [[versions/v2.30.0/variables/etcd|Переменные etcd]] · [[versions/v2.30.0/ansible-tags|Ansible-теги (kubeadm)]]
