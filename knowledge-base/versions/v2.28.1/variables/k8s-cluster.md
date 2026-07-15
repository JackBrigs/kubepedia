---
project: kubespray
kubespray_version: v2.28.1
git_commit: a20891a
source_type: code
source_path: versions/v2.28.1/variables/k8s-cluster.yaml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.28.1
retrieved_at: 2026-07-15
topics:
  - k8s-cluster
  - control-plane
  - kubelet
  - kube-proxy
reliability: authoritative
---

# Переменные ядра кластера — Kubespray v2.28.1

Справочник переменных ядра Kubernetes-кластера для Kubespray **v2.28.1** (коммит `a20891a`): версия Kubernetes, сеть и подсети, kube-apiserver, kube-controller-manager, kube-scheduler, kubelet, kube-proxy, DNS, сертификаты, kubeadm и подготовка ОС.

**Источник истины — парный YAML-справочник** `k8s-cluster.yaml` (в этом же каталоге): в нём все **489 записей переменных** с точными значениями по умолчанию (Jinja-выражения процитированы дословно), путями `source_path` и условиями применения. Эта заметка — обзор ключевых переменных.

Источники (пути относительно корня репозитория kubespray на теге v2.28.1; в скобках — число top-level ключей в файле):

- `roles/kubespray_defaults/defaults/main/main.yml` (231) и `roles/kubespray_defaults/vars/main/main.yml` (5)
- `roles/kubernetes/control-plane/defaults/main/` — main.yml (83), kube-proxy.yml (27), kube-scheduler.yml (10), etcd.yml (8) + vars/main.yaml (1)
- `roles/kubernetes/node/defaults/main.yml` (78) + переопределения `kube_resolv_conf` в `roles/kubernetes/node/vars/{fedora,ubuntu-18,ubuntu-20,ubuntu-22,ubuntu-24}.yml`
- `roles/kubernetes/kubeadm/defaults/main.yml` (3), `roles/kubernetes/kubeadm_common/defaults/main.yml` (3)
- `roles/kubernetes/preinstall/defaults/main.yml` (34) и `roles/kubernetes/preinstall/vars/main.yml` (6)
- `roles/kubernetes/client/defaults/main.yml` (6)

Общая роль дефолтов на теге v2.28.1 называется **`roles/kubespray_defaults`** (подчёркивание). Роль `roles/kubespray-defaults` (дефис) — deprecated-заглушка (только warn + import), её пути в справочнике не используются. Роли `roles/kubernetes/node-label/` и `roles/kubernetes/node-taint/` каталогов defaults/vars **не содержат** (только tasks), собственных переменных по умолчанию у них нет. Переменные загрузок (`download.yml`) и контрольные суммы (`checksums.yml`) вынесены в отдельные справочники; там же в v2.28.1 определены `kube_major_version`, `kube_next`, `kube_major_next_version`, `pod_infra_supported_versions` и `etcd_supported_versions` (в v2.29.1 они находились в `vars/main/main.yml`).

## Версия Kubernetes и kubeadm

| Переменная | Значение по умолчанию | Описание |
|---|---|---|
| `kube_version` | `{{ (kubelet_checksums['amd64'] \| dict2items)[0].key }}` | Версия Kubernetes; на теге v2.28.1 фактически резолвится в **1.32.8** |
| `kube_version_min_required` | последний ключ kubelet_checksums | Минимально поддерживаемая версия; на v2.28.1 — **1.30.0** |
| `kube_major_version` | `1.{{ minor }}` (в `download.yml`) | Мажорно-минорная версия; на v2.28.1 — **1.32** |
| `kubeadm_config_api_version` | `v1beta4` при K8s >= 1.31, иначе `v1beta3` | Версия API конфигурации kubeadm |
| `kubeadm_init_timeout` | `300s` | Тайм-аут kubeadm init на первом контрол-плейне |
| `kubeadm_init_phases_skip` | `["addon/coredns"]` (+ `addon/kube-proxy` при замене kube-proxy CNI-плагином) | Пропускаемые фазы kubeadm init |
| `kubeadm_join_timeout` | `120s` | Тайм-аут kubeadm join воркеров |
| `kubeadm_patches` | `[]` | Патчи kubeadm для манифестов контрол-плейна и kubelet-конфигурации |
| `kubeadm_ignore_preflight_errors` | `[]` | Игнорируемые ошибки preflight-проверок kubeadm |

