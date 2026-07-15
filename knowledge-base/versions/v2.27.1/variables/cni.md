---
project: kubespray
kubespray_version: v2.27.1
git_commit: 45140b5
source_type: code
source_path: versions/v2.27.1/variables/cni.yaml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.27.1
topics:
  - cni
  - cilium
  - network
reliability: authoritative
---

# Переменные CNI (Cilium) — Kubespray v2.27.1

Человекочитаемая заметка к машиночитаемому справочнику `cni.yaml`.
**Источник истины — YAML-справочник** `versions/v2.27.1/variables/cni.yaml`.
Назад к срезу: [[versions/v2.27.1/README|Срез v2.27.1]].

Ограничение проекта: из сетевых плагинов проиндексирован **только Cilium** (calico, kube-ovn, flannel, weave, kube-router, multus, macvlan — не разбираются).

Источники в коде тега `v2.27.1` (commit `45140b5`):

- `roles/network_plugin/cilium/defaults/main.yml` — 86 переменных Cilium;
- `roles/network_plugin/cni/defaults/main.yml` — единственная переменная `cni_bin_owner`;
- `roles/kubespray-defaults/defaults/main/main.yml` (каталог с **дефисом**) — выбор CNI;
- `roles/kubespray-defaults/defaults/main/download.yml` — версии и образы Cilium/CNI.

## Как выбирается CNI

Плагин выбирается переменной `kube_network_plugin` (по умолчанию `calico`). Cilium подключается при
`kube_network_plugin == 'cilium'` **или** при `cilium_deploy_additionally: true`. Роль
`network_plugin/cni` раскладывает базовые CNI-бинарники (`containernetworking/plugins`, `cni_version: v1.4.1`).

## Ключевое отличие v2.27.1: Cilium разворачивается манифестами

В v2.27.1 Cilium ставится **шаблонами-манифестами роли**, а не через helm/cilium-cli (как в v2.29.1).
Поэтому здесь актуальны переменные лимитов пода (`cilium_memory_limit`, `cilium_cpu_limit`,
`cilium_memory_requests`, `cilium_cpu_requests`) и отсутствуют helm-специфичные (`cilium_extra_values`,
`cilium_install_extra_flags`, `cilium_hubble_export_*` и т.п.).

## Версии и образы

| Переменная | Значение | Заметка |
|---|---|---|
| `cilium_version` | `v1.15.9` | явный литерал |
| `cilium_cli_version` | `v0.16.24` | явный литерал |
| `cilium_min_version_required` | `1.10` | в v2.29.1 — 1.15 |
| `cilium_image_repo` / `cilium_operator_image_repo` | `quay.io/cilium/cilium` / `.../operator` | тег = `cilium_version` |
| `cilium_hubble_certgen_image_tag` | `v0.1.8` | |
| `cilium_hubble_ui_image_tag` / `..._backend_image_tag` | `v0.11.0` | |
| `cilium_hubble_envoy_image_repo` / `_tag` | `docker.io/envoyproxy/envoy` / `v1.22.5` | в v2.29.1 — `quay.io/cilium/cilium-envoy` |

## Ключевые отличия от v2.29.1 (важно при обновлении)

| Переменная | v2.27.1 | v2.29.1 |
|---|---|---|
| `cilium_identity_allocation_mode` | **`kvstore`** | `crd` |
| `cilium_kube_proxy_replacement` | **`partial`** (строка strict/partial) | `false` (булево) |
| `cilium_enable_host_legacy_routing` | **`true`** | `false` |
| `cilium_enable_ipv4` / `cilium_enable_ipv6` | жёстко `true` / `false` | `{{ ipv4_stack }}` / `{{ ipv6_stack }}` |
| node-to-node шифрование | `cilium_ipsec_node_encryption` | `cilium_encryption_node_encryption` |
| устаревшие флаги | `cilium_tofqdns_enable_poller`, `cilium_enable_legacy_services` присутствуют | удалены |

При `cilium_identity_allocation_mode: kvstore` (значение по умолчанию!) Cilium хранит identity в etcd,
поэтому задачи роли линкуют etcd-сертификаты в `cilium_cert_dir` (`/etc/cilium/certs`) через
`kube_etcd_cacert_file`/`kube_etcd_cert_file`/`kube_etcd_key_file`.

