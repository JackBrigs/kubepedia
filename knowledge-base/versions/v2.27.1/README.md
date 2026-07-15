---
project: kubespray
kubespray_version: v2.27.1
git_commit: 45140b5
source_type: docs
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.27.1
retrieved_at: 2026-07-15
topics:
  - moc
  - v2-27-1
reliability: authoritative
---

# Kubespray v2.27.1 — срез базы знаний (MOC)

- **Тег:** `v2.27.1`
- **Commit:** `45140b558266014296ddc6075b0518662a4d4cbe` (`45140b5`)
- **Дата тега:** 2025-06-27
- **Предыдущая версия:** [[versions/v2.27.0/README|v2.27.0]]
- **Следующая версия:** [[versions/v2.28.0/README|v2.28.0]]
- **Ограничение среза:** из CNI детально проиндексирован только Cilium; из container runtime — containerd
- **Статус среза:** проиндексирован полностью (этапы 1–6, 8); troubleshooting — сквозным проходом по цепочке
- **Kubernetes по умолчанию:** 1.31.9 (мин. поддержка 1.29.0) | etcd 3.5.21 | containerd 1.7.27 | Cilium 1.15.9

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
| Справочник переменных | `variables/` | готово: 1126 переменных (387 k8s-cluster + 409 addons + 115 cni + 95 container-runtime + 66 etcd + 54 download), полнота сверена |
| Компоненты и версии | `components.yaml` | готово: 53 компонента |
| Ansible-теги запуска | `ansible-tags.yaml` | готово: 127 тегов (57 safe / 63 risky / 7 unsafe) |
| Разбор inventory | `inventory/` | готово: 641 переменная |
| Расхождения inventory vs defaults | `discrepancies.md` | готово: действующих расхождений нет |
| Дайджесты документации | `docs/` | готово: 10 дайджестов + README |
| Разбор GitHub Release | `release-notes.md` | готово |
| Troubleshooting | `troubleshooting/` (общий раздел) | сквозной проход по цепочке v2.27.1→v2.29.0 |
| Сравнение с v2.27.0 | [[diffs/v2.27.0__v2.27.1|Отчёт v2.27.0 → v2.27.1]] | патч-релиз: версии K8s/компонентов + kubeadm_image_pull_serial |

Назад к индексу: [[INDEX|Kubespray Encyclopedia — INDEX]]
