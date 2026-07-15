---
project: kubespray
kubespray_version: v2.29.0
git_commit: 9991412
source_type: code
source_path: roles/kubespray_defaults/defaults/main/download.yml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.29.0
retrieved_at: 2026-07-14
topics:
  - download
  - offline
reliability: authoritative
---

# Механизм загрузки (download) в Kubespray v2.29.0

Часть среза [[versions/v2.29.0/README|Срез v2.29.0]]. Источник истины — парный YAML-справочник [[versions/v2.29.0/variables/download|download.yaml]]; эта заметка — его человекочитаемое изложение.

**Важно:** в теге v2.29.0 каталога `roles/download/defaults/` **нет** — роль `download` содержит только `meta/`, `tasks/`, `templates/`. Все переменные механизма загрузки определены в `roles/kubespray_defaults/defaults/main/download.yml` и попадают в область видимости всех ролей через роль `kubespray_defaults`.

## Как устроен механизм

Центральный элемент — словарь `downloads` (~60 элементов: etcd, cni, kubelet, kubectl, kubeadm, crictl, containerd, runc, cilium, coredns, helm, addons и т.д.). Каждый элемент описывает **либо файл** (`file: true` + `url`, `dest`, `checksum`, `unarchive`), **либо контейнерный образ** (`container: true` + `repo`, `tag`), а также условие `enabled` и целевые группы хостов `groups`. Недостающие поля дополняются из `download_defaults`. Роль `download` (`roles/download/tasks/`) обходит этот словарь и выполняет загрузки.

### Режим run_once

- `download_run_once: false` (по умолчанию) — каждый узел скачивает всё сам.
- `download_run_once: true` — каждый файл/образ скачивается **один раз** на хосте-делегате (`download_delegate`), затем раздаётся на узлы. Делегат: `localhost`, если `download_localhost: true`, иначе первый узел группы `kube_control_plane`. Образы при передаче сжимаются (`download_compress: 1`).
- На Flatcar Container Linux режим работает только с `download_localhost: true` (при условии, что localhost — другая ОС; требуются docker и sudo).

### Кэш

- `local_release_dir: /tmp/releases` — куда складываются файлы на целевых узлах.
- `download_cache_dir: /tmp/kubespray_cache` — локальный кэш на делегате/раннере.
- `download_force_cache: false` — при `download_run_once: false` принудительно раздавать из кэша и пополнять его скачанным с узлов.
- `download_keep_remote_cache: false` — не удалять удалённый кэш (нужно только при разработке Kubespray).

### Проверки и повторы

- Каждая файловая загрузка проверяется по контрольной сумме: переменные вида `<компонент>_binary_checksum` / `<компонент>_archive_checksum` берут значение из словарей `*_checksums` (`roles/kubespray_defaults/vars/main/checksums.yml`) по ключам `[image_arch][<версия>]`. Пер-версионные таблицы сумм в справочник не включаются — см. `checksums.yml` тега.
- `download_retries: 4` — число повторов для файлов и образов.
- `download_validate_certs: true` — проверка SSL в `get_url` (checksum проверяется даже при отключении).
- `download_always_pull: false` — pull образа только если его нет локально (по тегу/дайджесту).

### Работа с образами

Инструмент выбирается по `container_manager`: `image_command_tool` = `nerdctl` (containerd) / `crictl` (crio) / `docker`. Итоговые команды `image_pull_command` и `image_info_command` разрешаются через `lookup('vars', ...)` в соответствующие `*_image_pull_command` / `*_image_info_command`.

### Зеркала и offline-установка

Все URL и реестры строятся от небольшого набора базовых переменных — их переопределение перенаправляет **все** загрузки на локальные зеркала:

| Переменная | Значение по умолчанию | Что покрывает |
|---|---|---|
| `github_url` | `https://github.com` | etcd, cni, runc, containerd, nerdctl, crictl и др. |
| `dl_k8s_io_url` | `https://dl.k8s.io` | kubelet, kubectl, kubeadm |
| `storage_googleapis_url` | `https://storage.googleapis.com` | cri-o, gVisor |
| `get_helm_url` | `https://get.helm.sh` | Helm |
| `kube_image_repo` | `registry.k8s.io` | kube-proxy, pause, coredns, addons |
| `docker_image_repo` | `docker.io` | flannel, nginx, haproxy и др. |
| `quay_image_repo` | `quay.io` | etcd, cilium, calico, metallb, cert-manager |
| `github_image_repo` | `ghcr.io` | multus, kube-vip |
| `gcr_image_repo` | `gcr.io` | образы gcr |

Более точечно каждая загрузка настраивается своим `*_download_url` (25 переменных: `kubelet_download_url`, `etcd_download_url`, `cni_download_url`, `containerd_download_url` и т.д.) и парами `*_image_repo` / `*_image_tag` для образов.

## Ключевые переменные

### Режимы и поведение

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `download_run_once` | `false` | Скачивать один раз на делегате и раздавать |
| `download_localhost` | `false` | Делегат — localhost (нужны docker и sudo) |
| `download_delegate` | первый `kube_control_plane` либо `localhost` | Хост загрузки в режиме run_once |
| `download_compress` | `1` | Уровень сжатия образов при раздаче |
| `download_container` | `true` | Скачивать контейнерные образы |
| `download_always_pull` | `false` | Всегда делать pull |
| `download_validate_certs` | `true` | Проверять SSL при get_url |
| `download_retries` | `4` | Повторы загрузок |
| `skip_downloads` | `false` | Пропустить загрузки (переменные всё равно вычисляются) |
| `skip_kubeadm_images` | `false` | Пропустить образы kubeadm |
| `unsafe_show_logs` | `false` | Отладочный вывод задач загрузки |

### Каталоги и кэш

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `local_release_dir` | `/tmp/releases` | Каталог файлов на узлах |
| `download_cache_dir` | `/tmp/kubespray_cache` | Локальный кэш |
| `download_force_cache` | `false` | Принудительная раздача из кэша при run_once=false |
| `download_keep_remote_cache` | `false` | Не удалять удалённый кэш |

### Архитектура

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `image_arch` | `{{ host_architecture \| default('amd64') }}` | Архитектура бинарников/образов; ключ в checksums и URL |

Полный перечень (66 переменных с дословными Jinja-значениями) — в [[versions/v2.29.0/variables/download|download.yaml]].
