---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: code
source_path: versions/v2.30.0/variables/k8s-cluster.yaml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0
retrieved_at: 2026-07-14
topics: [k8s-cluster, control-plane, kubelet, kube-proxy]
reliability: authoritative
---

# Переменные ядра кластера — Kubespray v2.30.0

Заметка описывает ключевые переменные ядра кластера Kubespray на теге `v2.30.0`
(commit `f4ccdb5`). Это человекочитаемая выжимка. **Источник истины — файл
`k8s-cluster.yaml`** в этой же директории: там перечислены все 506 записей переменных
из defaults/ и vars/ соответствующих ролей, с дословными Jinja-значениями и путями.

Проанализированы роли: `kubespray_defaults`, `kubernetes/control-plane`,
`kubernetes/node`, `kubernetes/kubeadm`, `kubernetes/kubeadm_common`,
`kubernetes/preinstall`, `kubernetes/client`. Роли `kubernetes/node-label` и
`kubernetes/node-taint` содержат только `tasks/` (без defaults/vars) и переменных
не дают. Переменные загрузок (`download.yml`) и контрольные суммы вынесены в
отдельные справочники.

## Версии Kubernetes и kubeadm

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `kube_version` | первая (свежая) версия из `kubelet_checksums` | Версия Kubernetes для установки |
| `kube_version_min_required` | последняя версия из `kubelet_checksums` | Минимально поддерживаемая версия |
| `kube_major_version` | `1.<minor>` из `kube_version` | Мажорная версия K8s |
| `kubeadm_config_api_version` | `v1beta4` для K8s ≥ 1.31, иначе `v1beta3` | Версия API конфига kubeadm |
| `kubeadm_init_timeout` | `300s` | Таймаут `kubeadm init` |
| `kubeadm_image_pull_serial` | `true` | Последовательная загрузка образов kubeadm |

## Сеть кластера и CNI

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `kube_network_plugin` | `calico` | CNI-плагин (cilium, calico, kube-ovn, flannel, cni, cloud) |
| `kube_service_addresses` | `10.233.0.0/18` | Сеть service-адресов (IPv4) |
| `kube_pods_subnet` | `10.233.64.0/18` | Сеть адресов подов (IPv4) |
| `kube_network_node_prefix` | `24` | Размер подсети подов на узел |
| `ipv4_stack` | `true` | Включить IPv4-стек |
| `ipv6_stack` | `{{ enable_dual_stack_networks \| default(false) }}` | Включить IPv6-стек |
| `kube_service_addresses_ipv6` | `fd85:ee78:d8a6:8607::1000/116` | Service-сеть IPv6 |
| `kube_pods_subnet_ipv6` | `fd85:ee78:d8a6:8607::1:0000/112` | Pod-сеть IPv6 |
| `kube_proxy_mode` | `ipvs` | Режим kube-proxy (ipvs, iptables, nftables) |
| `enable_network_policy` | `true` | Поддержка NetworkPolicy |
| `calico_datastore` | `kdd` | Хранилище данных Calico (etcd / kdd) |

`kube_service_subnets` и `kube_pods_subnets` (в `kubespray_defaults/vars`) собирают
итоговые подсети с учётом стека (dualstack / ipv6only / ipv4only).

## DNS

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `dns_mode` | `coredns` | Режим DNS (coredns, coredns_dual, manual, none) |
| `cluster_name` / `dns_domain` | `cluster.local` | Имя кластера и DNS-домен |
| `enable_dns_autoscaler` | `true` | Автоскейлер DNS |
| `enable_nodelocaldns` | `true` | NodeLocal DNS Cache |
| `nodelocaldns_ip` | `169.254.25.10` | Link-local IP NodeLocal DNS |
| `upstream_dns_servers` | `[]` | Внешние DNS для CoreDNS |
| `resolvconf_mode` | `host_resolvconf` | Управление resolv.conf |
| `ndots` | `2` | Опция ndots для hostnet-подов |

## API server, controller-manager, scheduler

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `kube_apiserver_port` | `6443` | HTTPS-порт API-сервера |
| `kube_apiserver_bind_address` | `::` | Адрес привязки API-сервера |
| `kube_apiserver_node_port_range` | `30000-32767` | Диапазон портов NodePort |
| `kube_apiserver_storage_backend` | `etcd3` | Backend-хранилище данных |
| `kube_api_anonymous_auth` | `true` | Анонимная аутентификация API |
| `authorization_modes` | `['Node', 'RBAC']` | Режимы авторизации |
| `kube_apiserver_use_authorization_config_file` | `false` | Структурированный AuthorizationConfiguration |
| `kube_apiserver_request_timeout` | `1m0s` | Таймаут запросов к apiserver |
| `event_ttl_duration` | `1h0m0s` | Время хранения событий |
| `kube_controller_node_monitor_grace_period` | `40s` | Grace-период перед NotReady |
| `kube_scheduler_bind_address` | `::` | Адрес привязки scheduler |
| `scheduler_plugins_enabled` | `false` | Плагины планировщика |

## PodSecurity, аудит, шифрование, сертификаты

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `kube_pod_security_use_default` | `false` | Дефолтная конфигурация PodSecurity |
| `kube_pod_security_default_enforce` | `baseline` | Уровень enforce PodSecurity |
| `kubernetes_audit` | `false` | Аудит kube-apiserver |
| `kube_encrypt_secret_data` | `false` | Шифрование Secret'ов в etcd |
| `kube_encryption_algorithm` | `secretbox` | Алгоритм шифрования (aescbc/secretbox/aesgcm) |
| `auto_renew_certificates` | `false` | Автообновление сертификатов control plane |
| `kube_cert_validity_period` | `8760h` | Срок не-CA сертификатов (1 год) |
| `kube_ca_cert_validity_period` | `87600h` | Срок CA-сертификатов (10 лет) |
| `kube_asymmetric_encryption_algorithm` | `RSA-2048` | Алгоритм ключей/сертификатов |
| `kube_external_ca_mode` | `false` | Внешнее управление CA |

