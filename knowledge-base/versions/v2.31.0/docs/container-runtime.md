---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: docs
source_paths:
  - docs/CRI/containerd.md
  - docs/CRI/cri-o.md
  - docs/CRI/docker.md
  - docs/CRI/gvisor.md
  - docs/CRI/kata-containers.md
  - docs/operations/cgroups.md
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0
retrieved_at: 2026-07-14
topics:
  - container-runtime
  - containerd
reliability: authoritative
---

# Container runtime в Kubespray v2.31.0

Дайджест документации по container runtime. Основной индексируемый runtime — **containerd** (разобран детально); остальные (CRI-O, Docker, gVisor, Kata Containers) — кратко. Runtime выбирается переменной `container_manager` (`containerd` | `crio` | `docker`).

См. также: [[versions/v2.31.0/variables/container-runtime|Переменные рантайма]].

## containerd (по умолчанию)

Промышленный стандартный runtime, используется в Kubespray как container runtime по умолчанию.

Включение:

```yaml
container_manager: containerd    # k8s_cluster.yml
etcd_deployment_type: host       # etcd.yml
```

Замечание из docs: при совмещении etcd с `kube_node` (etcd-узлы расшедулены под нагрузку) containerd и dockerd не могут работать одновременно — для запуска etcd-кластера только с containerd нужны настройки выше.

### Зеркала реестров (registry mirrors)

Настраиваются через `containerd_registries_mirrors` (список словарей):

```yaml
containerd_registries_mirrors:
  - prefix: docker.io
    mirrors:
      - host: https://mirror.gcr.io
        capabilities: ["pull", "resolve"]
        skip_verify: false
      - host: https://registry-1.docker.io
        capabilities: ["pull", "resolve"]
        skip_verify: false
```

- Если ни одно зеркало не отдало образ, containerd откатывается на `https://{{ prefix }}`. Это поведение переопределяется полем `server:` в элементе списка.
- `skip_verify: true` — доступ к insecure-реестрам (self-hosted, по IP:порт или host).
- Устаревшие (deprecated): конфиги `containerd_registries` и `containerd_insecure_registries`.

### Runtime-классы containerd

Containerd поддерживает несколько runtime-конфигураций для Kubernetes-фичи [RuntimeClass].

- Имя runtime по умолчанию — `runc`, настраивается словарём `containerd_runc_runtime`:

```yaml
containerd_runc_runtime:
  name: runc
  type: "io.containerd.runc.v2"
  options:
    Root: ""
    SystemdCgroup: "false"
    BinaryName: /usr/local/bin/my-runc
  base_runtime_spec: cri-base.json
```

- Дополнительные runtime — список `containerd_additional_runtimes`.
- Runtime по умолчанию меняется через `containerd_default_runtime`.

### Base runtime specs и лимит открытых файлов

- Ключ `base_runtime_spec` в словаре runtime задаёт JSON-файл спецификации runtime. У `runc` это `cri-base.json` (генерируется `ctr oci spec > /etc/containerd/cri-base.json` и дополняется настройкой максимального числа файловых дескрипторов на контейнер).
- Максимум файловых дескрипторов для `runc` меняется переменной `containerd_base_runtime_spec_rlimit_nofile`.
- Собственные файлы спецификаций задаются словарём `containerd_base_runtime_specs` (например, `cri-spec-custom.json`); файлы кладутся в каталог конфигурации containerd (по умолчанию `/etc/containerd`) и затем ссылаются по имени файла в runtime.

### NRI (Node Resource Interface)

Отключён по умолчанию. При containerd версии v1.7.0+ включается:

```yaml
nri_enabled: true
```

### Статический бинарник

Для совместимости со старыми дистрибутивами (например, Debian 11):

```yaml
containerd_static_binary: true
```

По умолчанию статический бинарник используется, если версия glibc системы < 2.34; иначе — обычный бинарник.

## CRI-O (кратко)

Лёгкий runtime для Kubernetes. Kubernetes поддерживает CRI-O с v1.11.1+; etcd — kubeadm-managed или host.

Включение:

```yaml
# all/all.yml
download_container: false
skip_downloads: false
etcd_deployment_type: host   # опционально kubeadm
# k8s_cluster/k8s_cluster.yml
container_manager: crio
```

- Зеркала реестров — `crio_registries` (в `all/crio.yml`), поля `prefix`, `insecure`, `blocked`, `location`, `unqualified`, `mirrors`.
- Insecure-реестры — `crio_insecure_registries`; аутентификация — `crio_registry_auth`.
- User namespaces: `crio_runtimes` (с `allowed_annotations: io.kubernetes.cri-o.userns-mode`) + `crio_remap_enable: true` (правит `/etc/subuid`/`/etc/subgid`; по умолчанию резервируется 16M uid/gid).
- Дефолтные capabilities — `crio_default_capabilities` (CHOWN, DAC_OVERRIDE, FSETID, FOWNER, SETGID, SETUID, SETPCAP, NET_BIND_SERVICE, KILL); для Rancher можно добавить MKNOD.
- NRI: `nri_enabled: true` (CRI-O v1.26.0+).

