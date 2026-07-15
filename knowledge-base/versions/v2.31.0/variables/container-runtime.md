---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: code
source_path: versions/v2.31.0/variables/container-runtime.yaml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0
retrieved_at: 2026-07-14
topics:
  - container-runtime
  - containerd
reliability: authoritative
---

# Контейнерный рантайм в v2.31.0 (фокус: containerd)

Эта заметка — человекочитаемое представление справочника переменных.
Источник истины — YAML-файл `container-runtime.yaml`; при расхождении верен YAML.

Все факты извлечены строго из кода тега `v2.31.0` (commit `1c9add4`).
Пути указаны от корня репозитория Kubespray.

## Обзор: как выбирается рантайм

Выбор рантайма задаётся переменной `container_manager`
(`roles/kubespray_defaults/defaults/main/main.yml`). Значение по умолчанию —
`containerd`. Допустимые значения: `containerd`, `crio`, `docker`.

От значения `container_manager` производно вычисляются:

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `container_manager` | `containerd` | Выбор рантайма CRI |
| `cri_socket` | `unix:///var/run/containerd/containerd.sock` (для containerd) | Путь к CRI-сокету для kubelet |
| `nri_enabled` | `{{ container_manager == 'containerd' }}` | Плагин NRI (включён только для containerd) |
| `container_manager_on_localhost` | `{{ container_manager }}` | Рантайм на управляющем узле Ansible |

Сокет `cri_socket` вычисляется по ветвлению: `crio` →
`unix:///var/run/crio/crio.sock`, `containerd` →
`unix:///var/run/containerd/containerd.sock`, `docker` →
`unix:///var/run/cri-dockerd.sock`.

## Ключевые переменные containerd

Полный набор — 45 ключей в
`roles/container-engine/containerd/defaults/main.yml`. Ниже — наиболее важные.

### Каталоги, процесс, рантайм по умолчанию

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `containerd_storage_dir` | `/var/lib/containerd` | Каталог данных (root) |
| `containerd_state_dir` | `/run/containerd` | Каталог состояния (state) |
| `containerd_cfg_dir` | `/etc/containerd` | Каталог конфигурации (config.toml) |
| `containerd_systemd_dir` | `/etc/systemd/system/containerd.service.d` | Drop-in каталог systemd-юнита |
| `containerd_oom_score` | `0` | oom_score_adj процесса containerd |
| `containerd_default_runtime` | `runc` | Рантайм CRI по умолчанию |
| `containerd_snapshotter` | `overlayfs` | Снапшоттер по умолчанию |
| `containerd_use_systemd_cgroup` | `true` | systemd cgroup driver (задан в `kubespray_defaults`) |

Переменная `containerd_runc_runtime` описывает рантайм runc
(`type: io.containerd.runc.v2`, `base_runtime_spec: cri-base.json`), где опция
`SystemdCgroup` берётся из `containerd_use_systemd_cgroup`, а `BinaryName` — из
`bin_dir`. Дополнительные рантаймы задаются через
`containerd_additional_runtimes` (по умолчанию `[]`).

### Реестры, лимиты, сеть, безопасность

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `containerd_registries_mirrors` | зеркало для `docker.io` → `https://registry-1.docker.io` | Зеркала реестров (hosts.toml) |
| `containerd_registry_auth` | `[]` | Аутентификация в реестрах |
| `containerd_max_container_log_line_size` | `16384` | Макс. размер строки лога контейнера |
| `containerd_grpc_max_recv_message_size` | `16777216` | Макс. размер входящего gRPC-сообщения |
| `containerd_grpc_max_send_message_size` | `16777216` | Макс. размер исходящего gRPC-сообщения |
| `containerd_enable_unprivileged_ports` | `false` | Непривилегированные порты < 1024 |
| `containerd_enable_unprivileged_icmp` | `false` | Непривилегированные ICMP-сокеты |
| `containerd_enable_selinux` | `false` | Поддержка SELinux |
| `containerd_disable_apparmor` | `false` | Отключение AppArmor |
| `containerd_image_pull_progress_timeout` | `5m` | Таймаут прогресса загрузки образа |
| `containerd_limit_open_file_num` | `1048576` | LimitNOFILE systemd-юнита |
| `containerd_limit_proc_num` | `infinity` | LimitNPROC systemd-юнита |
| `containerd_limit_core` | `infinity` | LimitCORE systemd-юнита |
| `containerd_limit_mem_lock` | `infinity` | LimitMEMLOCK systemd-юнита |

