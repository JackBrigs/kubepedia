---
project: kubespray
kubespray_version: v2.28.1
git_commit: a20891a
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/12132
retrieved_at: 2026-07-15
topics:
  - kubeadm
  - control-plane
  - upgrade
affected_versions:
  - v2.27.0
  - v2.27.1
  - v2.28.0
  - v2.28.1
fixed_versions:
  - v2.29.0
reliability: confirmed
---

# kubeadm: при file-discovery отсутствие `cluster-info-discovery-kubeconfig.yaml` ломало валидацию join (исправлено в v2.29.0)

## Симптом

При `kubeadm_use_file_discovery: true` присоединение вторичных узлов (в т.ч. при обновлении
кластера, ранее установленного без валидационного конфига) падало: файл
`cluster-info-discovery-kubeconfig.yaml` отсутствовал, и последующая валидация kubeadm завершалась ошибкой.

## Корневая причина

В `roles/kubernetes/kubeadm/tasks/main.yml` задача «Copy discovery kubeconfig» выполнялась при
условии `not kubelet_conf.stat.exists`, но не проверяла фактическое наличие самого файла
`cluster-info-discovery-kubeconfig.yaml`. Если файла не было (кластер устанавливался/обновлялся
без него ранее), нужный конфиг не создавался, а дальнейшая валидация на него опиралась.

## Проверка по коду тегов

Задача «Check if discovery kubeconfig exists» (stat-проверка) отсутствует в v2.27.0/v2.27.1/
v2.28.0/v2.28.1 и появляется только в v2.29.0 (`git grep 'Check if discovery kubeconfig exists'`).

## Решение

PR [#12132](https://github.com/kubernetes-sigs/kubespray/pull/12132) «Fix: upgrade cluster
discovery kubeconfig not found» (master, merge `ad31de422`, коммит `ac0b0e7d6`, вошёл в v2.29.0)
добавляет stat-проверку и расширяет условие копирования:

```yaml
- name: Check if discovery kubeconfig exists
  stat:
    path: "{{ kube_config_dir }}/cluster-info-discovery-kubeconfig.yaml"
  register: cluster_info_discovery_kubeconfig
# ...
  when:
    - ('kube_control_plane' not in group_names)
    - not kubelet_conf.stat.exists or not cluster_info_discovery_kubeconfig.stat.exists
    - kubeadm_use_file_discovery
```

**Бэкпорта в release-2.28 нет.**

## Версии

- **Затронуто:** v2.27.0…v2.28.1 при `kubeadm_use_file_discovery: true` (защитная проверка отсутствует).
- **Исправлено:** v2.29.0 (#12132).

## Связанное

[[versions/v2.28.1/docs/nodes|Дайджест: узлы]] · [[versions/v2.28.1/docs/upgrades|Дайджест: обновление кластера]]
