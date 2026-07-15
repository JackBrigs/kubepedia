---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: docs
source_paths:
  - docs/operations/etcd.md
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0
retrieved_at: 2026-07-14
topics:
  - etcd
reliability: authoritative
---

# etcd в v2.31.0 (дайджест документации)

Дайджест по `docs/operations/etcd.md` тега `v2.31.0`.
Переменные см. в [[versions/v2.31.0/variables/etcd|Переменные etcd]].

---

## Типы развёртывания (`etcd_deployment_type`)

Развернуть etcd можно тремя способами. Переменная — `etcd_deployment_type`,
значения: `host`, `kubeadm`, `docker`.

- **host** (по умолчанию) — etcd устанавливается как systemd-сервис.
- **docker** — устанавливает docker на членах группы etcd и запускает etcd в docker-контейнерах.
  Доступно только когда `container_manager: docker`.
- **kubeadm** — экспериментальный метод, только для новых развёртываний.
  Разворачивает etcd как статический под (static pod) на control plane хостах.

---

## Метрики etcd

- `etcd_metrics_port: 2381` — отдельный HTTP-порт для экспозиции метрик.
- `etcd_metrics_service_labels` — метки для создания сервиса `etcd-metrics` и endpoint'ов в namespace `kube-system`.
  Пример меток:
  - `k8s-app: etcd`
  - `app.kubernetes.io/managed-by: Kubespray`
  - `app: kube-prometheus-stack-kube-etcd`
  - `release: kube-prometheus-stack`
  Последние две метки позволяют скрейпить метрики chart'ом
  [kube-prometheus-stack](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack),
  установленным под release-именем `kube-prometheus-stack`, с Helm `values.yaml`:
  ```yaml
  kubeEtcd:
    service:
      enabled: false
  ```
  Если release-имя иное — соответственно скорректировать метку `release`.
- `etcd_listen_metrics_urls: "http://0.0.0.0:2381"` — полное переопределение URL экспозиции метрик.
  При экспозиции метрик на конкретных node IP kube-prometheus-stack настраивается на прямой скрейп:
  ```yaml
  kubeEtcd:
    enabled: true
    endpoints:
      - 10.141.4.22
      - 10.141.4.23
      - 10.141.4.24
  ```

---

## Что изменилось в этом doc в v2.31.0

Сравнение `git diff v2.30.0..v2.31.0 -- docs/operations/etcd.md` показывает, что
фактические правки документа касаются **только раздела метрик** (kube-prometheus-stack):

- метка `release` переименована с `prometheus-stack` на `kube-prometheus-stack`;
- уточнена формулировка про release-имя chart'а и добавлена фраза «If your Helm release name is different, adjust the `release` label accordingly»;
- добавлен пример скрейпа по конкретным node IP через `kubeEtcd.endpoints`;
- «urls» → «URLs» (косметика).

Раздел «Deployment Types» (host/docker/kubeadm) в тексте doc **не менялся** между v2.30.0 и v2.31.0.

---

## Важно про etcd 3.6.x

Текст `docs/operations/etcd.md` на теге v2.31.0 **не упоминает** конкретную версию etcd
и **не содержит** описания перехода на линию 3.6.x. Версия etcd определяется не этим
документом, а переменной `etcd_version` и логикой выбора по версии Kubernetes
(`etcd_supported_versions`, `etcd_binary_checksums`). Соответственно детали про
etcd 3.6.x относятся к [[versions/v2.31.0/components|Компоненты v2.31.0]] и справочнику
[[versions/v2.31.0/variables/etcd|Переменные etcd]], а не к этому doc.

Отмечено во избежание домысливания: в docs факт перехода на 3.6.x явно не описан.

---

## Источники

- `docs/operations/etcd.md`
- Тег: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0 (commit `1c9add4`)

Связанные заметки: [[versions/v2.31.0/variables/etcd|Переменные etcd]], [[versions/v2.31.0/README|Срез v2.31.0]]
