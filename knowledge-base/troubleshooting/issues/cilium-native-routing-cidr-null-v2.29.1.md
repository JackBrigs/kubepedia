---
project: kubespray
kubespray_version: v2.29.1
git_commit: 0c6a295
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/13109
retrieved_at: 2026-07-14
topics:
  - cilium
  - native-routing
  - helm-values
affected_versions:
  - v2.29.1
fixed_versions:
  - v2.31.0
reliability: confirmed
---

# Cilium: пустые `native_routing_cidr` рендерятся как `null` в Helm-values (затрагивает v2.29.1, не исправлено в v2.29.x/v2.30.x)

## Симптом

При включённой нативной маршрутизации Cilium (и, в частности, при настройке Cluster mesh со стеком только IPv4) генерация helm-values ломается из-за значений `null`. Проявляется, когда `cilium_native_routing_cidr` / `cilium_native_routing_cidr_ipv6` не заданы явно.

## Корневая причина

В шаблоне `roles/network_plugin/cilium/templates/values.yaml.j2` ключи `ipv4NativeRoutingCIDR` / `ipv6NativeRoutingCIDR` подставляют переменные **без кавычек**. При пустом строковом значении по умолчанию YAML-ключ получает пустое значение, которое Helm интерпретирует как `null` (а не как пустую строку).

## Проверка по коду тега v2.29.1

Уязвимый код присутствует в теге:

- дефолты — пустые строки: `roles/network_plugin/cilium/defaults/main.yml`
  - строка 93: `cilium_native_routing_cidr: ""`
  - строка 96: `cilium_native_routing_cidr_ipv6: ""`
- незакавыченные подстановки — `roles/network_plugin/cilium/templates/values.yaml.j2`:
  - строка 62: `ipv4NativeRoutingCIDR: {{ cilium_native_routing_cidr }}`
  - строка 63: `ipv6NativeRoutingCIDR: {{ cilium_native_routing_cidr_ipv6 }}`

При дефолтных (пустых) значениях строки рендерятся как `ipv4NativeRoutingCIDR:` → `null` в Helm.

## Решение

PR [#13109](https://github.com/kubernetes-sigs/kubespray/pull/13109) закавычивает обе подстановки:

```diff
-ipv4NativeRoutingCIDR: {{ cilium_native_routing_cidr }}
-ipv6NativeRoutingCIDR: {{ cilium_native_routing_cidr_ipv6 }}
+ipv4NativeRoutingCIDR: "{{ cilium_native_routing_cidr }}"
+ipv6NativeRoutingCIDR: "{{ cilium_native_routing_cidr_ipv6 }}"
```

Issue: [#13089](https://github.com/kubernetes-sigs/kubespray/issues/13089) (метка `triage/accepted`).

**Обходной путь на v2.29.1:** явно задавать `cilium_native_routing_cidr` (и `cilium_native_routing_cidr_ipv6` для IPv6) корректным CIDR при использовании нативной маршрутизации.

## Версии

- **Затронуто:** v2.29.1 (уязвимый код подтверждён в теге; проблема сохраняется и в v2.30.x).
- **Исправлено:** только в master → **v2.31.0**. **Бэкпорта в release-2.29 / release-2.30 нет** — в v2.29.x и v2.30.x проблема НЕ устранена; используйте обходной путь.

## Связанное

[[versions/v2.29.1/variables/cni|Переменные CNI (cilium_native_routing_cidr)]] · [[versions/v2.29.1/docs/cni|Дайджест: CNI/Cilium]]
