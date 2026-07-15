---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/12949
retrieved_at: 2026-07-14
topics:
  - etcd
  - remove-node
  - idempotency
affected_versions:
  - v2.29.0
  - v2.29.1
  - v2.30.0
fixed_versions:
  - v2.29.2
  - v2.30.1
reliability: confirmed
---

# etcd: `remove-node.yml` не идемпотентен — падает, если член etcd уже удалён (затрагивает v2.30.0)

## Симптом

Повторный или «после факта» запуск удаления узла завершается ошибкой шаблонизации (undefined), когда соответствующего члена уже нет в кластере etcd. Падает на вычислении ID члена через `selectattr('peerURLs.0','==',etcd_peer_url))[0].ID` — при пустом результате `selectattr` обращение `[0]` даёт undefined.

## Корневая причина

Задача «Remove member from cluster» (`roles/remove-node/remove-etcd-node/tasks/main.yml`) не проверяет наличие члена в кластере перед вычислением ID и вызовом `etcdctl member remove`. Защитного условия `when` нет.

## Проверка по коду тега v2.30.0

`roles/remove-node/remove-etcd-node/tasks/main.yml:24` содержит выражение `selectattr('peerURLs.0', '==', etcd_peer_url))[0].ID` без охранного `when`. Код идентичен уязвимому в v2.29.1 — v2.30.0 затронут.

## Решение

PR [#12949](https://github.com/kubernetes-sigs/kubespray/pull/12949) (master, «Fixes #12947»), бэкпорт release-2.29 [#12960](https://github.com/kubernetes-sigs/kubespray/pull/12960). Бэкпорт влит 2026-02-05 — **после** тега v2.30.0 (2026-01-30), поэтому в v2.30.0 фикса нет; войдёт в v2.30.1. Issue [#12947](https://github.com/kubernetes-sigs/kubespray/issues/12947).

**Обходной путь на v2.30.0:** не запускать удаление повторно для уже удалённого узла; проверять наличие `etcd_peer_url` в выводе `etcdctl member list` перед запуском.

## Версии

- **Затронуто:** v2.29.0, v2.29.1, **v2.30.0**.
- **Исправлено:** v2.29.2 и v2.30.1 (бэкпорты после тега v2.30.0). В v2.30.0 не исправлено.

## Связанное

[[versions/v2.30.0/docs/nodes|Дайджест: узлы]] · [[versions/v2.30.0/variables/etcd|Переменные etcd]]
