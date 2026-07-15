---
project: kubespray
kubespray_version: v2.29.0
git_commit: 9991412
source_type: code
source_path: versions/v2.29.0/variables/container-runtime.yaml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.29.0
retrieved_at: 2026-07-14
topics:
  - container-runtime
  - containerd
reliability: authoritative
---

# Container runtime в Kubespray v2.29.0

Справочник переменных container runtime для тега `v2.29.0` (commit `9991412`).
**Источник истины** — машинно-читаемый файл [[versions/v2.29.0/variables/container-runtime|container-runtime.yaml]] (85 переменных); эта заметка — его человекочитаемое изложение.

Назад к срезу: [[versions/v2.29.0/README|Срез v2.29.0]]

## Выбор рантайма

Рантайм по умолчанию — **containerd**:

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `container_manager` | `containerd` | Рантайм кластера: `containerd` / `crio` / `docker` |
| `deploy_container_engine` | `{{ 'k8s_cluster' in group_names or etcd_deployment_type == 'docker' }}` | Ставить ли движок на хост |
| `cri_socket` | вычисляется из `container_manager`; для containerd — `unix:///var/run/containerd/containerd.sock` | CRI-сокет для kubelet |
| `container_manager_on_localhost` | `{{ container_manager }}` | Рантайм на localhost при `download_localhost` |
| `nri_enabled` | `{{ container_manager == 'containerd' }}` | Плагин NRI в config.toml |

Источник: `roles/kubespray_defaults/defaults/main/main.yml`.

Роль `container-engine/validate-container-engine` перед установкой проверяет узел: находит установленные юниты `containerd.service` / `docker.service` / `crio.service` и, если работающий рантайм не совпадает с `container_manager` (кроме ostree-систем и Flatcar), дренирует узел, останавливает kubelet и удаляет чужой рантайм через `tasks_from: reset` соответствующей роли (`roles/container-engine/validate-container-engine/tasks/main.yml`).

Дополнительные рантаймы-флаги: `kata_containers_enabled`, `gvisor_enabled` (при true в config.toml containerd добавляются runtimes `kata-qemu` / `runsc`), а также `runc_enabled`, `crun_enabled`, `youki_enabled` (по комментариям в коде — для `container_manager=crio`). Все по умолчанию `false`.

Инструмент работы с образами: `image_command_tool` — при containerd это **nerdctl** (при crio — crictl); команды `image_pull_command` / `image_info_command` разрешаются через `lookup('vars', ...)` по имени инструмента (`roles/kubespray_defaults/defaults/main/download.yml`).

## containerd: версия и каталоги

| Переменная | Значение по умолчанию |
|---|---|
| `containerd_version` | первый ключ `containerd_archive_checksums['amd64']` → **2.1.4** в этом теге |
| `containerd_static_binary` | `false` (статическая сборка для старых дистрибутивов) |
| `containerd_bin_dir` | `{{ bin_dir }}` (обычно `/usr/local/bin`) |
| `containerd_storage_dir` | `/var/lib/containerd` (root) |
| `containerd_state_dir` | `/run/containerd` (state) |
| `containerd_cfg_dir` | `/etc/containerd` |
| `containerd_systemd_dir` | `/etc/systemd/system/containerd.service.d` |

Установка — бинарная (архив с GitHub, `containerd_download_url`), не из пакетов. Роль `containerd-common` хранит `containerd_package: 'containerd.io'` и `yum_repo_dir` только для миграции с пакетной установки.

Так как `containerd_version` по умолчанию >= 2.0.0, конфиг рендерится из `config.toml.j2` (format `version = 3`, плагины `io.containerd.cri.v1.*`); для containerd < 2.0.0 остаётся легаси-шаблон `config-v1.toml.j2` (`roles/container-engine/containerd/tasks/main.yml`).

## containerd: конфигурация (config.toml)

| Переменная | По умолчанию | Что задаёт |
|---|---|---|
| `containerd_default_runtime` | `runc` | `default_runtime_name` |
| `containerd_snapshotter` | `overlayfs` | снапшоттер CRI-плагина |
| `containerd_use_systemd_cgroup` | `true` | `SystemdCgroup` у runc |
| `containerd_runc_runtime` | тип `io.containerd.runc.v2`, `base_runtime_spec: cri-base.json`, `BinaryName: {{ bin_dir }}/runc` | описание рантайма runc |
| `containerd_additional_runtimes` | `[]` | дополнительные рантаймы |
| `containerd_oom_score` | `0` | oom_score в конфиге (юнит дополнительно ставит `OOMScoreAdjust=-999`) |
| `containerd_discard_unpacked_layers` | `true` | экономия диска |
| `containerd_image_pull_progress_timeout` | `5m` | таймаут пула образа |
| `containerd_max_container_log_line_size` | `16384` | длина строки лога |
| `containerd_grpc_max_recv_message_size` / `..._send_...` | `16777216` | лимиты gRPC |
| `containerd_enable_unprivileged_ports` / `..._icmp` | `false` | привилегии в контейнерах |
| `containerd_enable_selinux` | `false` | SELinux |
| `containerd_disable_apparmor` | `false` | AppArmor |
| `containerd_disable_hugetlb_controller` / `containerd_tolerate_missing_hugetlb_controller` | `true` | hugetlb cgroup |
| `enable_cdi` | `false` | Container Device Interface |
| `containerd_extra_args` | `''` | произвольный текст в config.toml |
| `containerd_extra_runtime_args` | `{}` | доп. опции CRI runtime-плагина |
| `containerd_debug_*`, `containerd_metrics_*` | пусто/выкл | debug-сокет и метрики |
| `containerd_tracing_*` | `containerd_tracing_enabled: false`; endpoint `[::]:4317`, protocol `grpc`, ratio `1.0` | OTLP-трассировка |

