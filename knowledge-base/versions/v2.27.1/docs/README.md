---
project: kubespray
kubespray_version: v2.27.1
git_commit: 45140b5
source_type: docs
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.27.1/docs
retrieved_at: 2026-07-15
topics:
  - docs
  - moc
reliability: authoritative
---

# Документация Kubespray v2.27.1 — дайджесты (MOC)

Структурированные выжимки из каталога `docs/` **строго тега v2.27.1** (не master), сгруппированные по областям раздела 6.3 CLAUDE.md. Каждый дайджест — сжатый пересказ на русском с сохранением точных имён переменных, команд и путей; в конце каждого файла — раздел «Источники» с путями исходных файлов docs.

## Дайджесты по областям

| Область | Файл | Основные источники docs/ |
|---|---|---|
| Установка и базовая эксплуатация | [[versions/v2.27.1/docs/installation\|installation]] | getting_started/*, ansible/*, operations/ha-mode, integration, port-requirements, large-deployments |
| Обновление кластера | [[versions/v2.27.1/docs/upgrades\|upgrades]] | operations/upgrades.md, upgrades/migrate_docker2containerd.md |
| Узлы: добавление/удаление/восстановление | [[versions/v2.27.1/docs/nodes\|nodes]] | operations/nodes.md, operations/recover-control-plane.md |
| CNI (Cilium) и DNS-стек | [[versions/v2.27.1/docs/cni\|cni]] | CNI/cilium.md, CNI/cni.md, advanced/dns-stack.md, advanced/netcheck.md |
| etcd | [[versions/v2.27.1/docs/etcd\|etcd]] | operations/etcd.md |
| Container runtime (containerd) | [[versions/v2.27.1/docs/container-runtime\|container-runtime]] | CRI/containerd.md, operations/cgroups.md |
| Offline / зеркала / registry | [[versions/v2.27.1/docs/offline\|offline]] | operations/offline-environment.md, mirror.md, advanced/downloads.md, advanced/registry.md |
| Proxy | [[versions/v2.27.1/docs/proxy\|proxy]] | advanced/proxy.md, advanced/mitogen.md |
| Безопасность (hardening, шифрование) | [[versions/v2.27.1/docs/security\|security]] | operations/hardening.md, operations/encrypting-secret-data-at-rest.md |
| Требования и troubleshooting | [[versions/v2.27.1/docs/troubleshooting\|troubleshooting]] | operations/port-requirements.md, advanced/kubernetes-reliability.md, advanced/ntp.md |

## Ключевые факты (для быстрого поиска)

- **Ansible/Python:** поддерживается Ansible `>= 2.16.4` с Python `3.10-3.12` (см. [[versions/v2.27.1/docs/installation|installation]]).
- **Обновление — строго по одному минорному тегу**, без пропусков; graceful-режим только через `upgrade-cluster.yml` (см. [[versions/v2.27.1/docs/upgrades|upgrades]]).
- **Cilium:** IPAM по умолчанию `cluster-pool`; kube-proxy replacement через `cilium_kube_proxy_replacement`; пример версии в доке — `v1.12.1`; DNS-стек — `dns_mode` (4 режима), nodelocaldns включён по умолчанию (см. [[versions/v2.27.1/docs/cni|cni]]).
- **etcd:** `etcd_deployment_type` — `host` (по умолчанию), `docker`, `kubeadm` (экспериментальный).
- **containerd:** registries через `containerd_registries_mirrors`; `containerd_registries`/`containerd_insecure_registries` — deprecated (см. [[versions/v2.27.1/docs/container-runtime|container-runtime]]).
- **Шифрование secrets at rest:** провайдер по умолчанию `secretbox` (см. [[versions/v2.27.1/docs/security|security]]).
- **hardening:** в `hardening.yaml` тега v2.27.1 etcd задан как `etcd_deployment_type: kubeadm` (см. [[versions/v2.27.1/docs/security|security]]).
- **Требования к ядру:** отдельного файла `kernel-requirements.md` в этом теге ещё нет (см. [[versions/v2.27.1/docs/troubleshooting|troubleshooting]]).

## Непроиндексированные разделы docs/

Согласно границам проекта не разбирались детально (упомянуты в соответствующих дайджестах со ссылками на исходники):

- прочие CNI: `docs/CNI/{calico,flannel,kube-ovn,kube-router,macvlan,multus,weave}.md`;
- прочие рантаймы: `docs/CRI/{cri-o,docker,gvisor,kata-containers}.md`;
- облачные провайдеры и CSI: `docs/cloud_controllers/*`, `docs/cloud_providers/*`, `docs/CSI/*`, `docs/ingress/*`, `docs/external_storage_provisioners/*`;
- специфичные ОС: `docs/operating_systems/*`;
- дополнительные разделы `docs/advanced/*` (arch, cert_manager, downloads уже разобран, gcp-lb, mitogen разобран, ntp разобран, registry разобран и др.), `docs/operations/*` (encrypting — разобран, ha-mode — разобран, hardening — разобран, cgroups — разобран, mirror — разобран, остальные — arch/большие деплойменты частично);
- для разработчиков: `docs/developers/*`, `docs/roadmap/*`.

Назад: [[versions/v2.27.1/README|Срез v2.27.1]] · [[INDEX|Kubespray Encyclopedia — INDEX]]
