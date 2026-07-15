---
project: kubespray
kubespray_version: v2.28.0
git_commit: 63cdf87
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/12351
retrieved_at: 2026-07-15
topics:
  - kubeadm
  - control-plane
  - kubernetes
affected_versions:
  - v2.28.0
fixed_versions:
  - v2.28.1
  - v2.29.0
reliability: confirmed
---

# kubeadm: флаг `--skip-phases` для v1.32.0+ добавлялся некорректно (исправлено в v2.28.1)

## Симптом

На Kubernetes v1.32.0+ (дефолт v2.28.0 — K8s 1.32.5) настройка control plane через kubeadm
вела себя неверно из-за безусловного/некорректного добавления флага `--skip-phases`, не
согласованного с версией kubeadm.

## Корневая причина

Логика формирования аргументов kubeadm не учитывала версию Kubernetes: флаг `--skip-phases`
нужно добавлять условно только для v1.32.0+, где он поддерживается в соответствующем контексте.

## Проверка по коду тега v2.28.0

Условная логика `--skip-phases` для v1.32.0+ отсутствует в v2.28.0 и добавляется коммитом
`7ead3e2f1` (master). Наличие фикса проверяется по коммиту (`git merge-base --is-ancestor`):
в v2.28.0 — нет, в v2.28.1 (бэкпорт `22e933548`) и v2.29.0 — есть.

## Решение

PR [#12351](https://github.com/kubernetes-sigs/kubespray/pull/12351) «fix(kubeadm):
Conditionally add --skip-phases flag for v1.32.0+» (master, commit `7ead3e2f1`) добавляет флаг
условно по версии. Бэкпорт в release-2.28 — PR #12354 (commit `22e933548`), вошёл в v2.28.1.

## Версии

- **Затронуто:** v2.28.0.
- **Исправлено:** v2.28.1 (бэкпорт #12354) и v2.29.0 (master #12351).

## Связанное

[[versions/v2.28.0/variables/k8s-cluster|Переменные k8s-cluster]] · [[versions/v2.28.0/docs/installation|Дайджест: установка]]
