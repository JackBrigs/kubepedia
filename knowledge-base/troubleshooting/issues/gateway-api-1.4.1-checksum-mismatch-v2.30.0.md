---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/13006
retrieved_at: 2026-07-14
topics:
  - gateway-api
  - download
  - upgrade
affected_versions:
  - v2.30.0
fixed_versions:
  - v2.31.0
reliability: confirmed
---

# Gateway API v1.4.1: сбой загрузки из-за неверной контрольной суммы (затрагивает v2.30.0)

## Симптом

При `gateway_api_enabled: true` установка или обновление до v2.30.0 падает на этапе `download`: контрольная сумма манифеста `standard-install.yaml` Gateway API v1.4.1 не совпадает — Kubespray ожидает `sha256:daa2999…`, а фактически скачивается артефакт с другим хешем (`73b91b7…`).

## Корневая причина

Upstream-артефакт релиза Gateway API v1.4.1 был перезаписан **после** среза тега v2.30.0, из-за чего зашитая в Kubespray контрольная сумма стала невалидной.

## Проверка по коду тега v2.30.0

- `roles/kubespray_defaults/defaults/main/download.yml:145` — `gateway_api_version` разрешается в **1.4.1** (первый ключ `gateway_api_standard_crds_checksums.no_arch`).
- `roles/kubespray_defaults/vars/main/checksums.yml:1390` — `1.4.1: sha256:daa2999f0978ba3e43b65fec179f82a1a690649da10aa5c7c5871165477368f8` (тот самый ожидаемый хеш, который перестал совпадать).

## Решение

PR [#13006](https://github.com/kubernetes-sigs/kubespray/pull/13006) «Fix Gateway API v1.4.1 unexpected checksum change» (master → v2.31.0), бэкпорт в ветку release-2.30 — PR [#13010](https://github.com/kubernetes-sigs/kubespray/pull/13010). Issue [#13122](https://github.com/kubernetes-sigs/kubespray/issues/13122).

**Обходной путь на v2.30.0:** закрепить в inventory `gateway_api_version: "1.4.0"` (артефакт 1.4.0 не затронут), либо отключить `gateway_api_enabled`.

## Версии

- **Затронуто:** v2.30.0 (при `gateway_api_enabled: true`).
- **Исправлено:** v2.31.0 (master). Бэкпорт влит в ветку release-2.30 (войдёт в будущий v2.30.1 — на момент составления записи тег v2.30.1 не выпущен).

## Связанное

[[versions/v2.30.0/variables/addons|Переменные аддонов (gateway_api)]] · [[versions/v2.30.0/docs/offline|Дайджест: offline/зеркала]]
