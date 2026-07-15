---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: code
source_path: versions/v2.31.0/variables/k8s-cluster.yaml
retrieved_at: 2026-07-14
topics:
  - k8s-cluster
  - control-plane
  - kubelet
  - kube-proxy
reliability: authoritative
---

# Переменные ядра кластера — v2.31.0

Заметка описывает ключевые переменные ядра кластера Kubernetes в Kubespray на теге **v2.31.0** (commit `1c9add4`). Источник истины — машиночитаемый справочник [[versions/v2.31.0/variables/k8s-cluster|k8s-cluster.yaml]] (507 записей). Все значения извлечены строго из кода тега; Jinja-выражения приведены дословно в YAML.

Ссылка на срез версии: [[versions/v2.31.0/README|Срез v2.31.0]].

## Источники (файлы тега v2.31.0)

| Файл | Роль | Кол-во ключей |
| --- | --- | --- |
| `roles/kubespray_defaults/defaults/main/main.yml` | глобальные defaults | 239 |
| `roles/kubespray_defaults/vars/main/main.yml` | внутренние vars (версии, подсети) | 10 |
| `roles/kubernetes/control-plane/defaults/main/main.yml` | control-plane (apiserver, controller-manager, аудит, PKI) | 88 |
| `roles/kubernetes/control-plane/defaults/main/kube-proxy.yml` | kube-proxy | 27 |
| `roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml` | kube-scheduler | 10 |
| `roles/kubernetes/control-plane/defaults/main/etcd.yml` | etcd (control-plane) | 8 |
| `roles/kubernetes/node/defaults/main.yml` | kubelet, kube-vip, резервы ресурсов | 77 |
| `roles/kubernetes/preinstall/defaults/main.yml` | преднастройка, DNS, NTP, ОС | 30 |
| `roles/kubernetes/preinstall/vars/main.yml` | внутренние vars DNS | 6 |
| `roles/kubernetes/kubeadm/defaults/main.yml` | kubeadm join/discovery | 3 |
| `roles/kubernetes/kubeadm_common/defaults/main.yml` | патчи kubeadm | 3 |
| `roles/kubernetes/client/defaults/main.yml` | клиентские артефакты | 6 |

## Версия Kubernetes и базовые идентификаторы

| Переменная | Значение по умолчанию | Назначение |
| --- | --- | --- |
| `kube_version` | `{{ (kubelet_checksums['amd64'] | dict2items)[0].key }}` | версия Kubernetes (старший ключ чек-сумм) |
| `kube_version_min_required` | `{{ (kubelet_checksums['amd64'] | dict2items)[-1].key }}` | минимально поддерживаемая версия |
| `kube_major_version` | `{{ (kube_version | split('.'))[:-1] | join('.') }}` | мажорная версия (1.x) |
| `cluster_name` | `cluster.local` | имя кластера и DNS-домен |
| `dns_domain` | `{{ cluster_name }}` | DNS-домен кластера |

## Сеть кластера

| Переменная | Значение по умолчанию | Назначение |
| --- | --- | --- |
| `kube_network_plugin` | `calico` | CNI-плагин (cilium, calico, kube-ovn, flannel, cni, cloud) |
| `kube_service_addresses` | `10.233.0.0/18` | подсеть сервисов (IPv4) |
| `kube_pods_subnet` | `10.233.64.0/18` | подсеть подов (IPv4) |
| `kube_network_node_prefix` | `24` | размер подсети подов на узел |
| `kube_service_addresses_ipv6` | `fd85:ee78:d8a6:8607::1000/116` | подсеть сервисов (IPv6) |
| `kube_pods_subnet_ipv6` | `fd85:ee78:d8a6:8607::1:0000/112` | подсеть подов (IPv6) |
| `ipv4_stack` | `true` | включение IPv4-стека |
| `ipv6_stack` | `{{ enable_dual_stack_networks | default(false) }}` | включение IPv6-стека |
| `kube_apiserver_ip` | первый IP первой service-подсети | cluster IP API-сервера |
| `kube_apiserver_port` | `6443` | HTTPS-порт API-сервера |

## kube-apiserver и авторизация

