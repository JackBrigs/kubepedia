---
project: kubespray
kubespray_version: v2.28.1
git_commit: a20891a
source_type: docs
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.28.1
retrieved_at: 2026-07-15
topics:
  - moc
  - v2-28-1
reliability: authoritative
---

# Kubespray v2.28.1 — срез базы знаний (MOC)

- **Тег:** `v2.28.1`
- **Commit:** `a20891ab67136f8c92ccad3fad9ad11fc71363d0` (`a20891a`)
- **Дата тега:** 2025-08-26
- **Тип релиза:** патч над v2.28.0 (только багфиксы и патч-версии компонентов; новых breaking changes нет)
- **Предыдущая версия:** [[versions/v2.28.0/README|v2.28.0]]
- **Следующая версия:** [[versions/v2.29.0/README|v2.29.0]]
- **Ограничение среза:** из CNI детально проиндексирован только Cilium; из container runtime — containerd
- **Статус среза:** проиндексирован полностью (этапы 1–6, 8); troubleshooting — сквозным проходом по цепочке v2.27.0→v2.29.0
- **Kubernetes по умолчанию:** 1.32.8 (мин. 1.30.0) | etcd 3.5.22 | containerd **2.0.6** | Cilium 1.17.7 | Calico 3.29.5

## Особенности версии

- Каноническая роль общих defaults переведена на `roles/kubespray_defaults` (**подчёркивание**); `roles/kubespray-defaults` (дефис) — deprecated-заглушка (warn + import). Аналогично `bootstrap_os`/`remove_node` (underscore) с дефисными заглушками.
- Новые роли: `system_packages`, `network_facts`, `validate_inventory`, `bootstrap_os`.
- Версии компонентов выводятся из `vars/main/checksums.yml` (верхний ключ `*_checksums['amd64']`) и словарей `*_supported_versions` — литеральные значения заменены выражениями.
- **containerd на линии 2.0.x** (в v2.28.1 — 2.0.6).
- Cilium ставится через Cilium CLI (а не Jinja-манифесты).
- Последняя версия с поддержкой RHEL 8; анонсировано удаление Weave в следующем релизе (в v2.28.1 Weave/kube-router/flannel ещё присутствуют).
- Удалены (в минорном v2.28.0, действует и в v2.28.1): провайдер Equinix Metal, Krew, Heketi, contrib/kvm-setup, contrib/mitogen; удалён `etcd_kubeadm_enabled`.
- **Патч v2.28.1 относительно v2.28.0:** подняты патч-версии (K8s 1.32.5→1.32.8, etcd 3.5.16→3.5.22, containerd 2.0.5→2.0.6, Cilium 1.17.3→1.17.7, Calico 3.29.3→3.29.5, cilium-cli/cri-dockerd/youki/gVisor); ArgoCD переведён на установку по контрольной сумме (`argocd_install_url` + `argocd_install_checksum` в `download.yml`); добавлены `cilium_remove_old_resources`, `cilium_hubble_peer_service_cluster_domain`, `kubeadm_upgrade_node_phases_skip*`.

## Содержание среза

| Раздел | Файл/директория | Статус |
|---|---|---|
| Метаданные среза | `meta.yaml` | готово |
| Справочник переменных | `variables/` | готово: 1199 переменных (489 k8s-cluster + 367 addons + 129 cni + 84 container-runtime + 65 etcd + 65 download), полнота сверена |
| Компоненты и версии | `components.yaml` | готово: 42 компонента |
| Ansible-теги запуска | `ansible-tags.yaml` | готово: 125 тегов (53 safe / 65 risky / 7 unsafe) |
| Разбор inventory | `inventory/` | готово: 608 переменных |
| Расхождения inventory vs defaults | `discrepancies.md` | готово: действующих расхождений нет |
| Дайджесты документации | `docs/` | готово: 10 дайджестов + README |
| Разбор GitHub Release | `release-notes.md` | готово |
| Troubleshooting | `troubleshooting/` (общий раздел) | сквозной проход по цепочке v2.27.0→v2.29.0 |
| Сравнение с v2.28.0 | [[diffs/v2.28.0__v2.28.1|Отчёт v2.28.0 → v2.28.1]] | готово |

Назад к индексу: [[INDEX|Kubespray Encyclopedia — INDEX]]
