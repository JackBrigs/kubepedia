---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: docs
source_paths:
  - docs/operations/etcd.md
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0
retrieved_at: 2026-07-14
topics:
  - etcd
reliability: authoritative
---

# etcd в v2.30.0

Дайджест `docs/operations/etcd.md` тега v2.30.0 (commit `f4ccdb5`). Полный список переменных и значения по умолчанию — в [[versions/v2.30.0/variables/etcd|Переменные etcd]].

## Типы развёртывания (etcd_deployment_type)

etcd можно развернуть тремя способами. Метод по умолчанию — `host`. Тип задаётся переменной `etcd_deployment_type`, допустимые значения: `host`, `kubeadm`, `docker`.

### host (по умолчанию)

Метод по умолчанию. etcd устанавливается как systemd-сервис.

### docker

Устанавливает docker на членов группы etcd и запускает etcd в docker-контейнерах. Используется **только** когда `container_manager` установлен в `docker`.

### kubeadm

Экспериментальный метод, доступен только для новых развёртываний. Разворачивает etcd как static pod на хостах control plane.

## Топология

Документация тега напрямую разбирает топологию только через тип развёртывания:
- при `host` и `docker` etcd работает на хостах группы `etcd` (systemd-сервис либо docker-контейнер) — внешняя (stacked/external определяется составом групп инвентаря) топология;
- при `kubeadm` etcd размещается как static pod непосредственно на хостах control plane (stacked-топология).

Явного описания stacked vs external топологии и переменных выбора состава узлов etcd в `docs/operations/etcd.md` тега нет — детали состава группы `etcd` и распределения узлов задаются инвентарём; см. [[versions/v2.30.0/variables/etcd|Переменные etcd]] и defaults роли `etcd`. Не додумано — в доке тега это явно не описано.

## Метрики

Экспозиция метрик на отдельном HTTP-порту (задаётся в инвентаре):

```yaml
etcd_metrics_port: 2381
```

Создание сервиса `etcd-metrics` и связанных endpoints в namespace `kube-system` — через задание меток:

```yaml
etcd_metrics_service_labels:
  k8s-app: etcd
  app.kubernetes.io/managed-by: Kubespray
  app: kube-prometheus-stack-kube-etcd
  release: prometheus-stack
```

Последние две метки в примере позволяют скрейпить метрики чартом [kube-prometheus-stack](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack) при `kubeEtcd.service.enabled: false`.

Полное переопределение URL экспозиции метрик:

```yaml
etcd_listen_metrics_urls: "http://0.0.0.0:2381"
```

## Источники

- `docs/operations/etcd.md` — https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0/docs/operations/etcd.md

См. также: [[versions/v2.30.0/variables/etcd|Переменные etcd]] · [[versions/v2.30.0/README|Срез v2.30.0]]
