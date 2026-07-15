---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: inventory
source_paths:
  - inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
  - inventory/sample/group_vars/k8s_cluster/kube_control_plane.yml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0
retrieved_at: 2026-07-14
topics:
  - inventory
  - k8s-cluster
  - control-plane
reliability: authoritative
---

# Sample-inventory: k8s-cluster.yml + kube_control_plane.yml (v2.30.0)

Разбор двух файлов group_vars группы `k8s_cluster` тега v2.30.0 (commit `f4ccdb5`). Источник истины — [[versions/v2.30.0/inventory/k8s-cluster|k8s-cluster.yaml]]. Ссылка на срез: [[versions/v2.30.0/README|Срез v2.30.0]].

## Обзор

`k8s-cluster.yml` — основной файл настроек ядра кластера (сеть, DNS, API-сервер, kube-proxy, container runtime, kubelet, сертификаты). `kube_control_plane.yml` — переопределения резервирования ресурсов только для узлов control plane; в sample все его переменные закомментированы.

В файле k8s-cluster.yml **57 переменных заданы явно** (раскомментированы) и **72 приведены как закомментированные примеры**. В kube_control_plane.yml все 8 переменных закомментированы. Расхождений раскомментированных значений с defaults ролей не обнаружено — см. [[versions/v2.30.0/inventory/discrepancies|discrepancies]] (пустой список).

## Ключевые реально заданные настройки (is_set: true)

| Переменная | Значение | Назначение |
|---|---|---|
| `kube_network_plugin` | `calico` | CNI по умолчанию |
| `kube_service_addresses` | `10.233.0.0/18` | Сеть service-адресов |
| `kube_pods_subnet` | `10.233.64.0/18` | Сеть подов |
| `kube_network_node_prefix` | `24` | Размер подсети на узел |
| `kube_apiserver_port` | `6443` | HTTPS-порт API |
| `kube_proxy_mode` | `ipvs` | Режим kube-proxy |
| `kube_proxy_strict_arp` | `false` | ARP-режим (нужен true для MetalLB/kube-vip) |
| `container_manager` | `containerd` | Container runtime |
| `dns_mode` | `coredns` | Режим кластерного DNS |
| `cluster_name` | `cluster.local` | Имя кластера и DNS-домен |
| `enable_nodelocaldns` | `true` | NodeLocal DNS Cache |
| `resolvconf_mode` | `host_resolvconf` | Управление resolv.conf |
| `kube_owner` | `kube` | Владелец установки (для cilium нужен root) |
| `kube_log_level` | `2` | Уровень логирования |
| `k8s_image_pull_policy` | `IfNotPresent` | imagePullPolicy |
| `event_ttl_duration` | `1h0m0s` | Хранение событий |
| `auto_renew_certificates` | `false` | Автообновление сертификатов control plane |
| `remove_anonymous_access` | `false` | Удаление привязки к анонимным пользователям |

## IPv6 / dual-stack

Переменные `kube_service_addresses_ipv6`, `kube_pods_subnet_ipv6`, `kube_network_node_prefix_ipv6` заданы явно, но, согласно комментариям файла, применяются **только при `ipv6_stack: true`** (который в defaults берётся из устаревшей `enable_dual_stack_networks`).

## Заметные закомментированные блоки

- **OIDC / webhook auth** — `kube_oidc_*`, `kube_webhook_*`: методы аутентификации и авторизации, по умолчанию выключены.
- **Резервирование ресурсов** — `kube_reserved`, `system_reserved` и связанные `*_reserved`: в k8s-cluster.yml приведены примеры (kube: 256Mi/100m, system: 512Mi/500m).
- **NVIDIA GPU** — `nvidia_*`: установка драйверов и device plugin.
- **Graceful shutdown** — `kubelet_shutdown_grace_period` (60s) и `..._critical_pods` (20s).
- **TLS** — `tls_min_version`, `tls_cipher_suites`.
- **kubeadm patches** — `kubeadm_patches` (пример структуры target/type/patch).

## Про kube_control_plane.yml

Файл задаёт **другие** значения резервирования для control plane, чем примеры в k8s-cluster.yml (все закомментированы):

| Переменная | control plane | k8s-cluster.yml |
|---|---|---|
| `kube_memory_reserved` | `512Mi` | `256Mi` |
| `kube_cpu_reserved` | `200m` | `100m` |
| `system_memory_reserved` | `256Mi` | `512Mi` |
| `system_cpu_reserved` | `250m` | `500m` |

Плюс `kube_ephemeral_storage_reserved: 2Gi`, `kube_pid_reserved: "1000"`, `system_ephemeral_storage_reserved: 2Gi`, `system_pid_reserved: "1000"`. Эти значения применяются только к группе `kube_control_plane`.

## Связанные материалы

- Дефолты ролей: [[versions/v2.30.0/variables/k8s-cluster|variables/k8s-cluster.yaml]]
- Аддоны: [[versions/v2.30.0/inventory/addons|inventory/addons.yaml]]
- Структура групп хостов: [[versions/v2.30.0/inventory/inventory-ini|inventory-ini]]
