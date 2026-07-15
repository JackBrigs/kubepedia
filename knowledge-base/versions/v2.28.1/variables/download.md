---
project: kubespray
kubespray_version: v2.28.1
git_commit: a20891a
source_type: code
source_path: roles/kubespray_defaults/defaults/main/download.yml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.28.1
retrieved_at: 2026-07-15
topics:
  - download
  - offline
reliability: authoritative
---

# Механизм загрузки (download) в Kubespray v2.28.1

Часть среза [[versions/v2.28.1/README|Срез v2.28.1]]. Источник истины — парный YAML-справочник [[versions/v2.28.1/variables/download|download.yaml]]; эта заметка — его человекочитаемое изложение.

**Важно:** в теге v2.28.1 каталога `roles/download/defaults/` **нет** — роль `download` содержит только `meta/`, `tasks/`, `templates/`. Все переменные механизма загрузки определены в `roles/kubespray_defaults/defaults/main/download.yml` и попадают в область видимости всех ролей через роль `kubespray_defaults`.

## Как устроен механизм

Центральный элемент — словарь `downloads` (~73 элемента: etcd, cni, kubelet, kubectl, kubeadm, crictl, containerd, runc, cilium, coredns, helm, weave_kube/weave_npc, argocd_install (новый в v2.28.1), addons и т.д.). Каждый элемент описывает **либо файл** (`file: true` + `url`, `dest`, `checksum`, `unarchive`), **либо контейнерный образ** (`container: true` + `repo`, `tag`), а также условие `enabled` и целевые группы хостов `groups`. Недостающие поля дополняются из `download_defaults`. Роль `download` (`roles/download/tasks/`) обходит этот словарь и выполняет загрузки.

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
| `docker_image_repo` | `docker.io` | flannel, weave, nginx, haproxy и др. |
| `quay_image_repo` | `quay.io` | etcd, cilium, calico, metallb, cert-manager |
| `github_image_repo` | `ghcr.io` | multus, kube-vip |
| `gcr_image_repo` | `gcr.io` | образы gcr |

Более точечно каждая загрузка настраивается своим `*_download_url` (24 переменные: `kubelet_download_url`, `etcd_download_url`, `cni_download_url`, `containerd_download_url`, `yq_download_url`, `gateway_api_crds_download_url` и т.д.) и парами `*_image_repo` / `*_image_tag` для образов.

## Отличия v2.28.1 от v2.29.1 (в области механизма загрузки)

- `unsafe_show_logs` в v2.28.1 задан **простым значением** `false` (в v2.29.1 — выражение с `lookup('env', 'CI_PROJECT_URL')`).
- `containerd_download_url` в v2.28.1 **без** условия `static-` в имени архива (опция статического бинарника containerd появилась в v2.29.1).
- В v2.28.1 **отсутствуют** переменные `kubeadm_image_repo`, `prometheus_operator_crds_download_url` — обе добавлены в v2.29.1.
- Отличие v2.28.1 от v2.28.0: ArgoCD переведён на загрузку по контрольной сумме. В `download.yml` добавлены `argocd_version` (= первый ключ `argocd_install_checksums.no_arch`, в теге 2.14.5), `argocd_install_url` (raw-манифест `install.yaml`), `argocd_install_checksum` и элемент словаря `downloads.argocd_install`. Ранее (v2.28.0) манифест ArgoCD скачивался ролью `kubernetes-apps/argocd` без проверки контрольной суммы.
- Пер-компонентные версии и таблицы поддерживаемых версий (`kube_major_version`, `pod_infra_supported_versions`, `etcd_supported_versions`, `crictl_supported_versions`, `crio_supported_versions`, `scheduler_plugins_supported_versions`) в v2.28.1 физически лежат в этом же `download.yml`; в v2.29.1 часть из них перенесена в `roles/kubespray_defaults/vars/main.yml`. Это переменные версий компонентов, а не механизма загрузки — в данный справочник подробно не включены.

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

Полный перечень (65 переменных с дословными Jinja-значениями) — в [[versions/v2.28.1/variables/download|download.yaml]].

## Охват справочника и сверка

- Извлечено переменных **механизма загрузки**: **65** (см. `download.yaml`; в v2.28.1 к перечню добавлены `argocd_install_url` и `argocd_install_checksum`).
- Всего top-level ключей в источнике `roles/kubespray_defaults/defaults/main/download.yml`: **284** (сверка: `grep -cE '^[a-z_][a-z0-9_]*:' roles/kubespray_defaults/defaults/main/download.yml` → `284`; в v2.28.0 было 281 — добавлены `argocd_version`, `argocd_install_url`, `argocd_install_checksum`).
- Остальные ~219 ключей — это **пер-компонентные версии** (`etcd_version`, `containerd_version`, `cilium_version`, `flannel_version`, `weave_version` и т.д.), **пер-компонентные образы** (`*_image_repo` / `*_image_tag`, включая `weave_kube_image_*`, `weave_npc_image_*`), **контрольные суммы** (`*_binary_checksum` / `*_archive_checksum`) и **таблицы поддерживаемых версий**. Они относятся к переменным компонентов и намеренно вынесены в другие справочники среза v2.28.1 (справочники компонентов и `components.yaml`), а таблицы сумм — в `checksums.yml` тега.
