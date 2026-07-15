---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: docs
source_paths:
  - docs/operations/kernel-requirements.md
  - docs/operations/port-requirements.md
  - docs/advanced/kubernetes-reliability.md
  - docs/advanced/ntp.md
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0
retrieved_at: 2026-07-14
topics:
  - troubleshooting
  - requirements
reliability: authoritative
---

# Требования и troubleshooting в v2.31.0

Дайджест по требованиям к ядру, сетевым портам, надёжности узлов и синхронизации времени. Источники — документация тега `v2.31.0` (commit `1c9add4`). Значения переменных — см. также [[versions/v2.31.0/variables/k8s-cluster|Переменные ядра]].

## Требования к ядру Linux

Для Kubernetes >= 1.32.0 рекомендуемая LTS-версия ядра из ветки 4.x — `4.19`. Любые версии 5.x и 6.x также поддерживаются. Для cgroups v2 минимальная версия ядра — `4.15`, рекомендуемая — `5.8+`.

Если версия ядра ОС ниже требуемой, добавьте настройку для игнорирования ошибок preflight-проверок kubeadm:

```yaml
kubeadm_ignore_preflight_errors:
  - SystemVerification
```

Матрица версий ядра по ОС (столбец «>=4.19» — соответствует ли рекомендации):

| ОС | Версия ядра | Ядро >= 4.19 |
|---|---|---|
| RHEL 9 | 5.14 | да |
| RHEL 8 | 4.18 | нет |
| Alma Linux 9 | 5.14 | да |
| Alma Linux 8 | 4.18 | нет |
| Rocky Linux 9 | 5.14 | да |
| Rocky Linux 8 | 4.18 | нет |
| Oracle Linux 9 | 5.14 | да |
| Oracle Linux 8 | 4.18 | нет |
| Ubuntu 24.04 | 6.6 | да |
| Ubuntu 22.04 | 5.15 | да |
| Ubuntu 20.04 | 5.4 | да |
| Debian 12 | 6.1 | да |
| Debian 11 | 5.10 | да |
| Fedora 40 | 6.8 | да |
| Fedora 39 | 6.5 | да |
| openSUSE Leap 15.5 | 5.14 | да |
| Amazon Linux 2 | 4.14 | нет |
| openEuler 24.03 | 6.6 | да |
| openEuler 22.03 | 5.10 | да |
| openEuler 20.03 | 4.19 | да |

## Требования к сетевым портам

Если сеть защищена firewall, необходимо открыть перечисленные порты между хостами. Часть портов опциональна и зависит от конфигурации.

### Kubernetes — control plane

| Протокол | Порт | Описание |
|---|---|---|
| TCP | 22 | SSH для Ansible |
| TCP | 2379 | etcd client port |
| TCP | 2380 | etcd peer port |
| TCP | 6443 | Kubernetes API |
| TCP | 10250 | kubelet API |
| TCP | 10257 | kube-scheduler |
| TCP | 10259 | kube-controller-manager |

### Kubernetes — worker-узлы

| Протокол | Порт | Описание |
|---|---|---|
| TCP | 22 | SSH для Ansible |
| TCP | 10250 | kubelet API |
| TCP | 30000-32767 | диапазон kube NodePort |

### Calico

| Протокол | Порт | Описание |
|---|---|---|
| TCP | 179 | Calico networking (BGP) |
| UDP | 4789 | Calico CNI при включённом VXLAN |
| TCP | 5473 | Calico CNI при включённом Typha |
| UDP | 51820 | Calico с IPv4 WireGuard |
| UDP | 51821 | Calico с IPv6 WireGuard |
| IPENCAP / IPIP | — | Calico CNI при включённом IPIP |

### Cilium

| Протокол | Порт | Описание |
|---|---|---|
| TCP | 4240 | Cilium health checks (`cilium-health`) |
| TCP | 4244 | Hubble server |
| TCP | 4245 | Hubble Relay |
| UDP | 8472 | VXLAN overlay |
| TCP | 9962 | Cilium-agent Prometheus metrics |
| TCP | 9963 | Cilium-operator Prometheus metrics |
| TCP | 9964 | Cilium-proxy Prometheus metrics |
| UDP | 51871 | WireGuard encryption tunnel endpoint |
| ICMP | — | health checks |

