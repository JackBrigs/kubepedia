---
project: kubespray
kubespray_version: v2.28.0
git_commit: 63cdf87
source_type: docs
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.28.0
retrieved_at: 2026-07-15
topics:
  - moc
  - v2-28-0
reliability: authoritative
---

# Kubespray v2.28.0 — срез базы знаний (MOC)

- **Тег:** `v2.28.0`
- **Commit:** `63cdf87915421dda5955281f38401fd1b55b230b` (`63cdf87`)
- **Дата тега:** 2025-05-20
- **Предыдущая версия:** [[versions/v2.27.1/README|v2.27.1]]
- **Следующая версия:** [[versions/v2.28.1/README|v2.28.1]]
- **Ограничение среза:** из CNI детально проиндексирован только Cilium; из container runtime — containerd
- **Статус среза:** проиндексирован полностью (этапы 1–6, 8); troubleshooting — сквозным проходом по цепочке v2.27.0→v2.29.0
- **Kubernetes по умолчанию:** 1.32.5 (мин. 1.30.0) | etcd 3.5.16 | containerd **2.0.5** | Cilium 1.17.3 | Calico 3.29.3

## Особенности версии

- Каноническая роль общих defaults переведена на `roles/kubespray_defaults` (**подчёркивание**); `roles/kubespray-defaults` (дефис) — deprecated-заглушка (warn + import). Аналогично `bootstrap_os`/`remove_node` (underscore) с дефисными заглушками.
- Новые роли: `system_packages`, `network_facts`, `validate_inventory`, `bootstrap_os`.
- Версии компонентов выводятся из `vars/main/checksums.yml` (верхний ключ `*_checksums['amd64']`) и словарей `*_supported_versions` — литеральные значения заменены выражениями.
- **containerd поднят до линии 2.0.x** (2.0.5).
- Cilium теперь ставится через Cilium CLI (а не Jinja-манифесты).
- Последняя версия с поддержкой RHEL 8; анонсировано удаление Weave в следующем релизе (в v2.28.0 Weave/kube-router/flannel ещё присутствуют).
- Удалены: провайдер Equinix Metal, Krew, Heketi, contrib/kvm-setup, contrib/mitogen. Удалён `etcd_kubeadm_enabled`.

## Содержание среза

| Раздел | Файл/директория | Статус |
|---|---|---|
| Метаданные среза | `meta.yaml` | готово |
| Справочник переменных | `variables/` | готово: 1194 переменных (487 k8s-cluster + 368 addons + 127 cni + 84 container-runtime + 65 etcd + 63 download), полнота сверена |
| Компоненты и версии | `components.yaml` | готово: 42 компонента |
| Ansible-теги запуска | `ansible-tags.yaml` | готово: 125 тегов (53 safe / 65 risky / 7 unsafe) |
| Разбор inventory | `inventory/` | готово: 607 переменных |
| Расхождения inventory vs defaults | `discrepancies.md` | готово: действующих расхождений нет |
| Дайджесты документации | `docs/` | готово: 10 дайджестов + README |
| Разбор GitHub Release | `release-notes.md` | готово |
| Troubleshooting | `troubleshooting/` (общий раздел) | сквозной проход по цепочке v2.27.0→v2.29.0 |
| Сравнение с v2.27.1 | [[diffs/v2.27.1__v2.28.0|Отчёт v2.27.1 → v2.28.0]] | готово |

Назад к индексу: [[INDEX|Kubespray Encyclopedia — INDEX]]
