---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: inventory
source_path: inventory/sample/group_vars/k8s_cluster/k8s-net-cilium.yml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0
retrieved_at: 2026-07-14
topics:
  - inventory
  - cni
  - cilium
reliability: authoritative
---

# Sample inventory: настройки Cilium (v2.30.0)

Разбор файла `inventory/sample/group_vars/k8s_cluster/k8s-net-cilium.yml` тега **v2.30.0** (commit `f4ccdb5`).

Источник истины — YAML-справочник [[versions/v2.30.0/inventory/cni-cilium|cni-cilium.yaml]]. Данная заметка — человекочитаемое представление на русском.

Связь: [[versions/v2.30.0/README|Срез v2.30.0]].

## Обзор

Файл содержит **83 переменные** конфигурации Cilium, сгруппированные по функциональным разделам. Это шаблонный (sample) файл: почти всё в нём **закомментировано** и приведено как пример со значением по умолчанию.

- **Фактически задана (раскомментирована) только 1 переменная:** `cilium_l2announcements: false`.
- **Закомментировано (пример, `is_set: false`): 82 переменные.**

Таким образом, при использовании sample-inventory «как есть» пользователь опирается на значения по умолчанию из роли `roles/network_plugin/cilium/defaults/main.yml`, а sample лишь документирует доступные ключи.

Из CNI в базе знаний индексируется **только Cilium**. Прочие сетевые файлы sample-inventory перечислены ниже без разбора.

## Заданные переменные

| Переменная | Значение в sample | Значение по умолчанию (роль) | Расхождение |
|---|---|---|---|
| `cilium_l2announcements` | `false` | `false` | нет |

Проверка расхождений по разделу 6.2 CLAUDE.md выполнена: единственная заданная переменная совпадает с ролевым default, расхождений нет (`discrepancies: []`).

## Переменные по разделам (закомментированные примеры)

### Общие: отладка и MTU

| Переменная | Пример значения | Смысл |
|---|---|---|
| `cilium_debug` | `false` | Уровень логирования / режим отладки агента. |
| `cilium_mtu` | `""` | MTU сети Cilium; пусто — автоопределение. |

### IPv4 / IPv6

| Переменная | Пример значения | Смысл |
|---|---|---|
| `cilium_enable_ipv4` | `true` | Поддержка IPv4. |
| `cilium_enable_ipv6` | `false` | Поддержка IPv6. |

### Health и идентичности

| Переменная | Пример значения | Смысл |
|---|---|---|
| `cilium_agent_health_port` | `"9879"` | Порт health-проверки агента. |
| `cilium_identity_allocation_mode` | `kvstore` | Режим выделения идентичностей: `crd` или `kvstore`. Для внешних нагрузок требуется `crd`. |

### SSL-каталоги etcd

| Переменная | Пример значения | Смысл |
|---|---|---|
| `cilium_cert_dir` | `/etc/cilium/certs` | Каталог SSL-сертификатов Cilium для etcd. |
| `kube_etcd_cacert_file` | `ca.pem` | Имя файла CA-сертификата etcd. |
| `kube_etcd_cert_file` | `cert.pem` | Имя файла клиентского сертификата etcd. |
| `kube_etcd_key_file` | `cert-key.pem` | Имя файла приватного ключа клиента etcd. |

### Лимиты ресурсов

| Переменная | Пример значения | Смысл |
|---|---|---|
| `cilium_memory_limit` | `500M` | Лимит памяти подов Cilium. |
| `cilium_cpu_limit` | `500m` | Лимит CPU подов Cilium. |
| `cilium_memory_requests` | `64M` | Запрос памяти (requests). |
| `cilium_cpu_requests` | `100m` | Запрос CPU (requests). |

### Режим оверлея и балансировка нагрузки

| Переменная | Пример значения | Смысл |
|---|---|---|
| `cilium_tunnel_mode` | `vxlan` | Режим туннелирования (vxlan/geneve/disabled). |
| `cilium_loadbalancer_mode` | `snat` | Режим LoadBalancer: snat/dsr/hybrid. |

### Опциональные функции

| Переменная | Пример значения | Смысл |
|---|---|---|
| `cilium_enable_prometheus` | `false` | Экспорт метрик Prometheus. |
| `cilium_enable_portmap` | `false` | Поддержка hostPort через portmap. |
| `cilium_monitor_aggregation` | `medium` | Уровень агрегации монитора: none/low/medium/maximum. |
| `cilium_monitor_aggregation_flags` | `"all"` | Флаги TCP для уведомлений монитора (при агрегации medium+). |
| `cilium_kube_proxy_replacement` | `false` | Замена kube-proxy средствами Cilium. |
| `cilium_preallocate_bpf_maps` | `false` | Предвыделение BPF-карт (актуально при апгрейде с Cilium < 1.5). |

