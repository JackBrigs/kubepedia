---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: docs
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/docs
retrieved_at: 2026-07-14
topics:
  - docs
  - moc
reliability: authoritative
---

# Документация Kubespray v2.31.0 — дайджесты (MOC)

Структурированные выжимки из `docs/` **строго тега v2.31.0** по областям раздела 6.3 CLAUDE.md.

| Область | Файл | Источники docs/ |
|---|---|---|
| Установка | [[versions/v2.31.0/docs/installation\|installation]] | getting_started/*, ansible/*, operations/ha-mode, port-requirements |
| Обновление | [[versions/v2.31.0/docs/upgrades\|upgrades]] | operations/upgrades.md, upgrades/migrate_docker2containerd.md |
| Узлы | [[versions/v2.31.0/docs/nodes\|nodes]] | operations/nodes.md, recover-control-plane.md |
| CNI (Cilium) и DNS | [[versions/v2.31.0/docs/cni\|cni]] | CNI/cilium.md, advanced/dns-stack.md |
| etcd | [[versions/v2.31.0/docs/etcd\|etcd]] | operations/etcd.md |
| Container runtime | [[versions/v2.31.0/docs/container-runtime\|container-runtime]] | CRI/containerd.md, operations/cgroups.md |
| Offline / зеркала | [[versions/v2.31.0/docs/offline\|offline]] | operations/offline-environment.md, mirror.md, advanced/registry.md |
| Proxy | [[versions/v2.31.0/docs/proxy\|proxy]] | advanced/proxy.md |
| Безопасность | [[versions/v2.31.0/docs/security\|security]] | operations/hardening.md, encrypting-secret-data-at-rest.md |
| Требования и troubleshooting | [[versions/v2.31.0/docs/troubleshooting\|troubleshooting]] | operations/kernel-requirements.md, port-requirements.md |

## Отличия от v2.30.0

- **Требование Ansible поднято** до `>=2.18.0,<2.19.0`, Python 3.11–3.13 (в v2.30.0 было `>=2.17.3`, Python 3.10–3.12).
- **Удалён `docs/ingress/ingress_nginx.md`** (роль ingress_nginx убрана).
- `docs/CNI/cilium.md` — пример версии обновлён 1.18.6 → 1.19.3.
- `docs/operations/etcd.md` — изменения только в разделе метрик (kube-prometheus-stack), не в типах развёртывания; переход etcd на 3.6.x отражён в `components.yaml`, а не в docs.
- `docs/operations/offline-environment.md` — переработан (раздельные инструкции для Containerd 2+ и 1.7).

Назад: [[versions/v2.31.0/README|Срез v2.31.0]] · [[INDEX|Kubespray Encyclopedia — INDEX]]