| Переменная | Значение по умолчанию | Назначение |
| --- | --- | --- |
| `kube_apiserver_bind_address` | `::` | адрес привязки apiserver |
| `kube_apiserver_node_port_range` | `30000-32767` | диапазон NodePort |
| `authorization_modes` | `['Node', 'RBAC']` | режимы авторизации |
| `kube_apiserver_use_authorization_config_file` | `false` | структурированная AuthorizationConfiguration (GA в 1.32) |
| `kube_apiserver_use_authentication_config_file` | `false` | структурированная AuthenticationConfiguration (GA в 1.34) |
| `kube_api_anonymous_auth` | `true` | анонимная аутентификация |
| `kube_encrypt_secret_data` | `false` | шифрование Secret'ов at rest |
| `kube_encryption_algorithm` | `secretbox` | алгоритм шифрования (aescbc/secretbox/aesgcm) |
| `kubernetes_audit` | `false` | аудит API-сервера |

## kubelet и резервирование ресурсов

| Переменная | Значение по умолчанию | Назначение |
| --- | --- | --- |
| `kubelet_max_pods` | `110` | максимум подов на узел |
| `kube_reserved` | `false` | резервировать ресурсы для kube |
| `kube_memory_reserved` | `256Mi` | резерв памяти kube |
| `kube_cpu_reserved` | `100m` | резерв CPU kube |
| `system_reserved` | `false` | резерв ресурсов для системных демонов |
| `kubelet_fail_swap_on` | `true` | падать при включённом swap |
| `kubelet_fail_cgroup_v1` | `true` | падать при cgroup v1 (k8s 1.35+) |
| `kubelet_rotate_certificates` | `true` | ротация клиентских сертификатов kubelet |

## kube-proxy

| Переменная | Значение по умолчанию | Назначение |
| --- | --- | --- |
| `kube_proxy_mode` | `ipvs` | режим (ipvs/iptables/nftables) |
| `kube_proxy_scheduler` | `rr` | планировщик IPVS |
| `kube_proxy_strict_arp` | `false` | arp_ignore/arp_announce (нужно для MetalLB, kube-vip) |
| `kube_proxy_masquerade_all` | `false` | SNAT всего трафика (режим iptables) |
| `kube_proxy_metrics_bind_address` | `127.0.0.1:10249` | адрес метрик |

## etcd (адресация и параметры)

| Переменная | Значение по умолчанию | Назначение |
| --- | --- | --- |
| `etcd_deployment_type` | `host` | тип развёртывания (host/docker) |
| `etcd_events_cluster_enabled` | `false` | отдельный кластер etcd-events |
| `etcd_heartbeat_interval` | `"250"` | интервал heartbeat (мс) |
| `etcd_election_timeout` | `"5000"` | таймаут выборов лидера (мс) |
| `etcd_metrics` | `basic` | уровень метрик |

## Container runtime

| Переменная | Значение по умолчанию | Назначение |
| --- | --- | --- |
| `container_manager` | `containerd` | runtime (containerd/crio/docker) |
| `containerd_use_systemd_cgroup` | `true` | systemd cgroup driver |
| `cri_socket` | зависит от `container_manager` | путь к CRI-сокету |
| `nri_enabled` | `{{ container_manager == 'containerd' }}` | NRI-плагин для containerd |

## Важные нюансы и переопределения между ролями

Ряд переменных определён более чем в одном файле defaults. При совпадении значения различий нет; ниже отмечены случаи, где значение **отличается** или где переопределение существенно:

- **`discovery_timeout`** — `5m0s` в `control-plane/defaults/main/main.yml`, но **`60s`** в `kubeadm/defaults/main.yml`. В рамках роли `kubeadm` действует значение `60s` (оно должно быть меньше `kubeadm_join_timeout: 120s`).
- **`kube_apiserver_port`** — `6443` (число) в `kubespray_defaults`, `"6443"` (строка) в `client/defaults`.
- **`kube_apiserver_bind_address`** — `::` задан и в `kubespray_defaults`, и в `control-plane` (значения совпадают).
- **`kube_proxy_nodeport_addresses`** — идентичный Jinja-блок в `kubespray_defaults` и `kube-proxy.yml`.
- Дубли-константы с совпадающими значениями: `kube_config_dir`, `kube_cert_dir`, `kube_cert_compat_dir`, `kube_owner`, `kube_cert_group`, `sysctl_file_path`, `kube_apiserver_node_port_range`, `etcd_heartbeat_interval`, `etcd_election_timeout`, `ignore_assert_errors`, `kubeconfig_localhost`, `kubectl_localhost`, `kubeadm_use_file_discovery`.

Согласно разделу 6.2 CLAUDE.md, при расхождении значений приоритет у кода роли, применяемой в соответствующем контексте; расхождения (прежде всего `discovery_timeout`) зафiксированы отдельно в `discrepancies.md` среза.
