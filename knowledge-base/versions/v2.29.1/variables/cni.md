---
project: kubespray
kubespray_version: v2.29.1
git_commit: 0c6a295
source_type: code
source_path: versions/v2.29.1/variables/cni.yaml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.29.1
retrieved_at: 2026-07-14
topics:
  - cni
  - cilium
  - network
reliability: authoritative
---

# Переменные CNI в Kubespray v2.29.1

Обзорная заметка по переменным сетевой подсистемы (CNI) для тега `v2.29.1` (коммит `0c6a295`).
**Источник истины — YAML-справочник** [[versions/v2.29.1/variables/cni|cni.yaml]] (131 переменная); эта заметка — его человекочитаемое изложение.
Срез версии: [[versions/v2.29.1/README|Срез v2.29.1]].

Ограничение проекта: из сетевых плагинов проиндексирован **только Cilium**. Список непроиндексированных ролей — в конце заметки.

## Как выбирается CNI

Плагин выбирается переменной `kube_network_plugin` (по умолчанию `calico`, задаётся в `roles/kubespray_defaults/defaults/main/main.yml`). Подключение ролей происходит через зависимости мета-роли `roles/network_plugin/meta/main.yml`:

- `network_plugin/cni` подключается всегда, кроме `kube_network_plugin: 'none'` — раскладывает базовые CNI-бинарники (`containernetworking/plugins`) в `/opt/cni/bin`;
- `network_plugin/cilium` подключается при `kube_network_plugin == 'cilium'` **или** при `cilium_deploy_additionally: true` (Ansible-тег `cilium`);
- остальные роли (`calico`, `flannel`, `macvlan`, `kube-ovn`, `kube-router`, `custom_cni`) подключаются по совпадению значения `kube_network_plugin`;
- `network_plugin/multus` подключается по отдельному флагу `kube_network_plugin_multus` поверх основного плагина.

Полный справочник переменных ядра кластера (включая `kube_pods_subnet`, `kube_network_node_prefix` и т.п.) — в `k8s-cluster.yaml`; здесь из ядра приведены только переменные, непосредственно относящиеся к CNI.

| Переменная | Значение по умолчанию | Назначение |
| --- | --- | --- |
| `kube_network_plugin` | `calico` | выбор сетевого плагина (cilium, calico, kube-ovn, flannel, cni, cloud) |
| `kube_network_plugin_multus` | `false` | Multus поверх основного CNI |
| `cilium_deploy_additionally` | `false` | развернуть Cilium рядом с другим CNI (например, только для замены kube-proxy) |
| `cni_bin_owner` | `{{ kube_owner }}` | владелец `/opt/cni/bin` |
| `cni_version` | `{{ (cni_binary_checksums['amd64'] \| dict2items)[0].key }}` | версия containernetworking/plugins |

## Как разворачивается Cilium в v2.29.1

В этом теге Cilium разворачивается **через cilium-cli по helm-values**, а не через статические манифесты:

1. `tasks/check.yml` — проверки (версия >= `cilium_min_version_required` = 1.15, корректность режимов, наличие `cilium_ipsec_key` для ipsec);
2. `tasks/install.yml` — монтирование BPFFS, при `kvstore` линковка etcd-сертификатов, рендер `values.yaml.j2` в `cilium-values.yaml` и `cilium_extra_values` в `cilium-extra-values.yaml`, копирование бинарника `cilium` (cilium-cli);
3. `tasks/apply.yml` — `cilium install|upgrade --version {{ cilium_version }} -f cilium-values.yaml -f cilium-extra-values.yaml {{ cilium_install_extra_flags }}`, ожидание готовности подов, применение CRD-манифестов (LB IP pools, BGP).

Роль `roles/kubernetes-apps/` в этом теге **не содержит** cilium-задач (каталога `kubernetes-apps/network_plugin` нет) — развёртывание целиком в `roles/network_plugin/cilium/`.

Важное следствие перехода на helm-values: заметная часть переменных в `defaults/main.yml` роли осталась от прежней (манифестной) схемы и **в этом теге нигде не используется** — в YAML-справочнике такие переменные помечены `reliability: unconfirmed` с пояснением. Примеры: `cilium_memory_limit`/`cilium_cpu_limit`/`cilium_memory_requests`/`cilium_cpu_requests`, `cilium_enable_prometheus`, `cilium_*_scrape_port`, `cilium_certgen_args`, `cilium_hubble_install`, `cilium_hubble_tls_generate`, `cilium_monitor_aggregation_flags`, `cilium_enable_bpf_clock_probe`, `cilium_enable_remote_node_identity`, `cilium_enable_well_known_identities`, `cilium_disable_cnp_status_updates`, `cilium_operator_api_serve_addr`, `cilium_agent_custom_args`, `cilium_operator_custom_args`, `cilium_agent_extra_env_vars`, `cilium_wireguard_userspace_fallback`. Ресурсы и прочие тонкие настройки теперь задаются через `cilium_extra_values`.

