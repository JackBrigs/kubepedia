---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: inventory
source_paths:
  - inventory/sample/group_vars/all/all.yml
  - inventory/sample/group_vars/all/etcd.yml
  - inventory/sample/group_vars/all/containerd.yml
  - inventory/sample/group_vars/all/cri-o.yml
  - inventory/sample/group_vars/all/docker.yml
  - inventory/sample/group_vars/all/coreos.yml
  - inventory/sample/group_vars/all/offline.yml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0
retrieved_at: 2026-07-14
topics:
  - inventory
  - all
  - offline
reliability: authoritative
---

# Общий inventory group_vars/all в v2.30.0

Разбор общих (не облачных) файлов `inventory/sample/group_vars/all/` тега **v2.30.0** (commit `f4ccdb5`). Источник истины — машиночитаемый справочник [[versions/v2.30.0/inventory/all|all.yaml]]; данная заметка — только изложение. Связь со срезом: [[versions/v2.30.0/README|Срез v2.30.0]].

Переменные из `group_vars/all` применяются ко **всем** хостам инвентаря. В sample-файлах большинство переменных **закомментировано** (пример «значения по умолчанию»); фактическое значение при этом берётся из `roles/*/defaults`. Раскомментированные переменные (`is_set: true`) задают значение явно.

Соглашение в справочнике:

- `is_set: true` — переменная в sample раскомментирована и задаёт значение;
- `is_set: false` — переменная закомментирована, `sample_value` содержит пример из комментария (`commented: ...`).

## Обзор по файлам

| Файл | Назначение | Раскомментировано (is_set: true) |
| --- | --- | --- |
| `all.yml` | Базовые параметры узлов: каталоги, локальный балансировщик apiserver, DNS, proxy, сертификаты, подписка RHEL, sysctl, webhook-token-auth, NTP | 11 переменных |
| `etcd.yml` | Развёртывание etcd (каталог данных, тип развёртывания, движок контейнеров для etcd) | 2 переменные |
| `containerd.yml` | Тонкая настройка containerd (пути, рантаймы, debug, метрики, реестры) | 0 (всё закомментировано) |
| `cri-o.yml` | Insecure-реестры и аутентификация CRI-O | 0 (всё закомментировано) |
| `docker.yml` | Параметры docker-движка (актуальны при `container_manager: docker`) | 7 переменных |
| `coreos.yml` | Автообновление CoreOS | 0 (всё закомментировано) |
| `offline.yml` | Offline/air-gapped: приватный реестр, репозитории файлов и пакетов, переопределение URL загрузок | 0 (всё закомментировано) |

## all.yml — ключевые настройки

Раскомментированные по умолчанию переменные:

| Переменная | Значение | Смысл |
| --- | --- | --- |
| `bin_dir` | `/usr/local/bin` | Каталог установки бинарников |
| `loadbalancer_apiserver_port` | `6443` | Порт локального балансировщика apiserver (обязан быть 6443) |
| `loadbalancer_apiserver_healthcheck_port` | `8081` | Порт liveness-проверки nginx-балансировщика |
| `no_proxy_exclude_workers` | `false` | Включать воркеры в `no_proxy` (true — только control plane) |
| `kube_webhook_token_auth` | `false` | Webhook token authentication на apiserver |
| `kube_webhook_token_auth_url_skip_tls_verify` | `false` | Пропуск проверки TLS URL webhook-auth |
| `ntp_enabled` | `false` | Запуск сервиса ntpd/chrony |
| `ntp_manage_config` | `false` | Управление конфигурацией NTP |
| `ntp_servers` | `0..3.pool.ntp.org iburst` | Список NTP-серверов |
| `unsafe_show_logs` | `false` | Атрибут no_log; true раскрывает приватные данные в выводе |
| `allow_unsupported_distribution_setup` | `false` | Разрешить установку на неподдерживаемых ОС |

Важные закомментированные (значение берётся из defaults):

- **Балансировщик apiserver:** `loadbalancer_apiserver` (внешний LB — адрес/порт), `apiserver_loadbalancer_domain_name`, `loadbalancer_apiserver_localhost`, `loadbalancer_apiserver_type` (`nginx`/`haproxy`).
- **Proxy:** `http_proxy`, `https_proxy`, `https_proxy_cert_file`, `no_proxy`, `additional_no_proxy`, `skip_http_proxy_on_os_packages`, `download_validate_certs`.
- **DNS:** `disable_host_nameservers`, `upstream_dns_servers`.
- **Облако:** `cloud_provider` (только `external` после K8s v1.31), `external_cloud_provider` (openstack, vsphere, oci, huaweicloud, hcloud, manual).
- **Сертификаты и проверки:** `cert_management` (`script`/`none`), `ignore_assert_errors`, `ping_access_ip`.
- **Прочее:** `access_ip`, `kube_read_only_port` (10255, выключен), `download_container`, `deploy_container_engine`, подписка RHEL (`rh_subscription_*`), sysctl (`sysctl_file_path`, `sysctl_ignore_unknown_keys`).

## etcd.yml

| Переменная | Значение | is_set | Смысл |
| --- | --- | --- | --- |
| `etcd_data_dir` | `/var/lib/etcd` | true | Каталог данных etcd (WAL и snapshot) |
| `etcd_deployment_type` | `host` | true | `host` — бинарник как systemd-сервис; при `container_manager: docker` ставить `docker` |
| `container_manager` | `containerd` (закомм.) | false | Движок контейнеров именно для etcd-узлов; если не задан — наследуется из Kubespray defaults (`containerd`), а не из `k8s-cluster.yml` |

