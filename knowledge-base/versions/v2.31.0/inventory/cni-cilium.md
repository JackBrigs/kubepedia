---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: inventory
source_path: inventory/sample/group_vars/k8s_cluster/k8s-net-cilium.yml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0
retrieved_at: 2026-07-14
topics:
  - inventory
  - cni
  - cilium
reliability: authoritative
---

# Sample inventory: Cilium (v2.31.0)

Разбор файла `inventory/sample/group_vars/k8s_cluster/k8s-net-cilium.yml` тега
**v2.31.0** (commit `1c9add4`). Из всех CNI-плагинов в этом срезе детально
индексируется **только Cilium**.

Источник истины по значениям — машиночитаемый справочник
[[versions/v2.31.0/inventory/cni-cilium|cni-cilium.yaml]]. Эта заметка —
человекочитаемое представление. Значения по умолчанию из кода роли см. в
[[versions/v2.31.0/variables/cni|variables/cni.yaml]].

Навигация: [[versions/v2.31.0/README|Срез v2.31.0]].

## Обзор

Файл `k8s-net-cilium.yml` в sample-инвентаре — это шаблон настроек Cilium,
который пользователь копирует в свой инвентарь и правит под себя.

**Ключевой факт: почти весь файл закомментирован.** Все строки, кроме одной,
начинаются с `#` и служат лишь примерами-подсказками со значениями по умолчанию.
Раскомментированные (реально применяемые) настройки:

| Переменная | Значение | Совпадает с defaults роли |
|---|---|---|
| `cilium_l2announcements` | `false` | да (`false`) |

Итог: **82 переменные** в файле, из них **1 задана** (`is_set: true`) и
**81 закомментирована** (`is_set: false`).

## Проверка расхождений (раздел 6.2)

Расхождение между sample-инвентарём и `roles/*/defaults` фиксируется только для
**реально заданных** переменных. Единственная заданная переменная
`cilium_l2announcements: false` совпадает со своим значением по умолчанию в
`roles/network_plugin/cilium/defaults/main.yml`. Поэтому:

**Расхождений нет — `discrepancies: []`.**

### Примечание: закомментированные примеры, отличающиеся от defaults

Ряд закомментированных значений-примеров в sample отличается от фактических
значений по умолчанию роли. Так как строки закомментированы, они **не
переопределяют** defaults и не являются расхождениями, но их стоит знать: при
простом раскомментировании поведение изменится относительно значения по умолчанию.

| Переменная | Пример в sample | Default роли |
|---|---|---|
| `cilium_identity_allocation_mode` | `kvstore` | `crd` |
| `cilium_ipam_mode` | `kubernetes` | `cluster-pool` |
| `cilium_bpf_map_dynamic_size_ratio` | `"0.0"` | `"0.0025"` |
| `cilium_enable_host_legacy_routing` | `true` | `false` |
| `cilium_mtu` | `""` | `"0"` |
| `cilium_enable_ipv4` | `true` | `{{ ipv4_stack }}` |
| `cilium_enable_ipv6` | `false` | `{{ ipv6_stack }}` |
| `kube_etcd_cert_file` | `cert.pem` | `node-{{ inventory_hostname }}.pem` |
| `kube_etcd_key_file` | `cert-key.pem` | `node-{{ inventory_hostname }}-key.pem` |
| `cilium_hubble_metrics` | `{}` | `[]` |

### Примечание: переменные, которых нет в defaults роли v2.31.0

Некоторые переменные присутствуют только в sample (как примеры/legacy) и
отсутствуют в `roles/network_plugin/cilium/defaults/main.yml`:

- `cilium_tofqdns_enable_poller` — DEPRECATED (устарело в 1.8, удалено в 1.9);
- `cilium_enable_legacy_services` — DEPRECATED (устарело в 1.6, удалено в 1.9);
- `cilium_ipsec_node_encryption` — в defaults аналог называется
  `cilium_encryption_node_encryption`;
- `cilium_hubble_event_buffer_capacity`, `cilium_hubble_event_queue_size` —
  настраиваемые примеры Hubble только в sample.

## Тематические группы настроек

Файл сгруппирован по разделам (порядок соответствует sample):

- **Базовая сеть**: `cilium_debug`, `cilium_mtu`, `cilium_enable_ipv4`,
  `cilium_enable_ipv6`, `cilium_agent_health_port`, `cilium_tunnel_mode`.
- **L2-анонсирование** (замена MetalLB): `cilium_l2announcements` (единственная
  заданная), `cilium_loadbalancer_ip_pools`.
