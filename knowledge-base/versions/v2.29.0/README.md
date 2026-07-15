---
project: kubespray
kubespray_version: v2.29.0
git_commit: 9991412
source_type: docs
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.29.0
retrieved_at: 2026-07-14
topics:
  - moc
  - v2-29-0
reliability: authoritative
---

# Kubespray v2.29.0 — срез базы знаний (MOC)

- **Тег:** `v2.29.0`
- **Commit:** `9991412b4597d6eaf37f86e5f20f9f903a731c08` (`9991412`)
- **Дата тега:** 2025-10-14
- **Источник:** https://github.com/kubernetes-sigs/kubespray/tree/v2.29.0
- **Предыдущая версия:** [[versions/v2.28.1/README|v2.28.1]]
- **Следующая версия:** [[versions/v2.29.1/README|v2.29.1]]

- **Kubernetes по умолчанию:** 1.33.5 (минимально поддерживаемая: 1.31.0)
- **Ограничение среза:** из сетевых плагинов проиндексирован только Cilium; из container runtime полностью проиндексирован containerd
- **Статус среза:** проиндексирован полностью (этапы 1–8 завершены, база прошла валидацию)

## Содержание среза

| Раздел | Файл/директория | Статус |
|---|---|---|
| Метаданные среза | `meta.yaml` | готово |
| Справочник переменных | `variables/` | готово (этап 2): 1200 переменных |
| Компоненты и версии | `components.yaml` | готово (этап 2): 36 компонентов |
| Ansible-теги запуска | `ansible-tags.yaml` | готово (этап 3): 124 тега |
| Разбор inventory | `inventory/` | готово (этап 4): 598 переменных |
| Расхождения inventory vs defaults | `discrepancies.md` | готово (этап 4): 0 расхождений действующих значений |
| Дайджесты документации | `docs/` | готово (этап 5): 10 дайджестов |
| Разбор GitHub Release | `release-notes.md` | готово (этап 6): минорный релиз, версии и breaking changes сверены |
| Troubleshooting | `troubleshooting/` | готово (этап 7): 8 подтверждённых проблем |

## Справочники переменных (этап 2)

| Справочник | YAML (источник истины) | Заметка | Переменных |
|---|---|---|---|
| Ядро кластера | `variables/k8s-cluster.yaml` | [[versions/v2.29.0/variables/k8s-cluster\|k8s-cluster]] | 485 |
| CNI (только Cilium) | `variables/cni.yaml` | [[versions/v2.29.0/variables/cni\|cni]] | 131 |
| etcd | `variables/etcd.yaml` | [[versions/v2.29.0/variables/etcd\|etcd]] | 66 |
| Container runtime (containerd) | `variables/container-runtime.yaml` | [[versions/v2.29.0/variables/container-runtime\|container-runtime]] | 85 |
| Механизм загрузки | `variables/download.yaml` | [[versions/v2.29.0/variables/download\|download]] | 66 |
| Аддоны (kubernetes-apps) | `variables/addons.yaml` | [[versions/v2.29.0/variables/addons\|addons]] | 367 |
| Компоненты и версии | `components.yaml` | [[versions/v2.29.0/components\|components]] | 36 компонентов |

## Ansible-теги запуска (этап 3)

Справочник тегов `--tags`/`--skip-tags`: `ansible-tags.yaml` (источник истины) + заметка [[versions/v2.29.0/ansible-tags|ansible-tags]]. Всего 124 тега; изолированный запуск: safe — 53, risky — 64, unsafe — 7.

## Разбор sample-inventory (этап 4)

| Срез | YAML (источник истины) | Заметка | Переменных (задано) |
|---|---|---|---|
| Ядро кластера + control plane | `inventory/k8s-cluster.yaml` | [[versions/v2.29.0/inventory/k8s-cluster\|inventory/k8s-cluster]] | 128 (57) |
| Аддоны (флаги включения) | `inventory/addons.yaml` | [[versions/v2.29.0/inventory/addons\|inventory/addons]] | 92 (16) |
| Общие (all/*, offline) | `inventory/all.yaml` | [[versions/v2.29.0/inventory/all\|inventory/all]] | 135 (20) |
| Cilium (сеть) | `inventory/cni-cilium.yaml` | [[versions/v2.29.0/inventory/cni-cilium\|inventory/cni-cilium]] | 83 (1) |
| Облачные провайдеры | `inventory/cloud-providers.yaml` | [[versions/v2.29.0/inventory/cloud-providers\|inventory/cloud-providers]] | 160 (0) |
| Группы хостов | — | [[versions/v2.29.0/inventory/inventory-ini\|inventory/inventory-ini]] | — |

Расхождения sample ↔ defaults: [[versions/v2.29.0/discrepancies|discrepancies]] (расхождений действующих значений нет).

## Дайджесты документации (этап 5)

10 структурированных выжимок из `docs/` тега — оглавление в [[versions/v2.29.0/docs/README|docs/README]]: установка, обновление, узлы, CNI/Cilium, etcd, container runtime, offline, proxy, безопасность, troubleshooting.

Назад к индексу: [[INDEX|Kubespray Encyclopedia — INDEX]]
