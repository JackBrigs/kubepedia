---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: docs
source_paths:
  - docs/operations/hardening.md
  - docs/operations/encrypting-secret-data-at-rest.md
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0
retrieved_at: 2026-07-14
topics:
  - security
  - hardening
reliability: authoritative
---

# Безопасность и харденинг кластера в v2.31.0

Дайджест по усилению безопасности кластера и шифрованию секретов «at rest». Источники — документация тега `v2.31.0` (commit `1c9add4`). Значения переменных приводятся строго из docs; фактические значения по умолчанию проверяются по коду роли (см. [[versions/v2.31.0/variables/k8s-cluster|Переменные ядра]]).

## Харденинг кластера (CIS Benchmarks)

Минимальное требование: Kubernetes не ниже `v1.23.6` — для доступности актуальных функций безопасности (в т.ч. admission-плагина `PodSecurity`). Конфигурация применяется отдельным файлом (например, `hardening.yaml`), передаваемым через `-e "@hardening.yaml"`.

### kube-apiserver

| Переменная | Значение из docs | Назначение |
|---|---|---|
| `authorization_modes` | `['Node', 'RBAC']` | Режимы авторизации; при включённом RBAC `anonymous-auth=true` считается безопасным |
| `kube_apiserver_request_timeout` | `120s` | Таймаут запросов к API |
| `kube_apiserver_service_account_lookup` | `true` | Проверка существования токена ServiceAccount |
| `kubernetes_audit` | `true` | Включение аудита Kubernetes |
| `audit_log_path` | `/var/log/kube-apiserver-log.json` | Путь к журналу аудита |
| `audit_log_maxage` | `30` | Хранение записей аудита, дней |
| `audit_log_maxbackups` | `10` | Число ротационных копий журнала |
| `audit_log_maxsize` | `100` | Максимальный размер файла журнала, МБ |
| `tls_min_version` | `VersionTLS12` | Минимальная версия TLS |
| `tls_cipher_suites` | `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305` | Разрешённые наборы шифров |
| `kube_profiling` | `false` | Отключение профилирования |
| `remove_anonymous_access` | `true` | Удаление анонимного доступа к кластеру |
| `kube_apiserver_admission_control_config_file` | `true` | Генерация конфиг-файла admission control |

Шифрование «at rest» (подробнее — раздел ниже):

| Переменная | Значение из docs | Назначение |
|---|---|---|
| `kube_encrypt_secret_data` | `true` | Включение шифрования данных перед записью в etcd |
| `kube_encryption_resources` | `[secrets]` | Какие ресурсы шифруются |
| `kube_encryption_algorithm` | `secretbox` | Алгоритм/провайдер шифрования |

Admission-плагины (`kube_apiserver_enable_admission_plugins`): `EventRateLimit`, `AlwaysPullImages`, `ServiceAccount`, `NamespaceLifecycle`, `NodeRestriction`, `LimitRanger`, `ResourceQuota`, `MutatingAdmissionWebhook`, `ValidatingAdmissionWebhook`, `PodNodeSelector`, `PodSecurity`.

Конфигурация `EventRateLimit` (`kube_apiserver_admission_event_rate_limits`): для файлов настроек admission создаются и монтируются в контейнер `kube-apiserver` автоматически.

| Лимит | type | qps | burst | cache_size |
|---|---|---|---|---|
| `limit_1` | Namespace | 50 | 100 | 2000 |
| `limit_2` | User | 50 | 100 | — |

Опциональные (закомментированы в docs) параметры `PodNodeSelector`: `kube_apiserver_admission_plugins_needs_configuration: [PodNodeSelector]` и `kube_apiserver_admission_plugins_podnodeselector_default_node_selector` (например `network=srv1`).

### kube-controller-manager

| Переменная | Значение | Назначение |
|---|---|---|
| `kube_controller_manager_bind_address` | `127.0.0.1` | Привязка только к loopback |
| `kube_controller_terminated_pod_gc_threshold` | `50` | Порог сборки мусора завершённых Pod |
| `kube_controller_feature_gates` | `["RotateKubeletServerCertificate=true"]` | Feature gates |

### kube-scheduler

| Переменная | Значение | Назначение |
|---|---|---|
| `kube_scheduler_bind_address` | `127.0.0.1` | Привязка только к loopback |

### etcd

| Переменная | Значение | Назначение |
|---|---|---|
| `etcd_deployment_type` | `host` | Запуск etcd на выделенных хостах вне кластера |

