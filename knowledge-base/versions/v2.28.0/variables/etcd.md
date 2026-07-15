---
project: kubespray
kubespray_version: v2.28.0
git_commit: 63cdf87
source_type: code
source_path: versions/v2.28.0/variables/etcd.yaml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.28.0
retrieved_at: 2026-07-15
topics:
  - etcd
reliability: authoritative
---

# Переменные etcd — Kubespray v2.28.0

Человекочитаемая заметка к машиночитаемому справочнику `etcd.yaml` (65 переменных).
**Источник истины — YAML-справочник** `versions/v2.28.0/variables/etcd.yaml`; эта заметка — его изложение.
Назад к срезу: [[versions/v2.28.0/README|Срез v2.28.0]].

Источники в коде тега `v2.28.0` (commit `63cdf87`):

- `roles/etcd/defaults/main.yml` — в v2.28.0 значения по умолчанию роли `etcd` лежат **прямо в её каталоге `defaults/`** (отдельной роли `roles/etcd_defaults`, как в v2.29.1, здесь ещё **нет**). Файл содержит 33 активных top-level ключа и 7 закомментированных;
- `roles/etcd/vars/main.yml` — внутренняя переменная `cert_files`;
- `roles/kubespray_defaults/defaults/main/main.yml` — топология (`etcd_deployment_type`), адреса/URL-ы кластера, `etcd_snapshot_count`, `etcd_events_data_dir`;
- `roles/kubespray_defaults/defaults/main/download.yml` — версия, URL загрузки, образ (подробно — в справочнике downloads).

## Типы развёртывания etcd в v2.28.0

Топология выбирается **единственной** переменной `etcd_deployment_type`
(`roles/kubespray_defaults/defaults/main/main.yml`, значение по умолчанию `host`).

| Значение | Что делает | Примечания |
|---|---|---|
| `host` (по умолчанию) | Бинарник etcd на хосте + systemd-юнит | Рекомендуемый вариант |
| `docker` | etcd в docker-контейнере, управляемом systemd | Разрешён только при `container_manager: docker`; действуют лимиты `etcd_memory_limit`/`etcd_cpu_limit`/`etcd_blkio_weight` |
| `kubeadm` | etcd как static pod, управляемый kubeadm | Группа `etcd` в инвентаре может быть пустой (`etcd_hosts` откатывается на `kube_control_plane`) |

Допустимые значения проверяются в `roles/validate_inventory/tasks/main.yml:216-217`.

> Важно: переменная `etcd_kubeadm_enabled` в коде v2.28.0 **удалена** — её
> использование вызывает явную остановку с сообщением
> (`roles/validate_inventory/tasks/main.yml:229-235`). Нужно использовать
> `etcd_deployment_type: kubeadm`.

Отдельный кластер для событий Kubernetes включается парой `etcd_events_cluster_enabled` /
`etcd_events_cluster_setup` (обе по умолчанию `false`); он живёт на портах 2382 (peer) и
2383 (client) с данными в `etcd_events_data_dir`.

## Версия и загрузка

| Переменная | Значение по умолчанию | Комментарий |
|---|---|---|
| `etcd_version` | `{{ etcd_supported_versions[kube_major_version] }}` | Словарь `etcd_supported_versions` (`download.yml:137-141`) задаёт `3.5.16` для `1.30`/`1.31`/`1.32`. При K8s по умолчанию 1.32.5 фактически **3.5.16** |
| `etcd_download_url` | архив с GitHub `etcd-io/etcd` | деплой `host` + бинарники `etcdctl`/`etcdutl` |
| `etcd_image_repo` / `etcd_image_tag` | `{{ quay_image_repo }}/coreos/etcd` / `v{{ etcd_version }}` | деплои `docker`/`kubeadm` |

Подробности по загрузкам и контрольным суммам — в справочнике downloads (переменные помечены отсылкой в YAML).

## Каталоги и данные

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `etcd_data_dir` | `/var/lib/etcd` | данные etcd (определена и в `etcd/defaults`, и в `kubespray_defaults`) |
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

`cert_files` — внутренняя переменная из `roles/etcd/vars/main.yml` (vars имеют высокий
приоритет и через инвентарь не переопределяются): наборы путей сертификатов `master`/`node`.

## Тюнинг

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `etcd_snapshot_count` | `100000` | транзакций до снапшота |
| `etcd_heartbeat_interval` | `250` (мс) | heartbeat лидера |
| `etcd_election_timeout` | `5000` (мс) | таймаут выборов |
| `etcd_compaction_retention` | `8` (часов) | auto-compaction mvcc |
| `etcd_metrics` | `basic` | детализация метрик (`extensive` — с гистограммами) |
| `etcd_extra_vars` | `{}` | произвольные переменные окружения в `etcd.env` |
| `etcd_retries` | `4` | число повторов циклических операций роли |
| `etcd_experimental_initial_corrupt_check` | `true` | обход известной проблемы etcd 3.5.x |
| `unsafe_show_logs` | `false` | вывод отладочной информации (может содержать приватные данные) |