Базовая OCI-спецификация контейнеров: роль выполняет `ctr oci spec`, накладывает патч `containerd_default_base_runtime_spec_patch` (rlimit `RLIMIT_NOFILE` = `containerd_base_runtime_spec_rlimit_nofile` = **65535**) и записывает результат как `{{ containerd_cfg_dir }}/cri-base.json` (`containerd_base_runtime_specs`).

## containerd: registries, mirrors, sandbox image

- `containerd_registries_mirrors` — по умолчанию один prefix `docker.io` с зеркалом `https://registry-1.docker.io` (capabilities `pull`, `resolve`, `skip_verify: false`). Для каждого prefix создаётся `{{ containerd_cfg_dir }}/certs.d/<prefix>/hosts.toml`; поддерживаются поля `server`, `ca`, `client`, `header`, `override_path`, `skip_verify`. Небезопасный (insecure) registry в containerd в этом теге настраивается именно через `skip_verify: true` в зеркалах — отдельной переменной `containerd_insecure_registries` нет (переменные `docker_insecure_registries`, `crio_insecure_registries` относятся к другим рантаймам).
- `containerd_registry_auth` — `[]`; список registry/username/password. Внимание: в теге используется только легаси-шаблоном `config-v1.toml.j2`, то есть при дефолтном containerd 2.1.4 не применяется (в YAML помечено `reliability: unconfirmed`).
- Sandbox (pause): `pinned_images.sandbox = {{ pod_infra_image_repo }}:{{ pod_infra_image_tag }}`, где repo — `{{ kube_image_repo }}/pause`, тег — `pod_infra_version` (выбирается по мажорной версии Kubernetes).

## containerd: systemd-лимиты (containerd.service)

| Переменная | По умолчанию | Директива юнита |
|---|---|---|
| `containerd_limit_proc_num` | `infinity` | `LimitNPROC` |
| `containerd_limit_core` | `infinity` | `LimitCORE` |
| `containerd_limit_open_file_num` | `1048576` | `LimitNOFILE` |
| `containerd_limit_mem_lock` | `infinity` | `LimitMEMLOCK` |

При заданных `http_proxy`/`https_proxy` роль пишет drop-in `http-proxy.conf` в `containerd_systemd_dir`. Список поддерживаемых ОС — `containerd_supported_distributions` (18 дистрибутивов).

## runc, crictl, nerdctl, skopeo (кратко)

| Инструмент | Версия в теге | Ключевые переменные | Заметки |
|---|---|---|---|
| runc | 1.3.2 (`runc_version`) | `runc_bin_dir: {{ bin_dir }}`, `runc_package_name: runc` | роль удаляет пакетный runc и ставит бинарник с GitHub |
| crictl | 1.33.0 (`crictl_version`, выбирается младше `kube_major_next_version`) | конфиг `/etc/crictl.yaml` из `cri_socket` | у роли нет своих defaults |
| nerdctl | 2.1.6 (`nerdctl_version`) | конфиг `/etc/nerdctl/nerdctl.toml`; `nerdctl_snapshotter` — только default в шаблоне (`overlayfs`) | namespace `k8s.io`, `hosts_dir` = `certs.d` containerd |
| skopeo | 1.16.1 (`skopeo_version`) | скачивается из `lework/skopeo-binary` | пакетный skopeo удаляется |

## Непроиндексированные рантаймы

В теге v2.29.0 в `roles/container-engine/` существуют, но по переменным в этом справочнике **не разобраны**:

- `cri-o` (roles/container-engine/cri-o)
- `docker` (roles/container-engine/docker)
- `cri-dockerd` (roles/container-engine/cri-dockerd)
- `gvisor` (roles/container-engine/gvisor)
- `kata-containers` (roles/container-engine/kata-containers)
- `crun` (roles/container-engine/crun)
- `youki` (roles/container-engine/youki)
