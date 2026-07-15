---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: docs
source_paths:
  - docs/operations/hardening.md
  - docs/operations/encrypting-secret-data-at-rest.md
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0
retrieved_at: 2026-07-14
topics:
  - security
  - hardening
reliability: authoritative
---

# Безопасность кластера в v2.30.0

Дайджест по усилению безопасности (hardening) и шифрованию секретов at rest.
Источники — только документация тега v2.30.0 (commit `f4ccdb5`).

## Усиление кластера (Hardening)

Конфигурация приводит установку Kubernetes в соответствие с
[CIS Benchmarks](https://learn.cisecurity.org/benchmarks). Все переменные
задаются через отдельный файл (например `hardening.yaml`) и передаются
в `cluster.yml`.

**Минимальное требование:** версия Kubernetes не ниже `v1.23.6` — для наличия
современных функций безопасности (например admission-плагина `PodSecurity`).

Запуск:

```bash
ansible-playbook -v cluster.yml \
        -i inventory.ini \
        -b --become-user=root \
        --private-key ~/.ssh/id_ecdsa \
        -e "@vars.yaml" \
        -e "@hardening.yaml"
```

### kube-apiserver

| Переменная | Значение из примера | Назначение |
|---|---|---|
| `authorization_modes` | `['Node', 'RBAC']` | Режимы авторизации |
| `kube_apiserver_request_timeout` | `120s` | Таймаут запросов к API |
| `kube_apiserver_service_account_lookup` | `true` | Проверка существования service account токена |
| `tls_min_version` | `VersionTLS12` | Минимальная версия TLS |
| `tls_cipher_suites` | список шифров | Разрешённые наборы шифров TLS |
| `kube_apiserver_enable_admission_plugins` | список плагинов | Включаемые admission-плагины |
| `kube_apiserver_admission_control_config_file` | `true` | Генерировать файл конфигурации admission control |
| `kube_apiserver_admission_event_rate_limits` | `limit_1`, `limit_2` | Конфигурация плагина `EventRateLimit` |
| `kube_profiling` | `false` | Отключение профилирования |
| `remove_anonymous_access` | `true` | Удаление анонимного доступа к кластеру |

`tls_cipher_suites` из примера:

```yaml
tls_cipher_suites:
  - TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
  - TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
  - TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305
```

**Admission-плагины** (`kube_apiserver_enable_admission_plugins`):
`EventRateLimit`, `AlwaysPullImages`, `ServiceAccount`, `NamespaceLifecycle`,
`NodeRestriction`, `LimitRanger`, `ResourceQuota`, `MutatingAdmissionWebhook`,
`ValidatingAdmissionWebhook`, `PodNodeSelector`, `PodSecurity`.

Дополнительные переменные конфигурации admission (закомментированы в примере):

- `kube_apiserver_admission_plugins_needs_configuration: [PodNodeSelector]` — создать конфиг-файл для `PodNodeSelector`;
- `kube_apiserver_admission_plugins_podnodeselector_default_node_selector` — селектор узлов по умолчанию (например `network=srv1`).

Пример конфигурации `EventRateLimit`:

```yaml
kube_apiserver_admission_event_rate_limits:
  limit_1:
    type: Namespace
    qps: 50
    burst: 100
    cache_size: 2000
  limit_2:
    type: User
    qps: 50
    burst: 100
```

Примечание из документации: `anonymous-auth` у `kube-apiserver` по умолчанию
`true` — это считается безопасным при включённом `RBAC` в `authorization-mode`.

### kube-controller-manager

| Переменная | Значение | Назначение |
|---|---|---|
| `kube_controller_manager_bind_address` | `127.0.0.1` | Привязка только к localhost |
| `kube_controller_terminated_pod_gc_threshold` | `50` | Порог сборки мусора завершённых подов |
| `kube_controller_feature_gates` | `["RotateKubeletServerCertificate=true"]` | Feature gates |

### kube-scheduler

| Переменная | Значение | Назначение |
|---|---|---|
| `kube_scheduler_bind_address` | `127.0.0.1` | Привязка только к localhost |

### etcd

| Переменная | Значение | Назначение |
|---|---|---|
| `etcd_deployment_type` | `host` | Развёртывание etcd на выделенных хостах вне кластера |

Согласно документации, запуск etcd на выделенных хостах вне кластера — самый
безопасный вариант: изолирует etcd от CNI-сети кластера, убирает векторы атак
на уровне подов и создаёт дополнительную границу безопасности для критичного
хранилища состояния.

### kubelet

| Переменная | Значение | Назначение |
|---|---|---|
| `kubelet_authorization_mode_webhook` | `true` | Авторизация kubelet через webhook |
| `kubelet_authentication_token_webhook` | `true` | Аутентификация токенов через webhook |
| `kube_read_only_port` | `0` | Отключение read-only порта kubelet |
| `kubelet_rotate_server_certificates` | `true` | Ротация серверных сертификатов |
| `kubelet_protect_kernel_defaults` | `true` | Защита параметров ядра по умолчанию |
| `kubelet_event_record_qps` | `1` | Ограничение частоты записи событий |
| `kubelet_rotate_certificates` | `true` | Ротация клиентских сертификатов |
| `kubelet_streaming_connection_idle_timeout` | `"5m"` | Таймаут простоя streaming-соединений |
| `kubelet_make_iptables_util_chains` | `true` | Создание util-цепочек iptables |
| `kubelet_feature_gates` | `["RotateKubeletServerCertificate=true"]` | Feature gates |
| `kubelet_seccomp_default` | `true` | Профиль seccomp по умолчанию |
| `kubelet_systemd_hardening` | `true` | Усиление через systemd |
| `kubelet_static_pod_path` | `""` | Отключение staticPodPath (для worker-узлов без static pods) |
| `kubelet_secure_addresses` | строка IP | IP-адреса, с которых kubelet принимает пакеты |

Пример `kubelet_secure_addresses`:
`"localhost link-local {{ kube_pods_subnet }} 192.168.10.110 192.168.10.111 192.168.10.112"`.

`kubelet_systemd_hardening` вместе с `kubelet_secure_addresses` настраивают
минимальный firewall на системе.

**Ротация сертификатов:** `rotateCertificates` в `KubeletConfiguration` = `true`
вместе с `serverTLSBootstrap`. CSR одобряются автоматически через
[kubelet-csr-approver](https://github.com/postfinance/kubelet-csr-approver);
настройка одобрения — через Helm-values в переменной `kubelet_csr_approver_values`.

### Дополнительные переменные

| Переменная | Значение | Назначение |
|---|---|---|
| `kube_owner` | `root` | Владелец файлов Kubernetes |
| `kube_cert_group` | `root` | Группа сертификатов |
| `kube_pod_security_use_default` | `true` | Создать конфигурацию Pod Security по умолчанию (namespace `kube-system` исключён) |
| `kube_pod_security_default_enforce` | `restricted` | Уровень enforce для Pod Security |

## Шифрование секретов at rest

Включается в hardening через набор переменных:

| Переменная | Значение из примера | Назначение |
|---|---|---|
| `kube_encrypt_secret_data` | `true` | Включить шифрование данных at rest |
| `kube_encryption_resources` | `[secrets]` | Какие ресурсы шифровать |
| `kube_encryption_algorithm` | `"secretbox"` | Провайдер (алгоритм) шифрования |

Механизм: `kube-apiserver` шифрует данные перед их записью в etcd
(`encryption-provider-config`), поэтому в etcd они нечитаемы.

### Провайдеры шифрования

Значение по умолчанию в Kubespray — `secretbox`. Всего поддерживается 5
провайдеров:

| Провайдер | Комментарий из документации |
|---|---|
| `identity` | Без шифрования |
| `secretbox` | Выбран по умолчанию |
| `aesgcm` | Требует ротацию ключа каждые 200k записей |
| `aescbc` | Не рекомендуется из-за уязвимости CBC к padding oracle атакам |
| `kms` | Официально рекомендуемый способ, но требует внешний KMS — не подходит как значение по умолчанию для всех окружений |

**Secretbox** использует [Poly1305](https://cr.yp.to/mac.html) как код
аутентификации сообщений и [XSalsa20](https://www.xsalsa20.com/) как
secret-key шифрование.

## Источники

- `docs/operations/hardening.md` (тег v2.30.0)
- `docs/operations/encrypting-secret-data-at-rest.md` (тег v2.30.0)
- [[versions/v2.30.0/variables/k8s-cluster|Переменные ядра]]
- [[versions/v2.30.0/README|Срез v2.30.0]]