### Устаревшие опции

| Переменная | Пример значения | Смысл |
|---|---|---|
| `cilium_tofqdns_enable_poller` | `false` | УСТАРЕЛО в 1.8, удалено в 1.9. Поллер ToFQDNs. |
| `cilium_enable_legacy_services` | `false` | УСТАРЕЛО в 1.6, удалено в 1.9. Старый формат сервисов. |

### Кластер-меш

| Переменная | Пример значения | Смысл |
|---|---|---|
| `cilium_cluster_id` | (без значения) | Уникальный ID кластера (1–255), по умолчанию не задан. Только для меша. |
| `cilium_deploy_additionally` | `false` | Развёртывание Cilium рядом с другим CNI ради замены kube-proxy. |
| `cilium_cluster_name` | `default` | Имя кластера. Только для меша. |

### Прямая маршрутизация и native routing CIDR

| Переменная | Пример значения | Смысл |
|---|---|---|
| `cilium_auto_direct_node_routes` | `false` | Автоанонс маршрутов подов без туннелирования (требует L2 и `cilium_native_routing_cidr`). |
| `cilium_native_routing_cidr` | `""` | IPv4 CIDR для native routing (трафик без SNAT). |
| `cilium_native_routing_cidr_ipv6` | `""` | IPv6 CIDR для native routing. |

### Шифрование

| Переменная | Пример значения | Смысл |
|---|---|---|
| `cilium_encryption_enabled` | `false` | Прозрачное шифрование трафика. |
| `cilium_encryption_type` | `"ipsec"` | Метод: ipsec или wireguard (при enabled=true). |
| `cilium_ipsec_node_encryption` | `false` | Шифрование трафика узел-узел (только для ipsec). |
| `cilium_wireguard_userspace_fallback` | `false` | Fallback на wireguard-go, если ядро без WireGuard (только для wireguard). |

### IP Masquerade Agent

| Переменная | Пример значения | Смысл |
|---|---|---|
| `cilium_ip_masq_agent_enable` | `false` | Включение IP Masquerade Agent. |
| `cilium_non_masquerade_cidrs` | список CIDR | CIDR, трафик в которые не маскируется. |
| `cilium_masq_link_local` | `false` | Маскировать ли link-local; при false 169.254.0.0/16 добавляется в non-masquerade. |
| `cilium_ip_masq_resync_interval` | `60s` | Интервал перечитывания конфигурации с диска. |

### Host Firewall и Policy Audit

| Переменная | Пример значения | Смысл |
|---|---|---|
| `cilium_enable_host_firewall` | `false` | Host firewall Cilium. |
| `cilium_policy_audit_mode` | `false` | Режим аудита политик без блокирования. |

### Hubble

| Переменная | Пример значения | Смысл |
|---|---|---|
| `cilium_enable_hubble` | `false` | Включение Hubble без установки. |
| `cilium_enable_hubble_ui` | `"{{ cilium_enable_hubble }}"` | Hubble UI; по умолчанию наследует `cilium_enable_hubble`. |
| `cilium_enable_hubble_metrics` | `false` | Метрики Hubble. |
| `cilium_hubble_metrics` | `{}` | Набор метрик (dns, drop, tcp, flow, icmp, http). |
| `cilium_hubble_install` | `false` | Установка Hubble. |
| `cilium_hubble_tls_generate` | `false` | Автогенерация сертификатов (при install=true). |
| `cilium_hubble_event_buffer_capacity` | `4095` | Ёмкость буфера событий (на 1 меньше степени двойки, ≤65535). |
| `cilium_hubble_event_queue_size` | `50` | Размер канала приёма событий монитора. |
| `cilium_hubble_peer_service_cluster_domain` | `"{{ dns_domain }}"` | DNS-суффикс для резолва peer-сервиса Hubble-Relay. |

### IPAM

| Переменная | Пример значения | Смысл |
|---|---|---|
| `cilium_ipam_mode` | `kubernetes` | Режим управления IP-адресами (v1.9+). |

### Дополнительные аргументы и тома агента

| Переменная | Пример значения | Смысл |
|---|---|---|
| `cilium_agent_custom_args` | `[]` | Доп. аргументы командной строки агента. |
| `cilium_agent_extra_volumes` | `[]` | Доп. тома в под агента. |
| `cilium_agent_extra_volume_mounts` | `[]` | Точки монтирования доп. томов агента. |
| `cilium_agent_extra_env_vars` | `[]` | Доп. переменные окружения агента. |