Согласно docs, размещение etcd на выделенных хостах вне кластера Kubernetes — наиболее безопасный вариант: изолирует etcd от сети CNI, убирает атаки на уровне Pod и предотвращает компрометацию etcd через ошибки RBAC, создавая дополнительную границу безопасности для критичного хранилища состояния кластера.

### kubelet

| Переменная | Значение | Назначение |
|---|---|---|
| `kubelet_authorization_mode_webhook` | `true` | Авторизация kubelet через webhook |
| `kubelet_authentication_token_webhook` | `true` | Аутентификация токенов через webhook |
| `kube_read_only_port` | `0` | Отключение read-only порта kubelet |
| `kubelet_rotate_server_certificates` | `true` | Ротация серверных сертификатов |
| `kubelet_protect_kernel_defaults` | `true` | Защита параметров ядра по умолчанию |
| `kubelet_event_record_qps` | `1` | Ограничение частоты событий |
| `kubelet_rotate_certificates` | `true` | Ротация клиентских сертификатов |
| `kubelet_streaming_connection_idle_timeout` | `5m` | Таймаут простоя streaming-соединений |
| `kubelet_make_iptables_util_chains` | `true` | Создание вспомогательных цепочек iptables |
| `kubelet_feature_gates` | `["RotateKubeletServerCertificate=true"]` | Feature gates |
| `kubelet_seccomp_default` | `true` | Профиль seccomp по умолчанию |
| `kubelet_systemd_hardening` | `true` | Усиление через systemd (минимальный firewall) |
| `kubelet_secure_addresses` | напр. `localhost link-local {{ kube_pods_subnet }} <IP CP>` | С каких адресов kubelet принимает пакеты |

При `kubelet_rotate_server_certificates: true` (совместно с `serverTLSBootstrap`) сертификаты генерируются автоматически; CSR по умолчанию одобряются через [kubelet-csr-approver](https://github.com/postfinance/kubelet-csr-approver). Настройка одобрения — через Helm-значения `kubelet_csr_approver_values`.

`kubelet_systemd_hardening` вместе с `kubelet_secure_addresses` настраивают минимальный firewall на узле.

### Дополнительные параметры и Pod Security

| Переменная | Значение | Назначение |
|---|---|---|
| `kube_owner` | `root` | Владелец файлов Kubernetes |
| `kube_cert_group` | `root` | Группа сертификатов |
| `kube_pod_security_use_default` | `true` | Создание Pod Security Configuration по умолчанию |
| `kube_pod_security_default_enforce` | `restricted` | Уровень enforce (namespace `kube-system` исключён по умолчанию) |

### Пример запуска

```bash
ansible-playbook -v cluster.yml \
    -i inventory.ini \
    -b --become-user=root \
    --private-key ~/.ssh/id_ecdsa \
    -e "@vars.yaml" \
    -e "@hardening.yaml"
```

## Шифрование секретов «at rest»

Данные шифруются `kube-apiserver` перед записью в etcd, поэтому в etcd они нечитаемы. Провайдер по умолчанию в Kubespray — `secretbox`.

| Провайдер | Причина, почему НЕ выбран по умолчанию |
|---|---|
| `identity` | Отсутствие шифрования |
| `aesgcm` | Требует ротации ключа каждые 200k записей |
| `aescbc` | Не рекомендуется из-за уязвимости CBC к padding oracle |
| `kms` | Официально рекомендуемый способ, но требует внешней (независимой от Kubernetes) KMS, что нельзя гарантировать во всех окружениях |
| `secretbox` | Значение по умолчанию в Kubespray |

Доступные значения `kube_encryption_algorithm`: `secretbox` (по умолчанию), `identity`, `aesgcm`, `aescbc`, `kms`.

### Детали Secretbox

Secretbox использует [Poly1305](https://cr.yp.to/mac.html) как код аутентификации сообщения (MAC) и [XSalsa20](https://www.xsalsa20.com/) как алгоритм аутентифицированного шифрования с секретным ключом.

## Источники

- `docs/operations/hardening.md` (v2.31.0, commit `1c9add4`)
- `docs/operations/encrypting-secret-data-at-rest.md` (v2.31.0, commit `1c9add4`)
- Тег репозитория: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0
- См. также: [[versions/v2.31.0/README|Срез v2.31.0]], [[versions/v2.31.0/variables/k8s-cluster|Переменные ядра]]
