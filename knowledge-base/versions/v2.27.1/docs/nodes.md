---
project: kubespray
kubespray_version: v2.27.1
git_commit: 45140b5
source_type: docs
source_paths: [docs/operations/nodes.md, docs/operations/recover-control-plane.md]
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.27.1
retrieved_at: 2026-07-15
topics: [nodes, scale, recovery]
reliability: authoritative
---

# Управление узлами и восстановление control plane в v2.27.1

Дайджест построен строго по документации тега `v2.27.1` (commit `45140b5`): `docs/operations/nodes.md` и `docs/operations/recover-control-plane.md`. Выжимка, не дословный перевод; имена плейбуков, переменных и команд приведены точно.

## Ключевые переменные и плейбуки

- Плейбуки: `scale.yml` (добавление worker), `cluster.yml` (добавление control plane / etcd, перегенерация конфигов), `upgrade-cluster.yml`, `remove-node.yml` (удаление), `facts.yml` (обновление кэша фактов), `recover-control-plane.yml` (восстановление).
- Переменные удаления/восстановления:
  - `-e node=NODE_NAME` — ограничить выполнение удаляемым узлом (обязательна для `remove-node.yml`).
  - `-e reset_nodes=false` — не выполнять reset на узле (когда узел offline).
  - `-e allow_ungraceful_removal=true` — разрешить «жёсткое» удаление недоступного узла.
  - `-e ignore_assert_errors=yes` — игнорировать ошибки assert (при работах с etcd).
  - `-e etcd_retries=10` — увеличить число повторов при join etcd-узлов.
  - `-e etcd_snapshot=/tmp/etcd_snapshot` — путь к снапшоту для восстановления из потери кворума.

## Добавление / замена worker-узла

Самый простой сценарий:

1. Добавить новый узел в инвентарь.
2. Запустить `scale.yml`. Можно ограничить `--limit=NODE_NAME`, чтобы не трогать остальные узлы. **Перед** `--limit` прогнать `facts.yml` без limit для обновления кэша фактов по всем узлам.
3. Удалить старый узел через `remove-node.yml` (старый узел ещё в инвентаре), передав `-e node=NODE_NAME`. Если удаляемый узел offline — добавить `-e reset_nodes=false -e allow_ungraceful_removal=true`. Эти флаги применяются и для узлов других типов (control plane, etcd).
4. Убрать узел из инвентаря.

## Добавление / замена control plane узла

1. Дописать новый хост в инвентарь и запустить **`cluster.yml`** (использовать `scale.yml` для control plane **нельзя**).
2. На **всех** хостах перезапустить под `kube-system/nginx-proxy` (локальный прокси к apiserver): Kubespray обновляет его статический конфиг, но под нужно перезапустить для перечитывания:

   ```sh
   # docker
   docker ps | grep k8s_nginx-proxy_nginx-proxy | awk '{print $1}' | xargs docker restart
   # containerd
   crictl ps | grep nginx-proxy | awk '{print $1}' | xargs crictl stop
   ```

3. Удалить старые control plane узлы через `remove-node.yml` с `-e node=NODE_NAME` (offline — добавить `reset_nodes=false` и `allow_ungraceful_removal=true`).

## Удаление / замена ПЕРВОГО `kube_control_plane` и etcd-master

Первый узел в списках `kube_control_plane` и etcd-master **напрямую удалить нельзя**. Порядок действий:

1. Изменить порядок control plane: перенести первую запись на любую другую позицию (в группах `kube_control_plane`, `kube_node`, `etcd` инвентаря переставить `node-1` в конец).
2. Запустить `upgrade-cluster.yml` или `cluster.yml`.
3. Удалить старый первый control plane через `remove-node.yml` с `-e node=node-1` (offline — `reset_nodes=false`, `allow_ungraceful_removal=true`).
4. Отредактировать configmap `cluster-info` в namespace `kube-public`: `kubectl edit cm -n kube-public cluster-info` — заменить IP старого узла на IP живого control plane (поле `server`); при смене сертификатов обновить `certificate-authority-data`.
5. Добавить новый control plane: обновить инвентарь и запустить `cluster.yml` с `--limit=kube_control_plane`.

