---
project: kubespray
kubespray_version: v2.28.1
git_commit: a20891a
source_type: docs
source_paths:
  - docs/operations/offline-environment.md
  - docs/operations/mirror.md
  - docs/advanced/downloads.md
  - docs/advanced/registry.md
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.28.1
retrieved_at: 2026-07-15
topics:
  - offline
  - airgap
  - mirror
  - registry
  - downloads
reliability: authoritative
---

# Оффлайн-развёртывание и зеркала в v2.28.1

Дайджест документации по offline/airgap-развёртыванию и зеркалам строго с тега
`v2.28.1` (commit `a20891a`). Все четыре исходных файла идентичны версии v2.29.1.

## Оффлайн-развёртывание (airgap)

Источник: `docs/operations/offline-environment.md`.

Если у серверов нет прямого доступа в интернет, заранее из среды с доступом
нужно получить артефакты:

- статические файлы (архивы и бинарники);
- пакеты ОС (rpm/deb);
- контейнерные образы, используемые Kubespray;
- [опционально] Python-пакеты (если ОС не даёт нужных версий из `requirements.txt`);
- [опционально] Helm-чарты (если `helm_enabled=true`).

Во внутренней сети требуется поднять сервисы:

- HTTP reverse proxy/cache/mirror для статических файлов;
- внутренний Yum/Deb репозиторий для пакетов ОС;
- внутренний реестр контейнерных образов (наполнить всеми образами Kubespray);
- [опционально] внутренний PyPi-сервер;
- [опционально] внутренний Helm-реестр.

Список артефактов формируется скриптом `contrib/offline/generate_list.sh`;
инструменты для offline — в `contrib/offline/`.

Запуск после подготовки — обычной командой:

```bash
ansible-playbook -i inventory/my_airgap_cluster/hosts.yaml -b cluster.yml
```

### Контроль доступа (аутентификация)

- Для доступа к `files_repo` (скачивание бинарников) логин/пароль задаются через
  url-encoding: `files_repo_host`, `files_repo_path`, `files_repo_user`,
  `files_repo_pass` (можно через ansible-vault), затем
  `files_repo: "https://{{ files_repo_user ~ ':' ~ files_repo_pass ~ '@' ~ files_repo_host ~ files_repo_path }}"`.
  Внимание: булев `unsafe_show_logs` покажет эти учётные данные в задаче
  "Download_file | Show url of file to download" (`roles/download/tasks/download_file.yml`);
  отключается в job-template AWX/AAP/Semaphore.
- Для приватного реестра образов — `containerd_registry_auth` (список с
  `registry`/`username`/`password`, пароль через vault).

### Переменные зеркал в inventory

Настройки правятся в `inventory/sample/group_vars/all/offline.yml`. Ключевые
переменные (overrides реестров образов — `*_image_repo`):

```yaml
kube_image_repo: "{{ registry_host }}"
gcr_image_repo: "{{ registry_host }}"
docker_image_repo: "{{ registry_host }}"
quay_image_repo: "{{ registry_host }}"
github_image_repo: "{{ registry_host }}"
local_path_provisioner_helper_image_repo: "{{ registry_host }}/busybox"
```

Переопределение URL для бинарников (`*_download_url`):

```yaml
kubeadm_download_url:  "{{ files_repo }}/kubernetes/v{{ kube_version }}/kubeadm"
kubectl_download_url:  "{{ files_repo }}/kubernetes/v{{ kube_version }}/kubectl"
kubelet_download_url:  "{{ files_repo }}/kubernetes/v{{ kube_version }}/kubelet"
etcd_download_url:     "{{ files_repo }}/kubernetes/etcd/etcd-v{{ etcd_version }}-linux-{{ image_arch }}.tar.gz"
cni_download_url:      "{{ files_repo }}/kubernetes/cni/cni-plugins-linux-{{ image_arch }}-v{{ cni_version }}.tgz"
crictl_download_url:   "{{ files_repo }}/kubernetes/cri-tools/crictl-v{{ crictl_version }}-{{ ansible_system | lower }}-{{ image_arch }}.tar.gz"
calicoctl_download_url:    "{{ files_repo }}/kubernetes/calico/v{{ calico_ctl_version }}/calicoctl-linux-{{ image_arch }}"
calico_crds_download_url:  "{{ files_repo }}/kubernetes/calico/v{{ calico_version }}.tar.gz"
containerd_download_url:   "{{ files_repo }}/containerd-{{ containerd_version }}-linux-{{ image_arch }}.tar.gz"
runc_download_url:         "{{ files_repo }}/runc.{{ image_arch }}"
nerdctl_download_url:      "{{ files_repo }}/nerdctl-{{ nerdctl_version }}-{{ ansible_system | lower }}-{{ image_arch }}.tar.gz"
get_helm_url:              "{{ files_repo }}/get.helm.sh"
```

- `etcd_download_url` — опционально, не нужен при `etcd_deployment_type: host`.
- Insecure-реестр для containerd в оффлайне — через `containerd_registries_mirrors`
  (`prefix: "{{ registry_addr }}"`, `host: "{{ registry_host }}"`, `skip_verify: true`).

Репозитории пакетов ОС (задавать только под свою ОС): для Docker/containerd —
`docker_rh_repo_base_url`, `containerd_fedora_repo_base_url`,
`containerd_debian_repo_base_url`, `containerd_ubuntu_repo_base_url` и парные
`*_gpgkey` / `*_repokey`.

