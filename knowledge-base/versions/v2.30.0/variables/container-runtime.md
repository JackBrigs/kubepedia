---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: code
source_path: versions/v2.30.0/variables/container-runtime.yaml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0
retrieved_at: 2026-07-14
topics:
  - container-runtime
  - containerd
reliability: authoritative
---

# Рантайм контейнеров в v2.30.0 (containerd)

Заметка описывает переменные выбора рантайма контейнеров и полную конфигурацию **containerd** — рантайма по умолчанию в Kubespray v2.30.0 (commit `f4ccdb5`). Источник истины — YAML-справочник [[versions/v2.30.0/variables/container-runtime|container-runtime.yaml]]. Значения по умолчанию приведены строго из кода тега; Jinja-выражения даны дословно.

## Выбор рантайма

Рантайм задаётся переменной `container_manager` (по умолчанию `containerd`). От неё производно вычисляются CRI-сокет, движок на localhost и включение NRI.

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `container_manager` | `containerd` | Движок контейнеров (CRI). Допустимо: `containerd`, `crio`, `docker` |
| `deploy_container_engine` | `{{ 'k8s_cluster' in group_names or etcd_deployment_type == 'docker' }}` | Разворачивать ли движок на хосте |
| `container_manager_on_localhost` | `{{ container_manager }}` | Движок на управляющем хосте (для загрузки образов) |
| `cri_socket` | вычисляется из `container_manager`; для containerd — `unix:///var/run/containerd/containerd.sock` | Путь к CRI-сокету для kubeadm/kubelet |
| `nri_enabled` | `{{ container_manager == 'containerd' }}` | Node Resource Interface, включён только для containerd |

Логика перехода между рантаймами реализована в `roles/container-engine/validate-container-engine/tasks/main.yml`: роль обнаруживает установленные `containerd.service`, `docker.service`, `crio.service` и при несоответствии `container_manager` выполняет drain узла, останов kubelet и удаление лишнего рантайма (задачи `reset` соответствующих ролей). Для Flatcar и ostree-систем удаление не выполняется.

### Флаги дополнительных рантаймов

Следующие флаги включают дополнительные рантаймы поверх основного `container_manager` (по умолчанию все `false`):

| Переменная | Требование | Комментарий |
|---|---|---|
| `kata_containers_enabled` | `container_manager` != docker | Kata Containers |
| `gvisor_enabled` | `container_manager` docker или containerd | gVisor |
| `runc_enabled` | `container_manager=crio` | runc как доп. рантайм crio |
| `crun_enabled` | `container_manager=crio` | crun |
| `youki_enabled` | `container_manager=crio` | youki |

## Версии containerd-стека

Версии вычисляются как первый ключ соответствующих словарей контрольных сумм в `roles/kubespray_defaults/vars/main/checksums.yml`. Фактические значения для тега v2.30.0:

| Переменная | Jinja-выражение | Фактическое значение в v2.30.0 |
|---|---|---|
| `containerd_version` | `{{ (containerd_archive_checksums['amd64'] \| dict2items)[0].key }}` | `2.2.1` |
| `runc_version` | `{{ (runc_checksums['amd64'] \| dict2items)[0].key }}` | `1.3.4` |
| `nerdctl_version` | `{{ (nerdctl_archive_checksums['amd64'] \| dict2items)[0].key }}` | `2.2.1` |
| `crictl_version` | `{{ (crictl_checksums['amd64'].keys() \| select('version', kube_major_next_version, '<'))[0] }}` | зависит от версии K8s (первый ключ словаря — `1.34.0`), `reliability: unconfirmed` |
| `docker_containerd_version` | `1.6.32` | только при `container_manager == 'docker'` |

`containerd_static_binary: false` — при `true` используется статический бинарник (для старых дистрибутивов, например Debian 11).

## Ключевые переменные containerd

### Пути и бинарники

| Переменная | Значение по умолчанию |
|---|---|
| `containerd_bin_dir` | `{{ bin_dir }}` (то есть `/usr/local/bin`) |
| `containerd_storage_dir` | `/var/lib/containerd` |
| `containerd_state_dir` | `/run/containerd` |
| `containerd_systemd_dir` | `/etc/systemd/system/containerd.service.d` |
| `containerd_cfg_dir` | `/etc/containerd` |
| `containerd_package` | `containerd.io` |