## Маршрутизация, маскарадинг, шифрование

- Overlay: `cilium_tunnel_mode: vxlan`; нативная маршрутизация — при `disabled` + `cilium_auto_direct_node_routes` + `cilium_native_routing_cidr`.
- Балансировка: `cilium_loadbalancer_mode: snat`; замена kube-proxy — `cilium_kube_proxy_replacement: partial`.
- Маскарадинг: `cilium_enable_ipv4_masquerade`/`cilium_enable_ipv6_masquerade: true`, eBPF-вариант `cilium_enable_bpf_masquerade: false`; ip-masq-agent (`cilium_ip_masq_agent_enable` + `cilium_non_masquerade_cidrs`).
- Шифрование: `cilium_encryption_enabled: false`, тип `cilium_encryption_type: ipsec`, node-to-node `cilium_ipsec_node_encryption`, wireguard-fallback `cilium_wireguard_userspace_fallback`.

## Наблюдаемость и Hubble

Метрики агента/оператора/Hubble включаются `cilium_enable_prometheus: false`; порты
(`cilium_agent_scrape_port`, `cilium_operator_scrape_port`, `cilium_hubble_scrape_port`) и
`cilium_agent_health_port` **вычисляются по версии Cilium**. Hubble: `cilium_enable_hubble: false`
(флаг продублирован в `download.yml`), UI (`cilium_enable_hubble_ui`), метрики
(`cilium_enable_hubble_metrics` + `cilium_hubble_metrics`), установка relay/UI (`cilium_hubble_install`),
mTLS-сертификаты (`cilium_hubble_tls_generate` + `cilium_certgen_args`).

## BGP, IPAM, дополнительные возможности

- IPAM: `cilium_ipam_mode: cluster-pool`; пулы (`cilium_pool_cidr`, `cilium_pool_mask_size` и IPv6-аналоги) закомментированы, по умолчанию берутся из `kube_pods_subnet` / `kube_network_node_prefix`.
- BGP: новый bgpv2 API (`cilium_bgp_cluster_configs`, `cilium_bgp_peer_configs`, `cilium_bgp_advertisements`, `cilium_bgp_node_config_overrides`) и legacy `cilium_bgp_peering_policies`; включение — `cilium_enable_bgp_control_plane`.
- Bandwidth Manager (`cilium_enable_bandwidth_manager`, ядро >= 5.1), host firewall (`cilium_enable_host_firewall` + `cilium_policy_audit_mode`), portmap для hostPort (`cilium_enable_portmap`).
- Расширения пода агента/оператора: `cilium_agent_extra_*`, `cilium_operator_extra_*`, `cilium_config_extra_vars`, `cilium_clusterrole_rules_operator_extra_vars`.

## Связанное

- [[versions/v2.27.1/variables/k8s-cluster|k8s-cluster.yaml]] — переменные ядра сети (`kube_pods_subnet`, `kube_network_node_prefix`)
- [[versions/v2.27.1/variables/download|download.yaml]] — механизм загрузок
- [[versions/v2.27.1/variables/etcd|etcd.yaml]] — etcd используется Cilium при `identity_allocation_mode: kvstore`
- [[versions/v2.27.1/README|Срез v2.27.1]]

## Сверка полноты

Извлечено: `roles/network_plugin/cilium/defaults/main.yml` — все **86** top-level ключей (плюс 4 закомментированные `cilium_pool_*` задокументированы как «не задана»; `cilium_hubble_event_buffer_capacity`/`cilium_hubble_event_queue_size` закомментированы и в справочник не выносятся). Дополнительно: `cni_bin_owner` из `network_plugin/cni/defaults`, 3 переменные выбора CNI из `main.yml` и 21 переменная версий/образов Cilium/CNI из `download.yml`. Итого в `cni.yaml` — **115 записей**; сверка `grep -cE '^[a-z_]...:'` по cilium/defaults = 86, все покрыты. Прочие сетевые плагины исключены по охвату.
