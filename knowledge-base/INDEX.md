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

Непрерывная цепочка апгрейда (строго последовательно, без пропусков):

| Версия | Commit | Дата тега | Тип | Статус |
|---|---|---|---|---|
| [[versions/v2.27.0/README\|v2.27.0]] | `9ec9b3a` | 2025-01-02 | minor | проиндексирована (нижняя граница) |
| [[versions/v2.27.1/README\|v2.27.1]] | `45140b5` | 2025-06-27 | patch | проиндексирована |
| [[versions/v2.28.0/README\|v2.28.0]] | `63cdf87` | 2025-05-20 | minor | проиндексирована |
| [[versions/v2.28.1/README\|v2.28.1]] | `a20891a` | 2025-08-26 | patch | проиндексирована |
| [[versions/v2.29.0/README\|v2.29.0]] | `9991412` | 2025-10-14 | minor | проиндексирована |
| [[versions/v2.29.1/README\|v2.29.1]] | `0c6a295` | 2025-12-11 | patch | проиндексирована |
| [[versions/v2.30.0/README\|v2.30.0]] | `f4ccdb5` | 2026-01-30 | minor | проиндексирована |
| [[versions/v2.31.0/README\|v2.31.0]] | `1c9add4` | 2026-04-24 | minor | проиндексирована |

Последняя проиндексированная версия: **v2.31.0**. Следующая к добавлению (по последовательности): `v2.32.0` (тег в upstream пока не выпущен). Нижняя граница базы: **v2.27.0** (предыдущий тег v2.26.1 не индексирован).

**Сравнения соседних версий (diffs/):**
[[diffs/v2.27.0__v2.27.1|v2.27.0 → v2.27.1]] · [[diffs/v2.27.1__v2.28.0|v2.27.1 → v2.28.0]] · [[diffs/v2.28.0__v2.28.1|v2.28.0 → v2.28.1]] · [[diffs/v2.28.1__v2.29.0|v2.28.1 → v2.29.0]] · [[diffs/v2.29.0__v2.29.1|v2.29.0 → v2.29.1]] · [[diffs/v2.29.1__v2.30.0|v2.29.1 → v2.30.0]] · [[diffs/v2.30.0__v2.31.0|v2.30.0 → v2.31.0]].

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

## Нижняя цепочка v2.27.0 → v2.29.0 — карты срезов

Полные срезы (переменные, компоненты, Ansible-теги, inventory, docs, release-notes). Локальный MOC каждой версии — её `README`.

- **v2.29.0** [[versions/v2.29.0/README|README]] — K8s 1.33.5, etcd 3.5.23, containerd 2.1.4, Cilium 1.18.2; удалён Weave, тег `master`→`control-plane`. Переменные: [[versions/v2.29.0/variables/k8s-cluster|k8s-cluster]] · [[versions/v2.29.0/variables/cni|cni]] · [[versions/v2.29.0/variables/etcd|etcd]] · [[versions/v2.29.0/variables/container-runtime|container-runtime]] · [[versions/v2.29.0/variables/download|download]] · [[versions/v2.29.0/variables/addons|addons]]. [[versions/v2.29.0/ansible-tags|ansible-tags]] · [[versions/v2.29.0/components|components]] · [[versions/v2.29.0/docs/README|docs]] · [[versions/v2.29.0/release-notes|release-notes]]
- **v2.28.1** [[versions/v2.28.1/README|README]] — K8s 1.32.8, etcd 3.5.22, containerd 2.0.6, Cilium 1.17.7 (патч). Переменные: [[versions/v2.28.1/variables/k8s-cluster|k8s-cluster]] · [[versions/v2.28.1/variables/cni|cni]] · [[versions/v2.28.1/variables/etcd|etcd]] · [[versions/v2.28.1/variables/container-runtime|container-runtime]] · [[versions/v2.28.1/variables/download|download]] · [[versions/v2.28.1/variables/addons|addons]]. [[versions/v2.28.1/ansible-tags|ansible-tags]] · [[versions/v2.28.1/components|components]] · [[versions/v2.28.1/docs/README|docs]] · [[versions/v2.28.1/release-notes|release-notes]]
- **v2.28.0** [[versions/v2.28.0/README|README]] — K8s 1.32.5, containerd **2.0.5** (мажорный скачок), Cilium 1.17.3; удалены Equinix/Krew/Heketi, Cilium через CLI. Переменные: [[versions/v2.28.0/variables/k8s-cluster|k8s-cluster]] · [[versions/v2.28.0/variables/cni|cni]] · [[versions/v2.28.0/variables/etcd|etcd]] · [[versions/v2.28.0/variables/container-runtime|container-runtime]] · [[versions/v2.28.0/variables/download|download]] · [[versions/v2.28.0/variables/addons|addons]]. [[versions/v2.28.0/ansible-tags|ansible-tags]] · [[versions/v2.28.0/components|components]] · [[versions/v2.28.0/docs/README|docs]] · [[versions/v2.28.0/release-notes|release-notes]]
- **v2.27.1** [[versions/v2.27.1/README|README]] — K8s 1.31.9, etcd 3.5.21, containerd 1.7.27, Cilium 1.15.9 (патч; CVE-2025-1974 в ingress-nginx). Переменные: [[versions/v2.27.1/variables/k8s-cluster|k8s-cluster]] · [[versions/v2.27.1/variables/cni|cni]] · [[versions/v2.27.1/variables/etcd|etcd]] · [[versions/v2.27.1/variables/container-runtime|container-runtime]] · [[versions/v2.27.1/variables/download|download]] · [[versions/v2.27.1/variables/addons|addons]]. [[versions/v2.27.1/ansible-tags|ansible-tags]] · [[versions/v2.27.1/components|components]] · [[versions/v2.27.1/docs/README|docs]] · [[versions/v2.27.1/release-notes|release-notes]]
- **v2.27.0** [[versions/v2.27.0/README|README]] — K8s 1.31.4, etcd 3.5.16, containerd 1.7.24, Cilium 1.15.9; роль defaults `kubespray-defaults` (дефис), тег `master`, присутствуют Weave/kube-router. Переменные: [[versions/v2.27.0/variables/k8s-cluster|k8s-cluster]] · [[versions/v2.27.0/variables/cni|cni]] · [[versions/v2.27.0/variables/etcd|etcd]] · [[versions/v2.27.0/variables/container-runtime|container-runtime]] · [[versions/v2.27.0/variables/download|download]] · [[versions/v2.27.0/variables/addons|addons]]. [[versions/v2.27.0/ansible-tags|ansible-tags]] · [[versions/v2.27.0/components|components]] · [[versions/v2.27.0/docs/README|docs]] · [[versions/v2.27.0/release-notes|release-notes]]

