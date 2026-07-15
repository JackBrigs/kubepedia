---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: docs
source_paths:
  - docs/operations/kernel-requirements.md
  - docs/operations/port-requirements.md
  - docs/advanced/kubernetes-reliability.md
  - docs/advanced/ntp.md
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0
retrieved_at: 2026-07-14
topics:
  - troubleshooting
  - requirements
reliability: authoritative
---

# Требования и надёжность в v2.30.0

Дайджест по требованиям к ядру, сетевым портам, надёжности узлов и NTP.
Источники — только документация тега v2.30.0 (commit `f4ccdb5`).

## Требования к ядру

Для Kubernetes >= 1.32.0 рекомендуемая LTS-версия ядра из серии 4.x — **4.19**.
Любые версии 5.x и 6.x также поддерживаются. Для поддержки **cgroups v2**
минимальная версия — **4.15**, рекомендуемая — **5.8+**.

Если версия ядра ОС ниже требуемой, добавьте конфигурацию для игнорирования
ошибок preflight-проверки kubeadm:

```yaml
kubeadm_ignore_preflight_errors:
  - SystemVerification
```

Матрица версий ядра по ОС:

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

## Требования к портам

При настроенном firewall необходимо открыть порты для связи компонентов.
Часть портов опциональна и зависит от конфигурации.

### Kubernetes — Control plane

| Протокол | Порт | Описание |
|---|---|---|
| TCP | 22 | ssh для ansible |
| TCP | 2379 | etcd client port |
| TCP | 2380 | etcd peer port |
| TCP | 6443 | kubernetes api |
| TCP | 10250 | kubelet api |
| TCP | 10257 | kube-scheduler |
| TCP | 10259 | kube-controller-manager |

### Kubernetes — Worker-узлы

| Протокол | Порт | Описание |
|---|---|---|
| TCP | 22 | ssh для ansible |
| TCP | 10250 | kubelet api |
| TCP | 30000-32767 | диапазон kube nodePort |

### Calico

| Протокол | Порт | Описание |
|---|---|---|
| TCP | 179 | Calico networking (BGP) |
| UDP | 4789 | Calico CNI с включённым VXLAN |
| TCP | 5473 | Calico CNI с включённым Typha |
| UDP | 51820 | Calico с IPv4 Wireguard |
| UDP | 51821 | Calico с IPv6 Wireguard |
| IPENCAP / IPIP | - | Calico CNI с включённым IPIP |

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
| ICMP | - | health checks |

### Addons

| Протокол | Порт | Описание |
|---|---|---|
| TCP | 9100 | node exporter |
| TCP/UDP | 7472 | metallb metrics ports |
| TCP/UDP | 7946 | metallb L2 operating mode |

## Надёжность и реакция на сбой узлов

Механизм взаимодействия Kubelet <-> Controller Manager и параметры,
влияющие на скорость обнаружения сбоя узла и вытеснения подов.

### Нормальное поведение (значения по умолчанию)

| Параметр | Значение по умолчанию | Описание |
|---|---|---|
| `--node-status-update-frequency` | 10s | Частота обновления статуса kubelet в apiserver |
| `--node-monitor-period` | 5s | Частота проверки статусов kubelet контроллером |
| `--node-monitor-grace-period` | 40s | Время, в течение которого статус считается здоровым |
| `--default-not-ready-toleration-seconds` | 300s | Глобальный таймер toleration для NotReady |
| `--default-unreachable-toleration-seconds` | 300s | Глобальный таймер toleration для Unreachable |

Kubelet делает `nodeStatusUpdateRetry` попыток (константа = 5). Итоговое число
попыток установки статуса = `nodeStatusUpdateRetry` * `--node-status-update-frequency`.
После `--node-monitor-grace-period` контроллер считает узел нездоровым, после
чего поды вытесняются согласно Taint Based Eviction (индивидуальные toleration
или глобальные таймеры apiserver). Kube-proxy замечает вытеснение и обновляет
iptables узла, убирая endpoint'ы недоступных подов.

Важно: контроллер и kubelet работают асинхронно — реальная задержка включает
сетевую задержку, задержку API Server, etcd и нагрузку на control plane.

### Рекомендованные профили

**Быстрое обновление и быстрая реакция:**

| Параметр | Значение |
|---|---|
| `--node-status-update-frequency` | 4s |
| `--node-monitor-period` | 2s |
| `--node-monitor-grace-period` | 20s |
| toleration-seconds | 30 |

Поды вытесняются за ~50s (20s на признание узла упавшим + 30s toleration).
Создаёт нагрузку на etcd: 1000 узлов = 15000 обновлений в минуту.

**Среднее обновление и средняя реакция:**

| Параметр | Значение |
|---|---|
| `--node-status-update-frequency` | 20s |
| `--node-monitor-grace-period` | 2m |
| toleration-seconds | 60 |

~30 попыток до признания узла нездоровым, вытеснение через ~3m суммарно.
1000 узлов = 3000 обновлений etcd в минуту.

**Медленное обновление и медленная реакция:**

| Параметр | Значение |
|---|---|
| `--node-status-update-frequency` | 1m |
| `--node-monitor-grace-period` | 5m |
| toleration-seconds | 60 |

~25 попыток до нездорового статуса, вытеснение через ~6m суммарно.

Значения toleration-seconds задаются целыми числами в секундах (без суффиксов
"s"/"m"). Возможны комбинации (например быстрое обновление + медленная реакция).

## NTP синхронизация

Синхронизация времени важна для Kubernetes и etcd.

| Переменная | Пример значения | Назначение |
|---|---|---|
| `ntp_enabled` | `true` | Включить и запустить службу ntpd/chrony при загрузке |
| `ntp_manage_config` | `true` | Управлять конфиг-файлом NTP (нужно для кастомных серверов) |
| `ntp_servers` | список | Свои NTP-серверы (для air-gap окружений) |
| `ntp_timezone` | `Etc/UTC`, `Asia/Shanghai` | Часовой пояс (если не задан — не меняется) |
| `ntp_tinker_panic` | `true` | `tinker panic` — против дрейфа часов в VM (работает только при `ntp_manage_config: true`) |
| `ntp_force_sync_immediately` | `true` | Немедленная синхронизация после установки (полезно на новых системах) |
| `ntp_package` | `ntpsec` | Пакет NTP; для Ubuntu 24.04 и дистрибутивов с `systemd-timesyncd` использовать `ntpsec` |

Пример своих серверов:

```yaml
ntp_enabled: true
ntp_manage_config: true
ntp_servers:
  - "0.your-ntp-server.org iburst"
  - "1.your-ntp-server.org iburst"
  - "2.your-ntp-server.org iburst"
  - "3.your-ntp-server.org iburst"
```

## Источники

- `docs/operations/kernel-requirements.md` (тег v2.30.0)
- `docs/operations/port-requirements.md` (тег v2.30.0)
- `docs/advanced/kubernetes-reliability.md` (тег v2.30.0)
- `docs/advanced/ntp.md` (тег v2.30.0)
- [[versions/v2.30.0/variables/k8s-cluster|Переменные ядра]]
- [[versions/v2.30.0/README|Срез v2.30.0]]
