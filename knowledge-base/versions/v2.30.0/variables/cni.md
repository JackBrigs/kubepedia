---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: code
source_path: versions/v2.30.0/variables/cni.yaml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0
retrieved_at: 2026-07-14
topics: [cni, cilium, network]
reliability: authoritative
---

# CNI и Cilium в Kubespray v2.30.0

Заметка описывает переменные выбора сетевого плагина (CNI) и переменные плагина **Cilium** для тега `v2.30.0` (commit `f4ccdb5`). Источник истины — машиночитаемый справочник [[versions/v2.30.0/variables/cni|cni.yaml]]; здесь дано человекочитаемое изложение.

> Область охвата проекта: из сетевых плагинов индексируется **только Cilium**. Прочие плагины лишь перечислены ниже.

## Ключевое изменение v2.30.0: установка Cilium через Helm/CLI

В `v2.30.0` роль `roles/network_plugin/cilium` устанавливает Cilium официальным **Cilium CLI** с передачей Helm-values:

```
cilium install/upgrade --version {{ cilium_version }} -f cilium-values.yaml -f cilium-extra-values.yaml {{ cilium_install_extra_flags }}
```
(`roles/network_plugin/cilium/tasks/apply.yml`)

Values формируются из шаблона `roles/network_plugin/cilium/templates/values.yaml.j2`, а произвольные значения чарта — из `cilium_extra_values` (файл `cilium-extra-values.yaml`).

