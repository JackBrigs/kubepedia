---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: docs
source_paths:
  - docs/operations/offline-environment.md
  - docs/operations/mirror.md
  - docs/advanced/downloads.md
  - docs/advanced/registry.md
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0
retrieved_at: 2026-07-14
topics:
  - offline
  - airgap
  - downloads
  - mirror
  - registry
reliability: authoritative
---

# Offline (air-gapped) развёртывание в v2.30.0

## Артефакты, необходимые offline

Источник: `docs/operations/offline-environment.md`.

При отсутствии прямого доступа в интернет заранее готовятся:

- статические файлы (архивы и бинарники);
- пакеты ОС (rpm/deb);
- контейнерные образы, используемые Kubespray (точный список зависит от setup);
- (опц.) Python-пакеты Kubespray — если ОС не даёт всех из `requirements.txt`;
- (опц.) Helm chart'ы — если `helm_enabled=true`.

Сервисы во внутренней сети:

- HTTP reverse proxy / cache / mirror для статических файлов;
- внутренний Yum/Deb-репозиторий для пакетов ОС;
- внутренний реестр контейнерных образов (заполнить всеми образами Kubespray);
- (опц.) внутренний PyPi-сервер;
- (опц.) внутренний Helm-реестр.

Списки артефактов генерирует `contrib/offline/generate_list.sh`;
инструменты offline-деплоя — в `contrib/offline/`.

### Контроль доступа

- Для доступа к `files_repo` учётные данные передаются url-encoding через
  `files_repo_host`, `files_repo_path`, `files_repo_user`, `files_repo_pass`
  (пароль — Ansible Vault). Внимание: булев `unsafe_show_logs` покажет учётные
  данные в задаче "Download_file | Show url of file to download"
  (`roles/download/tasks/download_file.yml`) — отключайте его в job-template
  (AWX/AAP/Semaphore).
- Для реестра — `registry_pass` (Vault) и `containerd_registry_auth`
  (`registry`, `username`, `password`).

### Настройка inventory (`group_vars/all/offline.yml`)

Переопределения реестров образов:

```yaml
kube_image_repo: "{{ registry_host }}"
gcr_image_repo: "{{ registry_host }}"
docker_image_repo: "{{ registry_host }}"
quay_image_repo: "{{ registry_host }}"
github_image_repo: "{{ registry_host }}"
```

URL загрузки бинарников: `kubeadm_download_url`, `kubectl_download_url`,
`kubelet_download_url`, `etcd_download_url` (нужен, если НЕ
`etcd_deployment=host`), `cni_download_url`, `crictl_download_url`,
`calicoctl_download_url`, `calico_crds_download_url`,
`containerd_download_url`, `runc_download_url`, `nerdctl_download_url`,
`get_helm_url`, `local_path_provisioner_helper_image_repo` — все строятся от
`{{ files_repo }}` с подстановкой `*_version`.

Insecure-реестр для containerd — `containerd_registries_mirrors`
(`prefix: {{ registry_addr }}`, `host: {{ registry_host }}`,
`skip_verify: true`).

Репозитории пакетов ОС для Docker/Containerd (по дистрибутивам):
`docker_rh_repo_base_url`, `docker_rh_repo_gpgkey`,
`docker_fedora_repo_*`, `containerd_fedora_repo_*`,
`docker_debian_repo_*`, `containerd_debian_repo_*`,
`docker_ubuntu_repo_*`, `containerd_ubuntu_repo_*` (+ `*_repokey`).

Ключевые переменные среды:

- `registry_host` — реестр образов (при нестандартном пути переопределить
  `*_image_repo`);
- `registry_addr` — реестр только как `[домен|ip]:[порт]`;
- `files_repo` — HTTP-сервер/reverse proxy для файлов (рекомендуется
  `*_version` в пути);
- `yum_repo` / `debian_repo` / `ubuntu_repo` — репозитории пакетов ОС (только
  для пакетов Docker/Containerd; остальные пакеты можно пропустить, отключив
  Ansible-тег `system-packages`).

### Python-пакеты

