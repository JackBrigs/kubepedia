---
project: kubespray
kubespray_version: v2.28.1
git_commit: a20891a
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/12606
retrieved_at: 2026-07-15
topics:
  - kubeadm
  - control-plane
  - nodes
affected_versions:
  - v2.27.0
  - v2.27.1
  - v2.28.0
  - v2.28.1
fixed_versions:
  - v2.29.0
reliability: confirmed
---

# kubeadm: `kubeadm_ignore_preflight_errors: ['all']` ломал join из-за смешивания с конкретными проверками (исправлено в v2.29.0)

## Симптом

При установке `kubeadm_ignore_preflight_errors: ['all']` присоединение узла падало: kubeadm
завершался ошибкой, потому что `all` был указан одновременно с конкретной проверкой.

## Корневая причина

В `roles/kubernetes/kubeadm/tasks/main.yml` к списку игнорируемых preflight-ошибок Kubespray
безусловно добавлял захардкоженную проверку `DirAvailable--etc-kubernetes-manifests` и затем
пользовательский `kubeadm_ignore_preflight_errors`. kubeadm выдаёт ошибку, если `all` указан
вместе с конкретными проверками, — поэтому смешение `all` + `DirAvailable--...` ломало join.

Связано с breaking change v2.27.0: переменная `kubeadm_ignore_preflight_errors` заменила прежнее
поведение `all`.

## Проверка по коду тегов

Захардкоженная проверка `DirAvailable--etc-kubernetes-manifests` присутствует в
`roles/kubernetes/kubeadm/tasks/main.yml` во всех тегах v2.27.0…v2.29.0. Однако защита
`if 'all' not in kubeadm_ignore_preflight_errors` появляется только в v2.29.0 (коммит `fbf957ab5`);
в v2.27.0/v2.27.1/v2.28.0/v2.28.1 её нет.

## Решение

PR [#12606](https://github.com/kubernetes-sigs/kubespray/pull/12606) «Fix breakage when ignoring
all kubeadm preflight errors» (master, commit `fbf957ab5`, вошёл в v2.29.0):

```jinja
- "{{ 'DirAvailable--etc-kubernetes-manifests' if 'all' not in kubeadm_ignore_preflight_errors }}"
- "{{ kubeadm_ignore_preflight_errors }}"
# ...
--ignore-preflight-errors={{ ignored | select | flatten | join(',') }}
```

Захардкоженная проверка не добавляется, если пользователь указал `all`. **Бэкпорта в release-2.28
нет** — на v2.28.1 актуален обходной путь.

**Обходной путь** на v2.27.x/v2.28.x: не использовать `all`, а перечислять конкретные проверки в
`kubeadm_ignore_preflight_errors`.

## Версии

- **Затронуто:** v2.27.0, v2.27.1, v2.28.0, v2.28.1 (при `kubeadm_ignore_preflight_errors: ['all']`).
- **Исправлено:** v2.29.0 (#12606).

## Связанное

[[versions/v2.28.1/variables/k8s-cluster|Переменные k8s-cluster (kubeadm_ignore_preflight_errors)]] · [[versions/v2.28.1/docs/nodes|Дайджест: узлы]]
