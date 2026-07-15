---
project: kubespray
kubespray_version: v2.27.0
git_commit: 9ec9b3a
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/12314
retrieved_at: 2026-07-15
topics:
  - offline
  - download
  - registry
affected_versions:
  - v2.27.0
  - v2.28.0
fixed_versions:
  - v2.27.1
  - v2.28.1
  - v2.29.0
reliability: confirmed
---

# Offline: `manage-offline-container-images.sh register` падает при получении image_id (Podman) (исправлено в v2.27.1)

## Симптом

При offline-развёртывании запуск `contrib/offline/manage-offline-container-images.sh register`
с рантаймом **Podman** прерывался: не удавалось получить `image_id`, скрипт завершался с ошибкой
«Failed to get image_id for file ...». С Docker парсинг мог работать, с Podman — нет.

## Корневая причина

`image_id` извлекался текстовым парсингом JSON-вывода `image inspect` через
`grep "\"Id\":" | awk -F: '{print $3}' | sed ...`. Формат вывода Podman отличается от Docker,
поэтому такой хрупкий парсинг возвращал пустую строку.

## Проверка по коду тегов

Уязвимая строка присутствует в `contrib/offline/manage-offline-container-images.sh`:

- `v2.27.0:contrib/offline/manage-offline-container-images.sh:149`
- `v2.28.0:contrib/offline/manage-offline-container-images.sh:151`

```sh
image_id=$(sudo ${runtime} image inspect ${org_image} | grep "\"Id\":" | awk -F: '{print $3}'| sed s/'\",'//)
```

В исправленных тегах (v2.27.1, v2.28.1, v2.29.0) строка заменена на использование
`--format`:

```sh
image_id=$(sudo ${runtime} image inspect --format "{{.Id}}" "${org_image}")
```

## Решение

PR [#12314](https://github.com/kubernetes-sigs/kubespray/pull/12314) «fix
manage-offline-container-images.sh get image_id» (commit `266117d17`) — бэкпорт в release-2.27,
вошёл в v2.27.1. Аналогичный бэкпорт в release-2.28 (PR #12316) вошёл в v2.28.1; в v2.29.0
исправление присутствует из master.

**Обходной путь** на затронутых версиях: локально заменить строку получения `image_id` на
`image inspect --format "{{.Id}}"`, либо выполнять `register` под Docker.

## Версии

- **Затронуто:** v2.27.0 и v2.28.0 (баг подтверждён по коду обоих тегов).
- **Исправлено:** v2.27.1 (#12314), v2.28.1 (#12316), v2.29.0 (master).

## Связанное

[[versions/v2.27.0/docs/offline|Дайджест: offline-развёртывание]] · [[versions/v2.28.0/docs/offline|Дайджест: offline (v2.28.0)]]
