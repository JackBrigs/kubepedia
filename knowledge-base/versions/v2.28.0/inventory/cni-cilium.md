---
project: kubespray
kubespray_version: v2.28.0
git_commit: 63cdf87
source_type: inventory
source_path: inventory/sample/group_vars/k8s_cluster/k8s-net-cilium.yml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.28.0
retrieved_at: 2026-07-15
topics:
  - inventory
  - cni
  - cilium
reliability: authoritative
---

# Sample-inventory: настройки Cilium (v2.28.0)

Разбор файла `inventory/sample/group_vars/k8s_cluster/k8s-net-cilium.yml` тега
**v2.28.0** (commit `63cdf87`). Из сетевых плагинов в проекте индексируется
**только Cilium**.

Источник истины по машиночитаемым данным — [[versions/v2.28.0/inventory/cni-cilium|cni-cilium.yaml]].
Значения по умолчанию самой роли — в [[versions/v2.28.0/variables/cni|variables/cni.yaml]].
Родительский срез: [[versions/v2.28.0/README|Срез v2.28.0]].

## Обзор

Файл содержит **81 переменную** Cilium, сгруппированную по темам: базовые
настройки, туннелирование/маршрутизация, замена kube-proxy, шифрование,
маскарадинг, Hubble, IPAM, BGP, agent/operator.

Ключевая особенность файла: **почти всё закомментировано** — это примеры
значений, а не заданные настройки. Раскомментирована ровно **одна**
переменная:

- `cilium_l2announcements: false`

Остальные **80 переменных** приведены как закомментированные примеры
(`is_set: false`) и в реальном развёртывании берут значения из defaults роли
`roles/network_plugin/cilium/defaults/main.yml`.

Важно: приведённые в sample примеры местами **отличаются** от фактических
defaults роли (это примеры для наглядности, а не рабочие значения). Наиболее
заметные расхождения примеров с defaults роли:

| Переменная | Пример в sample | Default роли |
| --- | --- | --- |
| `cilium_identity_allocation_mode` | `kvstore` | `crd` |
| `cilium_kube_proxy_replacement` | `partial` | `false` |
| `cilium_ipam_mode` | `kubernetes` | `cluster-pool` |
| `cilium_bpf_map_dynamic_size_ratio` | `"0.0"` | `"0.0025"` |
| `cilium_enable_host_legacy_routing` | `true` | `false` |

Эти отличия относятся к **закомментированным** примерам и потому не являются
расхождениями действующих настроек (см. раздел ниже).

## Ключевые опции по разделам

### Базовые

| Переменная | Пример (commented) | Назначение |
| --- | --- | --- |
| `cilium_debug` | `false` | Отладочное логирование агента |
| `cilium_mtu` | `""` | MTU (0/пусто — автоопределение) |
| `cilium_enable_ipv4` | `true` | Включить IPv4 |
| `cilium_enable_ipv6` | `false` | Включить IPv6 |
| `cilium_l2announcements` | `false` (**задана**) | L2-анонсы (замена MetalLB) |
| `cilium_identity_allocation_mode` | `kvstore` | Хранение identity: crd/kvstore |
| `cilium_cni_exclusive` | `true` | Единоличное владение /etc/cni/net.d |

### Туннелирование / маршрутизация

| Переменная | Пример (commented) | Назначение |
| --- | --- | --- |
| `cilium_tunnel_mode` | `vxlan` | Overlay-режим; disabled — native |
| `cilium_auto_direct_node_routes` | `false` | Анонс маршрутов подов без туннеля |
| `cilium_native_routing_cidr` | `""` | IPv4 CIDR нативной маршрутизации |
| `cilium_native_routing_cidr_ipv6` | `""` | IPv6 CIDR нативной маршрутизации |
| `cilium_enable_host_legacy_routing` | `true` | Direct-routing через хостовый стек |

### Замена kube-proxy

| Переменная | Пример (commented) | Назначение |
| --- | --- | --- |
| `cilium_kube_proxy_replacement` | `partial` | Замена kube-proxy (strict/partial) |
| `cilium_loadbalancer_mode` | `snat` | Режим LB: snat/dsr/hybrid |
| `cilium_deploy_additionally` | `false` | Развернуть рядом с другим CNI |

### Шифрование

| Переменная | Пример (commented) | Назначение |
| --- | --- | --- |
| `cilium_encryption_enabled` | `false` | Прозрачное шифрование node-to-node |
| `cilium_encryption_type` | `"ipsec"` | ipsec или wireguard |
| `cilium_ipsec_node_encryption` | `false` | Шифрование node-to-node (ipsec) |
| `cilium_wireguard_userspace_fallback` | `false` | Userspace-fallback WireGuard |

### Маскарадинг / ip-masq-agent

