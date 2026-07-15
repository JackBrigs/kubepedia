---
project: kubespray
kubespray_version: v2.29.0
git_commit: 9991412
source_type: code
source_path: versions/v2.29.0/variables/etcd.yaml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.29.0
retrieved_at: 2026-07-14
topics:
  - etcd
reliability: authoritative
---

# Переменные etcd — Kubespray v2.29.0

Человекочитаемая заметка к машиночитаемому справочнику `etcd.yaml` (66 переменных).
**Источник истины — YAML-справочник** `versions/v2.29.0/variables/etcd.yaml`; эта заметка — его изложение.
Назад к срезу: [[versions/v2.29.0/README|Срез v2.29.0]].

Источники в коде тега `v2.29.0` (commit `9991412`):

- `roles/etcd_defaults/defaults/main.yml` и `roles/etcd_defaults/vars/main.yml` — у самой роли `roles/etcd` каталога `defaults/` **нет**, все её значения по умолчанию вынесены в отдельную роль `etcd_defaults`;
- `roles/kubespray_defaults/defaults/main/main.yml` — топология, адреса/URL-ы кластера, часть тюнинга;
- `roles/kubespray_defaults/defaults/main/download.yml` — версия, URL загрузки, образ (подробно — в справочнике downloads);
- роль `roles/etcdctl_etcdutl` собственных defaults **не имеет**: она использует `etcd_image_repo`, `etcd_image_tag`, `etcd_version`, `bin_dir`, `container_manager`.

## Типы развёртывания etcd в v2.29.0

Топология выбирается **единственной** переменной `etcd_deployment_type`
(`roles/kubespray_defaults/defaults/main/main.yml`, значение по умолчанию `host`;
то же значение продублировано в `inventory/sample/group_vars/all/etcd.yml`).

| Значение | Что делает | Примечания |
|---|---|---|
| `host` (по умолчанию) | Бинарник etcd на хосте + systemd-юнит (`roles/etcd/tasks/install_host.yml`) | Рекомендуемый вариант |
| `docker` | etcd в docker-контейнере, управляемом systemd (`roles/etcd/tasks/install_docker.yml`) | Разрешён только при `container_manager: docker`; действуют лимиты `etcd_memory_limit`/`etcd_cpu_limit`/`etcd_blkio_weight` |
| `kubeadm` | etcd как static pod, управляемый kubeadm | Экспериментально; группа `etcd` в инвентаре может быть пустой (`etcd_hosts` откатывается на `kube_control_plane`) |

Допустимые значения проверяются в `roles/validate_inventory/tasks/main.yml:175-176`.

> Важно: переменная `etcd_kubeadm_enabled` в коде v2.29.0 **не существует** — она
> объявлена устаревшей ещё в v2.19 (упоминание осталось только в
> `docs/operations/upgrades.md:338`). Использовать нужно `etcd_deployment_type: kubeadm`.

Отдельный кластер для событий Kubernetes включается парой `etcd_events_cluster_enabled` /
`etcd_events_cluster_setup` (обе по умолчанию `false`); он живёт на портах 2382 (peer) и
2383 (client) с данными в `etcd_events_data_dir`.

## Версия и загрузка

| Переменная | Значение по умолчанию | Комментарий |
|---|---|---|
| `etcd_version` | `{{ etcd_supported_versions[kube_major_version] }}` | Для K8s 1.31–1.33 выбирается новейшая 3.5.x из checksums — фактически **3.5.23** (`roles/kubespray_defaults/vars/main/main.yml:14`, `vars/main/checksums.yml`) |
| `etcd_download_url` | архив с GitHub `etcd-io/etcd` | деплой `host` + бинарники `etcdctl`/`etcdutl` |
| `etcd_image_repo` / `etcd_image_tag` | `{{ quay_image_repo }}/coreos/etcd` / `v{{ etcd_version }}` | деплои `docker`/`kubeadm` |

Подробности по загрузкам и контрольным суммам — в справочнике downloads (переменные помечены отсылкой в YAML).

## Каталоги и данные

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `etcd_data_dir` | `/var/lib/etcd` | данные etcd (определена и в `etcd_defaults`, и в `kubespray_defaults`) |
| `etcd_events_data_dir` | `/var/lib/etcd-events` | данные кластера событий |
| `etcd_backup_prefix` | `/var/backups` | бэкапы перед изменениями (handler `backup.yml`) |
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

