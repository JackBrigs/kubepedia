---
project: kubespray
kubespray_version: v2.27.1
git_commit: 45140b5
source_type: code
source_path: versions/v2.27.1/variables/k8s-cluster.yaml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.27.1
retrieved_at: 2026-07-15
topics:
  - k8s-cluster
  - control-plane
  - kubelet
  - kube-proxy
reliability: authoritative
---

# Переменные ядра кластера — Kubespray v2.27.1

Человекочитаемая заметка к машиночитаемому справочнику `k8s-cluster.yaml`.
**Источник истины — YAML-справочник** `versions/v2.27.1/variables/k8s-cluster.yaml`.
Назад к срезу: [[versions/v2.27.1/README|Срез v2.27.1]].

Источники в коде тега `v2.27.1` (commit `45140b5`):

- `roles/kubespray-defaults/defaults/main/main.yml` (каталог с **дефисом**) — общие defaults кластера;
- `roles/kubernetes/control-plane/defaults/main/{main,kube-proxy,kube-scheduler,etcd}.yml`;
- `roles/kubernetes/node/defaults/main.yml` — kubelet узла, kube-vip, локальный балансировщик;
- `roles/kubernetes/kubeadm/defaults/main.yml`, `roles/kubernetes/kubeadm_common/defaults/main.yml`;
- `roles/kubernetes/preinstall/defaults/main.yml`, `roles/kubernetes/client/defaults/main.yml`.

Переменные доменов **etcd**, **container runtime** и **Cilium** вынесены в отдельные справочники
([[versions/v2.27.1/variables/etcd|etcd.yaml]], [[versions/v2.27.1/variables/container-runtime|container-runtime.yaml]],
[[versions/v2.27.1/variables/cni|cni.yaml]]) и здесь по большей части не дублируются. Флаги addon-компонентов —
в `addons.yaml` (отдельный срез), переменные загрузок — в [[versions/v2.27.1/variables/download|download.yaml]].

## Ключевые значения тега

| Параметр | Значение |
|---|---|
| `kube_version` | **v1.31.9** (явный литерал) |
| `kube_version_min_required` | v1.29.0 |
| `kube_network_plugin` | calico (по умолчанию) |
| `kube_proxy_mode` | ipvs |
| `kube_service_addresses` | 10.233.0.0/18 |
| `kube_pods_subnet` | 10.233.64.0/18 |
| `container_manager` | containerd (см. container-runtime.yaml) |
| `dns_mode` | coredns |

## Отличия от v2.29.1 (важно при обновлении)

- IP-стек управляется `enable_dual_stack_networks` (по умолчанию false). Переменных `ipv4_stack` / `ipv6_stack`, появившихся в v2.29.1, **в v2.27.1 нет**.
- `kube_apiserver_bind_address` по умолчанию **`0.0.0.0`** (в v2.29.1 — `::`); в `kube_apiserver_endpoint` `0.0.0.0` заменяется на `127.0.0.1`.
- `authorization_modes` и `rbac_enabled` **проще**: нет структурного `AuthorizationConfiguration` (`kube_apiserver_use_authorization_config_file` и связанных), появившегося в v2.29.1.
- Адреса узлов строятся на `ip` / `access_ip` / `fallback_ip` (в v2.29.1 — `main_ip` / `main_access_ip`).
- `skydns_server` берётся напрямую из `kube_service_addresses` (в v2.29.1 — из `kube_service_subnets`).
- `kube_proxy_mode` в комментарии кода допускает только iptables/ipvs (nftables добавлен позже).

## Сеть кластера

`kube_service_addresses` (10.233.0.0/18) — сервисы; `kube_pods_subnet` (10.233.64.0/18) — поды;
`kube_network_node_prefix` (24) — размер подсети на ноду; `kube_apiserver_ip` — первый адрес сервисной
подсети (10.233.0.1). Двойной стек — `enable_dual_stack_networks` + `kube_*_ipv6`.

## DNS

`dns_mode: coredns`, `enable_dns_autoscaler: true`, nodelocaldns (`enable_nodelocaldns: true`,
`nodelocaldns_ip: 169.254.25.10`), `dns_domain: {{ cluster_name }}` (cluster.local),
upstream/ search-домены, режимы coredns_dual/manual.

## Контрол-плейн