### Отладка, метрики, трассировка, CDI

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `containerd_debug_level` | `info` | Уровень логирования |
| `containerd_debug_address` | `""` | Debug-сокет (пусто — выключен) |
| `containerd_metrics_address` | `""` | Эндпоинт метрик (пусто — выключен) |
| `containerd_metrics_grpc_histogram` | `false` | Гистограммы gRPC в метриках |
| `containerd_tracing_enabled` | `false` | Трассировка (OpenTelemetry) |
| `containerd_tracing_endpoint` | `[::]:4317` | Эндпоинт коллектора трассировки |
| `containerd_tracing_protocol` | `grpc` | Протокол экспорта трассировки |
| `containerd_tracing_sampling_ratio` | `1.0` | Доля сэмплирования трассировки |
| `enable_cdi` | `false` | Container Device Interface (без префикса `containerd_`) |

### Runtime spec, слои, extra

- `containerd_base_runtime_spec_rlimit_nofile` = `65535` — значение
  `RLIMIT_NOFILE` (hard/soft) в базовой runtime spec.
- `containerd_default_base_runtime_spec_patch` — патч базовой spec, задающий
  rlimits процесса.
- `containerd_base_runtime_specs` — набор spec-файлов; `cri-base.json`
  формируется объединением `containerd_default_base_runtime_spec` с патчем.
  Помечено `reliability: unconfirmed`, так как
  `containerd_default_base_runtime_spec` генерируется вне defaults
  (через `ctr oci spec` в задачах роли).
- `containerd_discard_unpacked_layers` = `true` — удаление распакованных слоёв
  (актуально для containerd < 2.1).
- `containerd_extra_args` = `''` — произвольный текст в `config.toml`.
- `containerd_extra_runtime_args` = `{}` — опции в секцию CRI-плагина
  `[plugins."io.containerd.cri.v1.runtime"]`.

### Версия и способ установки

- `containerd_version` (`roles/kubespray_defaults/defaults/main/download.yml`) —
  вычисляется как первый (старший) ключ `containerd_archive_checksums['amd64']`.
  В теге `v2.31.0` разрешается в **2.2.3**
  (`roles/kubespray_defaults/vars/main/checksums.yml`).
- `containerd_static_binary` = `false` — статическая сборка для старых
  дистрибутивов (например, Debian 11).
- `containerd_package` = `'containerd.io'`, `yum_repo_dir` = `/etc/yum.repos.d`
  (`containerd-common`) — сохранены для миграции с пакетных установок.

### runc (низкоуровневый OCI-рантайм containerd)

- `runc_bin_dir` = `{{ bin_dir }}` — каталог установки бинарника runc.
- `runc_package_name` = `runc` — имя пакета runc.

## Важное замечание: дублирование переменных

Переменные `containerd_storage_dir`, `containerd_state_dir`,
`containerd_systemd_dir` и `containerd_cfg_dir` определены **дважды** — в
`roles/container-engine/containerd/defaults/main.yml` и в
`roles/kubespray_defaults/defaults/main/main.yml` — с **одинаковыми
значениями**. Обе точки являются role defaults (одинаковый уровень
приоритетности Ansible), поэтому конфликта поведения по умолчанию нет.
Дублирование зафиксировано как наблюдение; переопределять переменную следует
через inventory (group_vars), а не в defaults.

## Непроиндексированные рантаймы (вне фокуса)

В этом срезе детально разобран только containerd. Прочие рантаймы Kubespray
v2.31.0 присутствуют, но не индексировались (перечислены каталоги в
`roles/container-engine/`):

- `docker` — рантайм Docker (через cri-dockerd);
- `cri-o` — CRI-O;
- `cri-dockerd` — shim CRI для Docker;
- `containerd-common` — общие переменные (частично затронуты выше);
- `runc` — низкоуровневый OCI-рантайм (частично затронут выше);
- `crun` — альтернативный OCI-рантайм (для crio);
- `youki` — OCI-рантайм на Rust (для crio);
- `kata-containers` — Kata Containers (изоляция через VM);
- `gvisor` — gVisor (песочница);
- `crictl` — CLI для CRI;
- `nerdctl` — CLI для containerd;
- `skopeo` — работа с образами;
- `validate-container-engine` — валидация/удаление конфликтующих рантаймов.

## Изменения относительно v2.30.0

- Файл `roles/container-engine/containerd/defaults/main.yml` **идентичен** тегу
  `v2.30.0` (git diff пуст) — состав из 45 ключей и их значения не изменились.
- Переменные выбора рантайма в `kubespray_defaults` (`container_manager`,
  `nri_enabled`, `containerd_use_systemd_cgroup`, `containerd_static_binary`)
  также не изменились.
- Фактически изменилась только **разрешаемая версия** `containerd_version`:
  `2.2.1` в `v2.30.0` → `2.2.3` в `v2.31.0` (добавлены новые патч-релизы в
  `checksums.yml`).

## Навигация

- [[versions/v2.31.0/README|Срез v2.31.0]]
- Справочник (источник истины): `container-runtime.yaml`
