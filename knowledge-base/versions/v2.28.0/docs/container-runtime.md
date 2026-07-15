---
project: kubespray
kubespray_version: v2.28.0
git_commit: 63cdf87
source_type: docs
source_paths:
  - docs/CRI/containerd.md
  - docs/CRI/cri-o.md
  - docs/CRI/docker.md
  - docs/CRI/gvisor.md
  - docs/CRI/kata-containers.md
  - docs/operations/cgroups.md
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.28.0
retrieved_at: 2026-07-15
topics:
  - containerd
  - container-runtime
  - cgroups
  - crio
  - docker
reliability: authoritative
---

# Container runtime в v2.28.0

Дайджест документации по container runtime строго с тега `v2.28.0` (commit `63cdf87`).
Выбор рантайма задаётся переменной `container_manager` (`containerd` | `crio` | `docker`).
В проекте детально индексируется **containerd**.

> Отличия от v2.29.1: (1) в `docs/CRI/containerd.md` тега v2.28.0 **ещё нет** раздела «Optional : Static Binary» и переменной `containerd_static_binary` (добавлены в v2.29.1); (2) в `docs/operations/cgroups.md` тега v2.28.0 **присутствуют** переменные резервирования для master-хостов (`kube_master_*`, `system_master_*`), которые удалены в v2.29.1. Файлы `cri-o.md`, `docker.md`, `gvisor.md`, `kata-containers.md` идентичны v2.29.1.

## containerd (детально)

Источник: `docs/CRI/containerd.md`.

### Включение containerd

Задать в inventory:

```yaml
# k8s_cluster.yml
container_manager: containerd
# etcd.yml
etcd_deployment_type: host
```

Важное замечание из документации: если группа `kube_node` содержит узлы etcd (etcd
как schedulable для рабочих нагрузок), то containerd и dockerd не могут работать
одновременно — для запуска кластера etcd только с containerd требуется
`etcd_deployment_type: host`.

### Реестры и зеркала (registries/mirrors, hosts.toml)

Основная переменная — `containerd_registries_mirrors` (список словарей). Каждый
элемент описывает `prefix` (реестр, для которого настраивается зеркало) и список
`mirrors` с полями `host`, `capabilities` (`["pull", "resolve"]`) и `skip_verify`.

Пример зеркала для Docker Hub:

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

- Поведение fallback: containerd откатывается на `https://{{ prefix }}`, если ни
  одно из зеркал не содержит образ. Это поведение меняется полем `server`
  (соответствует `server field` из hosts.md containerd):

```yaml
containerd_registries_mirrors:
  - prefix: docker.io
    mirrors:
      - host: https://mirror.gcr.io
        capabilities: ["pull", "resolve"]
        skip_verify: false
    server: https://mirror.example.org
```

- Доступ к небезопасным (insecure) self-hosted реестрам настраивается через тот
  же `containerd_registries_mirrors` с `host: http://...` и `skip_verify: true`
  (примеры: `test.registry.io`, `172.19.16.11:5000`, `repo:5000`).
- Переменные `containerd_registries` и `containerd_insecure_registries`
  объявлены **устаревшими (deprecated)** — использовать `containerd_registries_mirrors`.

### Runtimes (RuntimeClass)

containerd поддерживает несколько конфигураций runtime, используемых с фичей
Kubernetes RuntimeClass.

- Рантайм по умолчанию — `runc`, настраивается словарём `containerd_runc_runtime`
  (поля `name`, `type` = `io.containerd.runc.v2`, `engine`, `root`, `options`
  с `SystemdCgroup`, `BinaryName`, `base_runtime_spec`).
- Дополнительные рантаймы задаются списком словарей `containerd_additional_runtimes`.
- Рантайм по умолчанию меняется переменной `containerd_default_runtime`.

### Base runtime spec и лимит открытых файлов

- Ключ `base_runtime_spec` в словаре рантайма явно указывает json-файл спецификации.
  Для `runc` это `cri-base.json` (генерируется `ctr oci spec > /etc/containerd/cri-base.json`
  и дополняется настройкой максимального числа файловых дескрипторов на контейнер).
- Максимум файловых дескрипторов для рантайма `runc` по умолчанию задаётся
  переменной `containerd_base_runtime_spec_rlimit_nofile`.
- Собственные спецификации подаются через словарь `containerd_base_runtime_specs`
  (имя файла → содержимое); файлы кладутся в каталог конфигурации containerd
  (`/etc/containerd` по умолчанию) и затем ссылаются по имени в `base_runtime_spec`.

### Sandbox image и обёртки

- Опциональная обёртка/фича:
  - **NRI** (Node Resource Interface) — отключён по умолчанию; включается
    `nri_enabled: true` (требуется containerd v1.7.0 и выше).
- Аутентификация в приватном реестре образов настраивается через
  `containerd_registry_auth` (список с `registry`/`username`/`password`) —
  подробно в [[versions/v2.28.0/docs/offline|Оффлайн-развёртывание и зеркала]].

Примечание: раздел «Static Binary» (`containerd_static_binary`) в `docs/CRI/containerd.md`
тега v2.28.0 **отсутствует** — он появился только в v2.29.1. Sandbox/pause image как
отдельная переменная в документе также не описана; параметры образа pause относятся
к переменным download — см. [[versions/v2.28.0/variables/download|Переменные download]].

## Прочие рантаймы (не проиндексированы детально)

