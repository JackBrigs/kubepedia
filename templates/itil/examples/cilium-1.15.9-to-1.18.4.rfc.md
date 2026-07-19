# RFC-2026-0207 · Обновление Cilium 1.15.9 → 1.18.4 (Kubespray)

| Поле | Значение |
|---|---|
| Дата подачи | 2026-07-19 |
| Инициатор (requester) | Platform Engineering |
| Владелец изменения (change owner) | SRE / Networking |
| Тип изменения | **Normal** |
| Приоритет | High = impact (весь дата-плейн кластера) × urgency (плановая; блокирует дальнейшие апгрейды и закрытие CVE) |
| Запрашиваемый change authority | CAB |

## Описание
Обновить CNI Cilium с 1.15.9 до 1.18.4 на Kubespray-кластере. Cilium поддерживает переходы только
между соседними минорами, поэтому — 4 контролируемых шага: 1.15.9 → 1.16.x → 1.17.x → 1.18.4.

## Обоснование (reason for change)
1.15 вне активной поддержки (тех-долг), накопились security-фиксы; апгрейд готовит переход к 1.19.
Без обновления растёт риск незакрытых уязвимостей и невозможность двигать платформу дальше.

## Затронутые сервисы и конфигурационные единицы (CIs)
- Сервисы: pod-to-pod networking, Service/LoadBalancer, NetworkPolicy enforcement, (опц.) BGP, IPsec,
  ClusterMesh, Hubble.
- CIs: DaemonSet `cilium`, `cilium-operator`, `cilium-envoy`; ConfigMap `cilium-config`; CRD Cilium
  (BGP, LoadBalancerIPPool, NetworkPolicy).
- Косвенно: все рабочие нагрузки кластера (сетевая связность).

## Предлагаемый план (high-level)
На каждом хопе: preflight-DaemonSet → задать `cilium_version` + `cilium_upgrade_compatibility` →
`cluster.yml --tags=cilium` → валидация (`cilium status`, `cilium connectivity test`). Детали — в
раннбуке базы и в Change Record.

## Оценка риска (предварительная)
- Уровень: **High**.
- Ключевые риски: Kubespray перескакивает 1.16 (нарушение consecutive-minor); ядро ≥5.10 с 1.18;
  смена дефолтов (ENI-masquerade true→false, churn serviceaccount-identity, BGP CRD v2alpha1→v2,
  депрекация KPR-тогглов); IPsec+KPR+BPF-masq → авто eBPF host-routing, CVE-2025-37959 (нужен патч
  ядра или `--enable-host-legacy-routing=true`).

## План отката (backout)
До снятия `cilium_upgrade_compatibility` — возврат `cilium_version` на предыдущий минор + converge.
**Чистого отката нет после миграции CRD (BGP v2, IPPool) или churn identity** — это точка невозврата.

## Предлагаемое окно
Окно обслуживания; 4 шага можно разнести по окнам. Change schedule: не пересекать с другими сетевыми
изменениями.

## Зависимости
Пред-чек: ядро ≥5.10 на всех нодах; текущая версия ≥1.15.6 (выполнено — 1.15.9); актуальный etcd-снапшот.
