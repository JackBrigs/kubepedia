---
project: kubespray
kubespray_version: v2.28.0
git_commit: 63cdf87
source_type: inventory
source_paths:
  - inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.28.0
retrieved_at: 2026-07-15
topics:
  - inventory
  - k8s-cluster
reliability: authoritative
---

# Sample-inventory: k8s-cluster.yml (v2.28.0)

Разбор файла `k8s-cluster.yml` группы `k8s_cluster` из `inventory/sample/group_vars/`. Это главные пользовательские настройки кластера. Источник истины — [[versions/v2.28.0/inventory/k8s-cluster|k8s-cluster.yaml (справочник)]]; здесь человекочитаемое изложение.

Ссылка на срез: [[versions/v2.28.0/README|Срез v2.28.0]].

## Что это за файл

- **`k8s-cluster.yml`** — основные настройки кластера: каталоги, сеть, DNS, kube-proxy, API-сервер, рантайм, резервирование ресурсов, сертификаты. Большинство «боевых» переменных, которые правит пользователь, находятся здесь.

Резервирование ресурсов **для узлов control plane** вынесено в отдельный файл `kube_control_plane.yml` — см. [[versions/v2.28.0/inventory/kube_control_plane|kube_control_plane.yaml]].

Поле `is_set`: `true` — переменная в файле раскомментирована и реально задаётся; `false` — закомментированный пример/дефолт для справки.

Всего в справочнике `k8s-cluster.yaml`: **120 переменных**, из них реально задано (`is_set: true`) — **58**, закомментированных примеров — **62**.

## Ключевые заданные настройки (сеть и подсети)

| Переменная | Значение в sample | Назначение |
|---|---|---|
| `kube_network_plugin` | `calico` | CNI по умолчанию (варианты: cilium, calico, kube-ovn, weave, flannel, cni, cloud). `weave` есть в v2.28.0, удалён в v2.29.1 |
| `kube_network_plugin_multus` | `false` | Multus для нескольких CNI |
| `kube_service_addresses` | `10.233.0.0/18` | IPv4-подсеть сервисов |
| `kube_pods_subnet` | `10.233.64.0/18` | IPv4-подсеть подов |
| `kube_network_node_prefix` | `24` | Префикс подсети подов на ноду (ещё ограничено `kubelet_max_pods`) |
| `kube_service_addresses_ipv6` | `fd85:ee78:d8a6:8607::1000/116` | IPv6-подсеть сервисов (только при `ipv6_stack: true`) |
| `kube_pods_subnet_ipv6` | `fd85:ee78:d8a6:8607::1:0000/112` | IPv6-подсеть подов |
| `kube_network_node_prefix_ipv6` | `120` | IPv6-префикс на ноду |

## API-сервер и kube-proxy

| Переменная | Значение | Назначение |
|---|---|---|
| `kube_apiserver_ip` | первый адрес сервисной подсети | Виртуальный IP API (по умолчанию 10.233.0.1) |
| `kube_apiserver_port` | `6443` | HTTPS-порт API |
| `kube_proxy_mode` | `ipvs` | Режим kube-proxy (ipvs / iptables / nftables). В комментарии TODO о переходе на nftables |
| `kube_proxy_strict_arp` | `false` | Нужно `true` для MetalLB и kube-vip (ARP) |
| `kube_api_anonymous_auth` | `true` | Анонимная аутентификация к API |
| `remove_anonymous_access` | `false` | Удалить role binding анонимных пользователей от kubeadm |

## DNS

| Переменная | Значение | Назначение |
|---|---|---|
| `cluster_name` / `dns_domain` | `cluster.local` / `{{ cluster_name }}` | Имя кластера и DNS-домен |
| `dns_mode` | `coredns` | Режим DNS (coredns, coredns_dual, manual, none) |
| `ndots` | `2` | ndots в resolv.conf hostnet-подов |
| `resolvconf_mode` | `host_resolvconf` | Способ настройки resolv.conf хоста |
| `enable_nodelocaldns` | `true` | Локальный кеш DNS на нодах |
| `enable_nodelocaldns_secondary` | `false` | Вторичный daemonset nodelocaldns |
| `nodelocaldns_ip` | `169.254.25.10` | Link-local IP nodelocaldns |
| `skydns_server` / `_secondary` | 3-й / 4-й адрес сервисной подсети | IP кластерного DNS-сервиса |
| `deploy_netchecker` | `false` | HTTP-сервис проверки DNS |

## Рантайм, сертификаты, прочее

| Переменная | Значение | Назначение |
|---|---|---|
| `container_manager` | `containerd` | Контейнерный рантайм (containerd / crio / docker) |
| `kata_containers_enabled` | `false` | Kata Containers как доп. рантайм |
| `k8s_image_pull_policy` | `IfNotPresent` | imagePullPolicy компонентов |
| `kube_encrypt_secret_data` | `false` | Шифрование Secret Data at Rest |
| `kubernetes_audit` | `false` | Audit log Kubernetes |
| `auto_renew_certificates` | `false` | Автообновление сертификатов control plane |
| `event_ttl_duration` | `1h0m0s` | Время хранения событий |
| `kube_log_level` | `2` | Уровень логирования компонентов |
| `local_release_dir` | `/tmp/releases` | Каталог загрузок на нодах (нужно ~1 ГБ) |

## Каталоги (менять не рекомендуется)

`kube_config_dir` = `/etc/kubernetes`, а также производные: `kube_cert_dir` (`.../ssl`), `kube_token_dir` (`.../tokens`), `kube_manifest_dir` (`.../manifests`), `kube_script_dir` (`{{ bin_dir }}/kubernetes-scripts`). Владельцы: `kube_owner: kube`, `kube_cert_group: kube-cert`. В оригинальном комментарии прямо сказано, что изменение этих значений почти наверняка что-то сломает.

## Резервирование ресурсов

Секции `kube_reserved` и `system_reserved` в `k8s-cluster.yml` **закомментированы** (примеры для рабочих нод: `kube_memory_reserved: 256Mi`, `kube_cpu_reserved: 100m`, `system_memory_reserved: 512Mi`, `system_cpu_reserved: 500m`). Аналогичное резервирование для узлов control plane задаётся в отдельном файле `kube_control_plane.yml` с иными значениями примеров — см. [[versions/v2.28.0/inventory/kube_control_plane|kube_control_plane.yaml]].

## Крупные закомментированные блоки

В `k8s-cluster.yml` закомментированы (для справки): OIDC-аутентификация (`kube_oidc_*`), webhook authn/authz (`kube_webhook_*`), NVIDIA GPU (`nvidia_*`), TLS (`tls_min_version`, `tls_cipher_suites`), eviction thresholds, cgroups kubelet, копирование kubeconfig/kubectl на хост Ansible, внешние зоны nodelocaldns и опции CoreDNS.

## Соответствие defaults ролей

Все реально заданные (`is_set: true`) переменные проверены против `roles/*/defaults` (этап 2). **Расхождений не обнаружено** — значения sample совпадают с defaults. Подробности: [[versions/v2.28.0/discrepancies|Расхождения inventory vs defaults]]. По правилу раздела 6.2 CLAUDE.md при расхождении приоритет имеет код ролей.
