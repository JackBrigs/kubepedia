---
project: kubespray
kubespray_version: v2.28.0
git_commit: 63cdf87
source_type: docs
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.28.0/docs
retrieved_at: 2026-07-15
topics:
  - docs
  - moc
reliability: authoritative
---

# Документация Kubespray v2.28.0 — дайджесты (MOC)

Структурированные выжимки из каталога `docs/` **строго тега v2.28.0** (commit `63cdf87`, не master), сгруппированные по областям раздела 6.3 CLAUDE.md. Каждый дайджест — сжатый пересказ на русском с сохранением точных имён переменных, команд и путей; в конце каждого файла — раздел «Источники» с путями исходных файлов docs.

## Дайджесты по областям

| Область | Файл | Основные источники docs/ |
|---|---|---|
| Установка и базовая эксплуатация | [[versions/v2.28.0/docs/installation\|installation]] | getting_started/*, ansible/*, operations/ha-mode, port-requirements, large-deployments |
| Обновление кластера | [[versions/v2.28.0/docs/upgrades\|upgrades]] | operations/upgrades.md, upgrades/migrate_docker2containerd.md |
| Узлы: добавление/удаление/восстановление | [[versions/v2.28.0/docs/nodes\|nodes]] | operations/nodes.md, operations/recover-control-plane.md |
| CNI (Cilium) и DNS-стек | [[versions/v2.28.0/docs/cni\|cni]] | CNI/cilium.md, advanced/dns-stack.md, advanced/netcheck.md |
| etcd | [[versions/v2.28.0/docs/etcd\|etcd]] | operations/etcd.md |
| Container runtime (containerd) | [[versions/v2.28.0/docs/container-runtime\|container-runtime]] | CRI/containerd.md, operations/cgroups.md |
| Offline / зеркала / registry | [[versions/v2.28.0/docs/offline\|offline]] | operations/offline-environment.md, mirror.md, advanced/downloads.md, advanced/registry.md |
| Proxy | [[versions/v2.28.0/docs/proxy\|proxy]] | advanced/proxy.md, advanced/mitogen.md |
| Безопасность (hardening, шифрование) | [[versions/v2.28.0/docs/security\|security]] | operations/hardening.md, operations/encrypting-secret-data-at-rest.md |
| Требования и troubleshooting | [[versions/v2.28.0/docs/troubleshooting\|troubleshooting]] | operations/kernel-requirements.md, port-requirements.md, advanced/kubernetes-reliability.md, advanced/ntp.md |

## Ключевые факты (для быстрого поиска)

- **Обновление — строго по одному минорному тегу**, без пропусков; graceful-режим только через `upgrade-cluster.yml` (см. [[versions/v2.28.0/docs/upgrades|upgrades]]).
- **Cilium:** IPAM по умолчанию `cluster-pool`; kube-proxy replacement через `cilium_kube_proxy_replacement`; пример версии в доке `cilium_version: "1.17.3"`; DNS-стек — `dns_mode` (4 режима), nodelocaldns включён по умолчанию (см. [[versions/v2.28.0/docs/cni|cni]]).
- **etcd:** `etcd_deployment_type` — `host` (по умолчанию), `docker`, `kubeadm` (экспериментальный).
- **containerd:** registries через `containerd_registries_mirrors`; `containerd_registries`/`containerd_insecure_registries` — deprecated; раздела «Static Binary» ещё нет (см. [[versions/v2.28.0/docs/container-runtime|container-runtime]]).
- **Шифрование secrets at rest:** провайдер по умолчанию `secretbox` (см. [[versions/v2.28.0/docs/security|security]]).
- **Ядро:** для K8s ≥ 1.32 рекомендуется ≥ 4.19 (см. [[versions/v2.28.0/docs/troubleshooting|troubleshooting]]).

## Заметные отличия docs v2.28.0 от v2.29.1

- `docs/CNI/weave.md` **присутствует** в v2.28.0 (удалён в v2.29.1); тег `weave` и `weave_version` ещё в документации.
- `docs/CRI/containerd.md`: **нет** раздела «Static Binary» / `containerd_static_binary` (добавлен в v2.29.1).
- `docs/operations/cgroups.md`: **есть** резервирование для master-хостов (`kube_master_*`, `system_master_*`), удалённое в v2.29.1.
- `docs/operations/hardening.md`: пример задаёт `etcd_deployment_type: kubeadm` (в v2.29.1 — `host`); есть закомментированные AppArmor feature gates; **нет** `kubelet_static_pod_path`.
- `docs/ansible/ansible.md`: `pip install -U -r requirements.txt`; таблица Ansible `>= 2.16.4`; пример docker-образа `v2.27.0`; теги `master (DEPRECATED)` и `weave` ещё в списке.
- `docs/ansible/ansible_collection.md`: есть раздел «Requirements».
- `docs/getting_started/setting-up-your-first-cluster.md`: туториал на Ubuntu 18.04, firewall явно с `vxlan`.

## Непроиндексированные разделы docs/

Согласно границам проекта не разбирались детально (упомянуты в соответствующих дайджестах со ссылками на исходники):

- прочие CNI: `docs/CNI/{calico,flannel,weave,kube-ovn,kube-router,macvlan,multus}.md`;
- прочие рантаймы: `docs/CRI/{cri-o,docker,gvisor,kata-containers}.md`;
- облачные провайдеры и CSI: `docs/cloud_controllers/*`, `docs/cloud_providers/*`, `docs/CSI/*`, `docs/ingress/*`, `docs/external_storage_provisioners/*`;
- специфичные ОС: `docs/operating_systems/*`;
- для разработчиков: `docs/developers/*`, `docs/roadmap/*`.

Назад: [[versions/v2.28.0/README|Срез v2.28.0]] · [[INDEX|Kubespray Encyclopedia — INDEX]]
