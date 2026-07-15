---
project: kubespray
kubespray_version: v2.27.0
git_commit: 9ec9b3a
source_type: code
source_path: versions/v2.27.0/variables/etcd.yaml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.27.0
retrieved_at: 2026-07-15
topics:
  - etcd
reliability: authoritative
---

# Переменные etcd — Kubespray v2.27.0

Человекочитаемая заметка к машиночитаемому справочнику `etcd.yaml`.
**Источник истины — YAML-справочник** `versions/v2.27.0/variables/etcd.yaml`; эта заметка — его изложение.
Назад к срезу: [[versions/v2.27.0/README|Срез v2.27.0]].

Источники в коде тега `v2.27.0` (commit `9ec9b3a`):

- `roles/etcd/defaults/main.yml` — **все значения по умолчанию роли etcd лежат прямо здесь**. В отличие от v2.29.1, отдельной роли `roles/etcd_defaults` в этой версии **нет**;
- `roles/kubespray-defaults/defaults/main/main.yml` (обратите внимание — каталог с **дефисом** `kubespray-defaults`) — топология, адреса/URL-ы кластера, часть тюнинга;
- `roles/kubespray-defaults/defaults/main/download.yml` — версия, URL загрузки, образ (подробно — в справочнике download).

## Типы развёртывания etcd в v2.27.0

Топология выбирается **единственной** переменной `etcd_deployment_type`
(`roles/kubespray-defaults/defaults/main/main.yml`, значение по умолчанию `host`).

| Значение | Что делает | Примечания |
|---|---|---|
| `host` (по умолчанию) | Бинарник etcd на хосте + systemd-юнит | Рекомендуемый вариант |
| `docker` | etcd в docker-контейнере, управляемом systemd | Действуют лимиты `etcd_memory_limit`/`etcd_cpu_limit`/`etcd_blkio_weight` |
| `kubeadm` | etcd как static pod, управляемый kubeadm | Группа `etcd` в инвентаре может быть пустой (`etcd_hosts` откатывается на `kube_control_plane`) |

Отдельный кластер для событий Kubernetes включается парой `etcd_events_cluster_enabled` /
`etcd_events_cluster_setup` (обе по умолчанию `false`); он живёт на портах 2382 (peer) и
2383 (client) с данными в `etcd_events_data_dir`.

## Версия и загрузка

| Переменная | Значение по умолчанию | Комментарий |
|---|---|---|
| `etcd_version` | `{{ etcd_supported_versions[kube_major_version] }}` → **v3.5.16** | Для всех поддерживаемых версий K8s (1.29/1.30/1.31) — одна и та же v3.5.16. Значение **уже содержит префикс v** |
| `etcd_download_url` | архив с GitHub `etcd-io/etcd` | URL использует `{{ etcd_version }}` без добавления префикса (в v2.29.1 было `v{{ etcd_version }}`) |
| `etcd_image_repo` / `etcd_image_tag` | `{{ quay_image_repo }}/coreos/etcd` / `{{ etcd_version }}` | деплои `docker`/`kubeadm` |

## Каталоги и данные

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `etcd_data_dir` | `/var/lib/etcd` | данные etcd (определена и в `roles/etcd/defaults`, и в `roles/kubespray-defaults`) |
| `etcd_events_data_dir` | `/var/lib/etcd-events` | данные кластера событий |
| `etcd_backup_prefix` | `/var/backups` | бэкапы перед изменениями |
| `etcd_backup_retention_count` | `-1` | сколько бэкапов хранить; `< 0` — все |
| `etcd_script_dir` | `{{ bin_dir }}/etcd-scripts` | служебные скрипты (генерация сертификатов) |

## TLS и сертификаты

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `etcd_config_dir` | `/etc/ssl/etcd` | базовый каталог |
| `etcd_cert_dir` | `{{ etcd_config_dir }}/ssl` | каталог сертификатов |
| `etcd_cert_dir_mode` | `0700` | права на каталог |
| `etcd_owner` / `etcd_cert_group` | `etcd` / `root` | владелец процесса и группа файлов сертификатов |
| `etcd_secure_client` | `true` | требовать TLS-сертификаты от клиентов |
| `etcd_peer_client_auth` | `true` | клиентская аутентификация между peer-узлами |
| `force_etcd_cert_refresh` | `true` | принудительный перевыпуск сертификатов |
| `etcd_cert_alt_names` | `etcd.kube-system.svc.{{ dns_domain }}` и др. | дополнительные SAN (DNS-записи не создаются) |
| `etcd_cert_alt_ips` | `[]` | дополнительные IP SAN |
| `etcd_node_cert_hosts` | `{{ groups['k8s_cluster'] }}` | кому выпускаются node-сертификаты |
| `etcd_tls_cipher_suites` | не задана (закомментирована) | список cipher suites |

