---
project: kubespray
kubespray_version: v2.27.1
git_commit: 45140b5
source_type: inventory
source_path: inventory/sample/group_vars/k8s_cluster/k8s-net-cilium.yml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.27.1
retrieved_at: 2026-07-15
topics:
  - inventory
  - cni
  - cilium
reliability: authoritative
---

# Sample-inventory: настройки Cilium (v2.27.1)

Разбор файла `inventory/sample/group_vars/k8s_cluster/k8s-net-cilium.yml` тега
**v2.27.1** (commit `45140b5`). Из сетевых плагинов в проекте индексируется
**только Cilium**.

Источник истины по машиночитаемым данным — [[versions/v2.27.1/inventory/cni-cilium|cni-cilium.yaml]].
Значения по умолчанию самой роли — в [[versions/v2.27.1/variables/cni|variables/cni.yaml]].
Родительский срез: [[versions/v2.27.1/README|Срез v2.27.1]].

## Обзор

Файл содержит **82 переменные** Cilium, сгруппированные по темам: базовые
настройки, туннелирование/маршрутизация, замена kube-proxy, шифрование,
маскарадинг, Hubble, IPAM, BGP, agent/operator.

Ключевая особенность файла: **почти всё закомментировано** — это примеры
значений, а не заданные настройки. Раскомментирована ровно **одна**
переменная:

- `cilium_l2announcements: false`

Остальные **81 переменная** приведены как закомментированные примеры
(`is_set: false`) и в реальном развёртывании берут значения из defaults роли
`roles/network_plugin/cilium/defaults/main.yml`.

> [!note] Отличия от v2.29.1
> - В v2.27.1 присутствует закомментированная `cilium_version: "v1.15.9"` (совпадает с default роли).
> - **Отсутствуют** переменные `cilium_hubble_peer_service_cluster_domain` и `cilium_extra_values` (появились позже).
> - Имя переменной шифрования node-to-node — `cilium_ipsec_node_encryption`, и оно **совпадает** с defaults роли (в v2.29.1 роль переименовала её в `cilium_encryption_node_encryption`).
> - Меньше расхождений закомментированных примеров с defaults (см. ниже): в v2.27.1 совпадают `cilium_identity_allocation_mode`, `cilium_kube_proxy_replacement`, `cilium_enable_host_legacy_routing`.

## Отличия закомментированных примеров от defaults роли

| Переменная | Пример в sample | Default роли (v2.27.1) | Совпадает? |
| --- | --- | --- | --- |
| `cilium_identity_allocation_mode` | `kvstore` | `kvstore` | да |
| `cilium_kube_proxy_replacement` | `partial` | `partial` | да |
| `cilium_enable_host_legacy_routing` | `true` | `true` | да |
| `cilium_ipam_mode` | `kubernetes` | `cluster-pool` | **нет** |
| `cilium_bpf_map_dynamic_size_ratio` | `"0.0"` | `"0.0025"` | **нет** |

Отличающиеся примеры относятся к **закомментированным** переменным и потому не
являются расхождениями действующих настроек.

## Ключевые опции по разделам

### Базовые
`cilium_debug` (false), `cilium_mtu` (""), `cilium_enable_ipv4`/`_ipv6`,
`cilium_l2announcements` (**задана**, false), `cilium_identity_allocation_mode`
(kvstore), `cilium_cni_exclusive` (true).

### Туннелирование / маршрутизация
`cilium_tunnel_mode` (vxlan), `cilium_auto_direct_node_routes`,
`cilium_native_routing_cidr` / `_ipv6`, `cilium_enable_host_legacy_routing` (true).

### Замена kube-proxy
`cilium_kube_proxy_replacement` (partial), `cilium_loadbalancer_mode` (snat),
`cilium_deploy_additionally` (false).

### Шифрование
`cilium_encryption_enabled`, `cilium_encryption_type` (ipsec),
`cilium_ipsec_node_encryption`, `cilium_wireguard_userspace_fallback`.

### Маскарадинг / ip-masq-agent
`cilium_ip_masq_agent_enable`, `cilium_non_masquerade_cidrs` (список RFC-диапазонов),
`cilium_masq_link_local`, `cilium_enable_ipv4_masquerade` / `_ipv6_masquerade` (true),
`cilium_enable_bpf_masquerade`.

### Hubble
`cilium_enable_hubble`, `cilium_enable_hubble_ui`, `cilium_enable_hubble_metrics`,
`cilium_hubble_metrics`, `cilium_hubble_install`, `cilium_hubble_tls_generate`,
`cilium_hubble_event_buffer_capacity` (4095), `cilium_hubble_event_queue_size` (50).

### IPAM
`cilium_ipam_mode` (пример kubernetes; default роли — cluster-pool).

### BGP
`cilium_enable_bgp_control_plane`, `cilium_loadbalancer_ip_pools`,
`cilium_bgp_cluster_configs` / `_peer_configs` / `_advertisements` /
`_node_config_overrides` (bgpv2 API v1.16+), `cilium_bgp_peering_policies` (legacy).

### Agent / Operator
`cilium_agent_custom_args`, `cilium_operator_replicas` (2), `cilium_config_extra_vars`,
`cilium_operator_custom_args`.

## Опечатка в исходном sample

В строке примера `cilium_enable_hubble_ui: "{{ cilium_enable_hubble }}` **незакрытая
двойная кавычка** (комментарий), перенесена дословно. Так как строка закомментирована,
на кластер не влияет.

## Расхождения sample vs defaults роли

Проверка расхождений (раздел 6.2 CLAUDE.md) выполняется только для
**раскомментированных** (`is_set: true`) переменных.

В файле раскомментирована одна переменная — `cilium_l2announcements: false`.
Её значение совпадает с default роли (`false`), см.
[[versions/v2.27.1/variables/cni|variables/cni.yaml]].

**Расхождений действующих настроек нет.** Отличия закомментированных примеров
(`cilium_ipam_mode`, `cilium_bpf_map_dynamic_size_ratio`) расхождениями не считаются.

## Непроиндексированные сетевые sample-файлы

Из сетевых плагинов v2.27.1 индексируется только Cilium. Следующие sample-файлы
других CNI **не разобраны** по переменным (вне границ проекта):

- `inventory/sample/group_vars/k8s_cluster/k8s-net-calico.yml`
- `inventory/sample/group_vars/k8s_cluster/k8s-net-flannel.yml`
- `inventory/sample/group_vars/k8s_cluster/k8s-net-weave.yml`
- `inventory/sample/group_vars/k8s_cluster/k8s-net-kube-ovn.yml`
- `inventory/sample/group_vars/k8s_cluster/k8s-net-kube-router.yml`
- `inventory/sample/group_vars/k8s_cluster/k8s-net-macvlan.yml`
- `inventory/sample/group_vars/k8s_cluster/k8s-net-custom-cni.yml`
