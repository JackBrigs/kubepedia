---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: code
source_path: versions/v2.31.0/variables/etcd.yaml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0
retrieved_at: 2026-07-14
topics: [etcd]
reliability: authoritative
---

# Переменные etcd — v2.31.0

Человекочитаемая заметка к машинному справочнику переменных etcd. Источник истины — YAML-файл `etcd.yaml`; здесь приведены обзор и ключевые таблицы. Все данные извлечены строго из кода тега `v2.31.0` (commit `1c9add4`).

Связанный срез: [[versions/v2.31.0/README|Срез v2.31.0]]

## Источники

- `roles/etcd_defaults/defaults/main.yml` — основной набор defaults роли etcd (36 ключей)
- `roles/etcd_defaults/vars/main.yml` — карта путей сертификатов (`cert_files`)
- `roles/etcdctl_etcdutl/tasks/main.yml` — установка `etcdctl`/`etcdutl` (собственных defaults не имеет, потребляет `etcd_image_repo`, `etcd_image_tag`, `etcd_version`)
- `roles/kubespray_defaults/defaults/main/main.yml` — endpoint'ы, адреса, тип развёртывания, часть путей
- `roles/kubespray_defaults/defaults/main/download.yml` — загрузка бинарника и образа etcd
- `roles/kubespray_defaults/vars/main/main.yml` — карта `etcd_supported_versions`

Всего задокументировано 65 переменных. Проверка полноты: `grep '^[a-zA-Z_]\+:' roles/etcd_defaults/defaults/main.yml` → 36 активных ключей, все извлечены. `etcd_cert_dir_mode` в v2.31.0 отсутствует (удалена в v2.30.0).

## Обзор типов развёртывания

Тип задаётся переменной `etcd_deployment_type` (`roles/kubespray_defaults/defaults/main/main.yml`), значение по умолчанию — `host`.

| Значение | Как работает | Скачивание |
| --- | --- | --- |
| `host` | Бинарник etcd ставится на узлы группы `etcd` и запускается как systemd-сервис (`etcd-host.service`) | `file: true` — скачивается tar.gz бинарника, проверяется `etcd_binary_checksum` |
| `docker` | etcd запускается контейнером (`etcd-docker.service`); действует `etcd_memory_limit` | `container: true` — тянется образ `etcd_image_repo:etcd_image_tag` |
| прочие контейнерные | `etcd_deployment_type != 'host'` трактуется как контейнерный режим (`container: true`) | образ по тегу |

Отдельный кластер для событий Kubernetes включается через `etcd_events_cluster_enabled` / `etcd_events_cluster_setup`; его данные лежат в `etcd_events_data_dir` (`/var/lib/etcd-events`), а endpoint'ы используют порты 2382 (peer) и 2383 (client).

## Ключевые переменные: развёртывание и пути

| Переменная | Значение по умолчанию | Назначение |
| --- | --- | --- |
| `etcd_deployment_type` | `host` | Режим развёртывания etcd |
| `etcd_cluster_setup` | `true` | Полная настройка кластера (false — только сертификаты) |
| `etcd_events_cluster_enabled` | `false` | Вынести события K8s в отдельный кластер |
| `etcd_data_dir` | `/var/lib/etcd` | Каталог данных etcd |
| `etcd_events_data_dir` | `/var/lib/etcd-events` | Каталог данных etcd-events |
| `etcd_config_dir` | `/etc/ssl/etcd` | Каталог конфигурации/сертификатов |
| `etcd_cert_dir` | `{{ etcd_config_dir }}/ssl` | Каталог TLS-сертификатов |
| `etcd_owner` | `etcd` | Владелец файлов и процессов |
| `etcd_hosts` | `{{ groups['etcd'] | default(groups['kube_control_plane']) }}` | Список узлов etcd |

## Ключевые переменные: сеть и endpoint'ы

| Переменная | Значение по умолчанию | Порт |
| --- | --- | --- |
| `etcd_client_url` | `https://{{ etcd_access_address | ... }}:2379` | 2379 (client) |
| `etcd_peer_url` | `https://{{ etcd_access_address | ... }}:2380` | 2380 (peer) |
| `etcd_events_client_url` | `https://{{ etcd_events_access_address | ... }}:2383` | 2383 (events client) |
| `etcd_events_peer_url` | `https://{{ etcd_events_access_address | ... }}:2382` | 2382 (events peer) |
| `etcd_metrics_addresses` | список по узлам | `etcd_metrics_port` (по умолчанию 2381) |

`etcd_access_addresses`, `etcd_peer_addresses`, `etcd_member_name` формируются шаблонами Jinja по группе `etcd`; точные выражения — в `etcd.yaml`.

## Ключевые переменные: TLS и сертификаты