## Docker (кратко)

Поддерживается; `dockershim` устарел, вместо него используется [cri-dockerd] (Mirantis), заменивший dockershim начиная с kubespray 2.20.

Включение: `container_manager: docker`.

Ключевые переменные:

- `docker_storage_options: -s overlay2` — драйвер overlay2.
- `docker_cgroup_driver` — `systemd` (по умолчанию) или `cgroupfs`.
- `docker_dns_servers_strict: false` — не падать при > 3 nameservers.
- `docker_daemon_graph: "/var/lib/docker"` — каталог данных.
- `docker_iptables_enabled: "false"` — управление iptables.
- `docker_log_opts` — ротация логов (max-size, max-file).
- `docker_bin_dir: "/usr/bin"` — не менять без кастомного пакета.
- `docker_rpm_keepcache: 1` — сохранять пакеты после установки.
- `docker_insecure_registries`, `docker_registry_mirrors` — insecure-реестры и зеркала.
- `docker_mount_flags` — `shared`/`slave`/`private` (по умолчанию системное).
- `docker_options` — дополнительные опции демона.
- `docker_repo_key_keyring` — путь к GPG-ключу (Debian).

## gVisor (кратко)

Application kernel на Go, дополнительный уровень изоляции; OCI-runtime `runsc`. Требует container manager с поддержкой RuntimeClass (например, containerd).

```yaml
container_manager: containerd
gvisor_enabled: true
```

## Kata Containers (кратко)

Безопасный runtime на лёгких виртуальных машинах. Единственный поддерживаемый гипервизор — **Qemu**.

Включение:

```yaml
# k8s-cluster.yml
container_manager: containerd
kata_containers_enabled: true
# etcd.yml
etcd_deployment_type: host
```

- По умолчанию поды используют runc; Kubespray генерирует runtimeClass `kata-qemu` — для использования Kata указывают `runtimeClassName: kata-qemu` в spec пода.
- Pod Overhead (рекомендуется, обязателен для подов Kata с resource limits): требует настройки cgroup-драйвера kubelet. `cgroupfs` работает лучше всего; при cgroups v2 можно использовать `systemd`.
  - `kubelet_cgroup_driver: cgroupfs`
  - `kata_containers_qemu_overhead: true`, `kata_containers_qemu_overhead_fixed_cpu: 10m`, `kata_containers_qemu_overhead_fixed_memory: 290Mi`.
- Версия: `kata_containers_version` (например, `2.2.2`).
- Отладка: `kata_containers_qemu_debug: 'false'` (по умолчанию отключена).

## cgroups и резервирование ресурсов узла

kubelet использует cgroups, чтобы ограничить потребление ресурсов и избежать конкуренции между контейнерами и хостовыми демонами.

- `kubelet_enforce_node_allocatable` — уровни enforcement (по умолчанию `"pods"`; можно `"pods,kube-reserved,system-reserved"`).
- Для enforcement kube-reserved / system-reserved нужны `kube_reserved_cgroups` / `system_reserved_cgroups`.
- kube-reserved: `kube_reserved: true`, `kube_reserved_cgroups_for_service_slice: kube.slice`, `kube_reserved_cgroups: "/{{ kube_reserved_cgroups_for_service_slice }}"`, `kube_memory_reserved: 256Mi`, `kube_cpu_reserved: 100m` (опц. `kube_ephemeral_storage_reserved`, `kube_pid_reserved`).
- system-reserved: `system_reserved: true`, `system_reserved_cgroups_for_service_slice: system.slice`, `system_memory_reserved: 512Mi`, `system_cpu_reserved: 500m` (опц. `system_ephemeral_storage_reserved`, `system_pid_reserved`).
- Иерархия cgroups: `kubepods.slice`, `kube.slice` (содержит `{{container_manager}}.service`, `kubelet.service`), `system.slice`.

## Источники

- docs/CRI/containerd.md — детально
- docs/CRI/cri-o.md, docs/CRI/docker.md, docs/CRI/gvisor.md, docs/CRI/kata-containers.md — кратко
- docs/operations/cgroups.md
- [[versions/v2.31.0/variables/container-runtime|Переменные рантайма]]
- [[versions/v2.31.0/README|Срез v2.31.0]]

[RuntimeClass]: https://kubernetes.io/docs/concepts/containers/runtime-class/
[cri-dockerd]: https://github.com/Mirantis/cri-dockerd
