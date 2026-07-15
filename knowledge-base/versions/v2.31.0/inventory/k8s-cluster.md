---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: inventory
source_path: inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0
retrieved_at: 2026-07-14
topics:
  - k8s-cluster
  - control-plane
  - inventory
reliability: authoritative
---

# Sample inventory: k8s-cluster (v2.31.0)

Разбор основных пользовательских настроек кластера из sample-инвентаря тега `v2.31.0`
(commit `1c9add4`). Источник истины — YAML-файл [[versions/v2.31.0/inventory/k8s-cluster|k8s-cluster.yaml]];
данная заметка — человекочитаемое представление. Полный справочник значений по умолчанию из
`roles/*/defaults` — в [[versions/v2.31.0/variables/k8s-cluster|variables/k8s-cluster.yaml]].

Разбираемые файлы:

- `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml` — основные настройки кластера;
- `inventory/sample/group_vars/k8s_cluster/kube_control_plane.yml` — резервирование ресурсов конкретно для узлов control-plane (все примеры закомментированы).

Обозначения: **задана** — переменная раскомментирована в sample (`is_set: true`);
**пример** — закомментированный образец (`is_set: false`), значение по умолчанию берётся из `roles/*/defaults`.

## Что нового в v2.31.0

В `k8s-cluster.yml` добавлены закомментированные примеры структурированной
**AuthenticationConfiguration** (взаимоисключаема с флагами `--oidc-*`):

- `kube_apiserver_use_authentication_config_file`
- `kube_apiserver_authentication_config_jwt`
- `kube_apiserver_authentication_config_anonymous`

## Каталоги и общие параметры

| Переменная | Значение | Статус |
|---|---|---|
| `kube_config_dir` | `/etc/kubernetes` | задана |
| `kube_script_dir` | `{{ bin_dir }}/kubernetes-scripts` | задана |
| `kube_manifest_dir` | `{{ kube_config_dir }}/manifests` | задана |
| `kube_cert_dir` | `{{ kube_config_dir }}/ssl` | задана |
| `kube_token_dir` | `{{ kube_config_dir }}/tokens` | задана |
| `local_release_dir` | `/tmp/releases` | задана |
| `retry_stagger` | `5` | задана |
| `kube_owner` | `kube` | задана |
| `kube_cert_group` | `kube-cert` | задана |
| `kube_log_level` | `2` | задана |
| `credentials_dir` | `{{ inventory_dir }}/credentials` | задана |
| `kube_api_anonymous_auth` | `true` | задана |

## Аутентификация и авторизация

| Переменная | Значение | Статус |
|---|---|---|
| `kube_oidc_auth` / `kube_token_auth` | `false` | пример |
| `kube_oidc_url`, `kube_oidc_client_id`, ... | OIDC-настройки | пример |
| `kube_apiserver_use_authentication_config_file` | `false` | пример (новое в v2.31.0) |
| `kube_apiserver_authentication_config_jwt` | список issuer'ов | пример (новое в v2.31.0) |
| `kube_apiserver_authentication_config_anonymous` | `enabled: {{ kube_api_anonymous_auth }}` | пример (новое в v2.31.0) |
| `kube_webhook_token_auth` / `kube_webhook_authorization` | `false` | пример |

## Сеть и CNI

| Переменная | Значение | Статус |
|---|---|---|
| `kube_network_plugin` | `calico` | задана |
| `kube_network_plugin_multus` | `false` | задана |
| `kube_service_addresses` | `10.233.0.0/18` | задана |
| `kube_pods_subnet` | `10.233.64.0/18` | задана |
| `kube_network_node_prefix` | `24` | задана |
| `kube_service_addresses_ipv6` | `fd85:ee78:d8a6:8607::1000/116` | задана |
| `kube_pods_subnet_ipv6` | `fd85:ee78:d8a6:8607::1:0000/112` | задана |
| `kube_network_node_prefix_ipv6` | `120` | задана |
| `kube_apiserver_ip` | первый адрес service-подсети (jinja) | задана |
| `kube_apiserver_port` | `6443` | задана |
| `kube_proxy_mode` | `ipvs` | задана |
| `kube_proxy_strict_arp` | `false` | задана |
| `kube_proxy_nodeport_addresses` | `[]` (или CIDR из legacy-переменной) | задана |
| `kube_encrypt_secret_data` | `false` | задана |

