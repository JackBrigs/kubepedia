---
project: kubespray
kubespray_version: v2.27.0
git_commit: 9ec9b3a
source_type: docs
source_paths:
  - docs/operations/etcd.md
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.27.0
retrieved_at: 2026-07-15
topics:
  - etcd
reliability: authoritative
---

# etcd в v2.27.0

Дайджест документации `docs/operations/etcd.md` тега v2.27.0: типы развёртывания etcd, топология и экспозиция метрик.

Связанные заметки: [[versions/v2.27.0/variables/etcd|Переменные etcd]] · [[versions/v2.27.0/ansible-tags|Ansible-теги]] · [[versions/v2.27.0/README|Срез v2.27.0]].

---

## Типы развёртывания (`etcd_deployment_type`)

etcd можно развернуть тремя методами. Метод задаётся переменной `etcd_deployment_type`; допустимые значения: `host`, `kubeadm`, `docker`.

### host (по умолчанию)

Метод по умолчанию. etcd устанавливается как systemd-сервис на хостах.

### docker

Устанавливает docker на членах группы `etcd` и запускает etcd в docker-контейнерах. Применим только когда `container_manager` установлен в `docker`.

### kubeadm

Экспериментальный метод, доступен только для новых развёртываний. Разворачивает etcd как статический под (static pod) на хостах control plane.

> Примечание по топологии: метод `kubeadm` (static pod на control plane) соответствует stacked-топологии — etcd совмещён с узлами управления. Методы `host` и `docker` на выделенной группе `etcd` используются для внешней (external) топологии. Явных терминов «stacked» / «external» текст `docs/operations/etcd.md` тега v2.27.0 не вводит; распределение узлов по группам задаётся в инвентаре (группа `etcd`).

---

## Метрики

- `etcd_metrics_port: 2381` — экспозиция метрик на отдельном HTTP-порту (задаётся в инвентаре).
- `etcd_metrics_service_labels` — метки для создания сервиса `etcd-metrics` и связанных endpoints в namespace `kube-system`. Пример меток в доке позволяет скрейпить метрики чартом kube-prometheus-stack:
  ```yaml
  etcd_metrics_service_labels:
    k8s-app: etcd
    app.kubernetes.io/managed-by: Kubespray
    app: kube-prometheus-stack-kube-etcd
    release: prometheus-stack
  ```
  При этом в `values.yaml` чарта отключается собственный сервис: `kubeEtcd.service.enabled: false`.
- `etcd_listen_metrics_urls: "http://0.0.0.0:2381"` — полное переопределение URL экспозиции метрик.

---

## Источники

- `docs/operations/etcd.md` (v2.27.0)
- Репозиторий тега: https://github.com/kubernetes-sigs/kubespray/tree/v2.27.0

Связанные заметки: [[versions/v2.27.0/variables/etcd|Переменные etcd]] · [[versions/v2.27.0/ansible-tags|Ansible-теги]] · [[versions/v2.27.0/README|Срез v2.27.0]]
