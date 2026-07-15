---
project: kubespray
kubespray_version: v2.29.1
git_commit: 0c6a295
source_type: docs
source_paths:
  - docs/operations/hardening.md
  - docs/operations/encrypting-secret-data-at-rest.md
retrieved_at: 2026-07-14
topics:
  - security
  - hardening
reliability: authoritative
---

# Безопасность кластера в v2.29.1

Дайджест по усилению безопасности (hardening) и шифрованию секретов в покое (encryption at rest). Все переменные и значения взяты строго из документации тега `v2.29.1` (commit `0c6a295`).

## 1. Усиление безопасности (hardening)

Источник: `docs/operations/hardening.md`. Конфигурация приводит установку в соответствие с [CIS Benchmarks](https://learn.cisecurity.org/benchmarks). Рекомендуемый способ применения — отдельный файл `hardening.yaml`, передаваемый через `-e "@hardening.yaml"`.

### Минимальные требования

- Версия Kubernetes — не ниже `v1.23.6` (для новых security-фич, в т.ч. admission-плагина `PodSecurity`).
- Требуется свежая версия Kubespray, часть настроек добавлена недавно; проверить, что другие настройки их не переопределяют.

### kube-apiserver

| Переменная | Значение | Назначение |
|---|---|---|
| `authorization_modes` | `['Node', 'RBAC']` | Режимы авторизации |
| `kube_apiserver_request_timeout` | `120s` | Таймаут запроса |
| `kube_apiserver_service_account_lookup` | `true` | Проверка существования токенов SA |
| `kube_profiling` | `false` | Отключение профилирования |
| `remove_anonymous_access` | `true` | Удаление анонимного доступа к кластеру |

Примечание из документа: `anonymous-auth` у `kube-apiserver` по умолчанию `true` — это считается безопасным при включённом `RBAC`.

#### Аудит

| Переменная | Значение |
|---|---|
| `kubernetes_audit` | `true` |
| `audit_log_path` | `/var/log/kube-apiserver-log.json` |
| `audit_log_maxage` | `30` |
| `audit_log_maxbackups` | `10` |
| `audit_log_maxsize` | `100` |

#### TLS

| Переменная | Значение |
|---|---|
| `tls_min_version` | `VersionTLS12` |
| `tls_cipher_suites` | `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`, `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305` |

#### Admission-плагины

```yaml
kube_apiserver_enable_admission_plugins:
  - EventRateLimit
  - AlwaysPullImages
  - ServiceAccount
  - NamespaceLifecycle
  - NodeRestriction
  - LimitRanger
  - ResourceQuota
  - MutatingAdmissionWebhook
  - ValidatingAdmissionWebhook
  - PodNodeSelector
  - PodSecurity
kube_apiserver_admission_control_config_file: true
```

Сопутствующие переменные:

- `kube_apiserver_admission_plugins_needs_configuration: [PodNodeSelector]` — генерация конфиг-файла для `PodNodeSelector` (закомментировано в примере).
- `kube_apiserver_admission_plugins_podnodeselector_default_node_selector: "network=srv1"` — селектор узлов по умолчанию (закомментировано).
- `kube_apiserver_admission_event_rate_limits` — конфигурация плагина `EventRateLimit` (лимиты по `Namespace` и `User`, поля `qps`, `burst`, `cache_size`). Конфиг-файлы создаются автоматически и монтируются в контейнер `kube-apiserver`.

Плагин `PodSecurity` включает [Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/).

### kube-controller-manager

| Переменная | Значение |
|---|---|
| `kube_controller_manager_bind_address` | `127.0.0.1` |
| `kube_controller_terminated_pod_gc_threshold` | `50` |
| `kube_controller_feature_gates` | `["RotateKubeletServerCertificate=true"]` |

### kube-scheduler

| Переменная | Значение |
|---|---|
| `kube_scheduler_bind_address` | `127.0.0.1` |

### etcd

- `etcd_deployment_type: host` — запуск etcd на выделенных хостах вне кластера Kubernetes считается наиболее защищённым вариантом: изолирует etcd от CNI-сети кластера, убирает вектора атак уровня pod и создаёт дополнительную границу безопасности для хранилища состояния кластера.

### kubelet

| Переменная | Значение | Назначение |
|---|---|---|
| `kubelet_authorization_mode_webhook` | `true` | Авторизация через webhook |
| `kubelet_authentication_token_webhook` | `true` | Аутентификация токенов через webhook |
| `kube_read_only_port` | `0` | Отключение read-only порта kubelet |
| `kubelet_rotate_server_certificates` | `true` | Ротация серверных сертификатов |
| `kubelet_protect_kernel_defaults` | `true` | Защита дефолтов ядра |
| `kubelet_event_record_qps` | `1` | Лимит записи событий |
| `kubelet_rotate_certificates` | `true` | Ротация клиентских сертификатов |
| `kubelet_streaming_connection_idle_timeout` | `"5m"` | Таймаут простоя streaming-соединений |
| `kubelet_make_iptables_util_chains` | `true` | Создание iptables util-цепочек |
| `kubelet_feature_gates` | `["RotateKubeletServerCertificate=true"]` | Feature gate ротации |
| `kubelet_seccomp_default` | `true` | seccomp-профиль по умолчанию |
| `kubelet_systemd_hardening` | `true` | Усиление через systemd |
| `kubelet_static_pod_path` | `""` | Отключение staticPodPath (для worker-узлов без статических подов) |
| `kubelet_secure_addresses` | напр. `"localhost link-local {{ kube_pods_subnet }} 192.168.10.110 192.168.10.111 192.168.10.112"` | IP, с которых kubelet принимает пакеты |

Пары `kubelet_systemd_hardening` + `kubelet_secure_addresses` настраивают минимальный firewall на узле.

Ротация сертификатов: `rotateCertificates` в `KubeletConfiguration` = `true` вместе с `serverTLSBootstrap`. CSR по умолчанию подтверждаются автоматически через [kubelet-csr-approver](https://github.com/postfinance/kubelet-csr-approver); настройка через Helm-значения `kubelet_csr_approver_values`.

### Дополнительно

| Переменная | Значение | Назначение |
|---|---|---|
| `kube_owner` | `root` | Владелец файлов |
| `kube_cert_group` | `root` | Группа сертификатов |
| `kube_pod_security_use_default` | `true` | Дефолтная Pod Security конфигурация (namespace `kube-system` исключён по умолчанию) |
| `kube_pod_security_default_enforce` | `restricted` | Режим enforce для Pod Security |

### Пример запуска

```bash
ansible-playbook -v cluster.yml \
        -i inventory.ini \
        -b --become-user=root \
        --private-key ~/.ssh/id_ecdsa \
        -e "@vars.yaml" \
        -e "@hardening.yaml"
```

`vars.yaml` — общие данные кластера (SANs, load balancer, DNS), `hardening.yaml` — описанная выше конфигурация.

## 2. Шифрование секретов в покое (encryption at rest)

Источник: `docs/operations/encrypting-secret-data-at-rest.md`. Смысл: `kube-apiserver` шифрует данные до записи в `etcd`, поэтому в самом `etcd` данные нечитаемы.

Переменные (из `hardening.yaml`):

```yaml
kube_encrypt_secret_data: true
kube_encryption_resources: [secrets]
kube_encryption_algorithm: "secretbox"
```

### Провайдеры шифрования

Значение по умолчанию для провайдера (`kube_encryption_algorithm`) — `secretbox`. Доступные значения: `identity`, `aesgcm`, `aescbc`, `kms`.

| Провайдер | Почему не выбран по умолчанию |
|---|---|
| `identity` | Отсутствие шифрования |
| `aesgcm` | Требует ротации каждые 200k записей |
| `aescbc` | Не рекомендуется из-за уязвимости CBC к padding oracle атакам |
| `kms` | Официально рекомендуемый способ, но требует внешней KMS-службы, наличие которой нельзя гарантировать во всех окружениях |

### Про secretbox

`secretbox` использует [Poly1305](https://cr.yp.to/mac.html) в качестве message-authentication code и [XSalsa20](https://www.xsalsa20.com/) для secret-key authenticated encryption.

## Связанные срезы

- [[versions/v2.29.1/variables/k8s-cluster|Переменные ядра кластера]]
- [[versions/v2.29.1/variables/etcd|Переменные etcd]]
- [[versions/v2.29.1/docs/troubleshooting|Требования и troubleshooting]]

## Источники

- `docs/operations/hardening.md` — <https://github.com/kubernetes-sigs/kubespray/blob/v2.29.1/docs/operations/hardening.md>
- `docs/operations/encrypting-secret-data-at-rest.md` — <https://github.com/kubernetes-sigs/kubespray/blob/v2.29.1/docs/operations/encrypting-secret-data-at-rest.md>
- [[versions/v2.29.1/README|Срез v2.29.1]]