Рекомендуется контейнерный образ Kubespray (`quay.io/kubespray/kubespray`) —
все пакеты уже внутри. Иначе — HTTP(S)-прокси
(`pip install --proxy=... -r requirements.txt`) или внутренний PyPi
(`pip install -i https://pypiserver/pypi ...`).

Запуск как обычно: `ansible-playbook -i inventory/my_airgap_cluster/hosts.yaml
-b cluster.yml` (или через смонтированный inventory в контейнере).

## Публичное зеркало

Источник: `docs/operations/mirror.md`.

Ускоряет загрузку публичных ресурсов в отдельных регионах (например, Китай).
Настраивается как offline, но на публичное зеркало. Пример DaoCloud
(`<inventory>/group_vars/k8s_cluster.yml`):

```yaml
gcr_image_repo: "gcr.m.daocloud.io"
kube_image_repo: "k8s.m.daocloud.io"
docker_image_repo: "docker.m.daocloud.io"
quay_image_repo: "quay.m.daocloud.io"
github_image_repo: "ghcr.m.daocloud.io"
files_repo: "https://files.m.daocloud.io"
```

Предупреждение: используйте зеркала только доверенных провайдеров — команда
Kubespray не гарантирует их надёжность и безопасность.

## Режимы загрузки

Источник: `docs/advanced/downloads.md`.

Режим по умолчанию:

- каждый узел скачивает бинарники и образы сам (`download_run_once: False`);
- pull policy приложений — `k8s_image_pull_policy: IfNotPresent`;
- системные контейнеры (kubelet, etcd) — `download_always_pull: False`.

Режим "pull once, push many":

- `download_run_once: True` — Kubespray скачивает один раз и раздаёт узлам
  (делегат по умолчанию — первый `kube_control_plane`);
- `download_localhost: True` — делегатом становится localhost (требует
  установленного и запущенного runtime на Ansible-хосте и доступа к
  docker-группе / passwordless sudo).

Замечание: при `download_run_once: true` и `download_localhost: false` все
загрузки (включая образы, не нужные делегату) выполняются на делегате — под
кэш требуется больше места.

Кэширование:

- при `download_run_once: True` файлы кэшируются в `download_cache_dir` (по
  умолчанию `/tmp/kubespray_cache`, ~800MB на Ansible-узле);
- `download_force_cache: True` — использовать существующий кэш без загрузки
  (при `download_run_once: false`);
- `download_keep_remote_cache` — не удалять кэш с удалённых узлов после
  использования (рост места с ~150MB до ~550MB).

Артефакты описываются переменными: `foo_version`, `foo_download_url`,
`foo_checksum` (бинарники); `foo_image_repo`, `foo_image_tag`, опц.
`foo_digest_checksum` (образы). Образ можно задавать repo+tag или
repo+tag+sha256 digest (пример: `dnsmasq_digest_checksum`,
`dnsmasq_image_repo`, `dnsmasq_image_tag` — digest и tag должны
соответствовать друг другу). Полный список — в defaults роли `download`.

## Приватный реестр в кластере

Источник: `docs/advanced/registry.md`.

Опциональный аддон приватного Docker-реестра, запускаемый как `Pod` в
кластере (не поддерживает SSL/аутентификацию — срабатывает "insecure
registry"; обходится через прокси-DaemonSet `kube-registry-proxy` с hostPort
5000, доступный как `localhost:5000`). Компоненты: `PersistentVolume` /
`PersistentVolumeClaim` под хранилище (или `emptyDir`),
`ReplicationController` с образом `registry:2` (порт 5000, том
`/var/lib/registry`), `Service` `kube-registry`, `DaemonSet`
`kube-registry-proxy`. Использование образа: `localhost:5000/user/container`;
загрузка образов — через `kubectl port-forward`.

## Источники

- `docs/operations/offline-environment.md`
- `docs/operations/mirror.md`
- `docs/advanced/downloads.md`
- `docs/advanced/registry.md`
- [[versions/v2.30.0/variables/download|Переменные download]]
- [[versions/v2.30.0/variables/container-runtime|Переменные рантайма]]
- [[versions/v2.30.0/README|Срез v2.30.0]]