| Переменная | Пример (commented) | Назначение |
| --- | --- | --- |
| `cilium_ip_masq_agent_enable` | `false` | Включить ip-masq-agent |
| `cilium_non_masquerade_cidrs` | список RFC-диапазонов | Не маскарадить эти CIDR |
| `cilium_masq_link_local` | `false` | Маскарадить ли link-local |
| `cilium_enable_ipv4_masquerade` | `true` | Маскарадинг IPv4 (Cilium v1.10+) |
| `cilium_enable_ipv6_masquerade` | `true` | Маскарадинг IPv6 (Cilium v1.10+) |
| `cilium_enable_bpf_masquerade` | `false` | Нативный eBPF-маскарадинг |

### Hubble

| Переменная | Пример (commented) | Назначение |
| --- | --- | --- |
| `cilium_enable_hubble` | `false` | Включить Hubble + hubble-relay |
| `cilium_enable_hubble_ui` | `{{ cilium_enable_hubble }}` | Включить Hubble UI |
| `cilium_enable_hubble_metrics` | `false` | Метрики Hubble (deprecated) |
| `cilium_hubble_metrics` | `{}` | Список метрик (dns/drop/tcp/…) |
| `cilium_hubble_event_buffer_capacity` | `4095` | Ёмкость буфера событий |
| `cilium_hubble_event_queue_size` | `50` | Размер буфера канала monitor-событий |

### IPAM

| Переменная | Пример (commented) | Назначение |
| --- | --- | --- |
| `cilium_ipam_mode` | `kubernetes` | Режим IPAM (default роли — cluster-pool) |

### BGP

| Переменная | Пример (commented) | Назначение |
| --- | --- | --- |
| `cilium_enable_bgp_control_plane` | `false` | Включить BGP Control Plane |
| `cilium_loadbalancer_ip_pools` | пример пула | CiliumLoadBalancerIPPool |
| `cilium_bgp_cluster_configs` | пример | CiliumBGPClusterConfig (bgpv2, v1.16+) |
| `cilium_bgp_peer_configs` | пример | CiliumBGPPeerConfig (bgpv2) |
| `cilium_bgp_advertisements` | пример | CiliumBGPAdvertisement (bgpv2) |
| `cilium_bgp_node_config_overrides` | пример | CiliumBGPNodeConfigOverride (bgpv2) |
| `cilium_bgp_peering_policies` | пример | CiliumBGPPeeringPolicy (legacy, < 1.16) |

### Agent / Operator

| Переменная | Пример (commented) | Назначение |
| --- | --- | --- |
| `cilium_agent_custom_args` | `[]` | Доп. аргументы агента (deprecated) |
| `cilium_operator_replicas` | `2` | Реплики cilium-operator |
| `cilium_config_extra_vars` | `{}` | Доп. ключи cilium-config |
| `cilium_clusterrole_rules_operator_extra_vars` | `[]` | Доп. правила clusterrole cilium-operator |

## Расхождения sample vs defaults роли

Проверка расхождений (раздел 6.2 CLAUDE.md) выполняется только для
**раскомментированных** (`is_set: true`) переменных.

В файле раскомментирована одна переменная — `cilium_l2announcements: false`.
Её значение совпадает с default роли (`false`), см.
[[versions/v2.28.0/variables/cni|variables/cni.yaml]].

**Расхождений действующих настроек нет.**

Отличия закомментированных примеров sample от defaults роли (перечислены выше в
разделе «Обзор») расхождениями не считаются — это иллюстративные примеры, не
задающие значения.

## Непроиндексированные сетевые sample-файлы

Из сетевых плагинов v2.28.0 индексируется только Cilium. Следующие sample-файлы
других CNI **не разобраны** по переменным (вне границ проекта):

- `inventory/sample/group_vars/k8s_cluster/k8s-net-calico.yml`
- `inventory/sample/group_vars/k8s_cluster/k8s-net-flannel.yml`
- `inventory/sample/group_vars/k8s_cluster/k8s-net-kube-ovn.yml`
- `inventory/sample/group_vars/k8s_cluster/k8s-net-kube-router.yml`
- `inventory/sample/group_vars/k8s_cluster/k8s-net-macvlan.yml`
- `inventory/sample/group_vars/k8s_cluster/k8s-net-weave.yml` (присутствует в v2.28.0, удалён в v2.29.1)
- `inventory/sample/group_vars/k8s_cluster/k8s-net-custom-cni.yml`

> [!note] Отличия набора переменных Cilium от v2.29.1
> В v2.28.0 в файле **нет** двух переменных, добавленных позже в v2.29.1:
> `cilium_hubble_peer_service_cluster_domain` и `cilium_extra_values` (helm passthrough).
> Итог: 81 переменная против 83 в v2.29.1.
