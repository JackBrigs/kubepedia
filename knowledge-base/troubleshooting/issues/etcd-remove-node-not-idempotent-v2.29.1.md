---
project: kubespray
kubespray_version: v2.29.1
git_commit: 0c6a295
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

# etcd: `remove-node.yml` не идемпотентен — падает, если член etcd уже удалён (затрагивает v2.29.1)

## Симптом

Повторный или «после факта» запуск удаления узла (`remove-node.yml`) завершается ошибкой шаблонизации (undefined), когда соответствующего члена уже нет в кластере etcd. Падает на вычислении ID члена:

```
{{ '%x' | format(((etcd_members.stdout | from_json).members
   | selectattr('peerURLs.0', '==', etcd_peer_url))[0].ID) }}
```

Если `etcd_peer_url` отсутствует в списке членов, `selectattr(...)` возвращает пустой список, обращение `[0]` даёт undefined, и задача прерывается.

## Корневая причина

Задача «Remove member from cluster» (`roles/remove-node/remove-etcd-node/tasks/main.yml`) не проверяет, присутствует ли член etcd в кластере, перед вычислением его ID и вызовом `etcdctl member remove`. Нет условия `when`, обрабатывающего случай уже удалённого члена.

## Проверка по коду тега v2.29.1

`roles/remove-node/remove-etcd-node/tasks/main.yml`:
- строка 24 содержит указанное выражение `selectattr('peerURLs.0', '==', etcd_peer_url))[0].ID`;
- у задачи «Remove member from cluster» отсутствует защитное условие `when` на случай отсутствия члена.

Код полностью соответствует описанию Issue [#12947](https://github.com/kubernetes-sigs/kubespray/issues/12947) — v2.29.1 затронут.

## Решение

PR [#12949](https://github.com/kubernetes-sigs/kubespray/pull/12949) (влит в master, «Fixes #12947») делает удаление члена etcd идемпотентным. Бэкпорт в release-2.29 — PR [#12960](https://github.com/kubernetes-sigs/kubespray/pull/12960).

**Обходной путь на v2.29.1:** не запускать удаление повторно для уже удалённого узла; при необходимости удалять членов etcd вручную и убеждаться, что `etcd_peer_url` присутствует в выводе `etcdctl member list` перед запуском.

## Версии

- **Затронуто:** v2.29.0, v2.29.1, v2.30.0.
- **Исправлено:** бэкпорт в release-2.29 (#12960) влит **05.02.2026 — уже ПОСЛЕ** тега v2.29.1 (11.12.2025) и после v2.30.0 (29.01.2026), поэтому в самих v2.29.1 и v2.30.0 исправления НЕТ. Войдёт в будущие патчи **v2.29.2** и **v2.30.1**.

## Связанное

[[versions/v2.29.1/docs/nodes|Дайджест: узлы]] · [[versions/v2.29.1/variables/etcd|Переменные etcd]] · [[versions/v2.29.1/troubleshooting|см. также etcd-remove-external-member (другой баг того же кода)]]