- **CRI-O** — `docs/CRI/cri-o.md`. Лёгкий рантайм для Kubernetes;
  `container_manager: crio`, зеркала через `crio_registries` /
  `crio_insecure_registries`, аутентификация `crio_registry_auth`; поддержка
  user namespaces (`crio_remap_enable`) и NRI (`nri_enabled`, CRI-O v1.26.0+).
  Не проиндексирован детально.
- **Docker** — `docs/CRI/docker.md`. `container_manager: docker`; `dockershim`
  заменён на `cri-dockerd` (Mirantis) начиная с kubespray 2.20. Cgroup driver —
  `docker_cgroup_driver` (`systemd` по умолчанию). Не проиндексирован детально.
- **gVisor** — `docs/CRI/gvisor.md`. Sandbox-рантайм (runsc) поверх containerd;
  `container_manager: containerd` + `gvisor_enabled: true`. Не проиндексирован детально.
- **Kata Containers** — `docs/CRI/kata-containers.md`. Безопасный рантайм на
  лёгких ВМ (только Qemu); `container_manager: containerd` +
  `kata_containers_enabled: true`, RuntimeClass `kata-qemu`. Не проиндексирован детально.

## Cgroups и cgroup driver

Источник: `docs/operations/cgroups.md`.

Для избежания конкуренции за ресурсы между контейнерами и хостовыми демонами
kubelet использует cgroups для ограничения потребления ресурсов.

- **Enforce node allocatable**: `kubelet_enforce_node_allocatable` (по умолчанию
  `"pods"`); возможны `"pods,kube-reserved"`, `"pods,kube-reserved,system-reserved"`.
- Для enforcement `kube-reserved`/`system-reserved` необходимо задать
  `kube_reserved_cgroups` / `system_reserved_cgroups` соответственно.
- Резервирование под kube-демоны: `kube_reserved: true`,
  `kube_reserved_cgroups_for_service_slice: kube.slice`,
  `kube_reserved_cgroups: "/{{ kube_reserved_cgroups_for_service_slice }}"`,
  `kube_memory_reserved` (256Mi), `kube_cpu_reserved` (100m), опционально
  `kube_ephemeral_storage_reserved`, `kube_pid_reserved`.
- **Резервирование под kube-демоны на master-хостах** (только v2.28.0, удалено в
  v2.29.1): `kube_master_memory_reserved` (512Mi), `kube_master_cpu_reserved` (200m),
  опционально `kube_master_ephemeral_storage_reserved`, `kube_master_pid_reserved`.
- Резервирование под системные демоны: `system_reserved: true`,
  `system_reserved_cgroups_for_service_slice: system.slice`,
  `system_reserved_cgroups`, `system_memory_reserved` (512Mi),
  `system_cpu_reserved` (500m).
- **Резервирование под системные демоны на master-хостах** (только v2.28.0, удалено
  в v2.29.1): `system_master_memory_reserved` (256Mi), `system_master_cpu_reserved`
  (250m), опционально `system_master_ephemeral_storage_reserved`,
  `system_master_pid_reserved`.
- Итоговая иерархия cgroups: `kubepods.slice` (+ `kubepods-besteffort.slice`,
  `kubepods-burstable.slice`), `kube.slice` (содержит
  `{{container_manager}}.service`, `kubelet.service`), `system.slice`.

### cgroup driver: systemd vs cgroupfs

Файл `docs/operations/cgroups.md` тега v2.28.0 сам по себе не задаёт выбор
драйвера; выбор описан в разделах конкретных рантаймов:

- **Kata Containers** (`docs/CRI/kata-containers.md`): драйвер задаётся
  `kubelet_cgroup_driver`. Для Pod Overhead рекомендуется `cgroupfs`
  (`kubelet_cgroup_driver: cgroupfs`), но при cgroups v2 допустимо
  `kubelet_cgroup_driver: systemd`.
- **Docker** (`docs/CRI/docker.md`): драйвер Docker — `docker_cgroup_driver`,
  допустимые значения `systemd` или `cgroupfs`, по умолчанию `systemd`.
- **containerd** (`docs/CRI/containerd.md`): управление systemd-cgroup для
  рантайма runc — опция `SystemdCgroup` в `containerd_runc_runtime.options`.

Общая рекомендация экосистемы (systemd как init-система → systemd cgroup driver)
в docs тега прямо не формулируется; здесь фиксируются только документированные
в v2.28.0 переменные.

## Источники

- `docs/CRI/containerd.md` — https://github.com/kubernetes-sigs/kubespray/blob/v2.28.0/docs/CRI/containerd.md
- `docs/CRI/cri-o.md` — https://github.com/kubernetes-sigs/kubespray/blob/v2.28.0/docs/CRI/cri-o.md
- `docs/CRI/docker.md` — https://github.com/kubernetes-sigs/kubespray/blob/v2.28.0/docs/CRI/docker.md
- `docs/CRI/gvisor.md` — https://github.com/kubernetes-sigs/kubespray/blob/v2.28.0/docs/CRI/gvisor.md
- `docs/CRI/kata-containers.md` — https://github.com/kubernetes-sigs/kubespray/blob/v2.28.0/docs/CRI/kata-containers.md
- `docs/operations/cgroups.md` — https://github.com/kubernetes-sigs/kubespray/blob/v2.28.0/docs/operations/cgroups.md

Связанные заметки: [[versions/v2.28.0/variables/container-runtime|Переменные рантайма]] · [[versions/v2.28.0/variables/download|Переменные download]] · [[versions/v2.28.0/README|Срез v2.28.0]]