Закомментированные в `roles/etcd/defaults/main.yml` (по умолчанию не заданы, применяются
только при явном определении пользователем):

| Переменная | Пример из кода | Назначение |
|---|---|---|
| `etcd_quota_backend_bytes` | `"2147483648"` | квота бэкенда; по умолчанию 2G на стороне etcd, рекомендуемый максимум 8G |
| `etcd_max_request_bytes` | `"1572864"` | максимальный размер запроса |
| `etcd_max_snapshots` | `5` | ретенция snapshot-файлов (0 — без ограничения) |
| `etcd_max_wals` | `5` | ретенция WAL-файлов (0 — без ограничения) |
| `etcd_metrics_port` | `2381` | отдельный HTTP-порт метрик; включает `ETCD_LISTEN_METRICS_URLS` |
| `etcd_cpu_limit` | `300m` | cpu-shares контейнера (деплой docker) |
| `etcd_tls_cipher_suites` | `{}` со списком `TLS_*` | список разрешённых cipher suites |

Лимиты, актуальные только для `etcd_deployment_type: docker`:

| Переменная | По умолчанию | Назначение |
|---|---|---|
| `etcd_memory_limit` | `512M` при RAM < 4 ГБ, иначе `0` (без лимита) | лимит памяти контейнера |
| `etcd_cpu_limit` | не задана (пример `300m`) | cpu-shares контейнера |
| `etcd_blkio_weight` | `1000` | приоритет дискового I/O |

Distributed tracing (экспериментально): `etcd_experimental_enable_distributed_tracing: false`
+ `etcd_experimental_distributed_tracing_address: localhost:4317`,
`..._sample_rate: 100`, `..._service_name: etcd`;
`etcd_experimental_watch_progress_notify_interval: 5s`.

> В v2.28.0 переменной `etcd_log_level` в defaults роли etcd **нет** (в v2.29.1 она появляется).

## Адреса и URL-ы кластера

Порты **зашиты в Jinja-шаблоны значений**, отдельных переменных портов нет
(кроме опционального `etcd_metrics_port`): 2379 client, 2380 peer, 2381 метрики (по умолчанию),
2382/2383 — peer/client кластера событий.

Ключевые переменные (`roles/kubespray_defaults/defaults/main/main.yml:660-698`):
`etcd_hosts`, `etcd_address`, `etcd_access_address`, `etcd_peer_url`, `etcd_client_url`,
`etcd_access_addresses`, `etcd_metrics_addresses`, `etcd_member_name`, `etcd_peer_addresses`
и их `*_events_*`-аналоги. Имя члена кластера рекомендуется задавать в инвентаре
(`etcd_member_name` на хост), иначе генерируется `etcd1`, `etcd2`, ...

## Важные зависимости

- `etcd_deployment_type: docker` требует `container_manager: docker` (assert в `roles/validate_inventory/tasks/main.yml:217`); от него же зависит `deploy_container_engine` (`roles/kubespray_defaults/defaults/main/main.yml:312`).
- Группа `etcd` в инвентаре обязательна, кроме случая `etcd_deployment_type: kubeadm` (`roles/validate_inventory/tasks/main.yml:66`).
- `etcd_memory_limit` должен быть согласован с `etcd_quota_backend_bytes` — иначе возможны OOM-остановки etcd.
- `etcd_events_cluster_setup` управляет установкой кластера событий внутри роли, `etcd_events_cluster_enabled` — включает его использование компонентами; для рабочего кластера событий обе должны быть `true`.
- Шесть переменных продублированы с одинаковыми значениями в `roles/etcd/defaults/main.yml` и `roles/kubespray_defaults/defaults/main/main.yml`: `etcd_data_dir`, `etcd_events_cluster_enabled`, `etcd_heartbeat_interval`, `etcd_election_timeout`, `etcd_config_dir`, `etcd_cert_dir` (в YAML — поле `also_defined_in`). Переопределять их следует через инвентарь, чтобы значение попало в оба контекста. Дополнительно `unsafe_show_logs` продублирована в `roles/kubespray_defaults/defaults/main/download.yml`.

## Сверка полноты извлечения

- `roles/etcd/defaults/main.yml`: активных top-level ключей — **33** (проверка `grep -cE '^[a-z_][a-z0-9_]*:'`), плюс **7** закомментированных ключей (`etcd_quota_backend_bytes`, `etcd_max_request_bytes`, `etcd_cpu_limit`, `etcd_max_snapshots`, `etcd_max_wals`, `etcd_metrics_port`, `etcd_tls_cipher_suites`) — все 33 + 7 = 40 учтены в справочнике.
- `roles/etcd/vars/main.yml`: 1 переменная (`cert_files`) — учтена.
- `roles/kubespray_defaults/defaults/main/main.yml`: 19 etcd-переменных (без дублей с `etcd/defaults`) — учтены.
- `roles/kubespray_defaults/defaults/main/download.yml`: 5 переменных (`etcd_version`, `etcd_download_url`, `etcd_binary_checksum`, `etcd_image_repo`, `etcd_image_tag`) — учтены.
- **Итого в `etcd.yaml`: 65 переменных** (40 + 1 + 19 + 5).
