---
project: kubespray
kubespray_version: v2.29.1
git_commit: 0c6a295
source_type: docs
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.29.1
retrieved_at: 2026-07-14
topics:
  - moc
  - v2-29-1
reliability: authoritative
---

# Kubespray v2.29.1 — срез базы знаний (MOC)

- **Тег:** `v2.29.1`
- **Commit:** `0c6a29553f90c55cba5e0e359470321dc7cf7d29` (`0c6a295`)
- **Дата тега:** 2025-12-11
- **Источник:** https://github.com/kubernetes-sigs/kubespray/tree/v2.29.1

- **Kubernetes по умолчанию:** 1.33.7 (минимально поддерживаемая: 1.31.0)
- **Ограничение среза:** из сетевых плагинов проиндексирован только Cilium; из container runtime полностью проиндексирован containerd
- **Статус среза:** проиндексирован полностью (этапы 1–8 завершены, база прошла валидацию)

## Содержание среза

| Раздел | Файл/директория | Статус |
|---|---|---|
| Метаданные среза | `meta.yaml` | готово |
| Справочник переменных | `variables/` | готово (этап 2): 1198 переменных |
| Компоненты и версии | `components.yaml` | готово (этап 2): 36 компонентов |
| Ansible-теги запуска | `ansible-tags.yaml` | готово (этап 3): 124 тега |
| Разбор inventory | `inventory/` | готово (этап 4): 598 переменных |
| Расхождения inventory vs defaults | `discrepancies.md` | готово (этап 4): 1 расхождение значений |
| Дайджесты документации | `docs/` | готово (этап 5): 10 дайджестов |
| Разбор GitHub Release | `release-notes.md` | готово (этап 6): 4 PR, версии сверены |
| Troubleshooting | `troubleshooting/` | готово (этап 7): 8 подтверждённых проблем |

## Справочники переменных (этап 2)

| Справочник | YAML (источник истины) | Заметка | Переменных |
|---|---|---|---|
| Ядро кластера | `variables/k8s-cluster.yaml` | [[versions/v2.29.1/variables/k8s-cluster\|k8s-cluster]] | 485 |
| CNI (только Cilium) | `variables/cni.yaml` | [[versions/v2.29.1/variables/cni\|cni]] | 131 |
| etcd | `variables/etcd.yaml` | [[versions/v2.29.1/variables/etcd\|etcd]] | 65 |
| Container runtime (containerd) | `variables/container-runtime.yaml` | [[versions/v2.29.1/variables/container-runtime\|container-runtime]] | 85 |
| Механизм загрузки | `variables/download.yaml` | [[versions/v2.29.1/variables/download\|download]] | 66 |
| Аддоны (kubernetes-apps) | `variables/addons.yaml` | [[versions/v2.29.1/variables/addons\|addons]] | 366 |
| Компоненты и версии | `components.yaml` | [[versions/v2.29.1/components\|components]] | 36 компонентов |

## Ansible-теги запуска (этап 3)

Справочник тегов `--tags`/`--skip-tags`: `ansible-tags.yaml` (источник истины) + заметка [[versions/v2.29.1/ansible-tags|ansible-tags]]. Всего 124 тега; изолированный запуск: safe — 53, risky — 64, unsafe — 7.

## Разбор sample-inventory (этап 4)

| Срез | YAML (источник истины) | Заметка | Переменных (задано) |
|---|---|---|---|
| Ядро кластера + control plane | `inventory/k8s-cluster.yaml` | [[versions/v2.29.1/inventory/k8s-cluster\|inventory/k8s-cluster]] | 128 (57) |
| Аддоны (флаги включения) | `inventory/addons.yaml` | [[versions/v2.29.1/inventory/addons\|inventory/addons]] | 92 (16) |
| Общие (all/*, offline) | `inventory/all.yaml` | [[versions/v2.29.1/inventory/all\|inventory/all]] | 135 (20) |
| Cilium (сеть) | `inventory/cni-cilium.yaml` | [[versions/v2.29.1/inventory/cni-cilium\|inventory/cni-cilium]] | 83 (1) |
| Облачные провайдеры | `inventory/cloud-providers.yaml` | [[versions/v2.29.1/inventory/cloud-providers\|inventory/cloud-providers]] | 160 (0) |
| Группы хостов | — | [[versions/v2.29.1/inventory/inventory-ini\|inventory/inventory-ini]] | — |

Расхождения sample ↔ defaults: [[versions/v2.29.1/discrepancies|discrepancies]] (1 расхождение действующих значений — `unsafe_show_logs`).

## Дайджесты документации (этап 5)

10 структурированных выжимок из `docs/` тега — оглавление в [[versions/v2.29.1/docs/README|docs/README]]: установка, обновление, узлы, CNI/Cilium, etcd, container runtime, offline, proxy, безопасность, troubleshooting.

Назад к индексу: [[INDEX|Kubespray Encyclopedia — INDEX]]