Управление сертификатами в legacy-режиме etcd — переменная `cert_management: script`; размер
ключей и срок действия задаются `certificates_key_size` (2048) и `certificates_duration` (36500)
из `roles/kubespray-defaults/defaults/main/main.yml` (см. справочник k8s-cluster).

## Тюнинг

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `etcd_snapshot_count` | `10000` | транзакций до снапшота (в `main.yml`; в v2.29.1 значение выросло до 100000) |
| `etcd_heartbeat_interval` | `250` (мс) | heartbeat лидера |
| `etcd_election_timeout` | `5000` (мс) | таймаут выборов |
| `etcd_compaction_retention` | `8` (часов) | auto-compaction mvcc |
| `etcd_metrics` | `basic` | детализация метрик (`extensive` — с гистограммами) |
| `etcd_metrics_port` | не задана (пример `2381`) | отдельный HTTP-порт метрик |
| `etcd_retries` | `4` | повторов циклических операций роли |
| `etcd_extra_vars` | `{}` | произвольные переменные окружения в `etcd.env` |
| `etcd_quota_backend_bytes` | не задана (закомментирована) | квота бэкенда; по умолчанию действует значение etcd (2 ГиБ) |
| `etcd_max_request_bytes` | не задана (закомментирована) | максимальный размер запроса |
| `etcd_max_snapshots` / `etcd_max_wals` | не заданы (закомментированы) | ретенция snapshot/WAL-файлов |

Лимиты только для `etcd_deployment_type: docker`:

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `etcd_memory_limit` | `512M` при RAM < 4 ГБ, иначе `0` (без лимита) | лимит памяти контейнера |
| `etcd_cpu_limit` | не задана (пример `300m`) | cpu-shares контейнера |
| `etcd_blkio_weight` | `1000` | приоритет дискового I/O |

Экспериментальные флаги: `etcd_experimental_initial_corrupt_check: true` (обход известной
проблемы etcd 3.5.x), distributed tracing (`etcd_experimental_enable_distributed_tracing: false`
+ адрес/частота/имя сервиса), `etcd_experimental_watch_progress_notify_interval: 5s`.
Общий флаг отладки `unsafe_show_logs: false` объявлен и здесь, и в механизме загрузок.

## Адреса и URL-ы кластера

Порты **зашиты в Jinja-шаблоны значений**, отдельных переменных портов нет
(кроме опционального `etcd_metrics_port`): 2379 client, 2380 peer, 2381 метрики (по умолчанию),
2382/2383 — peer/client кластера событий.

В v2.27.0 адреса строятся на переменных узла `ip` / `access_ip` / `fallback_ip`
(в v2.29.1 это были `main_ip` / `main_access_ip`). Ключевые переменные
(`roles/kubespray-defaults/defaults/main/main.yml`): `etcd_hosts`, `etcd_address`,
`etcd_access_address`, `etcd_peer_url`, `etcd_client_url`, `etcd_access_addresses`,
`etcd_metrics_addresses`, `etcd_member_name`, `etcd_peer_addresses` и их `*_events_*`-аналоги.
Имя члена кластера рекомендуется задавать в инвентаре (`etcd_member_name` на хост),
иначе генерируется `etcd1`, `etcd2`, ...

## Важные зависимости

- Группа `etcd` в инвентаре обязательна, кроме случая `etcd_deployment_type: kubeadm`.
- `etcd_memory_limit` не должен быть меньше квоты бэкенда — иначе возможны OOM-остановки etcd.
- `etcd_events_cluster_setup` управляет установкой кластера событий внутри роли, `etcd_events_cluster_enabled` — включает его использование компонентами; для рабочего кластера событий обе должны быть `true`.
- Шесть переменных продублированы с одинаковыми значениями в `roles/etcd/defaults/main.yml` и `roles/kubespray-defaults/defaults/main/main.yml`: `etcd_data_dir`, `etcd_events_cluster_enabled`, `etcd_heartbeat_interval`, `etcd_election_timeout`, `etcd_config_dir`, `etcd_cert_dir` (в YAML — поле `also_defined_in`).

## Сверка полноты

`roles/etcd/defaults/main.yml` — 33 top-level ключа; извлечены все 33 (включая общую `unsafe_show_logs`), плюс 7 закомментированных переменных задокументированы как «не задана» (`etcd_tls_cipher_suites`, `etcd_quota_backend_bytes`, `etcd_max_request_bytes`, `etcd_cpu_limit`, `etcd_metrics_port`, `etcd_max_snapshots`, `etcd_max_wals`). Дополнительно извлечены переменные из `roles/kubespray-defaults/defaults/main/main.yml` (топология, адреса, `etcd_snapshot_count`, `cert_management`, дубли) и 6 из `roles/kubespray-defaults/defaults/main/download.yml` (версия, карта версий, URL, checksum, образ/тег). Итого в `etcd.yaml` — **66 записей**; сверка `grep -cE '^[a-z_]...:'` по `roles/etcd/defaults/main.yml` = 33, все покрыты.
