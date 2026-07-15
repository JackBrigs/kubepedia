---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: code
source_path: versions/v2.31.0/variables/cni.yaml
retrieved_at: 2026-07-14
topics:
  - cni
  - cilium
  - network
reliability: authoritative
---

# CNI в Kubespray v2.31.0 (фокус: Cilium)

Источник истины для этой заметки — YAML-справочник [[versions/v2.31.0/variables/cni|cni.yaml]]. Ниже человекочитаемое изложение. Все значения по умолчанию извлечены строго из кода тега `v2.31.0` (commit `1c9add4`).

## Выбор CNI-плагина

Сетевой плагин задаётся переменной `kube_network_plugin` в `roles/kubespray_defaults/defaults/main/main.yml`. По умолчанию — `calico`. Для использования Cilium нужно явно установить:

```yaml
kube_network_plugin: cilium
```

| Переменная | Значение по умолчанию | Назначение |
| --- | --- | --- |
| `kube_network_plugin` | `calico` | Выбор CNI: cilium, calico, kube-ovn, flannel, kube-router, cni, cloud |
| `kube_network_plugin_multus` | `false` | Установка Multus поверх основного CNI |
| `cilium_deploy_additionally` | `false` | Развернуть Cilium рядом с другим CNI (например, для замены kube-proxy) |
| `cilium_identity_allocation_mode` | `crd` | Хранение identities: `crd` (в Kubernetes) или `kvstore` (в etcd) |

Значение `cni` соответствует обобщённому внешнему CNI, а `cloud` перекладывает маршрутизацию на облачного провайдера.

## Версии и образы Cilium

Извлечено из `roles/kubespray_defaults/defaults/main/download.yml`:

| Переменная | Значение по умолчанию |
| --- | --- |
| `cilium_version` | `1.19.3` |
| `cilium_image_repo` | `{{ quay_image_repo }}/cilium/cilium` |
| `cilium_image_tag` | `v{{ cilium_version }}` |
| `cilium_operator_image_repo` | `{{ quay_image_repo }}/cilium/operator` |
| `cilium_hubble_relay_image_repo` | `{{ quay_image_repo }}/cilium/hubble-relay` |
| `cilium_hubble_certgen_image_tag` | `v0.2.4` |
| `cilium_hubble_ui_image_tag` | `v0.13.3` |
| `cilium_hubble_ui_backend_image_tag` | `v0.13.3` |
| `cilium_hubble_envoy_image_tag` | `v1.34.10-1762597008-ff7ae7d623be00078865cff1b0672cc5d9bfc6d5` |

Образы Hubble (`hubble-relay`, `certgen`, `hubble-ui`, `envoy`) скачиваются только при `cilium_enable_hubble: true`; образы `cilium`, `cilium_operator`, `ciliumcli` — при `kube_network_plugin == 'cilium'` или `cilium_deploy_additionally`.

## Ключевые переменные Cilium

Все они объявлены в `roles/network_plugin/cilium/defaults/main.yml`.

### Базовая сеть и режим работы

| Переменная | По умолчанию | Назначение |
| --- | --- | --- |
| `cilium_min_version_required` | `"1.15"` | Минимально поддерживаемая версия (проверка в tasks/check.yml) |
| `cilium_tunnel_mode` | `vxlan` | Оверлей: vxlan, geneve или disabled |
| `cilium_mtu` | `"0"` | MTU (0 — автоопределение) |
| `cilium_enable_ipv4` | `{{ ipv4_stack }}` | Поддержка IPv4 |
| `cilium_enable_ipv6` | `{{ ipv6_stack }}` | Поддержка IPv6 |
| `cilium_auto_direct_node_routes` | `false` | Прямые маршруты без туннелирования (при disabled) |
| `cilium_native_routing_cidr` | `""` | IPv4 CIDR для native routing без SNAT |
| `cilium_ipam_mode` | `cluster-pool` | Режим IPAM (Cluster Scope) |
| `cilium_debug` | `false` | Уровень логирования debug |

### Замена kube-proxy и балансировка

| Переменная | По умолчанию | Назначение |
| --- | --- | --- |
| `cilium_kube_proxy_replacement` | `false` | Замена kube-proxy средствами Cilium |
| `cilium_loadbalancer_mode` | `snat` | Режим LB: snat, dsr, hybrid |
| `cilium_loadbalancer_ip_pools` | `[]` | Пулы IP для LoadBalancer |
| `cilium_l2announcements` | `false` | L2-анонсирование (замена MetalLB) |

При включённом `cilium_kube_proxy_replacement` (`true`/`strict`) Kubespray учитывает это в расчёте удаления kube-proxy (`kube_proxy_remove`).

### Ресурсы подов

