---
project: kubespray
kubespray_version: v2.28.0
git_commit: 63cdf87
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/12280
retrieved_at: 2026-07-15
topics:
  - cilium
  - helm-values
  - encryption
affected_versions:
  - v2.28.0
fixed_versions:
  - v2.28.1
  - v2.29.0
reliability: confirmed
---

# Cilium: булевы значения и отступы в `values.yaml.j2` ломали установку при включении не-дефолтных функций (исправлено в v2.28.1)

## Симптом

При включении не-дефолтных функций Cilium (например, шифрования — `encryption`) установка
Cilium падала из-за синтаксических ошибок в сгенерированном файле Helm-values. Проблема
появилась после перевода установки Cilium с Jinja-манифестов на **Cilium CLI** (#12101 в v2.28.0).

## Корневая причина

В `roles/network_plugin/cilium/templates/values.yaml.j2` булевы переменные подставлялись
напрямую, из-за чего Python-значения рендерились как `True`/`False` (с заглавной буквы), а не
как валидный YAML/JSON `true`/`false`. Дополнительно отсутствовали `trim_blocks`/`lstrip_blocks`,
из-за чего условные блоки давали неверные отступы. Итоговый values.yaml был невалиден.

## Проверка по коду тега v2.28.0

В v2.28.0 `values.yaml.j2` начинается сразу с `MTU:` (без `#jinja2:`-директивы), а булевы поля
подставляются без фильтра:

```jinja
debug:
  enabled: {{ cilium_debug }}
ipv4:
  enabled: {{ cilium_enable_ipv4 }}
```

## Решение

PR [#12280](https://github.com/kubernetes-sigs/kubespray/pull/12280) «Fix indentation issue in
Cilium values file and ensure booleans are lowercase» (master, commit `d1bd61004`): добавлена
директива `#jinja2: trim_blocks: True, lstrip_blocks: True` и фильтр `| to_json` на булевы поля
(`enabled: {{ cilium_debug | to_json }}` и т.д.). Бэкпорт в release-2.28 — PR #12283
(commit `6ec991e77`), вошёл в v2.28.1.

## Версии

- **Затронуто:** v2.28.0 (после перехода на Cilium CLI).
- **Исправлено:** v2.28.1 (бэкпорт #12283) и v2.29.0 (master #12280).

## Связанное

[[versions/v2.28.0/variables/cni|Переменные CNI (Cilium)]] · [[versions/v2.28.0/docs/cni|Дайджест: CNI/Cilium]]
