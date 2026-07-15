---
project: kubespray
kubespray_version: v2.28.0
git_commit: 63cdf87
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/12342
retrieved_at: 2026-07-15
topics:
  - etcd
  - scale
  - nodes
affected_versions:
  - v2.28.0
fixed_versions:
  - v2.28.1
  - v2.29.0
reliability: confirmed
---

# etcd: некорректный `ETCD_INITIAL_CLUSTER` (лишние кавычки в URL) ломал добавление члена etcd (исправлено в v2.28.1)

## Симптом

Добавление нового узла etcd (scale) завершалось ошибкой: член etcd не поднимался из-за
неверного значения `ETCD_INITIAL_CLUSTER` в `etcd.env` / `etcd-events.env`. Каждый peer-URL
в списке оказывался обёрнут в двойные кавычки.

## Корневая причина

В `roles/etcd/tasks/join_etcd_member.yml` и `join_etcd-events_member.yml` при формировании
`etcd_peer_addresses` peer-URL подставлялся в кавычках:
`etcdN="https://host:2380",` — кавычки попадали прямо в значение `ETCD_INITIAL_CLUSTER`,
которое etcd не мог распарсить. Дефект внесён рефакторингом (переход на `main_ip` + `ipwrap`)
между v2.27.1 и v2.28.0.

## Проверка по коду тегов

- **v2.28.0 (баг), `roles/etcd/tasks/join_etcd_member.yml`:**
  ```jinja
  {{ "etcd" + loop.index | string }}="https://{{ ... | ansible.utils.ipwrap }}:2380",
  ```
- **v2.27.0 / v2.27.1 (без бага):** та же строка **без** кавычек (использовался `ip`/`fallback_ip`), поэтому линии v2.27.x проблема не касается.
- **v2.28.1 / v2.29.0 (исправлено):** кавычки убраны — `etcdN=https://...:2380,`.

## Решение

PR [#12342](https://github.com/kubernetes-sigs/kubespray/pull/12342) «fix
ETCD_INITIAL_CLUSTER config in etcd.env and etcd-events.env» (master, commit `62f49822d`)
убирает кавычки вокруг URL. Бэкпорт в release-2.28 — PR #12352 (commit `4789e9dd8`), вошёл в v2.28.1.

## Версии

- **Затронуто:** только v2.28.0.
- **Исправлено:** v2.28.1 (бэкпорт #12352) и v2.29.0 (master #12342).

## Связанное

[[versions/v2.28.0/variables/etcd|Переменные etcd]] · [[versions/v2.28.0/docs/nodes|Дайджест: узлы/масштабирование]]