Опорные переменные, которые нужно определить в inventory:

- `registry_host` — реестр образов (при нестандартных путях переопределить `*_image_repo`);
- `registry_addr` — реестр в формате `[domain|ip]:[port]`;
- `files_repo` — HTTP-сервер/reverse proxy для файлов (рекомендуется использовать
  `*_version` в путях);
- `yum_repo` / `debian_repo` / `ubuntu_repo` — репозитории пакетов ОС (только для
  Docker/containerd; установку прочих пакетов можно пропустить, скипнув тег
  `system-packages`).

Python-пакеты: проще всего использовать [kubespray container image](https://quay.io/kubespray/kubespray)
(все пакеты вшиты); иначе — прокси с доступом в интернет или внутренний PyPi
(`pip install -i https://pypiserver/pypi -r requirements.txt`).

## Публичное зеркало загрузок

Источник: `docs/operations/mirror.md`.

Публичное зеркало ускоряет загрузку публичных ресурсов в отдельных регионах
(например, Китай). Настройка аналогична offline — переопределяются те же
`*_image_repo` и `files_repo`. Пример (DaoCloud):

```yaml
# <your_inventory>/group_vars/k8s_cluster.yml
gcr_image_repo:    "gcr.m.daocloud.io"
kube_image_repo:   "k8s.m.daocloud.io"
docker_image_repo: "docker.m.daocloud.io"
quay_image_repo:   "quay.m.daocloud.io"
github_image_repo: "ghcr.m.daocloud.io"
files_repo:        "https://files.m.daocloud.io"
```

Предупреждение: использовать зеркала только доверенных провайдеров — команда
Kubespray не проверяет их надёжность и безопасность.

## Режимы загрузки (downloads)

Источник: `docs/advanced/downloads.md`.

Режим по умолчанию:

- каждый узел скачивает бинарники и образы самостоятельно — `download_run_once: False`;
- pull policy приложений K8s — `k8s_image_pull_policy: IfNotPresent`;
- для системных контейнеров (kubelet, etcd) — `download_always_pull: False`
  (pull только если repo и tag/sha256 отличаются от имеющегося на хосте).

Режим "pull once, push many":

- `download_run_once: True` — скачать образы/бинарники один раз и разложить по
  узлам; делегат по умолчанию — первый `kube_control_plane`;
- `download_localhost: True` — делегатом становится localhost (требуется
  установленный и запущенный container runtime на Ansible-хосте, доступ к
  docker-группе или passwordless sudo).
- Замечание: при `download_run_once: True` и `download_localhost: False` все
  загрузки (в т.ч. лишние образы) идут на узел-делегат — потребуется больше места.

Кэширование:

- при `download_run_once: True` файлы кэшируются в `download_cache_dir`
  (по умолчанию `/tmp/kubespray_cache`, ~800MB на Ansible-узле);
- при `download_run_once: False` кэш по умолчанию не наполняется; чтобы
  использовать готовый кэш без скачивания — `download_force_cache: True`;
- кэш-образы на узлах по умолчанию удаляются после использования;
  `download_keep_remote_cache` предотвращает удаление (рост места со 150MB до ~550MB).

Образы и бинарники описываются переменными `foo_version`, `foo_download_url`,
`foo_checksum` (бинарники) и `foo_image_repo`, `foo_image_tag`,
опционально `foo_digest_checksum` (образы). Полный список — в defaults роли download.

## Встроенный (in-cluster) Docker registry

Источник: `docs/advanced/registry.md`.

Kubernetes предлагает опциональный аддон приватного Docker registry внутри
кластера — место для приватных образов.

- Реестр работает как `Pod` (`registry:2`), без SSL/аутентификации (срабатывает
  логика Docker "insecure registry"). Обход: на каждом узле — прокси
  (`kube-registry-proxy`) через `hostPort`, Docker считает `localhost` безопасным.
- Хранилище: `PersistentVolume` + `PersistentVolumeClaim` (`kube-registry-pvc`)
  либо `emptyDir` при отсутствии сетевого хранилища. При нескольких репликах CSI
  должен поддерживать `ReadWriteMany`.
- Компоненты: `ReplicationController` `kube-registry-v0`, `Service`
  `kube-registry` (port 5000), `DaemonSet` `kube-registry-proxy` (hostPort 5000).
  Важно: уникальные идентификаторы rc-svc и daemon-set, иначе прокси начнёт
  проксировать сам себя.
- Использование: образ вида `localhost:5000/user/container`; заливка через
  `kubectl port-forward --namespace kube-system $POD 5000:5000`.

## Источники

- `docs/operations/offline-environment.md` — https://github.com/kubernetes-sigs/kubespray/blob/v2.28.1/docs/operations/offline-environment.md
- `docs/operations/mirror.md` — https://github.com/kubernetes-sigs/kubespray/blob/v2.28.1/docs/operations/mirror.md
- `docs/advanced/downloads.md` — https://github.com/kubernetes-sigs/kubespray/blob/v2.28.1/docs/advanced/downloads.md
- `docs/advanced/registry.md` — https://github.com/kubernetes-sigs/kubespray/blob/v2.28.1/docs/advanced/registry.md

Связанные заметки: [[versions/v2.28.1/variables/download|Переменные download]] · [[versions/v2.28.1/variables/container-runtime|Переменные рантайма]] · [[versions/v2.28.1/docs/proxy|Прокси]] · [[versions/v2.28.1/README|Срез v2.28.1]]
