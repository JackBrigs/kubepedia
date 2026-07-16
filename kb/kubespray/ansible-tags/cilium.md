---
id: TAG-CILIUM
type: ansible_tag
title: "cilium (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - cilium
  - "--tags cilium"
tags:
  - ansible-tag
  - network-plugin
sources:
  - type: code
    path: roles/network_plugin/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/meta/main.yml
    note: "run-tag cilium"
relations: []
---

# cilium (Ansible run-tag)

## Summary

Разворачивает CNI Cilium через утилиту cilium-cli по helm-values (в v2.30.0 это основной способ, не через статические манифесты).

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `k8s_cluster`, `kube_control_plane`
- **Roles:** `network_plugin`, `network_plugin/cilium`, `kubernetes/preinstall`

## Implementation

Разворачивает CNI Cilium через утилиту cilium-cli по helm-values (в v2.30.0 это основной способ, не через статические манифесты). Роль network_plugin/cilium выполняется как зависимость network_plugin при условии kube_network_plugin == 'cilium' или cilium_deploy_additionally. Порядок работы: 1) check.yml — набор assert-проверок: наличие cilium_ipsec_key при шифровании ipsec, корректность cilium_encryption_type (ipsec|wireguard), ядро >= 5.6.0 для wireguard, cilium_identity_allocation_mode в ['crd','kvstore'], cilium_cluster_id в диапазоне 0..255, cilium_version >= cilium_min_version_required, cilium_hubble_event_buffer_capacity равно степени двойки минус 1; обрабатывается устаревший флаг cilium_ipsec_enabled (переводится в cilium_encryption_type=ipsec). 2) install.yml — монтирует BPFFS в /sys/fs/bpf; при cilium_identity_allocation_mode == 'kvstore' создаёт каталог cilium_cert_dir и жёстко линкует etcd-сертификаты (ca_cert.crt, cert.crt, key.pem); на первом узле kube_control_plane рендерит values.yaml.j2 в {{ kube_config_dir }}/cilium-values.yaml, пишет cilium-extra-values.yaml из cilium_extra_values; копирует бинарник cilium-cli из local_release_dir в bin_dir. 3) apply.yml — на первом control-plane выполняет `cilium version`, по наличию helm-релиза выбирает действие install либо upgrade, затем запускает `cilium <install|upgrade> --version {{ cilium_version }} -f cilium-values.yaml -f cilium-extra-values.yaml {{ cilium_install_extra_flags }}`; ждёт готовности подов k8s-app=cilium; при заданных переменных применяет CRD-ресурсы Cilium: CiliumLoadBalancerIPPool, CiliumBGPPeeringPolicy, CiliumBGPClusterConfig, CiliumBGPPeerConfig, CiliumBGPAdvertisement, CiliumBGPNodeConfigOverride (каждый — после ожидания установки соответствующего CRD). Тег cilium также помечает создание CNI-каталогов (/etc/cni/net.d, /opt/cni/bin) в preinstall.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: risky.** Ключевое изменение относительно v2.29.1: установка Cilium выполняется через cilium-cli (команды `cilium install/upgrade -f <values>`), а не применением готовых манифестов. Требуется предварительно скачанный бинарник cilium-cli (роль download) и рабочий control-plane с доступным kubectl. Изолированный запуск --tags cilium без --tags download/network рискован: если бинарник cilium-cli не скопирован или values не отрендерены, установка упадёт. Часть шагов выполняется только на groups['kube_control_plane'][0].

## References

- `roles/network_plugin/meta/main.yml`
- `roles/network_plugin/cilium/tasks/main.yml`
- `roles/network_plugin/cilium/tasks/check.yml`
- `roles/network_plugin/cilium/tasks/install.yml`
- `roles/network_plugin/cilium/tasks/apply.yml`
- `roles/kubernetes/preinstall/tasks/0050-create_directories.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
