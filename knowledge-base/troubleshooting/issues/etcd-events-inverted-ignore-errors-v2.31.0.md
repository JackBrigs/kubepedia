---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/13343
retrieved_at: 2026-07-15
topics:
  - etcd
  - scale
  - control-plane
affected_versions:
  - v2.29.1
  - v2.30.0
  - v2.31.0
fixed_versions: []
reliability: confirmed
---

# etcd-events: инвертированное условие `ignore_errors` при запуске сервиса — ложные сбои (затрагивает все три версии)

## Симптом

Ложные сбои (false failures) плейбука при добавлении/масштабировании control-plane узлов, когда включён `etcd_events_cluster_setup: true`. Запуск сервиса `etcd-events` завершается ошибкой, хотя кластера etcd-events здоров.

## Корневая причина

В `roles/etcd/tasks/configure.yml` условие `ignore_errors` для запуска сервиса etcd-events задано **инвертированно** относительно параллельной задачи для основного etcd:

- основной etcd (корректно): `ignore_errors: "{{ etcd_cluster_is_healthy.rc == 0 }}"` — ошибки игнорируются, когда кластер уже здоров (rc == 0), т.е. «сервис уже запущен» не считается сбоем;
- etcd-events (баг): `ignore_errors: "{{ etcd_events_cluster_is_healthy.rc != 0 }}"` — использует `!= 0`, поэтому при здоровом кластере (rc == 0) ошибки НЕ игнорируются и безобидный сбой запуска всплывает как реальная ошибка.

## Проверка по коду тегов

Строка присутствует во всех трёх индексированных версиях (`git grep`):

- `v2.29.1:roles/etcd/tasks/configure.yml:96`
- `v2.30.0:roles/etcd/tasks/configure.yml:96`
- `v2.31.0:roles/etcd/tasks/configure.yml` (строка 96 в рабочем дереве тега)

Во всех: `ignore_errors: "{{ etcd_events_cluster_is_healthy.rc != 0 }}"` (рядом строка 85 для основного etcd — с корректным `== 0`).

## Решение

PR [#13343](https://github.com/kubernetes-sigs/kubespray/pull/13343) «Fix inverted ignore_errors condition for etcd-events service startup» (commit `63bdde2ad`, merged 2026-07-07, Issue #13342) меняет условие на `== 0`. Дефект внесён давно (коммит `7516fe1`, 2021) и присутствует во всех индексированных версиях.

**Статус фикса:** влит только в `master` **после** тега v2.31.0 — ни в один выпущенный релиз (включая v2.31.0) пока не входит. Проверено: коммит `63bdde2ad` не является предком v2.31.0.

**Обходной путь:** при масштабировании control-plane с `etcd_events_cluster_setup: true` игнорировать этот единичный сбой запуска etcd-events, если кластер etcd-events фактически здоров (проверить `etcdctl endpoint health` для events-эндпоинтов); либо локально поправить строку 96 на `== 0`.

## Версии

- **Затронуто:** v2.29.1, v2.30.0, v2.31.0 (все индексированные).
- **Исправлено:** пока нет выпущенного релиза с фиксом (в `master`, войдёт в следующий тег после v2.31.0).

## Связанное

[[versions/v2.31.0/variables/etcd|Переменные etcd (etcd_events_cluster_setup)]] · [[versions/v2.31.0/docs/nodes|Дайджест: узлы/масштабирование]]
