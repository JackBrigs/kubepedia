---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: docs
source_paths:
  - docs/operations/offline-environment.md
  - docs/operations/mirror.md
  - docs/advanced/downloads.md
  - docs/advanced/registry.md
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0
retrieved_at: 2026-07-14
topics:
  - offline
  - mirror
reliability: authoritative
---

# Offline / air-gapped развёртывание в Kubespray v2.31.0

Дайджест документации по развёртыванию без прямого доступа в интернет, публичным зеркалам, режимам скачивания и приватному реестру.

См. также: [[versions/v2.31.0/variables/download|Переменные download]].

## Offline environment (air-gapped)

Если у серверов нет прямого доступа в интернет, заранее из среды с доступом нужно получить артефакты:

- статические файлы (zip и бинарники);
- OS-пакеты (rpm/deb);
- container images, используемые Kubespray (полный список зависит от конфигурации);
- [опц.] Python-пакеты (если ОС не даёт всё из `requirements.txt`);
- [опц.] файлы Helm-чартов (только при `helm_enabled=true`).

Затем в offline-среде поднимаются сервисы:

- HTTP reverse proxy/cache/mirror для статических файлов;
- внутренний Yum/Deb-репозиторий OS-пакетов;
- внутренний container image registry со всеми образами Kubespray;
- [опц.] внутренний PyPi-сервер;
- [опц.] внутренний Helm registry.

Список артефактов генерируется скриптом `contrib/offline/generate_list.sh`; дополнительные инструменты — в `contrib/offline/`.

**Советы из docs (актуально для v2.31.0):**

- В `files_repo` использовать исходные домены как каталоги верхнего уровня: `github.com/`, `dl.k8s.io/`, `storage.googleapis.com/`, `get.helm.sh/`.
- Для Cilium зазеркалировать `https://helm.cilium.io/index.yaml` и чарт `cilium-1.18.2.tgz` в `files_repo`.

### Контроль доступа

- **files_repo с логином/паролем:** использовать url-encoding через переменные `files_repo_host`, `files_repo_path`, `files_repo_user`, `files_repo_pass` (пароль шифровать ansible-vault). Итоговый `files_repo` собирается как `https://user:pass@host/path`. Предупреждение: булев `unsafe_show_logs` покажет учётные данные в задаче "Download_file | Show url of file to download" (`roles/download/tasks/download_file.yml`) — его можно отключить в job-template AWX/AAP/Semaphore.
- **registry с логином/паролем:** `registry_user` и `registry_pass` для `registry_addr` (пароль шифровать ansible-vault).

### Доступ containerd к приватному реестру

- **Containerd 2+** — через `containerd_registries_mirrors` с заголовком авторизации:

```yaml
containerd_registries_mirrors:
  - prefix: "{{ registry_addr }}"
    mirrors:
      - host: "https://{{ registry_addr }}"
        capabilities: ["pull", "resolve"]
        skip_verify: false
        header:
          Authorization: ["Basic {{ (registry_user + ':' + registry_pass) | b64encode }}"]
```

- **Containerd 1.7** — через `containerd_registry_auth` (список с `registry`, `username`, `password`).

### Настройка inventory (переопределения реестров и URL)

Правятся в `inventory/sample/group_vars/all/offline.yml`. Ключевые переопределения:

```yaml
kube_image_repo: "{{ registry_host }}"
gcr_image_repo: "{{ registry_host }}"
docker_image_repo: "{{ registry_host }}"
quay_image_repo: "{{ registry_host }}"
github_image_repo: "{{ registry_host }}"
github_url: "{{ files_repo }}/github.com"
dl_k8s_io_url: "{{ files_repo }}/dl.k8s.io"
storage_googleapis_url: "{{ files_repo }}/storage.googleapis.com"
get_helm_url: "{{ files_repo }}/get.helm.sh"
local_path_provisioner_helper_image_repo: "{{ registry_host }}/busybox"
```

- **Cilium в offline:** `cilium_install_extra_flags: "--repository {{ files_repo }}/helm.cilium.io/"` и `cilium_extra_values` с `useDigest: false` для всех образов + `operator.image.override: "{{ registry_host }}/cilium/operator-generic:v1.18.2"`.
- **OS-пакеты Docker/Containerd** (задаётся только для своей ОС): переменные вида `docker_rh_repo_base_url`, `docker_rh_repo_gpgkey` (CentOS/RHEL/AlmaLinux/Rocky); `docker_fedora_repo_*`, `containerd_fedora_repo_*` (Fedora); `docker_debian_repo_*`, `containerd_debian_repo_*` + `containerd_debian_repo_repokey` (Debian); `docker_ubuntu_repo_*`, `containerd_ubuntu_repo_*` + `containerd_ubuntu_repo_repokey` (Ubuntu).

**Переменные, которые нужно определить в inventory:**

- `registry_host` — реестр образов. Если путь репозитория отличается от дефолтов роли (`roles/kubespray_defaults/defaults/main/download.yml`), нужно переопределить `*_image_repo`; при совпадении пути — переопределять ничего не нужно.
- `registry_addr` — реестр в формате `[domain или ip]:[port]`.
- `files_repo` — HTTP-сервер/reverse proxy для файлов; путь произвольный, рекомендуется включать `*_version` в путь, чтобы не менять настройку при апгрейде компонентов.
- `yum_repo` / `debian_repo` / `ubuntu_repo` — OS-репозиторий по вашей ОС (используются только для пакетов Docker/Containerd; прочие пакеты могут ставиться из других репозиториев — установку из них можно отключить, пропустив тег `system-packages`).