## Ключевые факты v2.29.1

- **Kubernetes по умолчанию:** 1.33.7 (минимально поддерживаемая: 1.31.0).
- **Основные компоненты:** etcd 3.5.25, containerd 2.1.5, Cilium 1.18.4, CoreDNS 1.12.0, Helm 3.18.4.
- **Границы охвата:** из CNI детально проиндексирован только **Cilium**; из container runtime — **containerd**.

## Статистика базы

Сводка по всем проиндексированным версиям (переменные roles/defaults · inventory · Ansible-теги):

| Версия | Переменные | Inventory | Ansible-теги | K8s по умолч. |
|---|---|---|---|---|
| v2.27.0 | 1125 | 640 | 127 | 1.31.4 |
| v2.27.1 | 1126 | 641 | 127 | 1.31.9 |
| v2.28.0 | 1194 | 607 | 125 | 1.32.5 |
| v2.28.1 | 1199 | 608 | 125 | 1.32.8 |
| v2.29.0 | 1200 | 598 | 124 | 1.33.5 |
| v2.29.1 | 1198 | 598 | 124 | 1.33.7 |
| v2.30.0 | 1206 | 583 | 123 | 1.34.3 |
| v2.31.0 | 1101 | 577 | 120 | 1.35.4 |

- **Записи troubleshooting (confirmed):** 34 (14 добавлено для цепочки v2.27.0–v2.29.0).
- **Отчёты сравнения (diffs/):** 7 (непрерывная цепочка v2.27.0 → v2.31.0).
- **Границы охвата:** из CNI детально — только **Cilium**; из container runtime — **containerd**.

## Разделы репозитория базы

- **versions/** — срезы по версиям (источник истины — YAML, парные Markdown-заметки для Obsidian)
- **diffs/** — 7 отчётов сравнения соседних версий (непрерывная цепочка v2.27.0 → v2.31.0)
- **troubleshooting/** — подтверждённые проблемы с привязкой к версиям (34 записи)
- **unversioned/** — материалы без подтверждённой версии (пока пусто)
- **reports/nightly/** — отчёты ежевечернего мониторинга (раздел 16)

## Порядок добавления версий

`v2.27.0 → v2.27.1 → v2.28.0 → v2.28.1 → v2.29.0 → v2.29.1 → v2.30.0 → v2.31.0 → ...` — строго последовательно, без пропусков минорных релизов (подтверждено документацией: [[versions/v2.29.1/docs/upgrades|upgrades]]). Нижняя цепочка v2.27.0–v2.29.0 добавлена для восстановления непрерывности до нижней границы v2.27.0.