## DNS

| Переменная | Значение | Статус |
|---|---|---|
| `cluster_name` | `cluster.local` | задана |
| `dns_domain` | `{{ cluster_name }}` | задана |
| `ndots` | `2` | задана |
| `dns_mode` | `coredns` | задана |
| `resolvconf_mode` | `host_resolvconf` | задана |
| `enable_nodelocaldns` | `true` | задана |
| `enable_nodelocaldns_secondary` | `false` | задана |
| `nodelocaldns_ip` | `169.254.25.10` | задана |
| `nodelocaldns_health_port` | `9254` | задана |
| `nodelocaldns_second_health_port` | `9256` | задана |
| `nodelocaldns_bind_metrics_host_ip` | `false` | задана |
| `nodelocaldns_secondary_skew_seconds` | `5` | задана |
| `enable_coredns_k8s_external` | `false` | задана |
| `coredns_k8s_external_zone` | `k8s_external.local` | задана |
| `enable_coredns_k8s_endpoint_pod_names` | `false` | задана |
| `skydns_server` / `skydns_server_secondary` | 3-й / 4-й адрес service-подсети | задана |
| `deploy_netchecker` | `false` | задана |
| `dns_timeout`, `dns_attempts`, `searchdomains`, `manual_dns_server` | — | пример |

## Container runtime и образы

| Переменная | Значение | Статус |
|---|---|---|
| `container_manager` | `containerd` | задана |
| `kata_containers_enabled` | `false` | задана |
| `kubeadm_certificate_key` | lookup password (jinja) | задана |
| `k8s_image_pull_policy` | `IfNotPresent` | задана |
| `kubernetes_audit` | `false` | задана |
| `default_kubelet_config_dir` | `{{ kube_config_dir }}/dynamic_kubelet_dir` | задана |

## Резервирование ресурсов (примеры)

В `k8s-cluster.yml` все параметры `kube_reserved` / `system_reserved` и связанные с ними
величины (`kube_memory_reserved: 256Mi`, `kube_cpu_reserved: 100m`, `system_memory_reserved: 512Mi`,
`system_cpu_reserved: 500m` и т.д.) приведены закомментированными.

Отдельный файл `kube_control_plane.yml` содержит **закомментированные** значения резервирования
именно для узлов control-plane (отличаются от значений в `k8s-cluster.yml`):

| Переменная | Значение (control-plane) |
|---|---|
| `kube_memory_reserved` | `512Mi` |
| `kube_cpu_reserved` | `200m` |
| `kube_ephemeral_storage_reserved` | `2Gi` |
| `kube_pid_reserved` | `"1000"` |
| `system_memory_reserved` | `256Mi` |
| `system_cpu_reserved` | `250m` |
| `system_ephemeral_storage_reserved` | `2Gi` |
| `system_pid_reserved` | `"1000"` |

## Сертификаты, события, kubeadm-патчи

| Переменная | Значение | Статус |
|---|---|---|
| `event_ttl_duration` | `1h0m0s` | задана |
| `auto_renew_certificates` | `false` | задана |
| `kubeadm_patches_dir` | `{{ kube_config_dir }}/patches` | задана |
| `kubeadm_patches` | `[]` | задана |
| `remove_anonymous_access` | `false` | задана |
| `volume_cross_zone_attachment` | `false` | задана |
| `persistent_volumes_enabled` | `false` | задана |

## Проверка расхождений с defaults

Все раскомментированные (`is_set: true`) переменные, присутствующие в `roles/*/defaults`,
сверены со значениями `default` из [[versions/v2.31.0/variables/k8s-cluster|variables/k8s-cluster.yaml]].
**Расхождений не обнаружено** — sample-значения совпадают с значениями по умолчанию.

## Навигация

- [[versions/v2.31.0/inventory/addons|Sample inventory: addons]]
- [[versions/v2.31.0/inventory/inventory-ini|Sample inventory.ini]]
- [[versions/v2.31.0/README|Срез v2.31.0]]