Важно: `kube_proxy_deployed` (vars) вычисляется как отсутствие `addon/kube-proxy` в `kubeadm_init_phases_skip` — kube-proxy не ставится при Cilium kube-proxy replacement, Calico eBPF, kube-router service proxy или `kube_proxy_remove: true`. В v2.28.1 (в отличие от v2.28.0) уже присутствуют переменные `kubeadm_upgrade_node_phases_skip_default` (`[]`) и `kubeadm_upgrade_node_phases_skip` — они задают пропускаемые фазы `kubeadm upgrade node` для вторичных узлов control-plane; при `kube_version >= 1.32.0` к базовому списку добавляются фазы `kubeadm_init_phases_skip`.

## Сеть и подсети

| Переменная | Значение по умолчанию | Описание |
|---|---|---|
| `kube_network_plugin` | `calico` | CNI: calico, cilium, kube-ovn, **weave**, flannel, cni, cloud. В v2.28.1 weave ещё поддерживается |
| `kube_service_addresses` | `10.233.0.0/18` | IPv4-подсеть сервисов |
| `kube_pods_subnet` | `10.233.64.0/18` | IPv4-подсеть подов |
| `kube_network_node_prefix` | `24` | Размер подсети подов на ноду |
| `ipv4_stack` / `ipv6_stack` | `true` / `false` | Включение IPv4/IPv6-стека (dualstack = оба true) |
| `kube_service_addresses_ipv6` | `fd85:ee78:d8a6:8607::1000/116` | IPv6-подсеть сервисов (при ipv6_stack) |
| `kube_pods_subnet_ipv6` | `fd85:ee78:d8a6:8607::1:0000/112` | IPv6-подсеть подов (при ipv6_stack) |
| `kube_network_node_prefix_ipv6` | `120` | IPv6-префикс подов на ноду |
| `enable_network_policy` | `true` | Поддержка NetworkPolicy в CNI |
| `kube_network_plugin_multus` | `false` | Установка Multus |
| `calico_datastore` | `kdd` | Хранилище Calico: kdd или etcd |
| `weave_password` | `EnterPasswordHere` | Пароль шифрования сети Weave (в v2.29.1 удалён вместе с поддержкой weave) |

Производные `kube_service_subnets` и `kube_pods_subnets` (vars) собирают итоговые списки подсетей с учётом стека.

## kube-apiserver и точки доступа

| Переменная | Значение по умолчанию | Описание |
|---|---|---|
| `kube_apiserver_port` | `6443` (в client — строка `"6443"`) | HTTPS-порт API-сервера |
| `kube_apiserver_bind_address` | `::` | Адрес прослушивания apiserver |
| `kube_apiserver_ip` | первый адрес сервисной подсети (10.233.0.1) | Кластерный VIP API |
| `loadbalancer_apiserver_localhost` | `true`, если внешний `loadbalancer_apiserver` не задан | Локальный LB (nginx/haproxy) на нодах |
| `loadbalancer_apiserver_type` | `nginx` | Тип локального балансировщика |
| `kube_apiserver_endpoint` | Jinja-выражение (см. YAML) | Endpoint API для конкретного хоста |
| `authorization_modes` | `['Node', 'RBAC']` | Режимы авторизации |
| `kube_api_anonymous_auth` | `true` | Анонимная аутентификация (false ломает деплой) |
| `kube_apiserver_node_port_range` | `30000-32767` | Диапазон NodePort |
| `kube_apiserver_enable_admission_plugins` | `[]` | Дополнительные admission-плагины |
| `kube_encrypt_secret_data` | `false` | Шифрование секретов в etcd (алгоритм `secretbox`) |
| `kubernetes_audit` | `false` | Аудит API-сервера в файл |
| `kube_apiserver_request_timeout` | `1m0s` | Глобальный тайм-аут запросов |
| `event_ttl_duration` | `1h0m0s` | Время хранения событий |
| `kube_feature_gates` | `[]` | Общие feature gates (+ отдельные списки на каждый компонент) |

