---
project: kubespray
source_type: docs
retrieved_at: 2026-07-14
topics:
  - index
  - moc
reliability: authoritative
---

# Kubespray Encyclopedia — INDEX (MOC)

Версионированная база знаний по Kubespray. Точка входа для навигации и справочного режима (раздел 15 методики).

## Проиндексированные версии

| Версия | Commit | Дата тега | Статус |
|---|---|---|---|
| [[versions/v2.29.1/README\|v2.29.1]] | `0c6a295` | 2025-12-11 | проиндексирована |
| [[versions/v2.30.0/README\|v2.30.0]] | `f4ccdb5` | 2026-01-30 | проиндексирована |
| [[versions/v2.31.0/README\|v2.31.0]] | `1c9add4` | 2026-04-24 | проиндексирована |

Последняя проиндексированная версия: **v2.31.0**. Следующая к добавлению (по последовательности): `v2.32.0` (тег в upstream пока не выпущен).

**Сравнения версий:** [[diffs/v2.29.1__v2.30.0|v2.29.1 → v2.30.0]] · [[diffs/v2.30.0__v2.31.0|v2.30.0 → v2.31.0]].

## Срез v2.31.0 — карта разделов

- **Метаданные:** [[versions/v2.31.0/README|README среза]] · `meta.yaml`
- **Переменные:** [[versions/v2.31.0/variables/k8s-cluster|k8s-cluster]] · [[versions/v2.31.0/variables/cni|cni (Cilium)]] · [[versions/v2.31.0/variables/etcd|etcd]] · [[versions/v2.31.0/variables/container-runtime|container-runtime]] · [[versions/v2.31.0/variables/download|download]] · [[versions/v2.31.0/variables/addons|addons]]
- **Компоненты:** [[versions/v2.31.0/components|components]] · **Ansible-теги:** [[versions/v2.31.0/ansible-tags|ansible-tags]]
- **Inventory:** [[versions/v2.31.0/inventory/k8s-cluster|k8s-cluster]] · [[versions/v2.31.0/inventory/all|all]] · [[versions/v2.31.0/inventory/cni-cilium|cni-cilium]] · [[versions/v2.31.0/inventory/cloud-providers|cloud-providers]] · [[versions/v2.31.0/inventory/addons|addons]]
- **Расхождения:** [[versions/v2.31.0/discrepancies|discrepancies]] · **Документация:** [[versions/v2.31.0/docs/README|docs/README]] · **Release notes:** [[versions/v2.31.0/release-notes|release-notes]]
- **Ключевые факты:** Kubernetes 1.35.4, etcd 3.6.10, containerd 2.2.3, Cilium 1.19.3; 8 breaking changes; **удалены ingress-nginx, Kubernetes Dashboard, Netchecker** (роли + теги); cgroup v1 отключён по умолчанию.

## Срез v2.30.0 — карта разделов

- **Метаданные:** [[versions/v2.30.0/README|README среза]] · `meta.yaml`
- **Переменные:** [[versions/v2.30.0/variables/k8s-cluster|k8s-cluster]] · [[versions/v2.30.0/variables/cni|cni (Cilium)]] · [[versions/v2.30.0/variables/etcd|etcd]] · [[versions/v2.30.0/variables/container-runtime|container-runtime]] · [[versions/v2.30.0/variables/download|download]] · [[versions/v2.30.0/variables/addons|addons]]
- **Компоненты:** [[versions/v2.30.0/components|components]] · **Ansible-теги:** [[versions/v2.30.0/ansible-tags|ansible-tags]]
- **Inventory:** [[versions/v2.30.0/inventory/k8s-cluster|k8s-cluster]] · [[versions/v2.30.0/inventory/all|all]] · [[versions/v2.30.0/inventory/cni-cilium|cni-cilium]] · [[versions/v2.30.0/inventory/cloud-providers|cloud-providers]] · [[versions/v2.30.0/inventory/addons|addons]]
- **Расхождения:** [[versions/v2.30.0/discrepancies|discrepancies]] · **Документация:** [[versions/v2.30.0/docs/README|docs/README]] · **Release notes:** [[versions/v2.30.0/release-notes|release-notes]]
- **Ключевые факты:** Kubernetes 1.34.3, etcd 3.5.26, containerd 2.2.1, Cilium 1.18.6; 6 breaking changes (см. release-notes); удалён Ansible-тег `master`.

## Срез v2.29.1 — карта разделов

- **Метаданные:** [[versions/v2.29.1/README|README среза]] · `meta.yaml`
- **Переменные (roles/defaults):** [[versions/v2.29.1/variables/k8s-cluster|k8s-cluster]] · [[versions/v2.29.1/variables/cni|cni (Cilium)]] · [[versions/v2.29.1/variables/etcd|etcd]] · [[versions/v2.29.1/variables/container-runtime|container-runtime]] · [[versions/v2.29.1/variables/download|download]] · [[versions/v2.29.1/variables/addons|addons]]
- **Компоненты и версии:** [[versions/v2.29.1/components|components]]
- **Ansible-теги запуска:** [[versions/v2.29.1/ansible-tags|ansible-tags]]
- **Inventory (sample):** [[versions/v2.29.1/inventory/k8s-cluster|k8s-cluster]] · [[versions/v2.29.1/inventory/all|all]] · [[versions/v2.29.1/inventory/cni-cilium|cni-cilium]] · [[versions/v2.29.1/inventory/cloud-providers|cloud-providers]] · [[versions/v2.29.1/inventory/addons|addons]] · [[versions/v2.29.1/inventory/inventory-ini|группы хостов]]
- **Расхождения sample ↔ defaults:** [[versions/v2.29.1/discrepancies|discrepancies]]
- **Документация (дайджесты):** [[versions/v2.29.1/docs/README|docs/README]]
- **Release notes:** [[versions/v2.29.1/release-notes|release-notes]]
- **Troubleshooting:** [[troubleshooting/README|индекс проблем]]

## Ключевые факты v2.29.1

- **Kubernetes по умолчанию:** 1.33.7 (минимально поддерживаемая: 1.31.0).
- **Основные компоненты:** etcd 3.5.25, containerd 2.1.5, Cilium 1.18.4, CoreDNS 1.12.0, Helm 3.18.4.
- **Границы охвата:** из CNI детально проиндексирован только **Cilium**; из container runtime — **containerd**.

## Статистика базы (v2.29.1)

| Раздел | Количество |
|---|---|
| Переменные (roles/defaults) | 1198 |
| Переменные inventory (sample) | 598 |
| Компоненты с разрешёнными версиями | 36 |
| Ansible-теги запуска | 124 |
| Дайджесты документации | 10 |
| Записи troubleshooting (confirmed) | 8 |
| Всего файлов (YAML + Markdown) | 52 |

## Разделы репозитория базы

- **versions/** — срезы по версиям (источник истины — YAML, парные Markdown-заметки для Obsidian)
- **diffs/** — отчёты сравнения соседних версий (появятся при добавлении v2.30.0)
- **troubleshooting/** — подтверждённые проблемы с привязкой к версиям
- **unversioned/** — материалы без подтверждённой версии (пока пусто)
- **reports/nightly/** — отчёты ежевечернего мониторинга (раздел 16, пока пусто)

## Порядок добавления версий

`v2.29.1 → v2.30.0 → v2.31.0 → ...` — строго последовательно, без пропусков минорных релизов (подтверждено документацией: [[versions/v2.29.1/docs/upgrades|upgrades]]).
