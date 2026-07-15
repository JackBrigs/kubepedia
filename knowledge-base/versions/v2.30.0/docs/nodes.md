---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: docs
source_paths:
  - docs/operations/nodes.md
  - docs/operations/recover-control-plane.md
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0
retrieved_at: 2026-07-14
topics:
  - nodes
  - scale
  - recovery
reliability: authoritative
---

# Управление узлами и восстановление control plane в v2.30.0

Дайджест по добавлению, удалению, замене узлов и восстановлению control plane / etcd. Источники — только `docs/` тега `v2.30.0` (commit `f4ccdb5`).

## Добавление/замена worker-узла

Самый простой сценарий:

1. Добавить новый узел в инвентарь.
2. Запустить `scale.yml`. Можно использовать `--limit=NODE_NAME`, чтобы не трогать остальные узлы. Перед использованием `--limit` запустить `facts.yml` **без** limit для обновления кэша фактов на всех узлах.
3. Удалить старый узел через `remove-node.yml`: старый узел ещё в инвентаре, запуск с `-e node=NODE_NAME`. Если узел **не в сети** — добавить `-e reset_nodes=false -e allow_ungraceful_removal=true`. Эти флаги используются и для других типов узлов (control plane, etcd).
4. Удалить узел из инвентаря.

## Добавление/замена control plane узла

1. **Запустить `cluster.yml`** (НЕ `scale.yml`). Новый хост добавляется в инвентарь.
   - Важно: новые control plane узлы всегда добавляются в **конец** группы `kube_control_plane`. Добавление на первую позицию не поддерживается и приведёт к падению playbook.
2. Перезапустить под `kube-system/nginx-proxy` на всех хостах (локальный прокси для apiserver; Kubespray обновляет его статический конфиг, но нужен перезапуск для перечитывания):
   - Docker: `docker ps | grep k8s_nginx-proxy_nginx-proxy | awk '{print $1}' | xargs docker restart`
   - containerd: `crictl ps | grep nginx-proxy | awk '{print $1}' | xargs crictl stop`
3. Удалить старый control plane узел через `remove-node.yml` с `-e node=NODE_NAME` (старый узел ещё в инвентаре). Если узел не в сети — `-e reset_nodes=false -e allow_ungraceful_removal=true`.

## Добавление/удаление первого `kube_control_plane` и etcd-master

Нельзя удалить **первый** узел в списках `kube_control_plane` и etcd-master напрямую. Чтобы всё же удалить его:

1. Изменить порядок control plane: переместить первую запись на любую другую позицию (одинаково в группах `kube_control_plane`, `kube_node`, `etcd`).
2. Обновить кластер: запустить `upgrade-cluster.yml` или `cluster.yml`.
3. Удалить старый первый control plane узел: `remove-node.yml` с `-e node=node-1` (узел ещё в инвентаре). Если не в сети — `-e reset_nodes=false -e allow_ungraceful_removal=true`.
4. Отредактировать configmap `cluster-info` в namespace `kube-public`: `kubectl edit cm -n kube-public cluster-info` — заменить IP старого control plane узла на IP живого (поле `server`), при смене сертификатов обновить `certificate-authority-data`.
5. Добавить новый control plane узел: обновить инвентарь и запустить `cluster.yml` с `--limit=kube_control_plane`.

## Добавление etcd-узла

В кластере всегда должно быть **нечётное** число etcd-узлов, поэтому это всегда замена или scale up (добавить два узла либо удалить один).

1. Добавить новый узел через `cluster.yml`: обновить инвентарь и запустить с `--limit=etcd,kube_control_plane -e ignore_assert_errors=yes`. Если узел уже является worker или control plane узлом — сначала удалить его через `remove-node.yml`. Затем запустить `upgrade-cluster.yml` тоже с `--limit=etcd,kube_control_plane -e ignore_assert_errors=yes` (нужно для обновления всей etcd-конфигурации в кластере).
   - На этом этапе число узлов станет чётным; работа продолжается, проблемы возможны только если кластер решит переизбрать etcd-лидера до удаления узла.
   - При добавлении нескольких etcd-узлов за один запуск можно добавить `-e etcd_retries=10` для увеличения числа повторов при join каждого узла (иначе etcd-кластер может ещё обрабатывать первый join и упасть на последующих). `etcd_retries=10` подходит для join 3 новых узлов.
2. Добавить новый узел в конфиг apiserver: на каждом control plane узле отредактировать `/etc/kubernetes/manifests/kube-apiserver.yaml`, убедиться, что новые etcd-узлы присутствуют в параметре `--etcd-servers=...`.

Переменные etcd см. [[versions/v2.30.0/variables/etcd|Переменные etcd]].

## Удаление etcd-узла

1. Удалить старый etcd-узел: `remove-node.yml` с `-e node=NODE_NAME` (узел ещё в инвентаре). Если не в сети — `-e reset_nodes=false -e allow_ungraceful_removal=true`.
2. Убедиться, что в инвентаре остались только оставшиеся узлы (удалить `NODE_NAME` из файла инвентаря).
3. Обновить конфиги Kubernetes и сети валидным списком etcd-членов: запустить `cluster.yml` для регенерации конфигов на всех оставшихся узлах.
4. Удалить старый etcd-узел из конфига apiserver: на каждом control plane узле в `/etc/kubernetes/manifests/kube-apiserver.yaml` оставить в `--etcd-servers=...` только активные etcd-узлы.
5. Выключить старый инстанс.

## Восстановление control plane

Для восстановления сломанных узлов control plane используется playbook `recover-control-plane.yml`.

Что означает «сломан»:
- один или несколько bare metal узлов с неустранимым аппаратным отказом;
- отказ узлов при патчинге/обновлении;
- повреждение базы данных etcd;
- прочие отказы, оставляющие control plane в деградированном/нерабочем состоянии.

Важно: для восстановления этим методом нужен **хотя бы один рабочий узел**.

### Runbook

- Сделать бэкап всего, что возможно.
- Подготовить новые узлы на замену сломанным.
- Скопировать сломанные etcd-узлы в группу `broken_etcd`, убедиться, что задана переменная `etcd_member_name`.
- Скопировать сломанные control plane узлы в группу `broken_kube_control_plane`.
- Разместить выжившие узлы control plane **первыми** в группах `etcd` и `kube_control_plane`.
- Разместить новые узлы **ниже** выживших в группах `etcd` и `kube_control_plane`.

Затем запустить playbook с `--limit etcd,kube_control_plane` и увеличить число повторов ETCD через `-e etcd_retries=10` (или больше; нужное число повторов трудно предсказать). По завершении control plane снова полностью работоспособен.

### Восстановление при потере кворума

Playbook пытается определить, сохранён ли кворум etcd. Если кворум потерян — он берёт снапшот с **первого** узла группы `etcd` и восстанавливает из него. Для восстановления из альтернативного снапшота задать путь в переменной `etcd_snapshot`:

```
-e etcd_snapshot=/tmp/etcd_snapshot
```

### Предостережения

- Playbook тестировался только на относительно небольших базах etcd.
- Во время работы playbook возможны перебои.
- Гарантий абсолютно никаких нет.

По возможности воспроизведите поломку кластера тем же способом на тестовом кластере и отработайте восстановление до применения на реальном.

## Источники

- `docs/operations/nodes.md`
- `docs/operations/recover-control-plane.md`
- [[versions/v2.30.0/README|Срез v2.30.0]]