## Версия и образы

| Переменная | Значение по умолчанию |
| --- | --- |
| `cilium_version` | `1.18.4` |
| `cilium_cli_version` | `{{ (ciliumcli_binary_checksums['amd64'] \| dict2items)[0].key }}` |
| `cilium_image_repo` | `{{ quay_image_repo }}/cilium/cilium` |
| `cilium_image_tag` | `v{{ cilium_version }}` |
| `cilium_operator_image_repo` / `_tag` | `{{ quay_image_repo }}/cilium/operator` / `v{{ cilium_version }}` |
| `cilium_hubble_relay_image_repo` / `_tag` | `{{ quay_image_repo }}/cilium/hubble-relay` / `v{{ cilium_version }}` |
| `cilium_hubble_ui_image_*`, `cilium_hubble_ui_backend_image_*` | hubble-ui `v0.13.3` |
| `cilium_hubble_certgen_image_*` | certgen `v0.2.4` |
| `cilium_hubble_envoy_image_*` | cilium-envoy `v1.34.10-...` |

Все версии/образы задаются в `roles/kubespray_defaults/defaults/main/download.yml`. Минимально допустимая версия — `cilium_min_version_required: "1.15"`.

## Туннелирование и нативная маршрутизация

| Переменная | По умолчанию | Назначение |
| --- | --- | --- |
| `cilium_tunnel_mode` | `vxlan` | режим overlay (`tunnelProtocol`); `disabled` — нативная маршрутизация |
| `cilium_auto_direct_node_routes` | `false` | прямые маршруты между узлами без туннеля (нужна L2-связность) |
| `cilium_native_routing_cidr` | `""` | IPv4 CIDR, в который трафик уходит без SNAT |
| `cilium_native_routing_cidr_ipv6` | `""` | то же для IPv6 |
| `cilium_enable_host_legacy_routing` | `false` | direct-routing через хостовый стек вместо BPF |
| `cilium_mtu` | `"0"` | MTU (0 — автоопределение) |

Для нативной маршрутизации: `cilium_tunnel_mode: disabled` + заданный `cilium_native_routing_cidr` (+ при необходимости `cilium_auto_direct_node_routes: true`).

## Замена kube-proxy

| Переменная | По умолчанию | Назначение |
| --- | --- | --- |
| `cilium_kube_proxy_replacement` | `false` | замена kube-proxy средствами Cilium |
| `cilium_loadbalancer_mode` | `snat` | режим балансировщика: snat / dsr / hybrid |
| `cilium_loadbalancer_ip_pools` | `[]` | пулы CiliumLoadBalancerIPPool |
| `cilium_l2announcements` | `false` | L2-анонсы (замена MetalLB) |
| `cilium_dns_proxy_enable_transparent_mode` | не задана | явное управление dnsProxy; `false` — обход конфликта с nodelocaldns |

Зависимости в ядре Kubespray (`roles/kubespray_defaults/defaults/main/main.yml`):

