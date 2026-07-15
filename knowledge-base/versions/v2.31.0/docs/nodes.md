---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: docs
source_paths:
  - docs/operations/nodes.md
  - docs/operations/recover-control-plane.md
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0
retrieved_at: 2026-07-14
topics:
  - nodes
  - scale
  - recovery
reliability: authoritative
---

# Добавление, удаление и восстановление узлов в Kubespray v2.31.0

Дайджест документации `docs/` тега v2.31.0: работа с worker/control-plane/etcd узлами и восстановление control plane. Связанные заметки: [[versions/v2.31.0/ansible-tags|Ansible-теги]], [[versions/v2.31.0/variables/k8s-cluster|Переменные ядра]], [[versions/v2.31.0/README|Срез v2.31.0]].

## Добавление/замена worker-узла (docs/operations/nodes.md)

1. Добавить узел в inventory (в нужную группу).
2. Запустить `scale.yml`. Можно ограничить через `--limit=NODE_NAME`, чтобы не трогать остальные узлы. **Перед `--limit` прогнать `facts.yml` без limit** для обновления кэша фактов всех узлов.
3. Удалить старый узел через `remove-node.yml` (узел ещё в inventory), передав `-e node=NODE_NAME`. Если узел офлайн — добавить `reset_nodes=false` и `allow_ungraceful_removal=true` (флаг используется и для control plane / etcd узлов).
4. Удалить узел из inventory.

## Добавление/замена control-plane узла

1. Дописать новый хост в inventory и запустить `cluster.yml` (**не** `scale.yml`). Новые control plane узлы всегда добавлять **в конец** группы `kube_control_plane` — добавление в первую позицию не поддерживается и приведёт к падению плейбука.
2. Перезапустить `kube-system/nginx-proxy` на всех хостах (локальный прокси к apiserver; Kubespray обновляет его статический конфиг, но нужен рестарт для перечитывания):

```sh
# docker
docker ps | grep k8s_nginx-proxy_nginx-proxy | awk '{print $1}' | xargs docker restart
# containerd
crictl ps | grep nginx-proxy | awk '{print $1}' | xargs crictl stop
```

3. Удалить старые control plane узлы через `remove-node.yml -e node=NODE_NAME` (при офлайне — `reset_nodes=false`, `allow_ungraceful_removal=true`).

## Удаление первого kube_control_plane / etcd-master

Первый узел в списках `kube_control_plane` и etcd-master удалить напрямую нельзя. Порядок:

1. Изменить порядок control plane — переставить первую запись на любую другую позицию (во всех группах: `kube_control_plane`, `kube_node`, `etcd`).
2. Запустить `upgrade-cluster.yml` или `cluster.yml`.
3. Удалить старый первый узел: `remove-node.yml -e node=node-1` (при офлайне — `reset_nodes=false`, `allow_ungraceful_removal=true`).
4. Отредактировать configmap cluster-info в namespace kube-public: `kubectl edit cm -n kube-public cluster-info` — заменить IP старого узла в поле `server` на IP живого узла; при смене сертификатов обновить `certificate-authority-data`.
5. Добавить новый control plane узел: обновить inventory, запустить `cluster.yml --limit=kube_control_plane`.

## Добавление etcd-узла

Число etcd-узлов должно быть **нечётным** — операция всегда «замена» или «scale up» (добавлять два узла или убирать один).

1. Обновить inventory, запустить `cluster.yml --limit=etcd,kube_control_plane -e ignore_assert_errors=yes`. Если узел уже worker/control plane — сначала удалить его через `remove-node.yml`. Затем запустить `upgrade-cluster.yml` с теми же `--limit=etcd,kube_control_plane -e ignore_assert_errors=yes` (обновляет всю etcd-конфигурацию). При добавлении нескольких etcd-узлов за раз — `-e etcd_retries=10` (по умолчанию первого join может не хватить, `etcd_retries=10` подходит для 3 новых узлов).
   На этом этапе будет чётное число узлов — работает, проблема лишь если etcd выберет нового лидера до удаления узла.
2. На каждом control plane отредактировать `/etc/kubernetes/manifests/kube-apiserver.yaml` — новые etcd-узлы должны быть в параметре `--etcd-servers=...`.

## Удаление etcd-узла

1. `remove-node.yml -e node=NODE_NAME` (узел ещё в inventory; при офлайне — `reset_nodes=false`, `allow_ungraceful_removal=true`).
2. Убрать `NODE_NAME` из inventory.
3. `cluster.yml` — регенерирует конфигурацию (kubernetes + сеть) на всех оставшихся узлах с корректным списком etcd-членов.
4. На каждом control plane убрать старый etcd-узел из `--etcd-servers=...` в `/etc/kubernetes/manifests/kube-apiserver.yaml`.
5. Выключить старый инстанс.

## Восстановление control plane (docs/operations/recover-control-plane.md)

Плейбук `recover-control-plane.yml`. Применяется при: аппаратном сбое узлов, падении узлов при патчинге/апгрейде, повреждении БД etcd, деградации control plane. **Нужен минимум один рабочий узел.**

Runbook:
- Сделать бэкапы, чем возможно.
- Заменить сломанные узлы новыми.
- Сломанные etcd-узлы поместить в группу `broken_etcd` (обязательно задать переменную `etcd_member_name`).
- Сломанные control plane узлы — в группу `broken_kube_control_plane`.
- Выживших разместить **первыми** в группах `etcd` и `kube_control_plane`, новые узлы — **ниже** выживших.

Запуск с `--limit etcd,kube_control_plane` и увеличенным числом retries: `-e etcd_retries=10` (или больше; точное число предсказать сложно).

### Восстановление при потере кворума

Плейбук пытается определить целостность кворума etcd. При потере кворума — берёт снапшот с первого узла в группе `etcd` и восстанавливает из него. Для восстановления из альтернативного снапшота задать путь: `-e etcd_snapshot=/tmp/etcd_snapshot`.

### Оговорки

- Плейбук тестировался лишь на небольших БД etcd.
- Возможны перебои во время работы плейбука.
- Гарантий нет. Рекомендуется предварительно воспроизвести поломку на тестовом кластере тем же способом, что и на целевом.

## Источники

- docs/operations/nodes.md
- docs/operations/recover-control-plane.md
- [[versions/v2.31.0/README|Срез v2.31.0]]
