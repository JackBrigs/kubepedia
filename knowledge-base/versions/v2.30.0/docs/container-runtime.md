---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: docs
source_paths:
  - docs/CRI/containerd.md
  - docs/CRI/cri-o.md
  - docs/CRI/docker.md
  - docs/CRI/gvisor.md
  - docs/CRI/kata-containers.md
  - docs/operations/cgroups.md
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0
retrieved_at: 2026-07-14
topics:
  - containerd
  - container-runtime
  - cri
  - cgroups
reliability: authoritative
---

# Container runtime в v2.30.0

Выбор runtime задаётся переменной `container_manager` (значения: `containerd`,
`crio`, `docker`). Детально в базе знаний индексируется **containerd**;
остальные рантаймы перечислены кратко.

## containerd (детально)

Источник: `docs/CRI/containerd.md`.

Официально поддерживаемый и рекомендуемый runtime. Kubespray обеспечивает
базовую функциональность его использования как runtime по умолчанию.

### Включение

`k8s-cluster.yml`:

```yaml
container_manager: containerd
```

`etcd.yml`:

```yaml
etcd_deployment_type: host
```

Важно: когда узлы группы `etcd` входят также в `kube_node` (etcd
schedulable для рабочих нагрузок), containerd и dockerd не могут работать
одновременно — для запуска etcd-кластера только с containerd требуется
`etcd_deployment_type: host`.

### Зеркала реестров

`containerd_registries_mirrors` — список правил зеркалирования реестров.
Каждый элемент: `prefix`, `mirrors` (список: `host`, `capabilities`
`["pull", "resolve"]`, `skip_verify`), опционально `server`.

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

- Если ни одно зеркало не содержит образ, containerd делает fallback на
  `https://{{ prefix }}`. Поведение fallback переопределяется полем `server`.
- Для self-hosted (insecure) реестров задаётся `skip_verify: true` (пример с
  `http://test.registry.io`, `172.19.16.11:5000`, `repo:5000`).
- Переменные `containerd_registries` и `containerd_insecure_registries` —
  **устарели** (deprecated).

### Runtime-классы (RuntimeClass)

containerd поддерживает несколько конфигураций runtime через фичу Kubernetes
RuntimeClass.

- Runtime по умолчанию — `runc`, настраивается словарём `containerd_runc_runtime`
  (`name`, `type` `io.containerd.runc.v2`, `options`: `Root`, `SystemdCgroup`,
  `BinaryName`, `base_runtime_spec`).
- Дополнительные runtime — список словарей в `containerd_additional_runtimes`.
- Runtime по умолчанию меняется переменной `containerd_default_runtime`.

### Base runtime specs и лимит открытых файлов

- `base_runtime_spec` в словаре runtime указывает json-файл спецификации. Для
  `runc` установлено `cri-base.json` (генерируется
  `ctr oci spec > /etc/containerd/cri-base.json` с кастомным лимитом
  дескрипторов файлов на контейнер).
- Максимум file descriptors на контейнер для `runc` — переменная
  `containerd_base_runtime_spec_rlimit_nofile`.
- Собственные спецификации задаются через словарь `containerd_base_runtime_specs`
  (файлы помещаются в каталог конфигурации `/etc/containerd` по умолчанию и
  затем ссылаются по имени в runtime).

### NRI (Node Resource Interface)

Отключён по умолчанию. Для containerd версии v1.7.0 и выше включается:

```yaml
nri_enabled: true
```

### Статический бинарник

Для совместимости со старыми дистрибутивами (например Debian 11) используется
статический бинарник containerd. По умолчанию статический бинарник берётся,
если версия glibc системы < 2.34; иначе — обычный бинарник. Принудительно:

```yaml
containerd_static_binary: true
```

## Прочие рантаймы (кратко, не проиндексированы детально)

Перечислены для полноты; в базе знаний детально не разбираются.

- **CRI-O** (`docs/CRI/cri-o.md`) — `container_manager: crio`. Реестры
  настраиваются через `crio_registries`, `crio_insecure_registries`,
  `crio_registry_auth`. Поддержка user namespaces (`crio_runtimes`,
  `crio_remap_enable`), capabilities по умолчанию — `crio_default_capabilities`.
  NRI (`nri_enabled: true`) для CRI-O v1.26.0+.
- **Docker** (`docs/CRI/docker.md`) — `container_manager: docker`. `dockershim`
  заменён проектом `cri-dockerd` (Mirantis) начиная с kubespray 2.20. Ключевые
  переменные: `docker_storage_options`, `docker_cgroup_driver` (по умолчанию
  `systemd`), `docker_dns_servers_strict`, `docker_daemon_graph`,
  `docker_log_opts`, `docker_insecure_registries`, `docker_registry_mirrors`,
  `docker_options`.
- **gVisor** (`docs/CRI/gvisor.md`) — не отдельный `container_manager`, а
  runtime-класс (runsc) поверх containerd: `container_manager: containerd`
  + `gvisor_enabled: true`.
- **Kata Containers** (`docs/CRI/kata-containers.md`) — поверх containerd:
  `container_manager: containerd` + `kata_containers_enabled: true`
  (+ `etcd_deployment_type: host`). Единственный поддерживаемый гипервизор —
  Qemu. Генерируется runtimeClass `kata-qemu`. Pod Overhead
  (`kata_containers_qemu_overhead*`), выбор версии `kata_containers_version`,
  cgroup driver `kubelet_cgroup_driver`.

## cgroups и резервирование ресурсов

Источник: `docs/operations/cgroups.md`.

kubelet использует cgroups для ограничения потребления ресурсов и
предотвращения конкуренции между контейнерами и хостовыми демонами.

- `kubelet_enforce_node_allocatable` — уровни enforcement (по умолчанию
  `"pods"`; возможно `"pods,kube-reserved"`, `"pods,kube-reserved,system-reserved"`).
- Для enforcement `kube-reserved` / `system-reserved` требуется задать
  `kube_reserved_cgroups` / `system_reserved_cgroups`.
- Резервирование для kube: `kube_reserved: true`,
  `kube_reserved_cgroups_for_service_slice: kube.slice`,
  `kube_reserved_cgroups`, `kube_memory_reserved` (256Mi), `kube_cpu_reserved`
  (100m), опц. `kube_ephemeral_storage_reserved`, `kube_pid_reserved`.
- Резервирование для системы: `system_reserved: true`,
  `system_reserved_cgroups_for_service_slice: system.slice`,
  `system_reserved_cgroups`, `system_memory_reserved` (512Mi),
  `system_cpu_reserved` (500m), опц. `system_ephemeral_storage_reserved`,
  `system_pid_reserved`.

Итоговая иерархия cgroups: `kubepods.slice`, `kube.slice`
(с `{{container_manager}}.service` и `kubelet.service`), `system.slice`.

## Источники

- `docs/CRI/containerd.md`
- `docs/CRI/cri-o.md`, `docs/CRI/docker.md`, `docs/CRI/gvisor.md`, `docs/CRI/kata-containers.md`
- `docs/operations/cgroups.md`
- [[versions/v2.30.0/variables/container-runtime|Переменные рантайма]]
- [[versions/v2.30.0/README|Срез v2.30.0]]