## containerd.yml

Все переменные закомментированы; значения по умолчанию — в `roles/container-engine/containerd/defaults/main.yml` (см. [[versions/v2.30.0/variables/container-runtime|container-runtime.yaml]]). Файл демонстрирует тонкую настройку: пути (`containerd_storage_dir`, `containerd_state_dir`), рантаймы (`containerd_default_runtime`, `containerd_runc_runtime`, `containerd_additional_runtimes` — пример Kata), gRPC-лимиты, debug-сокет, метрики, зеркала и аутентификацию реестров (`containerd_registries_mirrors`, `containerd_registry_auth`).

> Примечание: в примере `containerd_snapshotter: "native"`, тогда как фактический default роли — `overlayfs`. Поскольку переменная закомментирована, это не расхождение фактических значений, но пример в inventory отличается от default.

## cri-o.yml

Два закомментированных параметра: `crio_insecure_registries` (список insecure-реестров) и `crio_registry_auth` (registry/username/password).

## docker.yml

Актуальны только при `container_manager: docker`. Раскомментированные:

| Переменная | Значение | Смысл |
| --- | --- | --- |
| `docker_container_storage_setup` | `false` | devicemapper через docker-storage-setup (CentOS7/RHEL7) |
| `docker_dns_servers_strict` | `false` | true — использовать только первые 3 nameserver |
| `docker_daemon_graph` | `/var/lib/docker` | Каталог данных Docker |
| `docker_iptables_enabled` | `"false"` | Управление iptables демоном Docker |
| `docker_log_opts` | `--log-opt max-size=50m --log-opt max-file=5` | Ротация логов: 50m, 5 файлов |
| `docker_bin_dir` | `/usr/bin` | Каталог бинарников Docker |
| `docker_rpm_keepcache` | `1` | Сохранять rpm-пакеты docker после установки |

Закомментированные: `docker_storage_options`, `docker_container_storage_setup_devs`, `docker_cgroup_driver`, `docker_insecure_registries`, `docker_registry_mirrors`, `docker_mount_flags`, `docker_options`.

## coreos.yml

Единственный параметр `coreos_auto_upgrade` (закомментирован, по умолчанию `true`) — автообновление CoreOS.

## offline.yml — offline / air-gapped развёртывание

Все переменные закомментированы; значения по умолчанию — в `roles/kubespray_defaults/defaults/main/download.yml` (см. [[versions/v2.30.0/variables/download|download.yaml]]). Файл — основной инструмент для развёртывания без прямого доступа к интернету.

Базовые точки подмены:

- **Приватный реестр образов:** `registry_host`; на него переопределяются `kube_image_repo`, `gcr_image_repo`, `github_image_repo`, `docker_image_repo`, `quay_image_repo`.
- **Внутренние репозитории файлов:** `files_repo` (бинарники/архивы), `yum_repo`, `debian_repo`, `ubuntu_repo` (пакеты ОС).

Два подхода к бинарникам:

1. **Переопределить целые репозитории** — базовые URL: `github_url`, `dl_k8s_io_url`, `storage_googleapis_url`, `get_helm_url` (заменяются на прокси/зеркала).
2. **Переопределить конкретные бинарники** через `files_repo` — `*_download_url`: kubeadm/kubectl/kubelet, `cni_download_url`, `crictl_download_url`, `etcd_download_url`, `calicoctl_download_url`, `calico_crds_download_url`, `ciliumcli_download_url`, `helm_download_url`, `crun_download_url`, `kata_containers_download_url`, `cri_dockerd_download_url`, `runc_download_url`, `crio_download_url`/`skopeo_download_url`, `containerd_download_url`/`nerdctl_download_url`, gVisor (`gvisor_runsc_download_url`, `gvisor_containerd_shim_runsc_download_url`).

Многие URL применимы только при соответствующем выборе: etcd — при `etcd_deployment_type: host`; calico/cilium — при соответствующем CNI; crun/kata/gvisor — при их `*_enabled`; cri-dockerd — при `container_manager: docker`; cri-o/skopeo — при `container_manager: crio`; containerd/nerdctl/runc — при `container_manager: containerd`.

Репозитории пакетов ОС (Docker CE и containerd) заданы отдельными переменными для RHEL-семейства (`rhel_enable_repos`, `docker_rh_repo_*`), Fedora (`docker_fedora_repo_*`, `containerd_fedora_repo_*`), Debian (`docker_debian_repo_*`, `containerd_debian_repo_*` + `containerd_debian_repo_repokey`) и Ubuntu (`docker_ubuntu_repo_*`, `containerd_ubuntu_repo_*` + `containerd_ubuntu_repo_repokey`).

## Расхождения с defaults

Сверка раскомментированных (`is_set: true`) переменных со справочниками `variables/{etcd, container-runtime, download, k8s-cluster}.yaml` показала: значения совпадают у `bin_dir`, `etcd_data_dir`, `etcd_deployment_type`, `docker_dns_servers_strict`, `docker_daemon_graph`, `docker_iptables_enabled`, `docker_log_opts`, `docker_bin_dir`.

Единственное текстовое расхождение — `unsafe_show_logs`: в sample жёстко `false`, в defaults вычисляется из переменной окружения `CI_PROJECT_URL` (`roles/kubespray_defaults/defaults/main/download.yml`). Вне CI Kubespray оба варианта дают `false`, поэтому расхождение несущественно. Приоритет — за кодом роли.
