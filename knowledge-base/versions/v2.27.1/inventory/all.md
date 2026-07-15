---
project: kubespray
kubespray_version: v2.27.1
git_commit: 45140b5
source_type: inventory
source_path: inventory/sample/group_vars/all/
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.27.1
retrieved_at: 2026-07-15
topics:
  - inventory
  - all
  - offline
reliability: authoritative
---

# Общие настройки инвентаря (group_vars/all) — v2.27.1

Разбор общих (не относящихся к облачным провайдерам) файлов sample-инвентаря
`inventory/sample/group_vars/all/`. Эти переменные применяются ко **всем** хостам
инвентаря. Источник истины — машиночитаемый справочник
[[versions/v2.27.1/inventory/all|all.yaml]] в этом же каталоге; данная заметка — человекочитаемое изложение.

Срез версии: [[versions/v2.27.1/README|Срез v2.27.1]].

> Обозначения: **задано** — переменная в sample раскомментирована (реально применяется);
> **пример** — переменная присутствует лишь как закомментированный образец.

## Обзор файлов

| Файл | Назначение | Реально заданных переменных |
|------|------------|-----------------------------|
| `all.yml` | Базовые настройки всех хостов: bin_dir, балансировщик apiserver, upstream DNS, proxy, NTP, RHEL-подписка, webhook-аутентификация | 11 |
| `etcd.yml` | Каталог данных, тип развёртывания и (опц.) container runtime для нод etcd | 2 |
| `containerd.yml` | Тонкая настройка containerd (все переменные — примеры) | 0 |
| `cri-o.yml` | Реестры и аутентификация CRI-O (все примеры) | 0 |
| `docker.yml` | Настройки Docker daemon: storage, логи, DNS, реестры | 7 |
| `coreos.yml` | Авто-обновление CoreOS (пример) | 0 |
| `offline.yml` | Offline/air-gapped: перенаправление всех загрузок на внутренние зеркала (все примеры) | 0 |

Всего в справочнике `all.yaml`: **135 переменных**, из них реально задано — **20**.

## all.yml — базовые настройки

Файл содержит общекластерные параметры. Реально заданы 11 переменных, остальное — примеры.

### Балансировщик apiserver

| Переменная | Значение | Статус | Смысл |
|------------|----------|--------|-------|
| `loadbalancer_apiserver` | `{address, port}` | пример | Внешний LB apiserver (адрес+порт) |
| `loadbalancer_apiserver_localhost` | `true` | пример | Локальный LB (nginx/haproxy) на нодах |
| `loadbalancer_apiserver_type` | `nginx` | пример | Тип локального LB: nginx или haproxy |
| `loadbalancer_apiserver_port` | `6443` | **задано** | Порт локального LB (должен быть 6443) |
| `loadbalancer_apiserver_healthcheck_port` | `8081` | **задано** | Порт liveness-проверки nginx |

### Upstream DNS

`upstream_dns_servers` (`[8.8.8.8, 8.8.4.4]`, default `[]`) и
`disable_host_nameservers` (`false`) даны как примеры.

### Proxy

Полностью закомментированный блок (примеры): `http_proxy`, `https_proxy`,
`https_proxy_cert_file`, `no_proxy`, `additional_no_proxy`,
`skip_http_proxy_on_os_packages`, `download_validate_certs`. Единственная реально
заданная переменная блока — `no_proxy_exclude_workers: false`.

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
`kube_read_only_port`, `sysctl_file_path`, `ping_access_ip` даны как примеры.

> [!note] Отличие от v2.29.1
> В `all.yml` тега v2.27.1 **отсутствует** переменная `sysctl_ignore_unknown_keys`
> (в sample есть только `sysctl_file_path`).

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
`overlayfs`** (пример в sample иллюстративен, но, будучи закомментированным,
на кластер не влияет).

## cri-o.yml и coreos.yml

Только примеры: `crio_insecure_registries`, `crio_registry_auth` (CRI-O),
`coreos_auto_upgrade` (CoreOS). Ничего реально не задаётся.

## docker.yml

Реально заданы 7 переменных:

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
     kata, cri-dockerd, runc, cri-o, skopeo, containerd, nerdctl, gVisor, **krew** и др.).
- **Репозитории пакетов ОС для движков**: `docker_*_repo_*` и `containerd_*_repo_*`
  для RedHat/Fedora/Debian/Ubuntu, плюс `rhel_enable_repos`.

> [!note] Отличия offline.yml от v2.29.1
> - В v2.27.1 присутствует `krew_download_url` (при `krew_enabled: true`).
> - Шаблоны `*_download_url` для Kubernetes-бинарников и ряда компонентов используют
>   версию **без префикса `v`** (например `.../release/{{ kube_version }}/...`,
>   `cri-o.{{ image_arch }}.{{ crio_version }}.tar.gz`), тогда как в v2.29.1 добавлен
>   префикс `v` (`.../release/v{{ kube_version }}/...`).

## Расхождения с defaults ролей

По правилу раздела 6.2 сверялись только реально заданные (is_set: true) переменные,
присутствующие в справочниках defaults. Значения совпадают у `bin_dir`, `ntp_enabled`,
`ntp_manage_config`, `etcd_data_dir`, `etcd_deployment_type`, `docker_bin_dir`,
`container_manager` (наследуемый) и, что важно для v2.27.1, у `unsafe_show_logs`.

> [!important] unsafe_show_logs в v2.27.1
> В отличие от v2.29.1, в v2.27.1 default роли `unsafe_show_logs` — жёсткий `false`
> (`roles/kubespray-defaults/defaults/main/download.yml`), поэтому значение sample
> (`false`) полностью **совпадает** с defaults. Расхождения формы, отмеченного в
> v2.29.1, здесь **нет**.

**Расхождений действующих значений не обнаружено.** Подробности:
[[versions/v2.27.1/discrepancies|Расхождения inventory vs defaults]].