## kube-controller-manager и kube-scheduler

| Переменная | Значение по умолчанию | Описание |
|---|---|---|
| `kube_controller_manager_bind_address` | `::` | Адрес controller-manager |
| `kube_controller_node_monitor_grace_period` | `40s` | Grace period до пометки ноды NotReady |
| `kube_controller_node_monitor_period` | `5s` | Период опроса нод |
| `kube_controller_terminated_pod_gc_threshold` | `12500` | Порог GC завершённых подов |
| `kube_apiserver_pod_eviction_not_ready_timeout_seconds` | `300` | Толерация до эвакуации подов с NotReady-нод |
| `kube_scheduler_bind_address` | `::` | Адрес kube-scheduler |
| `kube_scheduler_profiles` | `[]` | Scheduling-профили |
| `kube_kubeadm_apiserver_extra_args` / `..._controller_extra_args` / `..._scheduler_extra_args` | `{}` | Дополнительные аргументы компонентов через kubeadm |

Примечание: в v2.28.1 **нет** появившейся в v2.29.1 переменной `control_plane_health_retries` (число повторов health-проверок apiserver/scheduler/controller-manager).

## kubelet

| Переменная | Значение по умолчанию | Описание |
|---|---|---|
| `kubelet_max_pods` | `110` | Максимум подов на ноде |
| `kubelet_fail_swap_on` | `true` | Запрет запуска при включённом swap |
| `kubelet_rotate_certificates` | `true` | Ротация клиентского сертификата kubelet |
| `kubelet_rotate_server_certificates` | `false` | Ротация серверного сертификата kubelet |
| `kubelet_protect_kernel_defaults` | `true` | Контроль параметров ядра |
| `kubelet_authentication_token_webhook` | `true` | Webhook-аутентификация к kubelet API |
| `kubelet_authorization_mode_webhook` | `true` | Webhook-авторизация kubelet API |
| `kube_reserved` / `system_reserved` | `false` / `false` | Резервирование ресурсов (kube: 100m/256Mi, system: 500m/512Mi) |
| `eviction_hard` / `eviction_hard_control_plane` | `{}` | Жёсткие пороги эвакуации |
| `kubelet_status_update_frequency` | `10s` | Частота отправки статуса ноды |
| `kubelet_pod_pids_limit` | `-1` | Лимит PID на под |
| `kubelet_config_extra_args` | `{}` | Произвольные параметры kubelet-config.yaml |
| `kubelet_custom_flags` | `[]` | Произвольные флаги CLI kubelet |
| `kubelet_shutdown_grace_period` | `60s` (критические поды: `20s`) | Graceful Node Shutdown |
| `kube_read_only_port` | `0` | Read-only порт kubelet (отключён) |
| `kube_resolv_conf` | `/etc/resolv.conf` (Ubuntu 18–24, Fedora: `/run/systemd/resolve/resolv.conf`) | resolv.conf для DNS подов |

Примечание: в v2.28.1 роль `node` **не содержит** появившейся в v2.29.1 переменной `kubelet_static_pod_path` (каталог static pods управляется через `kube_manifest_dir`).

## kube-proxy

| Переменная | Значение по умолчанию | Описание |
|---|---|---|
| `kube_proxy_mode` | `ipvs` | Режим: ipvs, iptables, nftables |
| `kube_proxy_scheduler` | `rr` | Планировщик IPVS |
| `kube_proxy_strict_arp` | `false` | Строгий ARP — обязателен для MetalLB / kube-vip (ARP) |
| `kube_proxy_bind_address` | `0.0.0.0` | Адрес kube-proxy |
| `kube_proxy_metrics_bind_address` | `127.0.0.1:10249` | Адрес метрик |
| `kube_proxy_healthz_bind_address` | `0.0.0.0:10256` | Адрес health-check |
| `kube_proxy_conntrack_max_per_core` | `32768` | Лимит conntrack на ядро CPU |
| `kube_proxy_sync_period` | `30s` | Интервал обновления правил |
| `kube_proxy_masquerade_all` | `false` | SNAT всего трафика (iptables-режим) |
| `kube_proxy_nodeport_addresses` | `[]` | CIDR-ы для NodePort |

