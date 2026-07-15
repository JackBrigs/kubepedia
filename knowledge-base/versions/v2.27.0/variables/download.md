---
project: kubespray
kubespray_version: v2.27.0
git_commit: 9ec9b3a
source_type: code
source_path: versions/v2.27.0/variables/download.yaml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.27.0
retrieved_at: 2026-07-15
topics:
  - download
reliability: authoritative
---

# Переменные механизма загрузки — Kubespray v2.27.0

Человекочитаемая заметка к машиночитаемому справочнику `download.yaml`.
**Источник истины — YAML-справочник** `versions/v2.27.0/variables/download.yaml`.
Назад к срезу: [[versions/v2.27.0/README|Срез v2.27.0]].

Единственный источник в коде тега `v2.27.0` (commit `9ec9b3a`):
`roles/kubespray-defaults/defaults/main/download.yml` (каталог с **дефисом**). Отдельного
каталога `roles/download/defaults/` в этой версии нет.

## Что здесь и чего здесь нет

Файл `download.yml` в теге огромный (288 top-level ключей). В этот справочник вынесены переменные
**механизма загрузки**: каталоги/кэш, режимы (`download_run_once` и др.), команды и выбор инструмента
работы с образами, базовые репозитории/URL, примеры `*_download_url`, словарь `downloads` и
`download_defaults`. Версии, URL, теги образов и контрольные суммы **конкретных компонентов**
распределены по профильным справочникам:

- etcd → [[versions/v2.27.0/variables/etcd|etcd.yaml]];
- CNI/Cilium → [[versions/v2.27.0/variables/cni|cni.yaml]];
- containerd/runc/nerdctl/crictl/skopeo/pause → [[versions/v2.27.0/variables/container-runtime|container-runtime.yaml]];
- версии/образы addon-компонентов (helm, metrics-server, cert-manager, CSI и т.п.) — в `addons.yaml` (отдельный срез), в охват `download.yaml` не входят.

## Отличия v2.27.0 от v2.29.1

- Многие версии заданы **явными литералами** (`containerd_version: 1.7.24`, `runc_version: v1.2.3`, `cni_version: v1.4.0`, `cilium_version: v1.15.9`), а не вычисляются из `checksums`.
- Переменной `kubeadm_image_repo` **нет** (в v2.29.1 есть).
- URL Kubernetes используют `{{ kube_version }}` напрямую (`kube_version` уже с префиксом v: `v1.31.4`).
- `nerdctl_image_pull_command` использует `ctr` (обход issue kubespray#10670).

## Каталоги и кэш

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `local_release_dir` | `/tmp/releases` | куда складываются файлы на узлах |
| `download_cache_dir` | `/tmp/kubespray_cache` | локальный кэш на раннере/делегате |
| `download_keep_remote_cache` | `false` | не удалять удалённый кэш |
| `download_force_cache` | `false` | раздавать из кэша при `download_run_once: false` |

## Режимы работы

`download_run_once: false`, `download_localhost: false`, `download_delegate` (localhost либо первый
`kube_control_plane`), `download_container: true`, `download_always_pull: false`,
`download_validate_certs: true`, `download_retries: 4`, `download_compress: 1`,
`skip_downloads: false`, `skip_kubeadm_images: false`, `unsafe_show_logs: false`.

## Образы: выбор инструмента

`image_command_tool` по `container_manager`: containerd → `nerdctl` (но pull через `ctr`),
crio → `crictl`, docker → `docker`. Итоговые команды разрешаются через `lookup('vars', ...)`
в `image_pull_command` / `image_info_command` (+ `*_on_localhost`). `image_arch` = архитектура ключа checksums.

## Базовые репозитории и URL (точки подмены на зеркала)

| Репозитории образов | URL файлов |
|---|---|
| `gcr_image_repo: gcr.io` | `github_url: https://github.com` |
| `kube_image_repo: registry.k8s.io` | `dl_k8s_io_url: https://dl.k8s.io` |
| `docker_image_repo: docker.io` | `storage_googleapis_url: https://storage.googleapis.com` |
| `quay_image_repo: quay.io` | `get_helm_url: https://get.helm.sh` |
| `github_image_repo: ghcr.io` | |

`kube_major_version` (например `v1.31`) — ключ, по которому выбираются версии etcd, crictl, crio, pause из `*_supported_versions`.

## Словарь загрузок

`downloads` — главный реестр (~74 элемента): для каждого задаются `enabled`, `container`/`file`,
`repo`/`tag` или `url`/`dest`/`checksum`, `unarchive`, `owner`/`mode` и целевые `groups`.
`download_defaults` — значения по умолчанию для каждого элемента (в v2.27.0 включают поле `version`).

## Связанное

- [[versions/v2.27.0/variables/etcd|etcd.yaml]]
- [[versions/v2.27.0/variables/cni|cni.yaml]]
- [[versions/v2.27.0/variables/container-runtime|container-runtime.yaml]]
- [[versions/v2.27.0/README|Срез v2.27.0]]

## Сверка полноты

Источник `roles/kubespray-defaults/defaults/main/download.yml` — 288 top-level ключей. В `download.yaml` вынесены **54** переменные механизма загрузки (каталоги, режимы, команды образов, базовые репозитории/URL, `kube_major_version`, выборка `*_download_url`, `downloads`, `download_defaults`). Остальные ключи — это версии/URL/теги образов/контрольные суммы конкретных компонентов, которые по проектной структуре размещены в профильных справочниках (etcd.yaml, cni.yaml, container-runtime.yaml) и в addons.yaml (вне охвата этого файла).