## kubelet и резервирование ресурсов

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `kubelet_max_pods` | `110` | Максимум подов на узел |
| `kubelet_rotate_certificates` | `true` | Ротация клиентских сертификатов kubelet |
| `kubelet_protect_kernel_defaults` | `true` | Падать при нестандартных параметрах ядра |
| `kubelet_fail_swap_on` | `true` | Падать при включённом swap |
| `kubelet_swap_behavior` | `LimitedSwap` | Поведение при swap |
| `kube_reserved` | `false` | Резервировать ресурсы под kube |
| `kube_memory_reserved` | `256Mi` | Резерв памяти под kube |
| `system_reserved` | `false` | Резервировать ресурсы под систему |
| `kube_read_only_port` | `0` | Read-only порт kubelet (0 = выкл.) |
| `kubelet_shutdown_grace_period` | `60s` | Период graceful shutdown |
| `kube_resolv_conf` | `/etc/resolv.conf` (на Fedora/Ubuntu → `/run/systemd/resolve/resolv.conf`) | resolv.conf для DNS |

## kube-proxy

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `kube_proxy_mode` | `ipvs` | Режим работы (см. также раздел сети) |
| `kube_proxy_scheduler` | `rr` | IPVS-планировщик (rr, lc, dh, sh, sed, nq) |
| `kube_proxy_strict_arp` | `false` | arp_ignore/arp_announce (нужно для MetalLB/kube-vip) |
| `kube_proxy_masquerade_all` | `false` | SNAT всего трафика (iptables) |
| `kube_proxy_sync_period` | `30s` | Максимальный интервал обновления правил |
| `kube_proxy_metrics_bind_address` | `127.0.0.1:10249` | Адрес метрик kube-proxy |

## etcd

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `etcd_deployment_type` | `host` | Тип развёртывания etcd (legacy-режим) |
| `etcd_events_cluster_enabled` | `false` | Отдельный кластер etcd-events |
| `etcd_data_dir` | `/var/lib/etcd` | Каталог данных etcd |
| `etcd_heartbeat_interval` | `250` | Интервал heartbeat (мс) |
| `etcd_election_timeout` | `5000` | Таймаут выборов лидера (мс) |
| `etcd_snapshot_count` | `100000` | Транзакций между снапшотами |
| `etcd_metrics` | `basic` | Уровень метрик etcd |

## Container runtime

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `container_manager` | `containerd` | Runtime (containerd, crio, docker) |
| `containerd_use_systemd_cgroup` | `true` | systemd cgroup driver |
| `nri_enabled` | `true` при containerd | Node Resource Interface |
| `cri_socket` | зависит от `container_manager` | Путь к CRI-сокету |
| `kata_containers_enabled` / `gvisor_enabled` | `false` | Доп. runtime'ы |

## Балансировщик apiserver и kube-vip

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `loadbalancer_apiserver_type` | `nginx` | Локальный балансировщик (nginx / haproxy) |
| `loadbalancer_apiserver_localhost` | `{{ loadbalancer_apiserver is not defined }}` | Локальный балансировщик, если внешний не задан |
| `kube_vip_enabled` | `false` | Включить kube-vip |
| `kube_vip_arp_enabled` | `false` | ARP-режим kube-vip |
| `kube_vip_controlplane_enabled` | `false` | kube-vip для control plane |

## preinstall (система, NTP, проверки)

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `ntp_enabled` | `false` | Запуск ntpd/chrony |
| `ntp_manage_config` | `false` | Управлять конфигом NTP |
| `minimal_node_memory_mb` | `1024` | Минимум памяти узла (МБ) |
| `minimal_master_memory_mb` | `1500` | Минимум памяти control-plane (МБ) |
| `disable_fapolicyd` | `true` | Отключить fapolicyd (иначе падает CNI) |
| `preinstall_selinux_state` | `permissive` | Целевое состояние SELinux |

## Дублирующиеся переменные

Ряд переменных определён в нескольких ролях (значения совпадают, если не указано
иное). В YAML для каждой указан отдельный `source_path` с пометкой о дублировании.
Ключевые случаи:

- `kube_config_dir`, `kube_cert_dir`, `kube_cert_compat_dir`, `kube_owner`,
  `kube_cert_group` — в `kubespray_defaults` и `preinstall` (и часть в `client`);
- `kubeconfig_localhost`, `kubectl_localhost`, `kube_apiserver_port` — в
  `kubespray_defaults` и `client` (в `client` порт задан **строкой** `"6443"`, а в
  `kubespray_defaults` — числом `6443`);
- `kube_apiserver_bind_address`, `kube_apiserver_node_port_range` — в
  `kubespray_defaults` / `control-plane` / `node`;
- `discovery_timeout` — `5m0s` в `control-plane`, но переопределяется на `60s` в
  `kubeadm` (должен быть меньше `kubeadm_join_timeout`);
- `sysctl_file_path`, `etcd_heartbeat_interval`, `etcd_election_timeout`,
  `kubeadm_use_file_discovery`, `ignore_assert_errors` — в нескольких ролях.

## Полный список

За полным списком всех 506 переменных (все defaults/ и vars/ перечисленных ролей,
с дословными Jinja-значениями, условиями применения и связями) обращайтесь к
`k8s-cluster.yaml` в этой директории.

---

Назад к срезу: [[versions/v2.30.0/README|Срез v2.30.0]]