## DNS

| Переменная | Значение по умолчанию | Описание |
|---|---|---|
| `dns_mode` | `coredns` | Режим кластерного DNS: coredns, coredns_dual, manual, none |
| `cluster_name` / `dns_domain` | `cluster.local` | Имя кластера = DNS-домен |
| `enable_nodelocaldns` | `true` | Nodelocal DNS cache |
| `nodelocaldns_ip` | `169.254.25.10` | IP nodelocaldns |
| `skydns_server` | третий адрес сервисной подсети (10.233.0.3) | IP кластерного DNS-сервиса |
| `enable_dns_autoscaler` | `true` | Автомасштабирование CoreDNS |
| `upstream_dns_servers` | `[]` | Upstream DNS для внекластерных запросов |
| `resolvconf_mode` | `host_resolvconf` | Способ настройки resolv.conf хоста |
| `ndots` | `2` | ndots в resolv.conf |
| `remove_default_searchdomains` | `false` | Удалить кластерные search-домены по умолчанию |

Специфика v2.28.1: роль `preinstall` содержит управление `/etc/hosts` через `populate_inventory_to_hosts_file` (`true`), `populate_loadbalancer_apiserver_to_hosts_file` (`true`), `populate_localhost_entries_to_hosts_file` (`true`) и `etc_hosts_localhost_entries` — все четыре удалены в v2.29.1.

## Сертификаты и безопасность

| Переменная | Значение по умолчанию | Описание |
|---|---|---|
| `kube_cert_dir` | `/etc/kubernetes/ssl` | Каталог сертификатов |
| `kube_asymmetric_encryption_algorithm` | `RSA-2048` | Алгоритм ключей кластера |
| `certificates_key_size` / `certificates_duration` | `2048` / `36500` | Размер ключа и срок (дни) для скриптовой генерации (legacy etcd) |
| `auto_renew_certificates` | `false` | Автообновление сертификатов systemd-таймером |
| `kubeadm_upgrade_auto_cert_renewal` | `true` | Перевыпуск сертификатов при kubeadm upgrade |
| `kube_external_ca_mode` | `false` | Внешнее управление CA (отключает задачи с сертификатами) |
| `kube_pod_security_use_default` | `false` | Кластерные значения PodSecurity по умолчанию (enforce: `baseline`, audit/warn: `restricted`) |
| `kube_oidc_auth` / `kube_token_auth` / `kube_webhook_token_auth` | `false` | Дополнительные методы аутентификации |

Важное отличие от v2.29.1: в v2.28.1 **нет** переменных `kube_cert_validity_period` (`8760h`, 1 год) и `kube_ca_cert_validity_period` (`87600h`, 10 лет). Срок действия kubeadm-управляемых сертификатов в v2.28.1 определяется **дефолтами kubeadm** (листовые сертификаты — 1 год, CA — 10 лет), а не отдельными переменными Kubespray. Для скриптовой генерации сертификатов (legacy etcd) используется `certificates_duration` (36500 дней).

## Рантайм и etcd (со стороны ядра кластера)

| Переменная | Значение по умолчанию | Описание |
|---|---|---|
| `container_manager` | `containerd` | Рантайм: containerd, crio, docker |
| `cri_socket` | зависит от рантайма (см. YAML) | Путь к CRI-сокету |
| `nri_enabled` | `{{ container_manager == 'containerd' }}` | NRI-плагин (по умолчанию для containerd) |
| `etcd_deployment_type` | `host` | Развёртывание etcd: host, docker, kubeadm |
| `etcd_data_dir` | `/var/lib/etcd` | Каталог данных etcd |
| `etcd_events_cluster_enabled` | `false` | Отдельный etcd для событий |
| `kube_apiserver_storage_backend` | `etcd3` | Бэкенд хранения apiserver |
| `etcd_compaction_retention` | `8` | Retention компакции (kubeadm-managed etcd) |
| `etcd_heartbeat_interval` / `etcd_election_timeout` | `250` / `5000` | Параметры etcd (мс); дублируются в kubespray_defaults и control-plane/etcd.yml |

