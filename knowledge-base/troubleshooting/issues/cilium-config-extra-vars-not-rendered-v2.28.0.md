---
project: kubespray
kubespray_version: v2.28.0
git_commit: 63cdf87
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/12335
retrieved_at: 2026-07-15
topics:
  - cilium
  - helm-values
affected_versions:
  - v2.28.0
fixed_versions:
  - v2.28.1
  - v2.29.0
reliability: confirmed
---

# Cilium: `cilium_config_extra_vars` не рендерился в Helm-values (исправлено в v2.28.1)

## Симптом

Заданные пользователем дополнительные параметры Cilium через `cilium_config_extra_vars` не
попадали в итоговый values.yaml — блок `extraConfig` отсутствовал, и настройки молча игнорировались.

## Корневая причина

В `roles/network_plugin/cilium/templates/values.yaml.j2` (после перехода на Cilium CLI в v2.28.0)
не было секции, выводящей `cilium_config_extra_vars` в `extraConfig`.

## Проверка по коду тега v2.28.0

В v2.28.0 шаблон `values.yaml.j2` завершается блоком `envoy:` и не содержит `extraConfig`
(`git grep extraConfig v2.28.0 -- roles/network_plugin/cilium/templates/values.yaml.j2` — нет
совпадений). Блок добавляется коммитом `8cc5897d5` (master).

## Решение

PR [#12335](https://github.com/kubernetes-sigs/kubespray/pull/12335) «fix: add cilium extraConfig
values» (master, commit `8cc5897d5`) добавляет в шаблон:

```jinja
extraConfig:
  {{ cilium_config_extra_vars | to_yaml | indent(2) }}
```

Бэкпорт в release-2.28 — PR #12338 (commit `9a86253be`), вошёл в v2.28.1.

## Версии

- **Затронуто:** v2.28.0.
- **Исправлено:** v2.28.1 (бэкпорт #12338) и v2.29.0 (master #12335).

## Связанное

[[versions/v2.28.0/variables/cni|Переменные CNI (cilium_config_extra_vars)]] · [[versions/v2.28.0/docs/cni|Дайджест: CNI/Cilium]]