## Добавление etcd-узла

Число etcd-узлов должно быть **нечётным**, поэтому это всегда замена или scale up (добавить два узла или убрать один).

1. Обновить инвентарь и запустить `cluster.yml` с `--limit=etcd,kube_control_plane -e ignore_assert_errors=yes`. Если узел уже worker/control plane — сначала удалить его через `remove-node.yml`. Затем запустить `upgrade-cluster.yml` тоже с `--limit=etcd,kube_control_plane -e ignore_assert_errors=yes` — это нужно, чтобы обновить всю конфигурацию etcd в кластере.
   - На этом этапе число узлов чётное; кластер работает, проблема возможна только если etcd выберет нового лидера до удаления узла.
   - При добавлении нескольких etcd-узлов за один прогон добавить `-e etcd_retries=10`, иначе etcd-кластер может ещё обрабатывать первый join и упасть на последующих. `etcd_retries=10` может хватить для 3 новых узлов.
2. На каждом control plane узле отредактировать `/etc/kubernetes/manifests/kube-apiserver.yaml` — убедиться, что новые etcd-узлы есть в параметре `--etcd-servers=...`.

## Удаление etcd-узла

1. Запустить `remove-node.yml` с `-e node=NODE_NAME` (узел ещё в инвентаре; offline — `reset_nodes=false`, `allow_ungraceful_removal=true`).
2. Убрать `NODE_NAME` из инвентаря.
3. Запустить `cluster.yml` для перегенерации конфигурационных файлов на всех оставшихся узлах (валидный список etcd-членов).
4. На каждом control plane узле отредактировать `/etc/kubernetes/manifests/kube-apiserver.yaml` — оставить в `--etcd-servers=...` только активные etcd-узлы.
5. Выключить старый инстанс.

## Восстановление control plane

Плейбук `recover-control-plane.yml`. Что считается «сломанным»: неустранимый аппаратный сбой узлов, отказ узлов при патче/обновлении, повреждение базы etcd, прочие сбои, оставившие control plane деградированным/нерабочим.

> **Важно:** нужен минимум один рабочий узел, чтобы восстановиться этим методом.

Runbook:

1. Сделать бэкапы всего, что возможно.
2. Подготовить новые узлы взамен сломанных.
3. Сломанные etcd-узлы поместить в группу `broken_etcd`; убедиться, что задана переменная `etcd_member_name`.
4. Сломанные control plane узлы поместить в группу `broken_kube_control_plane`.
5. Выживших членов control plane поставить **первыми** в группах `etcd` и `kube_control_plane`.
6. Новые узлы добавить **ниже** выживших в группах `etcd` и `kube_control_plane`.

Запуск: `ansible-playbook recover-control-plane.yml --limit etcd,kube_control_plane -e etcd_retries=10` (или больше — точное число повторов предсказать трудно). После завершения control plane должен снова полностью работать.

### Восстановление после потери кворума

- Плейбук пытается определить, цел ли кворум etcd. Если кворум потерян — берёт снапшот с первого узла группы `etcd` и восстанавливает из него.
- Для восстановления из альтернативного снапшота задать путь: `-e etcd_snapshot=/tmp/etcd_snapshot`.

### Оговорки (caveats)

- Плейбук тестировался только на сравнительно небольших базах etcd.
- Во время работы плейбука возможны перебои.
- Гарантий никаких. Рекомендуется сначала воспроизвести аналогичную поломку на тестовом кластере и отработать восстановление на нём.

Связанные срезы: [[versions/v2.27.1/ansible-tags|Ansible-теги запуска v2.27.1]] (reset, pre-remove, post-remove), [[versions/v2.27.1/variables/etcd|Переменные etcd v2.27.1]].

## Источники

- `docs/operations/nodes.md` (тег v2.27.1)
- `docs/operations/recover-control-plane.md` (тег v2.27.1)
- Ссылки в документе: issue #3471
- [[versions/v2.27.1/README|Срез v2.27.1]]
