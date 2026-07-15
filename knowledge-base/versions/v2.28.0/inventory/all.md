---
project: kubespray
kubespray_version: v2.28.0
git_commit: 63cdf87
source_type: inventory
source_path: inventory/sample/group_vars/all/
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.28.0
retrieved_at: 2026-07-15
topics:
  - inventory
  - all
  - offline
reliability: authoritative
---

# Общие настройки инвентаря (group_vars/all) — v2.28.0

Разбор общих (не относящихся к облачным провайдерам) файлов sample-инвентаря
`inventory/sample/group_vars/all/`. Эти переменные применяются ко **всем** хостам
инвентаря. Источник истины — машиночитаемый справочник
`all.yaml` в этом же каталоге; данная заметка — человекочитаемое изложение.

Срез версии: [[versions/v2.28.0/README|Срез v2.28.0]].

> Обозначения: **задано** — переменная в sample раскомментирована (реально применяется);
> **пример** — переменная присутствует лишь как закомментированный образец.

## Обзор файлов

| Файл | Назначение | Реально заданных переменных |
|------|------------|-----------------------------|
| `all.yml` | Базовые настройки всех хостов: bin_dir, балансировщик apiserver, upstream DNS, proxy, NTP, RHEL-подписка, webhook-аутентификация | 10 |
| `etcd.yml` | Каталог данных, тип развёртывания и (опц.) container runtime для нод etcd | 2 |
| `containerd.yml` | Тонкая настройка containerd (все переменные — примеры) | 0 |
| `cri-o.yml` | Реестры и аутентификация CRI-O (все примеры) | 0 |
| `docker.yml` | Настройки Docker daemon: storage, логи, DNS, реестры | 6 |
| `coreos.yml` | Авто-обновление CoreOS (пример) | 0 |
| `offline.yml` | Offline/air-gapped: перенаправление всех загрузок на внутренние зеркала (все примеры) | 0 |
| `group_vars/etcd.yml` | Тонкая настройка etcd для группы `etcd` (все примеры) — отдельный файл уровня группы, не `all/etcd.yml` | 0 |

## all.yml — базовые настройки

Файл содержит общекластерные параметры. Реально заданы 10 переменных, остальное — примеры.

### Балансировщик apiserver

| Переменная | Значение | Статус | Смысл |
|------------|----------|--------|-------|
| `loadbalancer_apiserver` | `{address, port}` | пример | Внешний LB apiserver (адрес+порт) |
| `loadbalancer_apiserver_localhost` | `true` | пример | Локальный LB (nginx/haproxy) на нодах |
| `loadbalancer_apiserver_type` | `nginx` | пример | Тип локального LB: nginx или haproxy |
| `loadbalancer_apiserver_port` | `6443` | **задано** | Порт локального LB (должен быть 6443) |
| `loadbalancer_apiserver_healthcheck_port` | `8081` | **задано** | Порт liveness-проверки nginx |

Если внешний `loadbalancer_apiserver` не задан, в defaults ролей автоматически
включается локальный балансировщик (`loadbalancer_apiserver_localhost` вычисляется
как `{{ loadbalancer_apiserver is not defined }}`).

### Upstream DNS

| Переменная | Значение | Статус | Смысл |
|------------|----------|--------|-------|
| `upstream_dns_servers` | `[8.8.8.8, 8.8.4.4]` | пример | Внешние DNS для CoreDNS (default — `[]`) |
| `disable_host_nameservers` | `false` | пример | Не включать nameserver'ы хоста на стадии dns_late |

### Proxy

Полностью закомментированный блок (примеры): `http_proxy`, `https_proxy`,
`https_proxy_cert_file`, `no_proxy`, `additional_no_proxy`,
`skip_http_proxy_on_os_packages`, `download_validate_certs`. Единственная реально
заданная переменная блока — `no_proxy_exclude_workers: false` (включать в no_proxy
только контрол-плейн, чтобы не рестартовать движок на воркерах при их добавлении/удалении).

### NTP

| Переменная | Значение | Статус | Смысл |
|------------|----------|--------|-------|
| `ntp_enabled` | `false` | **задано** | Запускать/включать службу NTP |
| `ntp_manage_config` | `false` | **задано** | Управлять конфигом NTP через Kubespray |
| `ntp_servers` | `["0..3.pool.ntp.org iburst"]` | **задано** | Список NTP-серверов (при manage_config: true) |

### Прочее заданное в all.yml

`bin_dir: /usr/local/bin`, `kube_webhook_token_auth: false`,
`kube_webhook_token_auth_url_skip_tls_verify: false`, `unsafe_show_logs: false`,
`allow_unsupported_distribution_setup: false`. Блок RHEL-подписки
(`rh_subscription_*`) и параметры `access_ip`, `cloud_provider`,
`external_cloud_provider`, `cert_management`, `ignore_assert_errors`,
`kube_read_only_port`, `sysctl_*`, `ping_access_ip` даны как примеры.

## etcd.yml

