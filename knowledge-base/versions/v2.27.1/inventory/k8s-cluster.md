---
project: kubespray
kubespray_version: v2.27.1
git_commit: 45140b5
source_type: inventory
source_paths:
  - inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.27.1
retrieved_at: 2026-07-15
topics:
  - inventory
  - k8s-cluster
  - control-plane
reliability: authoritative
---

# Sample-inventory: k8s-cluster.yml (v2.27.1)

Разбор главного пользовательского файла настроек кластера `k8s-cluster.yml` из
группы `k8s_cluster`. Источник истины — [[versions/v2.27.1/inventory/k8s-cluster|k8s-cluster.yaml (справочник)]];
здесь человекочитаемое изложение. Аддоны разобраны отдельно:
[[versions/v2.27.1/inventory/addons|addons.yaml]].

Ссылка на срез: [[versions/v2.27.1/README|Срез v2.27.1]].

## Что это за файл

`k8s-cluster.yml` — основные настройки кластера: каталоги, версия K8s, сеть, DNS,
kube-proxy, API-сервер, рантайм, резервирование ресурсов, сертификаты. Большинство
«боевых» переменных, которые правит пользователь, находятся здесь.

Поле `is_set`: `true` — переменная в файле раскомментирована и реально задаётся;
`false` — закомментированный пример/дефолт для справки.

Всего в справочнике: **122 переменные**, из них реально задано (`is_set: true`) —
**60**, закомментированных примеров — **62**.

> [!important] Отличия v2.27.1 от v2.29.1
> - **`kube_version: v1.31.9` задан прямо в sample** (в v2.29.1 в этом файле его нет). Значение совпадает с defaults роли.
> - Dual stack управляется переменной **`enable_dual_stack_networks`** (в v2.29.1 — `ipv6_stack`); IPv6-подсети активны только при `true`.
> - `kube_apiserver_ip`, `skydns_server`, `skydns_server_secondary` опираются напрямую на `kube_service_addresses` (в v2.29.1 — на `kube_service_subnets.split(',')`).
> - `kube_proxy_mode`: комментарий перечисляет только **ipvs, iptables** (nftables ещё нет).
> - `kube_network_plugin`: в списке ещё присутствует **weave**.

> [!note] Изменение v2.27.0 → v2.27.1
> В v2.27.1 из `k8s-cluster.yml` **удалены** закомментированные примеры резервирования ресурсов control plane, которые в v2.27.0 использовали некорректные имена `kube_master_*` / `system_master_*` (таких переменных в коде ролей не существует). Вместо них добавлен **новый файл** `kube_control_plane.yml` с корректными именами (`kube_*_reserved` / `system_*_reserved`), применяемыми к группе `kube_control_plane`. Разбор нового файла — [[versions/v2.27.1/inventory/kube_control_plane|kube_control_plane.yaml]].

## Ключевые заданные настройки (сеть и подсети)

| Переменная | Значение в sample | Назначение |
|---|---|---|
| `kube_version` | `v1.31.9` | Версия Kubernetes |
| `kube_network_plugin` | `calico` | CNI по умолчанию (варианты: cilium, calico, kube-ovn, weave, flannel, cni, cloud) |
| `kube_network_plugin_multus` | `false` | Multus для нескольких CNI |
| `kube_service_addresses` | `10.233.0.0/18` | IPv4-подсеть сервисов |
| `kube_pods_subnet` | `10.233.64.0/18` | IPv4-подсеть подов |
| `kube_network_node_prefix` | `24` | Префикс подсети подов на ноду |
| `enable_dual_stack_networks` | `false` | Включение IPv4+IPv6 |
| `kube_service_addresses_ipv6` | `fd85:ee78:d8a6:8607::1000/116` | IPv6-подсеть сервисов (только при dual stack) |
| `kube_pods_subnet_ipv6` | `fd85:ee78:d8a6:8607::1:0000/112` | IPv6-подсеть подов |
| `kube_network_node_prefix_ipv6` | `120` | IPv6-префикс на ноду |

## API-сервер и kube-proxy

| Переменная | Значение | Назначение |
|---|---|---|
| `kube_apiserver_ip` | первый адрес сервисной подсети | Виртуальный IP API (по умолчанию 10.233.0.1) |
| `kube_apiserver_port` | `6443` | HTTPS-порт API |
| `kube_proxy_mode` | `ipvs` | Режим kube-proxy (ipvs / iptables) |
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

`kube_config_dir` = `/etc/kubernetes`, а также производные: `kube_cert_dir` (`.../ssl`),
`kube_token_dir` (`.../tokens`), `kube_manifest_dir` (`.../manifests`),
`kube_script_dir` (`{{ bin_dir }}/kubernetes-scripts`). Владельцы: `kube_owner: kube`,
`kube_cert_group: kube-cert`. В оригинальном комментарии прямо сказано, что изменение
этих значений почти наверняка что-то сломает.

## Резервирование ресурсов

В v2.27.1 резервирование ресурсов **рабочих нод** задаётся в `k8s-cluster.yml`
(все переменные закомментированы): `kube_*_reserved` и `system_*_reserved`:

| Переменная (worker) | Пример |
|---|---|
| `kube_memory_reserved` | `256Mi` |
| `kube_cpu_reserved` | `100m` |
| `kube_ephemeral_storage_reserved` | `2Gi` |
| `kube_pid_reserved` | `"1000"` |
| `system_memory_reserved` | `512Mi` |
| `system_cpu_reserved` | `500m` |
| `system_ephemeral_storage_reserved` | `2Gi` |

Резервирование ресурсов **узлов control plane** в v2.27.1 вынесено в отдельный файл
`kube_control_plane.yml` (те же имена переменных `kube_*_reserved` / `system_*_reserved`,
но в group_vars группы `kube_control_plane`). См. [[versions/v2.27.1/inventory/kube_control_plane|kube_control_plane.yaml]].
В v2.27.0 этих примеров control plane не было в правильном виде — там были ошибочные
`kube_master_*` / `system_master_*` прямо в `k8s-cluster.yml`, удалённые в v2.27.1.

## Крупные закомментированные блоки

Закомментированы (для справки): OIDC-аутентификация (`kube_oidc_*`),
webhook authn/authz (`kube_webhook_*`), NVIDIA GPU (`nvidia_*`), TLS
(`tls_min_version`, `tls_cipher_suites`), eviction thresholds, cgroups kubelet,
копирование kubeconfig/kubectl на хост Ansible, внешние зоны nodelocaldns и опции CoreDNS.

## Соответствие defaults ролей

Все реально заданные (`is_set: true`) переменные проверены против `roles/*/defaults`.
**Расхождений не обнаружено** — значения sample совпадают с defaults (в частности
`kube_version: v1.31.9` и `container_manager: containerd`). Подробности:
[[versions/v2.27.1/discrepancies|Расхождения inventory vs defaults]]. По правилу
раздела 6.2 CLAUDE.md при расхождении приоритет имеет код ролей.