Подробности рантайма (containerd 2.x, crio, docker) и etcd вынесены в отдельные справочники `container-runtime.yaml` и `etcd.yaml`; `etcd_version` в v2.28.1 резолвится в 3.5.22 через `etcd_supported_versions`/`download.yml` (в v2.28.1 значения словаря заданы выражением «наибольшая версия etcd < 3.6 из checksums», а не литералом 3.5.16, как в v2.28.0). Здесь приведены только переменные, определённые «со стороны ядра».

## Дубликаты и расхождения между ролями

- `discovery_timeout`: **`5m0s`** в `roles/kubernetes/control-plane/defaults/main/main.yml`, но **`60s`** в `roles/kubernetes/kubeadm/defaults/main.yml` (join воркеров) — это разные контексты kubeadm discovery.
- `kube_apiserver_port`: число `6443` в kubespray_defaults, строка `"6443"` в `roles/kubernetes/client/defaults/main.yml`.
- Идентичные дубликаты в нескольких ролях (значения совпадают, помечены в YAML через `also_defined_in`): `kube_apiserver_bind_address`, `kube_apiserver_node_port_range`, `sysctl_file_path`, `kube_owner`, `kube_cert_group`, `kube_config_dir`, `kube_cert_dir`, `kube_cert_compat_dir`, `ignore_assert_errors`, `kubeconfig_localhost`, `kubectl_localhost`, `kubeadm_use_file_discovery`, `kube_proxy_nodeport_addresses`, `etcd_heartbeat_interval`, `etcd_election_timeout`.
- `kube_resolv_conf`: переопределяется через `roles/kubernetes/node/vars/{fedora,ubuntu-18,ubuntu-20,ubuntu-22,ubuntu-24}.yml` на `/run/systemd/resolve/resolv.conf`.

## Сверка полноты извлечения

Для каждого in-scope defaults/vars-файла: число top-level ключей в источнике (`grep -cE '^[a-zA-Z_][a-zA-Z0-9_]*:'`) против числа извлечённых записей. Дубликаты, оформленные через `also_defined_in` на первичной записи, отдельной строкой не дублируются — это объясняет расхождение для `etcd.yml` (2 дубля etcd_heartbeat_interval/etcd_election_timeout) и `preinstall/defaults/main.yml` (6 дублей: ignore_assert_errors, kube_owner, kube_cert_group, kube_config_dir, kube_cert_dir, kube_cert_compat_dir).

| Источник | Ключей в источнике | Извлечено записей |
|---|---|---|
| `roles/kubespray_defaults/defaults/main/main.yml` | 231 | 231 |
| `roles/kubespray_defaults/vars/main/main.yml` | 5 | 5 |
| `roles/kubernetes/control-plane/defaults/main/main.yml` | 83 | 83 |
| `roles/kubernetes/control-plane/defaults/main/kube-proxy.yml` | 27 | 27 |
| `roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml` | 10 | 10 |
| `roles/kubernetes/control-plane/defaults/main/etcd.yml` | 8 | 6 (+2 дубля через also_defined_in) |
| `roles/kubernetes/control-plane/vars/main.yaml` | 1 | 1 |
| `roles/kubernetes/node/defaults/main.yml` | 78 | 78 |
| `roles/kubernetes/node/vars/*.yml` | 1 (kube_resolv_conf ×5 файлов) | override отражён в записи kube_resolv_conf |
| `roles/kubernetes/kubeadm/defaults/main.yml` | 3 | 3 |
| `roles/kubernetes/kubeadm_common/defaults/main.yml` | 3 | 3 |
| `roles/kubernetes/preinstall/defaults/main.yml` | 34 | 28 (+6 дублей через also_defined_in) |
| `roles/kubernetes/preinstall/vars/main.yml` | 6 | 6 |
| `roles/kubernetes/client/defaults/main.yml` | 6 | 6 |
| **Итого записей в YAML** | | **487** |

Полный список из 487 записей с условиями применения и связями — в `k8s-cluster.yaml` (источник истины).

Назад к срезу: [[versions/v2.28.1/README|Срез v2.28.1]]
