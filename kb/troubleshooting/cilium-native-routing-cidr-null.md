---
id: TROUBLE-CILIUM_NATIVE_ROUTING_CIDR_NULL
type: troubleshooting
title: Empty Cilium native_routing_cidr renders as null in Helm values
status: active
kubespray_version: ">=v2.29.1 <=v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - cilium native routing cidr null
tags:
  - cilium
  - native-routing
  - helm-values
sources:
  - type: github_pr
    url: https://github.com/kubernetes-sigs/kubespray/pull/13109
    note: "Merged PR quoting the ipv4/ipv6 NativeRoutingCIDR substitutions"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# Empty Cilium native_routing_cidr renders as null in Helm values

## Summary
With Cilium native routing enabled (in particular an IPv4-only Cluster mesh), helm-values generation breaks on `null` values when `cilium_native_routing_cidr` / `cilium_native_routing_cidr_ipv6` are not set explicitly. The template substitutes the variables unquoted, so an empty default is rendered as `null`. Fixed only in v2.31.0 (no backport to release-2.29 / release-2.30); workaround is to set the CIDR explicitly.

## Problem
With Cilium native routing enabled (notably an IPv4-only-stack Cluster mesh), helm-values generation breaks due to `null` values. It manifests when `cilium_native_routing_cidr` / `cilium_native_routing_cidr_ipv6` are not set explicitly.

## Context
- Affected versions: v2.29.1, v2.30.0 (vulnerable code confirmed in both tags).
- Fixed versions: v2.31.0 only. There is no backport to release-2.29 / release-2.30 — the problem is NOT resolved in v2.29.x and v2.30.x; use the workaround.
- Triggered when native routing is enabled and the CIDR variables are left at their empty-string defaults.

## Diagnostics
- With native routing enabled, inspect the rendered Cilium helm-values for `ipv4NativeRoutingCIDR:` / `ipv6NativeRoutingCIDR:` rendering with no value (interpreted by Helm as `null`).
- Confirm in tag v2.29.1 `roles/network_plugin/cilium/templates/values.yaml.j2`: line 62 `ipv4NativeRoutingCIDR: {{ cilium_native_routing_cidr }}` and line 63 `ipv6NativeRoutingCIDR: {{ cilium_native_routing_cidr_ipv6 }}` (unquoted); defaults are empty strings at `roles/network_plugin/cilium/defaults/main.yml` line 93 (`cilium_native_routing_cidr: ""`) and line 96 (`cilium_native_routing_cidr_ipv6: ""`).
- Confirm in tag v2.30.0 the same template at line 65 / line 66 (unquoted substitutions); defaults remain empty strings.

## Known Issues
Root cause: in `roles/network_plugin/cilium/templates/values.yaml.j2` the keys `ipv4NativeRoutingCIDR` / `ipv6NativeRoutingCIDR` substitute the variables without quotes. With the empty-string default value, the YAML key gets an empty value that Helm interprets as `null` (rather than an empty string).

Fix: PR #13109 quotes both substitutions:

```diff
-ipv4NativeRoutingCIDR: {{ cilium_native_routing_cidr }}
-ipv6NativeRoutingCIDR: {{ cilium_native_routing_cidr_ipv6 }}
+ipv4NativeRoutingCIDR: "{{ cilium_native_routing_cidr }}"
+ipv6NativeRoutingCIDR: "{{ cilium_native_routing_cidr_ipv6 }}"
```

It landed only in master → v2.31.0; there is no backport to release-2.29 / release-2.30. Issue #13089 (label `triage/accepted`).

Workaround on v2.29.1 / v2.30.0: explicitly set `cilium_native_routing_cidr` (and `cilium_native_routing_cidr_ipv6` for IPv6) to a valid CIDR when using native routing.

## References
- https://github.com/kubernetes-sigs/kubespray/pull/13109
- Migrated from Kubepedia 0.1.0 cache: cilium-native-routing-cidr-null-v2.29.1.md, cilium-native-routing-cidr-null-v2.30.0.md
