---
project: kubespray
kubespray_version: v2.28.0
git_commit: 63cdf87
source_type: docs
source_paths:
  - docs/operations/kernel-requirements.md
  - docs/operations/port-requirements.md
  - docs/advanced/kubernetes-reliability.md
  - docs/advanced/ntp.md
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.28.0
retrieved_at: 2026-07-15
topics:
  - troubleshooting
  - requirements
reliability: authoritative
---

# Эксплуатационные требования и troubleshooting в v2.28.0

Дайджест по требованиям к ядру, портам, надёжности при сбоях узлов и NTP. Данные взяты строго из документации тега `v2.28.0` (commit `63cdf87`). Все четыре исходных файла идентичны версии v2.29.1.

## 1. Требования к ядру

Источник: `docs/operations/kernel-requirements.md`.

- Для Kubernetes `>=1.32.0` рекомендуемая LTS-версия ядра из ветки 4.x — `4.19`. Версии 5.x и 6.x также поддерживаются.
- Для поддержки cgroups v2 минимальная версия ядра — `4.15`, рекомендуемая — `5.8+`.

Если версия ядра ниже требуемой, добавить обход preflight-ошибок kubeadm:

```yaml
kubeadm_ignore_preflight_errors:
  - SystemVerification
```

### Матрица версий ядра по ОС

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

## 2. Требования к портам

Источник: `docs/operations/port-requirements.md`. Часть портов опциональна и зависит от конфигурации.

### Kubernetes — Control plane

| Протокол | Порт | Назначение | Группа |
|---|---|---|---|
| TCP | 22 | ssh для ansible | kube_control_plane |
| TCP | 2379 | etcd client port | kube_control_plane / etcd |
| TCP | 2380 | etcd peer port | kube_control_plane / etcd |
| TCP | 6443 | kubernetes api | kube_control_plane |
| TCP | 10250 | kubelet api | kube_control_plane |
| TCP | 10257 | kube-scheduler | kube_control_plane |
| TCP | 10259 | kube-controller-manager | kube_control_plane |

### Kubernetes — Worker node(s)

| Протокол | Порт | Назначение | Группа |
|---|---|---|---|
| TCP | 22 | ssh для ansible | kube_node |
| TCP | 10250 | kubelet api | kube_node |
| TCP | 30000-32767 | диапазон kube nodePort | kube_node |

### Calico (если используется)

| Протокол | Порт | Назначение |
|---|---|---|
| TCP | 179 | Calico networking (BGP) |
| UDP | 4789 | Calico CNI с включённым VXLAN |
| TCP | 5473 | Calico CNI с включённым Typha |
| UDP | 51820 | Calico с IPv4 Wireguard |
| UDP | 51821 | Calico с IPv6 Wireguard |
| IPENCAP / IPIP | - | Calico CNI с включённым IPIP |

### Cilium (если используется)

| Протокол | Порт | Назначение |
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

| Протокол | Порт | Назначение |
|---|---|---|
| TCP | 9100 | node exporter |
| TCP/UDP | 7472 | metallb metrics ports |
| TCP/UDP | 7946 | metallb L2 operating mode |

## 3. Надёжность кластера и таймауты обнаружения сбоев узлов

Источник: `docs/advanced/kubernetes-reliability.md`. Рассматривается связка Kubelet ↔ Controller Manager.

### Поведение по умолчанию

1. `--node-status-update-frequency` — частота обновления статуса kubelet в apiserver. По умолчанию **10s**.
2. `--node-monitor-period` — частота проверки статусов kubelet контроллер-менеджером. По умолчанию **5s**.
3. `--node-monitor-grace-period` — период, в течение которого статус считается здоровым. По умолчанию **40s**.

Kubelet делает `nodeStatusUpdateRetry` попыток (константа = 5). Итог: число попыток обновить статус = `nodeStatusUpdateRetry` × `--node-status-update-frequency`.

