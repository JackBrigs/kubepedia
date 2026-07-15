---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: inventory
source_paths:
  - inventory/sample/group_vars/all/all.yml
  - inventory/sample/group_vars/all/etcd.yml
  - inventory/sample/group_vars/all/containerd.yml
  - inventory/sample/group_vars/all/cri-o.yml
  - inventory/sample/group_vars/all/docker.yml
  - inventory/sample/group_vars/all/coreos.yml
  - inventory/sample/group_vars/all/offline.yml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/inventory/sample/group_vars/all
retrieved_at: 2026-07-14
topics: [inventory, all, offline]
reliability: authoritative
---

# Инвентарь group_vars/all — v2.31.0

Разбор общих (не облачных) файлов `inventory/sample/group_vars/all/` тега **v2.31.0** (commit `1c9add4`). Источник истины — машиночитаемый справочник [[versions/v2.31.0/inventory/all|all.yaml]]; данная заметка — его читаемое представление.

Относится к срезу [[versions/v2.31.0/README|Срез v2.31.0]].

## Как читать

- **is_set: true** — переменная в sample-инвентаре **раскомментирована** (задана явно) и переопределяет значение из `roles/*/defaults`.
- **is_set: false** — переменная **закомментирована**, приведена лишь как пример/подсказка; фактически действует значение из role defaults. В колонке «Пример» показано значение из закомментированной строки.

Всего разобрано **135** переменных: **20** заданы (is_set: true), **115** закомментированы.

## Обзор по файлам

| Файл | Назначение | Заданных | Закомментированных |
|------|-----------|----------|--------------------|
| `all.yml` | Базовые параметры кластера: каталоги, LB API-сервера, прокси, DNS, NTP, webhook-аутентификация, подписка RHEL | 11 | 24 |
| `etcd.yml` | Каталог данных, тип развёртывания и container_manager для etcd | 2 | 1 |
| `containerd.yml` | Настройки containerd (все закомментированы, полные defaults в роли) | 0 | 20 |
| `cri-o.yml` | Реестры и аутентификация CRI-O (все закомментированы) | 0 | 2 |
| `docker.yml` | Параметры демона Docker: storage, DNS, логирование, реестры | 7 | 7 |
| `coreos.yml` | Автообновление CoreOS (закомментировано) | 0 | 1 |
| `offline.yml` | Offline/air-gapped установка: приватные реестры и репозитории, download-URL | 0 | 60 |

## all.yml — заданные переменные

| Переменная | Значение | Комментарий |
|------------|----------|-------------|
| `bin_dir` | `/usr/local/bin` | Каталог установки бинарников (совпадает с role default) |
| `loadbalancer_apiserver_port` | `6443` | Порт локального LB API-сервера (должен быть 6443) |
| `loadbalancer_apiserver_healthcheck_port` | `8081` | Порт проверки живости прокси nginx |
| `no_proxy_exclude_workers` | `false` | В no_proxy включать только control-plane (не воркеры) |
| `kube_webhook_token_auth` | `false` | Webhook token authentication для API-сервера |
| `kube_webhook_token_auth_url_skip_tls_verify` | `false` | Пропуск проверки TLS при обращении к webhook |
| `ntp_enabled` | `false` | Запуск и включение ntpd/chrony |
| `ntp_manage_config` | `false` | Управление конфигурацией NTP средствами Kubespray |
| `ntp_servers` | `0..3.pool.ntp.org iburst` | Список NTP-серверов (при ntp_manage_config: true) |
| `unsafe_show_logs` | `false` | Управление no_log; совпадает с non-CI значением role default |
| `allow_unsupported_distribution_setup` | `false` | Разрешить установку на неподдерживаемых ОС |

## all.yml — закомментированные (действует role default)

Ключевые примеры: `access_ip`, `loadbalancer_apiserver` (address/port), `loadbalancer_apiserver_localhost`, `loadbalancer_apiserver_type` (nginx/haproxy), `disable_host_nameservers`, `upstream_dns_servers`, `cloud_provider` (только `external` после K8s 1.31), `external_cloud_provider` (openstack/vsphere/oci/huaweicloud/hcloud/manual), прокси-набор (`http_proxy`, `https_proxy`, `https_proxy_cert_file`, `no_proxy`, `additional_no_proxy`, `skip_http_proxy_on_os_packages`), `download_validate_certs`, `cert_management` (script/none), `ignore_assert_errors`, `kube_read_only_port` (10255), `download_container`, `deploy_container_engine`, семь `rh_subscription_*`, `ping_access_ip`, `sysctl_file_path`, `sysctl_ignore_unknown_keys`, `kube_webhook_token_auth_url`, `kube_webhook_token_auth_ca_data`. Полный список с примерами значений — в [[versions/v2.31.0/inventory/all|all.yaml]].

## etcd.yml