| Переменная | По умолчанию |
| --- | --- |
| `cilium_memory_limit` | `500M` |
| `cilium_cpu_limit` | `500m` |
| `cilium_memory_requests` | `64M` |
| `cilium_cpu_requests` | `100m` |
| `cilium_operator_replicas` | `2` |

### Шифрование трафика

| Переменная | По умолчанию | Назначение |
| --- | --- | --- |
| `cilium_encryption_enabled` | `false` | Прозрачное шифрование |
| `cilium_encryption_type` | `"ipsec"` | Метод: ipsec или wireguard |
| `cilium_encryption_node_encryption` | `false` | Шифрование node-to-node (только wireguard) |

### Маскарадинг

| Переменная | По умолчанию | Назначение |
| --- | --- | --- |
| `cilium_enable_ipv4_masquerade` | `true` | Маскарадинг IPv4 |
| `cilium_enable_ipv6_masquerade` | `true` | Маскарадинг IPv6 |
| `cilium_enable_bpf_masquerade` | `false` | Нативный маскарадинг в eBPF |
| `cilium_ip_masq_agent_enable` | `false` | Включение ip-masq-agent |

### Hubble (наблюдаемость)

| Переменная | По умолчанию | Назначение |
| --- | --- | --- |
| `cilium_enable_hubble` | `false` | Включение Hubble |
| `cilium_enable_hubble_ui` | `{{ cilium_enable_hubble }}` | Hubble UI |
| `cilium_hubble_metrics` | `[]` | Список экспортируемых метрик |
| `cilium_hubble_export_dynamic_enabled` | `false` | Динамический экспорт потоков в файл |

### BGP Control Plane

| Переменная | По умолчанию | Назначение |
| --- | --- | --- |
| `cilium_enable_bgp_control_plane` | `false` | Включение BGP |
| `cilium_bgp_cluster_configs` | `[]` | BGP Instances (bgpv2 API, v1.16+) |
| `cilium_bgp_peer_configs` | `[]` | BGP Peers (bgpv2 API, v1.16+) |
| `cilium_bgp_peering_policies` | `[]` | BGP Peers (legacy API < v1.16) |

### Кастомизация установки (Helm)

В v2.31.0 Cilium устанавливается через Helm-чарт (`templates/values.yaml.j2`). Расширенная настройка:

| Переменная | По умолчанию | Назначение |
| --- | --- | --- |
| `cilium_config_extra_vars` | `{}` | Доп. параметры в cilium-config |
| `cilium_extra_values` | `{}` | Произвольные values Helm-чарта Cilium |
| `cilium_install_extra_flags` | `""` | Доп. флаги команды установки |
| `cilium_agent_extra_args` | `[]` | Доп. аргументы агента |
| `cilium_operator_extra_args` | `[]` | Доп. аргументы оператора |

## Переменные, объявленные но не используемые (reliability: unconfirmed)

Следующие 16 переменных объявлены в `defaults/main.yml`, но `grep -w` по `roles/` и `playbooks/` тега `v2.31.0` не находит их использования в задачах или шаблонах. Причина — перевод установки Cilium на Helm-чарт: часть legacy-ключей осталась в defaults, но фактически не влияет на развёртывание. В справочнике они помечены `reliability: unconfirmed`.

- `cilium_agent_custom_args` (deprecated), `cilium_operator_custom_args` (deprecated)
- `cilium_agent_extra_env_vars`
- `cilium_agent_scrape_port`, `cilium_operator_scrape_port`, `cilium_hubble_scrape_port`
- `cilium_certgen_args`
- `cilium_disable_cnp_status_updates`
- `cilium_enable_hubble_metrics` (deprecated)
- `cilium_enable_remote_node_identity`, `cilium_enable_well_known_identities`
- `cilium_hubble_install`, `cilium_hubble_tls_generate`
- `cilium_monitor_aggregation_flags`
- `cilium_operator_api_serve_addr`
- `cilium_wireguard_userspace_fallback`

## Непроиндексированные CNI-плагины

По ограничению этого среза индексируется только Cilium. Прочие плагины из `roles/network_plugin/` присутствуют в v2.31.0, но их переменные здесь НЕ разбираются:

- `calico` (плюс `calico_defaults`)
- `flannel`
- `kube-ovn`
- `kube-router`
- `macvlan`
- `multus`
- `ovn4nfv`
- `custom_cni` (установка произвольного CNI через Helm/манифесты)
- `cni` (обобщённый внешний CNI; единственная переменная `cni_bin_owner` включена в справочник)

## Навигация

- Полный машиночитаемый справочник: [[versions/v2.31.0/variables/cni|cni.yaml]]
- Срез версии: [[versions/v2.31.0/README|Срез v2.31.0]]