| Переменная | Значение по умолчанию | Назначение |
| --- | --- | --- |
| `force_etcd_cert_refresh` | `true` | Принудительный перевыпуск сертификатов |
| `etcd_secure_client` | `true` | TLS-сертификаты для клиентов (etcdctl) |
| `etcd_peer_client_auth` | `true` | Проверка клиентских сертификатов при peer-соединениях |
| `etcd_cert_alt_names` | список SAN с `etcd.kube-system...` | Доп. DNS-имена в сертификате |
| `etcd_cert_alt_ips` | `[]` | Доп. IP в сертификате |
| `etcd_tls_cipher_suites` | не задана (закомментирована) | Набор TLS cipher suites |

`cert_files` (`roles/etcd_defaults/vars/main.yml`) — внутренняя карта путей master/node сертификатов; переопределять не следует.

## Ключевые переменные: тюнинг и производительность

| Переменная | Значение по умолчанию | Назначение |
| --- | --- | --- |
| `etcd_heartbeat_interval` | `"250"` | Heartbeat лидера, мс |
| `etcd_election_timeout` | `"5000"` | Таймаут выборов лидера, мс |
| `etcd_snapshot_count` | `"100000"` | Число записей до снимка |
| `etcd_compaction_retention` | `"8"` | Compaction MVCC, часов |
| `etcd_quota_backend_bytes` | `"2147483648"` | Квота backend, байт (2 ГБ) |
| `etcd_max_request_bytes` | `"1572864"` | Макс. размер запроса, байт |
| `etcd_max_snapshots` | `5` | Число хранимых snapshot |
| `etcd_max_wals` | `5` | Число хранимых WAL |
| `etcd_memory_limit` | `512M` (<4 ГБ ОЗУ) / `0` иначе | Лимит памяти (только `docker`) |
| `etcd_experimental_initial_corrupt_check` | `true` | Проверка целостности при старте (обход бага 3.5.x) |

## Ключевые переменные: резервное копирование

| Переменная | Значение по умолчанию | Назначение |
| --- | --- | --- |
| `etcd_backup_prefix` | `/var/backups` | Каталог резервных копий |
| `etcd_backup_retention_count` | `-1` | Число хранимых копий (< 0 — все) |

## Ключевые переменные: загрузка бинарника и образа

| Переменная | Значение по умолчанию | Назначение |
| --- | --- | --- |
| `etcd_version` | `{{ etcd_supported_versions[kube_major_version] }}` | Версия etcd (для v2.31.0 по умолчанию — 3.6.10 при K8s 1.35) |
| `etcd_supported_versions` | карта 1.33/1.34/1.35 → версия etcd | Соответствие мажора K8s и версии etcd |
| `etcd_image_repo` | `{{ quay_image_repo }}/coreos/etcd` | Репозиторий образа |
| `etcd_image_tag` | `v{{ etcd_version }}` | Тег образа |
| `etcd_download_url` | ссылка на релиз etcd-io/etcd | URL архива бинарников |
| `etcd_binary_checksum` | `{{ etcd_binary_checksums[image_arch][etcd_version] }}` | SHA256 архива |

## Замечания

- `etcd_version` для v2.31.0 выбирается из `etcd_supported_versions` (`roles/kubespray_defaults/vars/main/main.yml`) по мажорной версии Kubernetes. Поддерживаются K8s `1.33`, `1.34`, `1.35`. Для `1.33` и `1.34` берётся старшая версия ветки `< 3.6` (`3.5.29`), для `1.35` — старшая версия `< 3.7` (`3.6.10`). По умолчанию `kube_version = 1.35.4`, поэтому etcd по умолчанию — `3.6.x` (переход на ветку etcd 3.6 относительно v2.30.0, где по умолчанию был 3.5.x).
- Ряд переменных (`etcd_data_dir`, `etcd_config_dir`, `etcd_cert_dir`, `etcd_heartbeat_interval`, `etcd_election_timeout`, `etcd_events_cluster_enabled`) определён одновременно в `roles/etcd_defaults/defaults/main.yml` и `roles/kubespray_defaults/defaults/main/main.yml` с идентичными значениями.
- Закомментированные в defaults переменные (`etcd_tls_cipher_suites`, `etcd_metrics_port`, `etcd_cpu_limit`) отмечены в YAML как `reliability: unconfirmed`, поскольку по умолчанию не активны и задаются пользователем.
- Роль `etcdctl_etcdutl` собственных defaults не имеет: при `container_manager: docker` она копирует `etcdctl`/`etcdutl` из образа `etcd_image_repo:etcd_image_tag`, иначе — из скачанного архива версии `etcd_version`.
- Состав и значения ключей `roles/etcd_defaults/defaults/main.yml`, `vars/main.yml`, а также etcd-переменных в `main.yml`/`download.yml` побайтово совпадают с v2.30.0; единственное содержательное изменение — сдвиг карты `etcd_supported_versions` и связанный переход на etcd 3.6 по умолчанию.