| Переменная | Значение | is_set | Комментарий |
|------------|----------|--------|-------------|
| `etcd_data_dir` | `/var/lib/etcd` | да | Каталог данных etcd (совпадает с role default) |
| `container_manager` | `containerd` | нет | Runtime для etcd; если не задан — берётся из Kubespray defaults, а не из k8s-cluster.yml |
| `etcd_deployment_type` | `host` | да | Тип развёртывания etcd (host/docker); совпадает с role default |

## docker.yml — заданные переменные

| Переменная | Значение | Комментарий |
|------------|----------|-------------|
| `docker_container_storage_setup` | `false` | Настройка devicemapper на CentOS7/RedHat7 |
| `docker_dns_servers_strict` | `false` | При >3 nameserver — использовать первые 3, иначе ошибка |
| `docker_daemon_graph` | `/var/lib/docker` | Каталог данных Docker |
| `docker_iptables_enabled` | `"false"` | Опция iptables демона (строка) |
| `docker_log_opts` | `--log-opt max-size=50m --log-opt max-file=5` | Ротация логов: 50m, 5 файлов |
| `docker_bin_dir` | `/usr/bin` | Каталог бинарников Docker |
| `docker_rpm_keepcache` | `1` | Сохранять пакеты docker после установки |

Закомментированы (примеры): `docker_storage_options` (`-s overlay2`), `docker_container_storage_setup_devs` (`/dev/vdb`), `docker_cgroup_driver` (systemd/cgroupfs), `docker_insecure_registries`, `docker_registry_mirrors`, `docker_mount_flags`, `docker_options`.

## containerd.yml и cri-o.yml

Все переменные закомментированы — фактические значения берутся из ролей (`roles/container-engine/containerd/defaults/main.yml`, `roles/container-engine/cri-o/...`). Полный справочник containerd-defaults — в [[versions/v2.31.0/variables/container-runtime|container-runtime.yaml]].

Обратите внимание: в `containerd.yml` пример `containerd_snapshotter: "native"` отличается от role default `overlayfs` — это лишь закомментированная подсказка, действует значение роли.

## offline.yml — offline / air-gapped установка

Файл целиком закомментирован (60 переменных) и предназначен для развёртывания без доступа в интернет. Логически делится на:

- **Приватный реестр образов и HTTP-репозитории**: `registry_host`, `files_repo`, `yum_repo`, `debian_repo`, `ubuntu_repo`.
- **Переопределение репозиториев образов**: `kube_image_repo`, `gcr_image_repo`, `github_image_repo`, `docker_image_repo`, `quay_image_repo` — все на `{{ registry_host }}`.
- **Компоненты Kubernetes**: `kubeadm_download_url`, `kubectl_download_url`, `kubelet_download_url` через `{{ files_repo }}`.
- **Вариант 1 — переопределение всего репозитория бинарников**: `github_url`, `dl_k8s_io_url`, `storage_googleapis_url`, `get_helm_url` (прокси/зеркала).
- **Вариант 2 — переопределение отдельных бинарников** через `{{ files_repo }}`: `cni_download_url`, `crictl_download_url`, `etcd_download_url`, `calicoctl_download_url`, `calico_crds_download_url`, `ciliumcli_download_url`, `helm_download_url`, `crun_download_url`, `kata_containers_download_url`, `cri_dockerd_download_url`, `runc_download_url`, `crio_download_base`/`crio_download_crio`/`crio_download_url`, `skopeo_download_url`, `containerd_download_url`, `nerdctl_download_url`, `gvisor_runsc_download_url`, `gvisor_containerd_shim_runsc_download_url`. Многие условны (например, `helm_download_url` — только при `helm_enabled: true`, `crio_*` — только при `container_manager: crio`).
- **Репозитории пакетов ОС**: наборы `docker_*_repo_base_url`/`_gpgkey` и `containerd_*_repo_base_url`/`_gpgkey`/`_repokey` для CentOS/RHEL/AlmaLinux, Fedora, Debian, Ubuntu, плюс `rhel_enable_repos`.

Механика: `files_repo` и `registry_host` задают базовые адреса, а остальные переменные собирают из них конкретные URL с подстановкой версий компонентов и `image_arch`.

## Проверка расхождений (раздел 6.2)

Сверялись только заданные (is_set: true) переменные, присутствующие в проверенных срезах defaults (`variables/{etcd,container-runtime,download,k8s-cluster}.yaml`): `bin_dir`, `etcd_data_dir`, `etcd_deployment_type`, `docker_dns_servers_strict`, `docker_daemon_graph`, `docker_iptables_enabled`, `docker_log_opts`, `docker_bin_dir`, `unsafe_show_logs`.

**Все значения совпадают с role defaults** (для `unsafe_show_logs` — с разрешённым non-CI значением `false`). Расхождений не выявлено.