Размер ключей и срок действия задаются общими переменными `certificates_key_size` (2048) и
`certificates_duration` (36500) из `roles/kubespray_defaults/defaults/main/main.yml:713-714` —
они используются скриптом `roles/etcd/templates/make-ssl-etcd.sh.j2` (см. справочник k8s-cluster).

## Тюнинг

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `etcd_quota_backend_bytes` | `2147483648` (2 ГиБ) | квота бэкенда; рекомендуемый максимум 8G |
| `etcd_snapshot_count` | `100000` | транзакций до снапшота |
| `etcd_heartbeat_interval` | `250` (мс) | heartbeat лидера |
| `etcd_election_timeout` | `5000` (мс) | таймаут выборов |
| `etcd_compaction_retention` | `8` (часов) | auto-compaction mvcc |
| `etcd_max_request_bytes` | `1572864` | максимальный размер запроса |
| `etcd_max_snapshots` / `etcd_max_wals` | `5` / `5` | ретенция snapshot/WAL-файлов |
| `etcd_metrics` | `basic` | детализация метрик (`extensive` — с гистограммами) |
| `etcd_metrics_port` | не задана (пример `2381`) | отдельный HTTP-порт метрик; включает `ETCD_LISTEN_METRICS_URLS` |
| `etcd_log_level` | `info` | уровень логов |
| `etcd_extra_vars` | `{}` | произвольные переменные окружения в `etcd.env` |

Лимиты только для `etcd_deployment_type: docker`:

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `etcd_memory_limit` | `512M` при RAM < 4 ГБ, иначе `0` (без лимита) | лимит памяти контейнера |
| `etcd_cpu_limit` | не задана (пример `300m`) | cpu-shares контейнера |
| `etcd_blkio_weight` | `1000` | приоритет дискового I/O |

Экспериментальные флаги: `etcd_experimental_initial_corrupt_check: true` (обход известной
проблемы etcd 3.5.x), distributed tracing (`etcd_experimental_enable_distributed_tracing: false`
+ адрес/частота/имя сервиса), `etcd_experimental_watch_progress_notify_interval: 5s`.

## Адреса и URL-ы кластера

Порты **зашиты в Jinja-шаблоны значений**, отдельных переменных портов нет
(кроме опционального `etcd_metrics_port`): 2379 client, 2380 peer, 2381 метрики (по умолчанию),
2382/2383 — peer/client кластера событий.

Ключевые переменные (`roles/kubespray_defaults/defaults/main/main.yml:665-718`):
`etcd_hosts`, `etcd_address`, `etcd_access_address`, `etcd_peer_url`, `etcd_client_url`,
`etcd_access_addresses`, `etcd_metrics_addresses`, `etcd_member_name`, `etcd_peer_addresses`
и их `*_events_*`-аналоги. Имя члена кластера рекомендуется задавать в инвентаре
(`etcd_member_name` на хост), иначе генерируется `etcd1`, `etcd2`, ...

## Важные зависимости

- `etcd_deployment_type: docker` требует `container_manager: docker` (assert в `roles/validate_inventory/tasks/main.yml:176`); от него же зависит `deploy_container_engine`.
- Группа `etcd` в инвентаре обязательна, кроме случая `etcd_deployment_type: kubeadm` (`roles/validate_inventory/tasks/main.yml:25`).
- `etcd_memory_limit` не должен быть меньше `etcd_quota_backend_bytes` — иначе возможны OOM-остановки etcd (комментарий в `roles/etcd_defaults/defaults/main.yml:55-58`).
- `etcd_events_cluster_setup` управляет установкой кластера событий внутри роли, `etcd_events_cluster_enabled` — включает его использование компонентами; для рабочего кластера событий обе должны быть `true`.
- Шесть переменных продублированы с одинаковыми значениями в `roles/etcd_defaults` и `roles/kubespray_defaults`: `etcd_data_dir`, `etcd_events_cluster_enabled`, `etcd_heartbeat_interval`, `etcd_election_timeout`, `etcd_config_dir`, `etcd_cert_dir` (в YAML — поле `also_defined_in`). Переопределять их следует через инвентарь, чтобы значение попало в оба контекста.
- `cert_files` — внутренняя переменная из `roles/etcd_defaults/vars/main.yml` (vars имеют высокий приоритет и через инвентарь не переопределяются).