- при `kube_network_plugin == 'cilium'` и включённом `cilium_kube_proxy_replacement` переменная `kubeadm_init_phases_skip` автоматически дополняется фазой `addon/kube-proxy` — kube-proxy не устанавливается;
- тот же эффект даёт `kube_proxy_remove: true` (переменная ядра, в defaults тега не объявлена — проверяется через `is defined`);
- `cilium_deploy_additionally: true` позволяет добавить Cilium к другому CNI именно ради замены kube-proxy;
- при `cilium_kube_proxy_replacement: true` Cilium автоматически включает dnsProxy, что конфликтует с nodelocaldns — лечится `cilium_dns_proxy_enable_transparent_mode: false` (комментарий в defaults, upstream issue cilium/cilium#33144).

## Hubble

| Переменная | По умолчанию | Назначение |
| --- | --- | --- |
| `cilium_enable_hubble` | `false` | включить Hubble и hubble-relay |
| `cilium_enable_hubble_ui` | `{{ cilium_enable_hubble }}` | включить Hubble UI |
| `cilium_hubble_metrics` | `[]` | список метрик (dns, drop, tcp, flow, icmp, http) |
| `cilium_hubble_export_file_max_backups` | `"5"` | ротация файла экспорта событий |
| `cilium_hubble_export_file_max_size_mb` | `"10"` | размер файла экспорта |
| `cilium_hubble_export_dynamic_enabled` | `false` | динамический экспорт событий |
| `cilium_hubble_peer_service_cluster_domain` | `{{ dns_domain }}` | DNS-суффикс peer-сервиса hubble-relay |
| `cilium_hubble_event_buffer_capacity` | не задана (upstream 4095) | ёмкость буфера событий; валидируется, но в values не рендерится |

Обратите внимание: `cilium_enable_hubble` объявлена дважды с одинаковым значением — в defaults роли и в `roles/kubespray_defaults/defaults/main/download.yml` (там она управляет скачиванием hubble-образов). Флаг `cilium_enable_hubble_metrics` помечен deprecated и в шаблоне не используется — метрики включаются самим списком `cilium_hubble_metrics`.

## IPAM

| Переменная | По умолчанию | Назначение |
| --- | --- | --- |
| `cilium_ipam_mode` | `cluster-pool` | режим IPAM (Cluster Scope) |
| `cilium_pool_cidr` | не задана → `kube_pods_subnet` | IPv4 CIDR пула подов |
| `cilium_pool_cidr_ipv6` | не задана → `kube_pods_subnet_ipv6` | IPv6 CIDR пула подов |
| `cilium_pool_mask_size` | не задана → `kube_network_node_prefix` | префикс на узел (IPv4) |
| `cilium_pool_mask_size_ipv6` | не задана → `kube_network_node_prefix_ipv6` | префикс на узел (IPv6) |
| `cilium_enable_ipv4` / `cilium_enable_ipv6` | `{{ ipv4_stack }}` / `{{ ipv6_stack }}` | включение стеков, следуют общекластерным флагам |

Предупреждение из комментариев кода: если сеть узлов пересекается с `cilium_pool_cidr` (по умолчанию `kube_pods_subnet`), возможна потеря связности между узлами.

## Шифрование

| Переменная | По умолчанию | Назначение |
| --- | --- | --- |
| `cilium_encryption_enabled` | `false` | прозрачное шифрование трафика |
| `cilium_encryption_type` | `"ipsec"` | ipsec или wireguard |
| `cilium_ipsec_key` | не задана | обязательна при ipsec (assert в check.yml) |
| `cilium_encryption_node_encryption` | `false` | node-to-node шифрование (только wireguard) |

WireGuard требует ядро >= 5.6.0 (assert в check.yml). Устаревший `cilium_ipsec_enabled: true` принудительно включает режим ipsec.

## Ресурсы и прочее

- `cilium_operator_replicas: 2`, `cilium_operator_tolerations: [{operator: Exists}]`;
- лимиты/реквесты (`cilium_memory_limit` и др.) в этом теге **не действуют** — задавайте ресурсы через `cilium_extra_values`;
- произвольные helm-values — `cilium_extra_values: {}`, дополнительные ключи cilium-config — `cilium_config_extra_vars: {}`;
- ожидание готовности: `cilium_rolling_restart_wait_retries_count: 30` x `cilium_rolling_restart_wait_retries_delay_seconds: 10`;
- BGP: новый bgpv2 API (`cilium_bgp_cluster_configs`, `cilium_bgp_peer_configs`, `cilium_bgp_advertisements`, `cilium_bgp_node_config_overrides`) и legacy `cilium_bgp_peering_policies`; включение control plane — `cilium_enable_bgp_control_plane`;
- identity: `cilium_identity_allocation_mode: crd`; режим `kvstore` требует etcd-сертификатов (`cilium_cert_dir`, `kube_etcd_*_file`);
- безопасность: `cilium_enable_host_firewall`, `cilium_policy_audit_mode`; hostPort — `cilium_enable_portmap`; Gateway API — `cilium_gateway_api_enabled`.

## Непроиндексированные сетевые плагины тега

В `roles/network_plugin/` тега v2.29.1 существуют, но по ограничению проекта **не проиндексированы**: `calico`, `calico_defaults`, `flannel`, `kube-ovn`, `kube-router`, `macvlan`, `multus`, `custom_cni`, `ovn4nfv`.

## Источники

- `roles/network_plugin/cilium/defaults/main.yml`
- `roles/network_plugin/cilium/tasks/` (`check.yml`, `install.yml`, `apply.yml`, `main.yml`)
- `roles/network_plugin/cilium/templates/values.yaml.j2`
- `roles/network_plugin/cni/defaults/main.yml`, `roles/network_plugin/cni/tasks/main.yml`
- `roles/network_plugin/meta/main.yml`
- `roles/kubespray_defaults/defaults/main/main.yml`, `roles/kubespray_defaults/defaults/main/download.yml`