| Переменная | Значение | Статус | Смысл |
|------------|----------|--------|-------|
| `etcd_data_dir` | `/var/lib/etcd` | **задано** | Каталог данных etcd |
| `etcd_deployment_type` | `host` | **задано** | Тип развёртывания: host / docker / kubeadm |
| `container_manager` | `containerd` | пример | Отдельный runtime для нод etcd (иначе наследуется из defaults) |

## containerd.yml

Все переменные — закомментированные примеры; полное описание с реальными значениями
по умолчанию см. в `variables/container-runtime.yaml`. Важная деталь: в качестве примера
`containerd_snapshotter` показан как `native`, тогда как **фактический default роли —
`overlayfs`** (пример в sample устарел/иллюстративен, но, будучи закомментированным,
на кластер не влияет).

## cri-o.yml и coreos.yml

Только примеры: `crio_insecure_registries`, `crio_registry_auth` (CRI-O),
`coreos_auto_upgrade` (CoreOS). Ничего реально не задаётся.

## docker.yml

Реально заданы 6 переменных:

| Переменная | Значение | Смысл |
|------------|----------|-------|
| `docker_container_storage_setup` | `false` | devicemapper через docker-storage-setup (CentOS7/RHEL7) |
| `docker_dns_servers_strict` | `false` | при >3 nameserver использовать первые 3, не падать |
| `docker_daemon_graph` | `/var/lib/docker` | каталог данных Docker |
| `docker_iptables_enabled` | `"false"` | управление iptables со стороны Docker |
| `docker_log_opts` | `--log-opt max-size=50m --log-opt max-file=5` | ротация логов |
| `docker_bin_dir` | `/usr/bin` | каталог бинарников Docker |
| `docker_rpm_keepcache` | `1` | кэшировать rpm-пакеты Docker |

Примеры: `docker_storage_options`, `docker_container_storage_setup_devs`,
`docker_cgroup_driver`, `docker_insecure_registries`, `docker_registry_mirrors`,
`docker_mount_flags`, `docker_options`.

## offline.yml — offline / air-gapped установка

Назначение файла — развёртывание кластера **без доступа в интернет**. Все переменные
закомментированы; администратор раскомментирует нужные, чтобы перенаправить загрузки
на внутренние зеркала. Логически файл делится на блоки:

- **Приватные репозитории-базы**: `registry_host` (реестр образов), `files_repo`
  (HTTP-репозиторий бинарников), `yum_repo` / `debian_repo` / `ubuntu_repo`
  (пакеты ОС).
- **Переопределение реестров образов**: `kube_image_repo`, `gcr_image_repo`,
  `github_image_repo`, `docker_image_repo`, `quay_image_repo` → `{{ registry_host }}`.
- **Два способа переопределения загрузок бинарников**:
  1. *Целиком репозитории* — `github_url`, `dl_k8s_io_url`, `storage_googleapis_url`,
     `get_helm_url` на прокси/зеркала.
  2. *Отдельные бинарники* — десятки `*_download_url` через `{{ files_repo }}`
     (kubeadm/kubectl/kubelet, cni, crictl, etcd, calicoctl, cilium-cli, helm, crun,
     kata, cri-dockerd, runc, cri-o, skopeo, containerd, nerdctl, gVisor и др.).
     Многие берутся под условием (например, `crio_download_url` — только при
     `container_manager: crio`).
- **Репозитории пакетов ОС для движков**: `docker_*_repo_*` и `containerd_*_repo_*`
  для RedHat/Fedora/Debian/Ubuntu, плюс `rhel_enable_repos`.

## group_vars/etcd.yml — тонкая настройка etcd (группа etcd)

Отдельный файл `inventory/sample/group_vars/etcd.yml` (уровень группы `etcd`, **не** `all/etcd.yml`). Все переменные закомментированы (примеры) и относятся к тюнингу etcd: авто-компакция (`etcd_compaction_retention`), метрики (`etcd_metrics`), лимит памяти и квота backend (`etcd_memory_limit`, `etcd_quota_backend_bytes`), максимальный размер запроса (`etcd_max_request_bytes`), аутентификация peer-клиентов (`etcd_peer_client_auth`) и блок экспериментальной распределённой трассировки (`etcd_experimental_*`).

> [!note] Отличие от v2.29.1
> В v2.29.1 этот файл **удалён** — соответствующие параметры перенесены в defaults роли `etcd`. В v2.28.0 файл ещё присутствует в sample-inventory.

## Расхождения с defaults ролей

По правилу раздела 6.2 сверялись только реально заданные (is_set: true) переменные,
присутствующие в справочниках defaults. Значения совпадают у `bin_dir`, `ntp_enabled`,
`etcd_data_dir`, `etcd_deployment_type`, `docker_dns_servers_strict`,
`docker_daemon_graph`, `docker_iptables_enabled`, `docker_log_opts`, `docker_bin_dir`,
`unsafe_show_logs`.

**Расхождений действующих значений не обнаружено.** В частности, `unsafe_show_logs` в
`roles/kubespray_defaults/defaults/main/download.yml` тега v2.28.0 задан прямым `false`
и совпадает с sample (в отличие от v2.29.1, где default вычисляется по CI-переменной
окружения — там это давало расхождение формы). Подробнее см. [[versions/v2.28.0/discrepancies|discrepancies.md]] среза.
