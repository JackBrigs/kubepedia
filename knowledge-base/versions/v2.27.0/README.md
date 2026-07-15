---
project: kubespray
kubespray_version: v2.27.0
git_commit: 9ec9b3a
source_type: docs
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.27.0
retrieved_at: 2026-07-15
topics:
  - moc
  - v2-27-0
reliability: authoritative
---

# Kubespray v2.27.0 — срез базы знаний (MOC)

- **Тег:** `v2.27.0`
- **Commit:** `9ec9b3a202ab15f7577cfd755df9b11881edde83` (`9ec9b3a`)
- **Дата тега:** 2025-01-02 (Release опубликован 2025-01-06)
- **Предыдущая версия:** v2.26.1 — **в базе не индексирована** (нижняя граница базы)
- **Следующая версия:** [[versions/v2.27.1/README|v2.27.1]]
- **Ограничение среза:** из CNI детально проиндексирован только Cilium; из container runtime — containerd
- **Статус среза:** проиндексирован полностью (этапы 1–6, 8); troubleshooting — сквозным проходом по цепочке v2.27.0→v2.29.0
- **Kubernetes по умолчанию:** 1.31.4 (мин. поддержка 1.29.0) | etcd 3.5.16 | containerd 1.7.24 | Cilium 1.15.9

## Особенности версии (относительно уже индексированных v2.29.x)

- Роль общих defaults называется `roles/kubespray-defaults` (**дефис**, не `kubespray_defaults`).
- etcd-defaults лежат прямо в `roles/etcd/defaults/main.yml` (отдельной роли `etcd_defaults` ещё нет).
- Версии компонентов заданы **явными литералами** в `download.yml` (механизм `*_supported_versions | dict2items` из v2.29.x ещё не применяется).
- Роль контрол-плейна в `cluster.yml` помечена Ansible-тегом **`master`** (в v2.29.x — `control-plane`).
- Cilium разворачивается статическими манифестами (`kubectl apply`), а не через `cilium-cli`.
- Присутствуют CNI weave/kube-router/flannel и роли `krew`, `cephfs_provisioner`, `rbd_provisioner` (удалены/перенесены в более поздних версиях).

## Содержание среза

| Раздел | Файл/директория | Статус |
|---|---|---|
| Метаданные среза | `meta.yaml` | готово: версии компонентов |
| Справочник переменных | `variables/` | готово: 1125 переменных (386 k8s-cluster + 409 addons + 115 cni + 95 container-runtime + 66 etcd + 54 download), полнота сверена |
| Компоненты и версии | `components.yaml` | готово: 53 компонента |
| Ansible-теги запуска | `ansible-tags.yaml` | готово: 127 тегов (57 safe / 63 risky / 7 unsafe) |
| Разбор inventory | `inventory/` | готово: 640 переменных |
| Расхождения inventory vs defaults | `discrepancies.md` | готово: действующих расхождений нет |
| Дайджесты документации | `docs/` | готово: 10 дайджестов + README |
| Разбор GitHub Release | `release-notes.md` | готово |
| Troubleshooting | `troubleshooting/` (общий раздел) | сквозной проход по цепочке v2.27.0→v2.29.0 |
| Сравнение с v2.27.1 | [[diffs/v2.27.0__v2.27.1|Отчёт v2.27.0 → v2.27.1]] | по мере добавления v2.27.1 |

Назад к индексу: [[INDEX|Kubespray Encyclopedia — INDEX]]