После истечения `--node-monitor-grace-period` узел считается нездоровым. Поды переселяются согласно [Taint Based Eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#taint-based-evictions) таймерам подов или глобальным таймерам apiserver: `--default-not-ready-toleration-seconds` и `--default-unreachable-toleration-seconds`. После вытеснения kube-proxy обновляет iptables и удаляет endpoint'ы упавшего узла.

Важное предупреждение: Controller Manager и Kubelet работают асинхронно; реальная задержка включает сетевую задержку, задержку API Server и etcd, нагрузку на control plane. Реальное время попадания статуса в etcd может быть больше заданного.

### Рекомендации по сценариям

| Сценарий | `--node-status-update-frequency` | `--node-monitor-period` | `--node-monitor-grace-period` | toleration-seconds (`not-ready`/`unreachable`) | Итог вытеснения подов | Нагрузка (1000 узлов) |
|---|---|---|---|---|---|---|
| По умолчанию | 10s | 5s | 40s | 300 | — | — |
| Fast Update / Fast Reaction | 4s | 2s | 20s | 30 | ~50s (20s down + 30s toleration) | ~15000 обновлений/мин |
| Medium Update / Average Reaction | 20s | 5s (по умолч.) | 2m | 60 | ~3m всего | ~3000 обновлений/мин |
| Low Update / Slow Reaction | 1m | 5s (по умолч.) | 5m | 60 | ~6m всего (5m unhealthy + 1m) | минимальная |

Примечания:
- Значения `--default-not-ready-toleration-seconds` и `--default-unreachable-toleration-seconds` — целые числа в секундах (без суффиксов "s"/"m").
- Fast-сценарий создаёт значительную нагрузку на etcd; для больших кластеров могут понадобиться выделенные узлы под etcd.
- Возможны комбинации, например «быстрое обновление + медленная реакция» под конкретные требования.

## 4. Синхронизация времени (NTP)

Источник: `docs/advanced/ntp.md`. Синхронизация времени важна для Kubernetes и etcd.

| Переменная | Значение / пример | Назначение |
|---|---|---|
| `ntp_enabled` | `true` | Запуск и автозапуск службы ntpd/chrony |
| `ntp_manage_config` | `true` | Управление конфигом NTP (для air-gap / кастомных серверов) |
| `ntp_servers` | список, напр. `"0.your-ntp-server.org iburst"` | Кастомные NTP-серверы |
| `ntp_timezone` | напр. `Etc/UTC`, `Asia/Shanghai` | Часовой пояс (если не задан — не меняется) |
| `ntp_tinker_panic` | `true` | Против дрейфа часов в VM (только при `ntp_manage_config: true`) |
| `ntp_force_sync_immediately` | `true` | Немедленная синхронизация после установки (полезно на свежих системах) |
| `ntp_package` | `ntpsec` | Пакет NTP; рекомендуется для Ubuntu 24.04 и дистрибутивов с `systemd-timesyncd` |

Пример кастомной конфигурации:

```yaml
ntp_enabled: true
ntp_manage_config: true
ntp_servers:
  - "0.your-ntp-server.org iburst"
  - "1.your-ntp-server.org iburst"
  - "2.your-ntp-server.org iburst"
  - "3.your-ntp-server.org iburst"
```

## Связанные срезы

- [[versions/v2.28.0/variables/k8s-cluster|Переменные ядра кластера]]
- [[versions/v2.28.0/variables/cni|Переменные CNI (Calico/Cilium)]]
- [[versions/v2.28.0/docs/security|Безопасность и hardening]]

## Источники

- `docs/operations/kernel-requirements.md` — <https://github.com/kubernetes-sigs/kubespray/blob/v2.28.0/docs/operations/kernel-requirements.md>
- `docs/operations/port-requirements.md` — <https://github.com/kubernetes-sigs/kubespray/blob/v2.28.0/docs/operations/port-requirements.md>
- `docs/advanced/kubernetes-reliability.md` — <https://github.com/kubernetes-sigs/kubespray/blob/v2.28.0/docs/advanced/kubernetes-reliability.md>
- `docs/advanced/ntp.md` — <https://github.com/kubernetes-sigs/kubespray/blob/v2.28.0/docs/advanced/ntp.md>
- [[versions/v2.28.0/README|Срез v2.28.0]]
