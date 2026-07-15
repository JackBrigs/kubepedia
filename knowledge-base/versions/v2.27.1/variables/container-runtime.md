---
project: kubespray
kubespray_version: v2.27.1
git_commit: 45140b5
source_type: code
source_path: versions/v2.27.1/variables/container-runtime.yaml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.27.1
retrieved_at: 2026-07-15
topics:
  - container-runtime
  - containerd
reliability: authoritative
---

# Переменные container runtime (containerd) — Kubespray v2.27.1

Человекочитаемая заметка к машиночитаемому справочнику `container-runtime.yaml`.
**Источник истины — YAML-справочник** `versions/v2.27.1/variables/container-runtime.yaml`.
Назад к срезу: [[versions/v2.27.1/README|Срез v2.27.1]].

Ограничение проекта: из container runtime детально индексируется **только containerd** (docker, cri-o, cri-dockerd, kata, gvisor, crun, youki — не разбираются).

Источники в коде тега `v2.27.1` (commit `45140b5`):

- `roles/container-engine/containerd/defaults/main.yml` — 44 переменные config.toml и systemd-юнита;
- `roles/container-engine/containerd-common/defaults/main.yml` — 7 переменных для миграции с пакетной установки;
- `roles/container-engine/runc/defaults/main.yml` — 2 переменные runc;
- `roles/kubespray-defaults/defaults/main/main.yml` (каталог с **дефисом**) — выбор рантайма, cri_socket, каталоги;
- `roles/kubespray-defaults/defaults/main/download.yml` — версии и загрузки (containerd, runc, nerdctl, crictl, skopeo, pause).

## Ключевые версии в теге

| Компонент | Переменная | Версия | Заметка |
|---|---|---|---|
| containerd | `containerd_version` | **1.7.27** | явный литерал (в v2.29.1 вычислялся из checksums, был 2.1.5) |
| runc | `runc_version` | **v1.2.6** | явный литерал |
| nerdctl | `nerdctl_version` | **1.7.7** | явный литерал |
| crictl | `crictl_version` | **v1.31.1** (для K8s 1.31) | по карте `crictl_supported_versions` |
| skopeo | `skopeo_version` | **v1.16.1** | сборка `lework/skopeo-binary` |
| pause | `pod_infra_version` | **3.10** (для K8s 1.31) | по карте `pod_infra_supported_versions` |

## Выбор рантайма

`container_manager: containerd` (допустимо `containerd`, `crio`, `docker`). Сокет
вычисляется в `cri_socket` — для containerd это `unix:///var/run/containerd/containerd.sock`.
`deploy_container_engine` включается на узлах `k8s_cluster` и на etcd при docker-развёртывании.
`image_command_tool` при containerd — `nerdctl`, но **фактический pull делается через `ctr`**
(`nerdctl_image_pull_command`, обход issue kubespray#10670).

Дополнительные рантаймы: `nri_enabled: false`, `kata_containers_enabled: false`,
`gvisor_enabled: false`, `runc_enabled`/`crun_enabled`/`youki_enabled: false` (последние три требуют crio).

## Отличия от v2.29.1 (важно при обновлении)

- `containerd_runc_runtime.options` в v2.27.1 называются **`systemdCgroup` / `binaryName`** (в v2.29.1 — `SystemdCgroup` / `BinaryName`).
- `containerd_limit_open_file_num` = **`infinity`** (в v2.29.1 — числовое `1048576`).
- `containerd_tracing_endpoint` = **`0.0.0.0:4317`** (в v2.29.1 — `[::]:4317`).
- Переменной `containerd_static_binary` **нет**, и в `containerd_download_url` отсутствует ветка `static-`.
- Переменной `containerd_extra_runtime_args` **нет** (добавлена в более поздних версиях).

## Каталоги containerd

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `containerd_storage_dir` | `/var/lib/containerd` | root в config.toml (дубль в main.yml) |
| `containerd_state_dir` | `/run/containerd` | state (дубль в main.yml) |
| `containerd_cfg_dir` | `/etc/containerd` | config.toml, base specs, certs.d (дубль в main.yml) |
| `containerd_systemd_dir` | `/etc/systemd/system/containerd.service.d` | drop-in systemd (дубль в main.yml) |
| `containerd_bin_dir` | `{{ bin_dir }}` | бинарники containerd (в main.yml) |

## config.toml: рантайм и снапшоттер

`containerd_default_runtime: runc`, `containerd_snapshotter: overlayfs`. Рантайм runc описан в
`containerd_runc_runtime` (тип `io.containerd.runc.v2`, base_runtime_spec `cri-base.json`,
systemd cgroup через `containerd_use_systemd_cgroup: true`). Базовая OCI-спецификация патчится
лимитом `containerd_base_runtime_spec_rlimit_nofile: 65535`. Дополнительные рантаймы — список
`containerd_additional_runtimes: []`.

## Зеркала и учётные данные реестров

`containerd_registries_mirrors` по умолчанию содержит зеркало для `docker.io` → `registry-1.docker.io`
(для каждого prefix создаётся `certs.d/<prefix>/hosts.toml`). `containerd_registry_auth: []` — учётные данные.

## systemd-лимиты сервиса

`containerd_limit_proc_num`, `containerd_limit_core`, `containerd_limit_open_file_num`,
`containerd_limit_mem_lock` — все по умолчанию `infinity`. `containerd_oom_score: 0`
(при этом сам юнит жёстко ставит `OOMScoreAdjust=-999`).

## Прочее

Логи/отладка (`containerd_debug_*`, `containerd_max_container_log_line_size: 16384`),
gRPC-лимиты (`containerd_grpc_max_recv/send_message_size: 16777216`), безопасность
(`containerd_enable_selinux`, `containerd_disable_apparmor`, `containerd_enable_unprivileged_ports/icmp`),
hugetlb (`containerd_tolerate_missing_hugetlb_controller`/`containerd_disable_hugetlb_controller: true`),
`enable_cdi: false`, трассировка (`containerd_tracing_enabled: false` + endpoint/protocol/ratio/service_name).

## Связанное

- [[versions/v2.27.1/variables/download|download.yaml]] — механизм загрузок и контрольные суммы
- [[versions/v2.27.1/variables/etcd|etcd.yaml]] — `etcd_deployment_type: docker` тоже требует движка
- [[versions/v2.27.1/README|Срез v2.27.1]]

## Сверка полноты

Извлечено: `roles/container-engine/containerd/defaults/main.yml` — все **44** top-level ключа; `containerd-common` — все **7**; `runc/defaults` — все **2**. Дополнительно 12 переменных выбора рантайма из `main.yml` (4 каталога containerd в нём — дубли, помечены `also_defined_in`) и 30 переменных из `download.yml` (команды образов, версии и загрузки containerd/runc/nerdctl/crictl/skopeo/pause). Итого в `container-runtime.yaml` — 95 записей. Не-containerd рантаймы (docker, cri-o, cri-dockerd, kata, gvisor, crun, youki) исключены по охвату.