### Addons

| Протокол | Порт | Описание |
|---|---|---|
| TCP | 9100 | node exporter |
| TCP/UDP | 7472 | metallb metrics ports |
| TCP/UDP | 7946 | metallb L2 operating mode |

## Надёжность узлов Kubernetes (HA, реакция на отказ)

Рассматривается связь Kubelet <-> Controller Manager. Штатное поведение и параметры по умолчанию:

| Параметр | Умолчание | Смысл |
|---|---|---|
| `--node-status-update-frequency` | 10s | Как часто kubelet обновляет статус в apiserver |
| `--node-monitor-period` | 5s | Как часто controller manager проверяет статусы kubelet |
| `--node-monitor-grace-period` | 40s | Через сколько узел считается нездоровым при отсутствии обновлений |
| `--default-not-ready-toleration-seconds` | 300 | Глобальный таймер toleration для NotReady |
| `--default-unreachable-toleration-seconds` | 300 | Глобальный таймер toleration для Unreachable |

Kubelet делает `nodeStatusUpdateRetry` попыток (константа = 5). Всего попыток обновления статуса: `nodeStatusUpdateRetry` * `--node-status-update-frequency`. После `--node-monitor-grace-period` узел считается нездоровым, Pod вытесняются по taint-based eviction, kube-proxy убирает endpoints из сервисов.

Важно: узел контроллера и kubelet работают асинхронно, реальные задержки включают сетевую латентность, латентность API Server, etcd и т. д. — фактическое время может превышать номинальное.

### Профили настройки

| Профиль | update-frequency | monitor-grace-period | toleration-seconds | Время до eviction | Нагрузка на etcd (1000 узлов) |
|---|---|---|---|---|---|
| Быстрая реакция | 4s | 20s (monitor-period 2s) | 30 | ~50s | ~15000 обновлений/мин |
| Средняя реакция | 20s | 2m | 60 | ~3m | ~3000 обновлений/мин |
| Медленная реакция | 1m | 5m | 60 | ~6m | наименьшая |

Значения toleration задаются целыми числами секунд (без суффиксов «s»/«m»). Быстрый профиль даёт высокую нагрузку на etcd (может потребоваться выделенные узлы etcd). Возможны комбинации, например «быстрое обновление + медленная реакция».

## Синхронизация времени (NTP)

Синхронизация времени важна для Kubernetes и etcd. Управляется переменными роли ntp.

| Переменная | Пример значения | Назначение |
|---|---|---|
| `ntp_enabled` | `true` | Запуск и включение службы ntpd/chrony при загрузке |
| `ntp_manage_config` | `true` | Управление конфиг-файлом NTP (нужно для кастомных серверов, tinker panic) |
| `ntp_servers` | список `"0.your-ntp-server.org iburst"` | Кастомные NTP-серверы (в т. ч. для air-gap) |
| `ntp_timezone` | `Etc/UTC`, `Asia/Shanghai` | Часовой пояс; если не задан — не меняется |
| `ntp_tinker_panic` | `true` | Полезно в VM для избежания дрейфа часов; действует только при `ntp_manage_config: true` |
| `ntp_force_sync_immediately` | `true` | Немедленная синхронизация сразу после установки NTP (полезно на новых системах) |
| `ntp_package` | `ntpsec` | Использовать при Ubuntu 24.04 / дистрибутивах с уже установленным `systemd-timesyncd` |

## Источники

- `docs/operations/kernel-requirements.md` (v2.31.0, commit `1c9add4`)
- `docs/operations/port-requirements.md` (v2.31.0, commit `1c9add4`)
- `docs/advanced/kubernetes-reliability.md` (v2.31.0, commit `1c9add4`)
- `docs/advanced/ntp.md` (v2.31.0, commit `1c9add4`)
- Тег репозитория: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0
- См. также: [[versions/v2.31.0/README|Срез v2.31.0]], [[versions/v2.31.0/variables/k8s-cluster|Переменные ядра]]
