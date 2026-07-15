---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: code
source_path: roles/kubespray_defaults/defaults/main/download.yml
source_url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
retrieved_at: 2026-07-14
topics:
  - download
  - cache
reliability: authoritative
---

# Механизм загрузки (download) в v2.31.0

Срез: [[versions/v2.31.0/README|Срез v2.31.0]]

Источник истины — YAML-справочник [[versions/v2.31.0/variables/download|download.yaml]]
(`roles/kubespray_defaults/defaults/main/download.yml`). Ниже — человекочитаемое
изложение. Версии компонентов вынесены в [[versions/v2.31.0/components|components]].

## Как устроен механизм

Роль `download` в Kubespray отвечает за скачивание всех артефактов кластера:
бинарных файлов (kubelet, kubeadm, kubectl, etcd, cni, crictl, containerd, helm и
т.д.) и контейнерных образов (calico, cilium, coredns, metrics-server и др.).

Центральная структура — словарь `downloads`: каждый его элемент описывает один
артефакт (файл или образ), условие его загрузки (`enabled`), путь назначения,
URL или репозиторий/тег образа, контрольную сумму и группы хостов, на которые он
распространяется. Значения по умолчанию для полей задаёт `download_defaults`.

Порядок работы регулируется несколькими режимами:

- **Обычный режим** (`download_run_once: false`) — каждый узел скачивает нужные
  ему артефакты самостоятельно.
- **Однократная загрузка** (`download_run_once: true`) — файлы и образы
  скачиваются один раз на узле-делегате (`download_delegate`), затем
  распространяются на остальные узлы. Экономит трафик.
- **Загрузка на localhost** (`download_localhost: true`) — в режиме
  `download_run_once` загрузка идёт на управляющем узле (нужны docker и sudo),
  а не на первом узле `kube_control_plane`.

Контрольные суммы файлов берутся из больших таблиц
`roles/kubespray_defaults/vars/main/checksums.yml`, индексируемых по
`[image_arch][version]`. Для контейнерных образов проверка по умолчанию идёт по
тегу (digest = `None`). Даже при отключённой валидации TLS
(`download_validate_certs: false`) контрольная сумма файлов всё равно проверяется.

## Ключевые переменные механизма

### Пути и режимы

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `local_release_dir` | `/tmp/releases` | Каталог загрузки бинарников/архивов на узлах |
| `download_cache_dir` | `/tmp/kubespray_cache` | Каталог кэша на runner/делегате |
| `download_run_once` | `false` | Скачивать один раз и раздавать на узлы |
| `download_localhost` | `false` | В режиме run_once качать на localhost |
| `download_delegate` | первый узел `kube_control_plane` (или localhost) | Узел-делегат загрузки |
| `download_container` | `true` | Скачивать контейнерные образы |
| `download_always_pull` | `false` | Всегда пуллить образы заново |
| `download_force_cache` | `false` | Использовать/пополнять кэш при run_once=false |
| `download_keep_remote_cache` | `false` | Не удалять удалённый кэш после использования |
| `download_compress` | `1` | Уровень сжатия при передаче (1 — самый быстрый) |

### Надёжность и отладка

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `download_retries` | `4` | Число повторов при скачивании |
| `download_validate_certs` | `true` | Проверка TLS в get_url (checksum проверяется всегда) |
| `skip_downloads` | `false` | Только вычислить переменные роли, без загрузок |
| `skip_kubeadm_images` | `false` | Пропустить образы, управляемые kubeadm |
| `unsafe_show_logs` | `false` (в CI — `true`) | Показ отладочной инфо (может содержать приватные данные) |
| `image_arch` | `amd64` | Архитектура образов/пакетов |

### Базовые URL и репозитории образов

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `github_url` | `https://github.com` | Релизы компонентов с GitHub |
| `dl_k8s_io_url` | `https://dl.k8s.io` | Бинарники Kubernetes |
| `storage_googleapis_url` | `https://storage.googleapis.com` | cri-o, gVisor |
| `get_helm_url` | `https://get.helm.sh` | Helm |
| `kube_image_repo` | `registry.k8s.io` | Образы Kubernetes |
| `docker_image_repo` | `docker.io` | Docker Hub |
| `quay_image_repo` | `quay.io` | calico, cilium, cert-manager, metallb |
| `github_image_repo` | `ghcr.io` | multus, kube-vip |
| `gcr_image_repo` | `gcr.io` | Google Container Registry |

### Шаблоны URL загрузки (`*_download_url`)

Для каждого файла есть переменная `<component>_download_url`, собираемая из
базового URL, версии компонента и `image_arch`. Примеры:

| Переменная | Шаблон |
|---|---|
| `kubelet_download_url` | `{{ dl_k8s_io_url }}/release/v{{ kube_version }}/bin/linux/{{ image_arch }}/kubelet` |
| `etcd_download_url` | `{{ github_url }}/etcd-io/etcd/releases/download/v{{ etcd_version }}/etcd-v{{ etcd_version }}-linux-{{ image_arch }}.tar.gz` |
| `cni_download_url` | `{{ github_url }}/containernetworking/plugins/releases/download/v{{ cni_version }}/cni-plugins-linux-{{ image_arch }}-v{{ cni_version }}.tgz` |
| `containerd_download_url` | `{{ github_url }}/containerd/containerd/releases/download/v{{ containerd_version }}/containerd-...{{ containerd_version }}-linux-{{ image_arch }}.tar.gz` |
| `helm_download_url` | `{{ get_helm_url }}/helm-v{{ helm_version }}-linux-{{ image_arch }}.tar.gz` |

Полный перечень `*_download_url` — в `download.yml` тега v2.31.0.

## Схема записи словаря `downloads`

Каждый элемент `downloads` содержит поля: `container` / `file`, `enabled`,
`dest`, `repo`, `tag`, `checksum`, `url`, `unarchive`, `owner`, `mode`, `groups`.
Значения по умолчанию задаются в `download_defaults`
(`owner: {{ kube_owner }}`, остальное — `false`/`None`).

В v2.31.0 словарь `downloads` включает загрузку файлов (cni, kubeadm, kubelet,
kubectl, crictl, crio, cri_dockerd, crun, youki, runc, kata_containers,
containerd, gvisor, nerdctl, skopeo, ciliumcli, calicoctl, calico_crds, helm, yq,
argocd_install, gateway_api_crds, prometheus_operator_crds) и контейнерных
образов (etcd, cilium и hubble-компоненты, multus, flannel, calico_*, kube_ovn,
kube_router, pod_infra/pause, kube-vip, nginx, haproxy, coredns, nodelocaldns,
dnsautoscaler, registry, metrics_server, local_*_provisioner, cert_manager_*,
csi_*, metallb_*, ingress_alb_controller). Условия `enabled` зависят от опций
кластера (`kube_network_plugin`, `container_manager`, `*_enabled`).