Следствие: часть переменных, объявленных в `defaults/main.yml`, **больше не подключена** к шаблону/задачам роли и фактически не применяется. В справочнике такие переменные помечены `reliability: unconfirmed`. Полный список — в разделе [«Объявленные, но не используемые переменные»](#объявленные-но-не-используемые-переменные).

## Выбор CNI

Плагин выбирается в `roles/kubespray_defaults/defaults/main/main.yml`. Подключение ролей плагинов описано в `roles/network_plugin/meta/main.yml`.

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `kube_network_plugin` | `calico` | Выбор CNI. Для Cilium задать `cilium`. Допустимо: cilium, calico, kube-ovn, flannel, kube-router, macvlan, custom_cni, cni, none, cloud |
| `kube_network_plugin_multus` | `false` | Подключение мета-плагина Multus (несколько интерфейсов у пода) поверх основного CNI |
| `cilium_deploy_additionally` | `false` | Развернуть Cilium рядом с другим CNI (например, для замены kube-proxy) |

Роль `network_plugin/cilium` подключается при `kube_network_plugin == 'cilium' or cilium_deploy_additionally` (тег запуска `cilium`). Универсальная роль `network_plugin/cni` (установка бинарников CNI) подключается всегда при `kube_network_plugin != 'none'`; её переменная — `cni_bin_owner` (по умолчанию `{{ kube_owner }}`).

## Версии и образы Cilium

Заданы в `roles/kubespray_defaults/defaults/main/download.yml`.

| Переменная | Значение по умолчанию |
|---|---|
| `cilium_version` | `1.18.6` |
| `cilium_cli_version` | из чек-сумм `ciliumcli_binary_checksums` |
| `cilium_image_tag` / `cilium_operator_image_tag` | `v{{ cilium_version }}` |
| `cilium_hubble_certgen_image_tag` | `v0.2.4` |
| `cilium_hubble_ui_image_tag` / `..._backend` | `v0.13.3` |
| `cilium_hubble_envoy_image_tag` | `v1.34.10-1762597008-ff7ae7...` |

Минимальная поддерживаемая версия — `cilium_min_version_required: "1.15"` (проверяется в `tasks/check.yml`).

## Базовая сеть

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `cilium_mtu` | `"0"` | MTU (0 — автоопределение) |
| `cilium_debug` | `false` | Отладочные логи агента |
| `cilium_enable_ipv4` | `{{ ipv4_stack }}` | Включение IPv4 |
| `cilium_enable_ipv6` | `{{ ipv6_stack }}` | Включение IPv6 (dual-stack) |
| `cilium_tunnel_mode` | `vxlan` | Протокол оверлея: vxlan / geneve / disabled |
| `cilium_identity_allocation_mode` | `crd` | Хранение identity: crd или kvstore (etcd) |
| `cilium_agent_health_port` | `"9879"` | Порт health-проверки агента |
| `cilium_l2announcements` | `false` | L2-анонсирование (замена MetalLB) |

При `cilium_identity_allocation_mode: kvstore` в `tasks/install.yml` в каталог `cilium_cert_dir` (`/etc/cilium/certs`) копируются сертификаты etcd (`kube_etcd_cacert_file`, `kube_etcd_cert_file`, `kube_etcd_key_file`).

## Замена kube-proxy и маршрутизация

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `cilium_kube_proxy_replacement` | `false` | Замена kube-proxy средствами Cilium; при включении Kubespray отключает установку kube-proxy |
| `cilium_dns_proxy_enable_transparent_mode` | не задана | dnsProxy.enableTransparentMode; рендерится только если определена; помогает избежать конфликта с nodelocaldns |
| `cilium_loadbalancer_mode` | `snat` | Режим LB: snat / dsr / hybrid |
| `cilium_loadbalancer_ip_pools` | `[]` | Пулы IP для LoadBalancer |
| `cilium_auto_direct_node_routes` | `false` | Нативные маршруты подов без туннелей (нужна L2-связность) |
| `cilium_native_routing_cidr` / `_ipv6` | `""` | CIDR нативной маршрутизации без SNAT |
| `cilium_enable_host_legacy_routing` | `false` | Маршрутизация через host stack вместо BPF |

## IPAM и Pod CIDR

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `cilium_ipam_mode` | `cluster-pool` | Режим IPAM (Cluster Scope) |
| `cilium_pool_cidr` / `_ipv6` | не задана → `kube_pods_subnet(_ipv6)` | Pod CIDR пула |
| `cilium_pool_mask_size` / `_ipv6` | не задана → `kube_network_node_prefix(_ipv6)` | Размер сегмента на узел |

## Шифрование

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `cilium_encryption_enabled` | `false` | Прозрачное шифрование трафика |
| `cilium_encryption_type` | `ipsec` | Метод: ipsec / wireguard (при `cilium_encryption_enabled`) |
| `cilium_encryption_node_encryption` | `false` | Шифрование node-to-node (только для wireguard) |

## IP-маскарадинг

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `cilium_enable_ipv4_masquerade` | `true` | Маскарадинг исходящего IPv4 |
| `cilium_enable_ipv6_masquerade` | `true` | Маскарадинг исходящего IPv6 |
| `cilium_enable_bpf_masquerade` | `false` | Нативный маскарадинг в eBPF |
| `cilium_ip_masq_agent_enable` | `false` | Включение ip-masq-agent |
| `cilium_non_masquerade_cidrs` | список приватных сетей | CIDR без маскарадинга |
| `cilium_masq_link_local` / `_ipv6` | `false` | Маскарадинг link-local |
| `cilium_ip_masq_resync_interval` | `60s` | Интервал перечитывания конфигурации |

## Hubble (наблюдаемость)

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `cilium_enable_hubble` | `false` | Включение Hubble |
| `cilium_enable_hubble_ui` | `{{ cilium_enable_hubble }}` | Hubble UI |
| `cilium_hubble_metrics` | `[]` | Список метрик (dns, drop, tcp, flow, icmp, http) |
| `cilium_hubble_export_dynamic_enabled` | `false` | Динамический экспорт потоков |
| `cilium_hubble_export_file_max_backups` | `"5"` | Число ротаций файла экспорта |
| `cilium_hubble_export_file_max_size_mb` | `"10"` | Размер файла экспорта, МБ |
| `cilium_hubble_peer_service_cluster_domain` | `{{ dns_domain }}` | DNS-суффикс для peer-сервиса Hubble-Relay |
| `cilium_hubble_event_buffer_capacity` | не задана (Cilium: 4095) | Ёмкость буфера событий; валидируется в check.yml |

## BGP Control Plane

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `cilium_enable_bgp_control_plane` | `false` | Включение BGP Control Plane |
| `cilium_bgp_cluster_configs` | `[]` | BGP Instances (bgpv2, v1.16+) |
| `cilium_bgp_peer_configs` | `[]` | BGP Peers (bgpv2, v1.16+) |
| `cilium_bgp_advertisements` | `[]` | BGP Advertisements (bgpv2, v1.16+) |
| `cilium_bgp_node_config_overrides` | `[]` | Node Config Overrides (bgpv2, v1.16+) |
| `cilium_bgp_peering_policies` | `[]` | BGP Peers (устаревший API, < v1.16) |

## Operator, cgroup, прочее

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `cilium_operator_replicas` | `2` | Реплики cilium-operator |
| `cilium_operator_tolerations` | `[{operator: Exists}]` | Tolerations оператора |
| `cilium_cgroup_auto_mount` | `true` | Автомонтирование cgroup2 |
| `cilium_cgroup_host_root` | `/run/cilium/cgroupv2` | Путь монтирования cgroup2 |
| `cilium_cni_exclusive` | `true` | Монопольное владение /etc/cni/net.d |
| `cilium_cni_log_file` | `/var/run/cilium/cilium-cni.log` | Файл логов CNI |
| `cilium_cluster_id` / `cilium_cluster_name` | `0` / `default` | Идентификация для Cluster Mesh |
| `cilium_enable_host_firewall` | `false` | Host Firewall |
| `cilium_policy_audit_mode` | `false` | Режим аудита сетевых политик |
| `cilium_gateway_api_enabled` | `false` | Поддержка Gateway API |
| `cilium_agent_extra_args` / `cilium_operator_extra_args` | `[]` | Доп. аргументы агента/оператора |
| `cilium_config_extra_vars` | `{}` | Доп. параметры cilium-config |
| `cilium_install_extra_flags` | `""` | Доп. флаги команды cilium install |
| `cilium_extra_values` | `{}` | Произвольные значения Helm-чарта |

## Объявленные, но не используемые переменные

В `v2.30.0` (переход на Helm/CLI) следующие переменные объявлены в `defaults`, но **не подключены** к шаблонам/задачам роли — в справочнике им проставлен `reliability: unconfirmed`, фактически они не влияют на установку:

- Ресурсы подов: `cilium_memory_limit`, `cilium_cpu_limit`, `cilium_memory_requests`, `cilium_cpu_requests`
- Метрики/порты: `cilium_enable_prometheus`, `cilium_agent_scrape_port`, `cilium_operator_scrape_port`, `cilium_hubble_scrape_port`
- Hubble: `cilium_enable_hubble_metrics` (deprecated), `cilium_hubble_install`, `cilium_hubble_tls_generate`, `cilium_hubble_event_queue_size`, `cilium_certgen_args`
- Identity/BPF: `cilium_enable_remote_node_identity`, `cilium_enable_well_known_identities`, `cilium_enable_bpf_clock_probe`, `cilium_monitor_aggregation_flags`, `cilium_disable_cnp_status_updates`
- Доп. параметры: `cilium_agent_extra_env_vars`, `cilium_operator_api_serve_addr`, `cilium_wireguard_userspace_fallback`
- Устаревшие (заменены на `*_extra_args`): `cilium_agent_custom_args`, `cilium_operator_custom_args`

Проверено grep-ом по `roles/` и `playbooks/` тега `v2.30.0`. Для нужного эффекта соответствующие значения следует задавать через `cilium_extra_values` (Helm-чарт).

## Непроиндексированные сетевые плагины тега v2.30.0

Присутствуют в `roles/network_plugin/`, но в этой базе знаний **не разбираются** (только Cilium):

`calico`, `calico_defaults`, `flannel`, `kube-ovn`, `kube-router`, `macvlan`, `custom_cni`, `ovn4nfv`, `multus`.

---

См. также: [[versions/v2.30.0/README|Срез v2.30.0]]