### Конфигурация рантайма

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `containerd_default_runtime` | `runc` | Рантайм по умолчанию в CRI-плагине |
| `containerd_snapshotter` | `overlayfs` | Снапшоттер |
| `containerd_use_systemd_cgroup` | `true` | systemd cgroup driver (опция `SystemdCgroup` рантайма runc) |
| `containerd_runc_runtime` | тип `io.containerd.runc.v2`, `base_runtime_spec: cri-base.json`, `BinaryName: {{ bin_dir }}/runc` | Определение рантайма runc |
| `containerd_additional_runtimes` | `[]` | Доп. рантаймы (например, kata) |
| `containerd_oom_score` | `0` | OOMScoreAdjust (фактически containerd ставит -999, см. PR #9275) |
| `containerd_base_runtime_spec_rlimit_nofile` | `65535` | RLIMIT_NOFILE в cri-base.json |
| `containerd_discard_unpacked_layers` | `true` | Экономия диска, только containerd < 2.1 |
| `containerd_image_pull_progress_timeout` | `5m` | Таймаут прогресса загрузки образа |
| `containerd_grpc_max_recv_message_size` / `containerd_grpc_max_send_message_size` | `16777216` | Лимиты gRPC-сообщений (16 МиБ) |
| `containerd_max_container_log_line_size` | `16384` | Макс. размер строки лога контейнера |

### Реестры образов

`containerd_registries_mirrors` по умолчанию содержит зеркало для `docker.io` → `https://registry-1.docker.io` с возможностями `pull`, `resolve` и `skip_verify: false`. `containerd_registry_auth: []` — аутентификация в реестрах (пусто по умолчанию).

### Безопасность и функции

| Переменная | По умолчанию |
|---|---|
| `containerd_enable_unprivileged_ports` | `false` |
| `containerd_enable_unprivileged_icmp` | `false` |
| `containerd_enable_selinux` | `false` |
| `containerd_disable_apparmor` | `false` |
| `containerd_tolerate_missing_hugetlb_controller` | `true` |
| `containerd_disable_hugetlb_controller` | `true` |
| `enable_cdi` | `false` |

### Лимиты systemd-сервиса

`containerd_limit_proc_num: infinity`, `containerd_limit_core: infinity`, `containerd_limit_open_file_num: 1048576`, `containerd_limit_mem_lock: infinity`.

### Отладка, метрики, трассировка

Отладка (`containerd_debug_address`, `containerd_debug_level: info`, `containerd_debug_format`, `containerd_debug_uid/gid: 0`), метрики (`containerd_metrics_address`, `containerd_metrics_grpc_histogram: false`) и трассировка OpenTelemetry (`containerd_tracing_enabled: false`, `containerd_tracing_endpoint: [::]:4317`, `containerd_tracing_protocol: grpc`, `containerd_tracing_sampling_ratio: 1.0`, `containerd_tracing_service_name: containerd`) по умолчанию выключены/пусты.

### Дополнительная конфигурация

- `containerd_extra_args: ''` — произвольный текст дословно в `config.toml`.
- `containerd_extra_runtime_args: {}` — доп. опции в секцию `[plugins."io.containerd.cri.v1.runtime"]`.
- `containerd_supported_distributions` — список поддерживаемых дистрибутивов ОС.

### runc

`runc_bin_dir: {{ bin_dir }}`, `runc_package_name: runc` (`roles/container-engine/runc/defaults/main.yml`).

## Непроиндексированные рантаймы

В этом срезе подробно разобран только **containerd** (рантайм по умолчанию). Следующие роли `roles/container-engine/*` не разбирались по переменным и перечислены как непроиндексированные:

- `cri-o`
- `docker`
- `cri-dockerd`
- `gvisor`
- `kata-containers`
- `crun`
- `youki`

Соответствующие флаги включения (`gvisor_enabled`, `kata_containers_enabled`, `crun_enabled`, `youki_enabled`, `runc_enabled`, а также `container_manager: crio | docker`) зафиксированы в разделе «Выбор рантайма».

## Источники

- `roles/container-engine/containerd/defaults/main.yml`
- `roles/container-engine/containerd-common/defaults/main.yml`
- `roles/container-engine/runc/defaults/main.yml`
- `roles/container-engine/validate-container-engine/tasks/main.yml`
- `roles/kubespray_defaults/defaults/main/main.yml`
- `roles/kubespray_defaults/defaults/main/download.yml`
- `roles/kubespray_defaults/vars/main/checksums.yml`

См. также: [[versions/v2.30.0/README|Срез v2.30.0]]