### Cilium Operator

| Переменная | Пример значения | Смысл |
|---|---|---|
| `cilium_operator_replicas` | `2` | Число реплик cilium-operator. |
| `cilium_operator_api_serve_addr` | `"127.0.0.1:9234"` | Адрес health-check API оператора. |
| `cilium_config_extra_vars` | `{}` | Доп. параметры в cilium-config. |
| `cilium_operator_extra_volumes` | `[]` | Доп. тома в под оператора. |
| `cilium_operator_extra_volume_mounts` | `[]` | Точки монтирования доп. томов оператора. |
| `cilium_operator_custom_args` | `[]` | Доп. аргументы командной строки оператора. |
| `cilium_clusterrole_rules_operator_extra_vars` | `[]` | Доп. правила clusterrole оператора. |

### CNI: эксклюзивность и логирование

| Переменная | Пример значения | Смысл |
|---|---|---|
| `cilium_cni_exclusive` | `true` | Cilium забирает `/etc/cni/net.d`, переименовывая чужие конфиги в `*.cilium_bak` (v1.10+). |
| `cilium_cni_log_file` | `"/var/run/cilium/cilium-cni.log"` | Файл логов CNI (7 дней); пусто — отключить (v1.12+). |

### cgroup

| Переменная | Пример значения | Смысл |
|---|---|---|
| `cilium_cgroup_auto_mount` | `true` | Автомонтирование cgroup2 (v1.11+). |
| `cilium_cgroup_host_root` | `"/run/cilium/cgroupv2"` | Путь монтирования cgroup2 на хосте. |

### BPF

| Переменная | Пример значения | Смысл |
|---|---|---|
| `cilium_bpf_map_dynamic_size_ratio` | `"0.0"` | Доля памяти системы под динамический размер BPF-карт. |

### Masquerade (eBPF)

| Переменная | Пример значения | Смысл |
|---|---|---|
| `cilium_enable_ipv4_masquerade` | `true` | Маскировка IPv4-трафика от эндпоинтов (v1.10+). |
| `cilium_enable_ipv6_masquerade` | `true` | Маскировка IPv6-трафика от эндпоинтов (v1.10+). |
| `cilium_enable_bpf_masquerade` | `false` | Нативная IP-маскировка в eBPF. |

### BGP Control Plane

| Переменная | Пример значения | Смысл |
|---|---|---|
| `cilium_enable_bgp_control_plane` | `false` | Включение BGP Control Plane. |
| `cilium_loadbalancer_ip_pools` | список пулов | Пулы IP-адресов LoadBalancer (name/cidrs/ranges). |
| `cilium_bgp_cluster_configs` | список | BGP-инстансы (bgpv2 API v1.16+). |
| `cilium_bgp_peer_configs` | список | BGP-пиры (bgpv2 API v1.16+). |
| `cilium_bgp_advertisements` | список | BGP-анонсы (bgpv2 API v1.16+). |
| `cilium_bgp_node_config_overrides` | список | Переопределения BGP на уровне узла (bgpv2 API v1.16+). |
| `cilium_bgp_peering_policies` | список | BGP-пиры в устаревшем формате (Legacy v1.16+). |

### Маршрутизация и идентичности

| Переменная | Пример значения | Смысл |
|---|---|---|
| `cilium_enable_host_legacy_routing` | `true` | Direct routing через host stack (true) или напрямую через BPF (false). |
| `cilium_enable_remote_node_identity` | `true` | Использование remote node identity. |
| `cilium_enable_well_known_identities` | `false` | Использование well-known identities. |
| `cilium_enable_bpf_clock_probe` | `true` | BPF clock probe. |
| `cilium_disable_cnp_status_updates` | `true` | Отключение обновлений статуса CiliumNetworkPolicy. |

### Extra values

| Переменная | Пример значения | Смысл |
|---|---|---|
| `cilium_extra_values` | `{}` | Произвольные значения из Helm Chart Cilium. |

## Непроиндексированные сетевые файлы sample-inventory

Индексируется только Cilium. Остальные сетевые файлы из `inventory/sample/group_vars/k8s_cluster/` не разбираются:

- `k8s-net-calico.yml`
- `k8s-net-flannel.yml`
- `k8s-net-kube-ovn.yml`
- `k8s-net-kube-router.yml`
- `k8s-net-macvlan.yml`
- `k8s-net-custom-cni.yml`