- **Identity / etcd kvstore**: `cilium_identity_allocation_mode`,
  `cilium_cert_dir`, `kube_etcd_cacert_file`, `kube_etcd_cert_file`,
  `kube_etcd_key_file`.
- **Ресурсы подов**: `cilium_memory_limit`, `cilium_cpu_limit`,
  `cilium_memory_requests`, `cilium_cpu_requests`.
- **LoadBalancer / kube-proxy replacement**: `cilium_loadbalancer_mode`,
  `cilium_kube_proxy_replacement`, `cilium_enable_prometheus`,
  `cilium_enable_portmap`, `cilium_monitor_aggregation(_flags)`,
  `cilium_preallocate_bpf_maps`.
- **Прямая маршрутизация / native routing**: `cilium_auto_direct_node_routes`,
  `cilium_native_routing_cidr(_ipv6)`, `cilium_enable_host_legacy_routing`.
- **Шифрование**: `cilium_encryption_enabled`, `cilium_encryption_type`,
  `cilium_ipsec_node_encryption`, `cilium_wireguard_userspace_fallback`.
- **IP Masquerade Agent**: `cilium_ip_masq_agent_enable`,
  `cilium_non_masquerade_cidrs`, `cilium_masq_link_local`,
  `cilium_ip_masq_resync_interval`.
- **Masquerade (BPF/eBPF)**: `cilium_enable_ipv4_masquerade`,
  `cilium_enable_ipv6_masquerade`, `cilium_enable_bpf_masquerade`.
- **Host Firewall**: `cilium_enable_host_firewall`, `cilium_policy_audit_mode`.
- **Hubble**: `cilium_enable_hubble`, `cilium_enable_hubble_ui`,
  `cilium_enable_hubble_metrics`, `cilium_hubble_metrics`,
  `cilium_hubble_install`, `cilium_hubble_tls_generate`,
  `cilium_hubble_event_buffer_capacity`, `cilium_hubble_event_queue_size`,
  `cilium_hubble_peer_service_cluster_domain`.
- **IPAM**: `cilium_ipam_mode`.
- **Агент**: `cilium_agent_custom_args`, `cilium_agent_extra_volumes`,
  `cilium_agent_extra_volume_mounts`, `cilium_agent_extra_env_vars`.
- **Оператор**: `cilium_operator_replicas`, `cilium_operator_api_serve_addr`,
  `cilium_config_extra_vars`, `cilium_operator_extra_volumes`,
  `cilium_operator_extra_volume_mounts`, `cilium_operator_custom_args`.
- **Cluster Mesh**: `cilium_cluster_id`, `cilium_cluster_name`,
  `cilium_deploy_additionally`.
- **CNI на узле**: `cilium_cni_exclusive`, `cilium_cni_log_file`.
- **cgroup v2**: `cilium_cgroup_auto_mount`, `cilium_cgroup_host_root`,
  `cilium_bpf_map_dynamic_size_ratio`.
- **BGP Control Plane**: `cilium_enable_bgp_control_plane`,
  `cilium_bgp_cluster_configs`, `cilium_bgp_peer_configs`,
  `cilium_bgp_advertisements`, `cilium_bgp_node_config_overrides`,
  `cilium_bgp_peering_policies`.
- **Identity (доп.)**: `cilium_enable_remote_node_identity`,
  `cilium_enable_well_known_identities`, `cilium_disable_cnp_status_updates`.
- **ClusterRole оператора**: `cilium_clusterrole_rules_operator_extra_vars`.
- **Helm-кастомизация**: `cilium_extra_values`.

Полный список всех 82 переменных с дословными значениями-примерами, флагом
`is_set` и комментариями — в
[[versions/v2.31.0/inventory/cni-cilium|cni-cilium.yaml]].

## Непроиндексированные сетевые файлы

В каталоге `inventory/sample/group_vars/k8s_cluster/` присутствуют другие
сетевые файлы CNI. В данном срезе они **не индексируются** (индексируется только
Cilium) и приведены здесь только для полноты:

- `inventory/sample/group_vars/k8s_cluster/k8s-net-calico.yml`
- `inventory/sample/group_vars/k8s_cluster/k8s-net-flannel.yml`
- `inventory/sample/group_vars/k8s_cluster/k8s-net-kube-ovn.yml`
- `inventory/sample/group_vars/k8s_cluster/k8s-net-kube-router.yml`
- `inventory/sample/group_vars/k8s_cluster/k8s-net-macvlan.yml`
- `inventory/sample/group_vars/k8s_cluster/k8s-net-custom-cni.yml`

Основной выбор CNI задаётся переменной `kube_network_plugin` в файле
`inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`; для использования
Cilium она должна быть равна `cilium`.
