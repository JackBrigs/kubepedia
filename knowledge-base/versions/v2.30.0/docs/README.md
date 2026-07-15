---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: docs
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0/docs
retrieved_at: 2026-07-14
topics:
  - docs
  - moc
reliability: authoritative
---

# Документация Kubespray v2.30.0 — дайджесты (MOC)

Структурированные выжимки из `docs/` **строго тега v2.30.0** по областям раздела 6.3 CLAUDE.md.

| Область | Файл | Источники docs/ |
|---|---|---|
| Установка | [[versions/v2.30.0/docs/installation\|installation]] | getting_started/*, ansible/*, operations/ha-mode, port-requirements |
| Обновление | [[versions/v2.30.0/docs/upgrades\|upgrades]] | operations/upgrades.md, upgrades/migrate_docker2containerd.md |
| Узлы | [[versions/v2.30.0/docs/nodes\|nodes]] | operations/nodes.md, recover-control-plane.md |
| CNI (Cilium) и DNS | [[versions/v2.30.0/docs/cni\|cni]] | CNI/cilium.md, advanced/dns-stack.md |
| etcd | [[versions/v2.30.0/docs/etcd\|etcd]] | operations/etcd.md |
| Container runtime | [[versions/v2.30.0/docs/container-runtime\|container-runtime]] | CRI/containerd.md, operations/cgroups.md |
| Offline / зеркала | [[versions/v2.30.0/docs/offline\|offline]] | operations/offline-environment.md, mirror.md, advanced/registry.md |
| Proxy | [[versions/v2.30.0/docs/proxy\|proxy]] | advanced/proxy.md |
| Безопасность | [[versions/v2.30.0/docs/security\|security]] | operations/hardening.md, encrypting-secret-data-at-rest.md |
| Требования и troubleshooting | [[versions/v2.30.0/docs/troubleshooting\|troubleshooting]] | operations/kernel-requirements.md, port-requirements.md |

## Отличие от v2.29.1

- **Удалён `docs/advanced/mitogen.md`** — в дайджесте proxy зафиксировано как устаревшее/удалённое.

Назад: [[versions/v2.30.0/README|Срез v2.30.0]] · [[INDEX|Kubespray Encyclopedia — INDEX]]