### Python-пакеты Kubespray

- **Рекомендуется:** использовать [kubespray container image](https://quay.io/kubespray/kubespray) — все пакеты уже внутри; достаточно скопировать образ в свой приватный реестр.
- **Вручную:** сверить `requirements.txt` с пакетами ОС; недостающие ставить через прокси с доступом в интернет (`pip install --proxy=...`) или через внутренний PyPi-сервер (`pip install -i https://pypiserver/pypi ...`).

### Запуск

Обычный запуск после подготовки артефактов и inventory: `ansible-playbook -i inventory/my_airgap_cluster/hosts.yaml -b cluster.yml`. При использовании контейнерного образа inventory монтируется внутрь контейнера.

## Публичное зеркало (mirror)

Полезно для быстрого скачивания публичных ресурсов в отдельных регионах (например, Китай). Настройка — по инструкции offline, с указанием зеркал:

```yaml
# в <inventory>/group_vars/k8s_cluster.yml
gcr_image_repo: "gcr.m.daocloud.io"
kube_image_repo: "k8s.m.daocloud.io"
docker_image_repo: "docker.m.daocloud.io"
quay_image_repo: "quay.m.daocloud.io"
github_image_repo: "ghcr.m.daocloud.io"
files_repo: "https://files.m.daocloud.io"
```

Предупреждение docs: использовать зеркала только при доверии провайдеру — команда Kubespray не проверяет их надёжность/безопасность. Пример community-зеркала: DaoCloud (Китай) — image-mirror и files-mirror.

## Режимы скачивания (downloads)

Режим по умолчанию:

- каждый узел скачивает бинарники и образы сам — `download_run_once: False`;
- pull policy для K8s-приложений — `k8s_image_pull_policy: IfNotPresent`;
- для системных контейнеров (kubelet, etcd) — `download_always_pull: False` (тянуть только если repo и tag/sha256 отличаются от имеющегося).

Режим "pull once, push many":

- `download_run_once: True` — скачать образы и бинарники один раз и раздать узлам; делегат по умолчанию — первый `kube_control_plane`.
- `download_localhost: True` — сделать делегатом localhost (полезно, если узлы не имеют внешнего доступа); требует установленного и запущенного container runtime на Ansible-хосте и прав пользователя (группа docker или passwordless sudo). Даже при `download_localhost: false` файлы всё равно копируются на Ansible-сервер с делегата и раздаются оттуда.
- Замечание: при `download_run_once: true` и `download_localhost: false` все загрузки (включая ненужные делегату образы) идут на делегат — на нём потребуется больше места.

Кэширование:

- при `download_run_once: True` файлы кэшируются локально в `download_cache_dir` (по умолчанию `/tmp/kubespray_cache`, ~800MB на Ansible-узле); на узлах для кэша образа нужно чуть меньше 150MB (самый большой образ).
- при `download_run_once: false` файлы по умолчанию не забираются в локальный кэш; чтобы использовать готовый кэш без скачивания — `download_force_cache: True`.
- кэш-образы на узлах по умолчанию удаляются после использования; `download_keep_remote_cache` сохраняет их (тогда потребность в месте растёт со 150MB до ~550MB).

Образы и бинарники описываются переменными `foo_version`, `foo_download_url`, `foo_checksum` (бинарники) и `foo_image_repo`, `foo_image_tag` или опц. `foo_digest_checksum` (контейнеры). Образ можно задать через repo+tag или repo+tag+sha256-digest (при указании digest tag и digest должны соответствовать друг другу). Полный список переменных — в defaults роли download.

## Приватный Docker-реестр в кластере (registry addon)

Опциональный addon-реестр запускается как `Pod` в кластере (место для приватных образов). Не поддерживает SSL и аутентификацию — срабатывает логика "insecure registry" Docker; обход: на каждом узле запускается прокси (DaemonSet `kube-registry-proxy`), пробрасывающий порт на узел через hostPort, что Docker принимает как "secure" (доступ через `localhost`).

- Хранилище: через `PersistentVolume`/`PersistentVolumeClaim` (для сетевого хранилища) или `emptyDir` (без persistent-хранилища). При нескольких репликах CSI-драйвер должен поддерживать `ReadWriteMany`.
- Реестр запускается как `ReplicationController` (`registry:2`, порт 5000), экспонируется `Service` `kube-registry` в namespace `kube-system`, на узлах — DaemonSet-прокси на порт 5000 (hostPort).
- Использование образа: `image: localhost:5000/user/container`. Загрузка образов извне — через `kubectl port-forward`.
- Важно: при изменении RC/Service/DaemonSet сохранять уникальные идентификаторы, иначе localhost-прокси зарегистрируются на upstream-сервис и начнут проксировать сами себя.

## Источники

- docs/operations/offline-environment.md (заметно изменён в v2.31.0)
- docs/operations/mirror.md
- docs/advanced/downloads.md
- docs/advanced/registry.md
- [[versions/v2.31.0/variables/download|Переменные download]]
- [[versions/v2.31.0/README|Срез v2.31.0]]
