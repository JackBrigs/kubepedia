---
project: kubespray
kubespray_version: v2.29.1
git_commit: 0c6a295
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/12705
retrieved_at: 2026-07-14
topics:
  - cilium
  - loadbalancer
affected_versions:
  - v2.29.0
fixed_versions:
  - v2.29.1
reliability: confirmed
---

# Cilium: параметр `loadBalancer.mode` не применялся (исправлено в v2.29.1)

## Симптом

При установке Cilium через Kubespray заданный режим балансировки (`cilium_loadbalancer_mode`, например `dsr` или `hybrid`) фактически не применялся — Cilium продолжал работать в режиме по умолчанию (`snat`), несмотря на настройку в инвентаре.

## Корневая причина

В шаблоне helm-values Cilium ключ секции был записан как `loadbalancer:` (строчная `b`). Helm-чарт Cilium ожидает camelCase-ключ `loadBalancer:`, поэтому вся секция (включая `mode`) молча игнорировалась.

Файл: `roles/network_plugin/cilium/templates/values.yaml.j2`.

## Решение

Исходный Issue: [#12666](https://github.com/kubernetes-sigs/kubespray/issues/12666). PR [#12705](https://github.com/kubernetes-sigs/kubespray/pull/12705) (cherry-pick исходного #12701 «Fixes #12666», commit `3c0cff983`) исправил ключ на camelCase:

```diff
-loadbalancer:
+loadBalancer:
   mode: {{ cilium_loadbalancer_mode }}
```

## Проверка по коду тега v2.29.1

Исправление присутствует в коде тега: `roles/network_plugin/cilium/templates/values.yaml.j2:30` содержит `loadBalancer:` и на строке 31 — `mode: {{ cilium_loadbalancer_mode }}`. Коммит `3c0cff983` входит в диапазон `v2.29.0..v2.29.1`.

## Версии

- **Затронуто:** v2.29.0.
- **Исправлено:** v2.29.1.
- Пользователям v2.29.0, задающим `cilium_loadbalancer_mode`, следует обновиться до v2.29.1.

## Связанное

[[versions/v2.29.1/variables/cni|Переменные CNI (cilium_loadbalancer_mode)]] · [[versions/v2.29.1/release-notes|Release notes v2.29.1]]