`roles/kubernetes/control-plane/defaults/main/main.yml` (83 переменные): API-сервер (admission-плагины,
PodSecurity, audit, tracing, encryption-at-rest, OIDC/webhook auth), controller-manager (leader election,
node monitor), сертификаты (`auto_renew_certificates`, `kube_asymmetric_encryption_algorithm: RSA-2048`).
Планировщик — `kube-scheduler.yml`; kube-proxy — `kube-proxy.yml` (conntrack, ipvs scheduler `rr`,
sync-периоды, `kube_proxy_strict_arp`). Файл `etcd.yml` дублирует часть переменных домена etcd для
kubeadm-конфига (основной справочник — etcd.yaml).

## Узел (kubelet, kube-vip, балансировщик)

`roles/kubernetes/node/defaults/main.yml` (78 переменных): адреса/cgroups kubelet, резервирование
ресурсов (`kube_reserved`/`system_reserved` + memory/cpu/storage/pid), eviction, лимиты
(`kubelet_max_pods: 110`, `kubelet_pod_pids_limit: -1`), логи, tracing, ipvs/conntrack модули,
полный набор `kube_vip_*` (версия v0.8.0, ARP/BGP/DDNS/LB), локальный балансировщик API.

## preinstall / kubeadm / client

- preinstall: DNS/resolv.conf (`nameservers`, `remove_default_searchdomains`), /etc/hosts, память-минимумы, NTP (`ntp_enabled: false`), поддерживаемые ОС, `disable_fapolicyd: true`.
- kubeadm: `kubeadm_join_timeout: 120s`, `discovery_timeout: 60s` (в роли kubeadm переопределяет 5m0s из control-plane); kubeadm_common: `kubeadm_patches`, `kubeadm_ignore_preflight_errors`.
- client: `kubeconfig_localhost`, `kubectl_localhost`, `artifacts_dir`.

## Прокси и системные настройки

`proxy_env_defaults` / `proxy_env` / `proxy_disable_env`, `ssl_ca_dirs` (по семейству ОС),
`system_upgrade`/`system_upgrade_reboot`, `additional_sysctl`, `host_architecture`/`host_os`.

## Cloud provider

`cloud_provider` (только external или пусто), `external_cloud_provider` (openstack/vsphere/oci/huaweicloud/hcloud),
блок OpenStack LBaaS и `external_hcloud_cloud`.

## Связанное

- [[versions/v2.27.1/variables/etcd|etcd.yaml]]
- [[versions/v2.27.1/variables/cni|cni.yaml]]
- [[versions/v2.27.1/variables/container-runtime|container-runtime.yaml]]
- [[versions/v2.27.1/variables/download|download.yaml]]
- [[versions/v2.27.1/README|Срез v2.27.1]]

## Сверка полноты

Извлечено по ролям:
- `roles/kubespray-defaults/defaults/main/main.yml` — 225 top-level ключей. В k8s-cluster.yaml вынесены ~113 переменных ядра. Остальные распределены по охвату: домен etcd (~40) → etcd.yaml; container runtime (~24: container_manager, cri_socket, containerd_* каталоги, kata/gvisor/runc/crun/youki, docker_*) → container-runtime.yaml; выбор CNI входит и сюда, и в cni.yaml; addon-флаги (~30: helm_enabled, metrics_server_enabled, ingress_*, cert_manager_enabled, *_csi_enabled, metallb_*, argocd_enabled, dashboard_enabled, *_provisioner_* и т.п.) → addons.yaml; local_release_dir → download.yaml.
- control-plane/main — все **83**; control-plane/kube-proxy — все **28**; control-plane/kube-scheduler — все **10**; control-plane/etcd — все **7** (как дубли домена etcd); node — все **78**; kubeadm — 3 (одна уникальная + 2 дубля с control-plane); kubeadm_common — все **3**; preinstall — все **39** (5 из них — дубли kube_owner/kube_cert_group/kube_config_dir/kube_cert_dir/kube_cert_compat_dir/sysctl_file_path/epel_enabled/ignore_assert_errors/yum_repo_dir, помечены also_defined_in либо разнесены); client — все **6** (kubeconfig_localhost/kubectl_localhost/kube_config_dir/kube_apiserver_port — дубли).

Итого в `k8s-cluster.yaml` — **387 записей**, покрывающих ядро кластера. Автоматическая сверка подтвердила, что все top-level ключи из перечисленных role-defaults-файлов присутствуют. Переменные вне охвата (etcd, container runtime, Cilium, addons, download) намеренно вынесены в профильные справочники и здесь не повторяются.
