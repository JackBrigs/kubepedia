---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/13109
retrieved_at: 2026-07-14
topics:
  - cilium
  - native-routing
  - helm-values
affected_versions:
  - v2.29.1
  - v2.30.0
fixed_versions:
  - v2.31.0
reliability: confirmed
---

# Cilium: пустые `native_routing_cidr` рендерятся как `null` в Helm-values (затрагивает v2.30.0)

## Симптом

При включённой нативной маршрутизации Cilium (в частности, Cluster mesh со стеком только IPv4) генерация helm-values ломается из-за значений `null`, когда `cilium_native_routing_cidr` / `cilium_native_routing_cidr_ipv6` не заданы явно.

## Корневая причина

В шаблоне `roles/network_plugin/cilium/templates/values.yaml.j2` ключи `ipv4NativeRoutingCIDR` / `ipv6NativeRoutingCIDR` подставляют переменные без кавычек. При пустом строковом значении по умолчанию Helm интерпретирует ключ как `null`.

## Проверка по коду тега v2.30.0

`roles/network_plugin/cilium/templates/values.yaml.j2`:
- строка 65: `ipv4NativeRoutingCIDR: {{ cilium_native_routing_cidr }}` (без кавычек);
- строка 66: `ipv6NativeRoutingCIDR: {{ cilium_native_routing_cidr_ipv6 }}` (без кавычек).

Дефолты обеих переменных — пустые строки (defaults роли Cilium). v2.30.0 затронут так же, как v2.29.1.

## Решение

PR [#13109](https://github.com/kubernetes-sigs/kubespray/pull/13109) закавычивает обе подстановки — влит только в master → **v2.31.0**. **Бэкпорта в release-2.29 / release-2.30 нет.** Issue [#13089](https://github.com/kubernetes-sigs/kubespray/issues/13089) (`triage/accepted`).

**Обходной путь на v2.30.0:** явно задавать `cilium_native_routing_cidr` (и `_ipv6` для IPv6) корректным CIDR при нативной маршрутизации.

## Версии

- **Затронуто:** v2.29.1, **v2.30.0** (уязвимый код подтверждён в теге).
- **Исправлено:** только v2.31.0. В v2.29.x и v2.30.x НЕ исправлено — используйте обходной путь.

## Связанное

[[versions/v2.30.0/variables/cni|Переменные CNI (cilium_native_routing_cidr)]] · [[versions/v2.30.0/docs/cni|Дайджест: CNI/Cilium]]
