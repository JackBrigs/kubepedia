---
id: TROUBLE-CILIUM_KPR_TOGGLES_REMOVED
type: troubleshooting
title: "Cilium 1.19 won't start / features off — piecemeal kube-proxy-replacement toggles removed"
status: active
kubespray_version: ">=v2.30.0 <=v2.31.0"
kubernetes_version: ">=1.34 <=1.35"
component_version: ">=1.18.2 <=1.19.3"
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - cilium enable-node-port removed
  - cilium unknown flag enable-host-port
  - cilium kube-proxy-replacement toggles
  - cilium 1.19 upgrade agent crashloop flag
  - enable-external-ips removed cilium
  - enable-session-affinity removed
tags:
  - cilium
  - troubleshooting
  - upgrade
  - kube-proxy-replacement
sources:
  - type: docs
    path: Documentation/operations/upgrade.rst
    url: https://github.com/cilium/cilium/blob/v1.19.3/Documentation/operations/upgrade.rst
    note: "1.18 deprecates then 1.19 removes --enable-node-port/-host-port/-external-ips/-session-affinity/-internal-traffic-policy/-svc-source-range-check"
relations:
  - type: see_also
    target: UPGRADE-CILIUM_1_15_TO_1_19
  - type: see_also
    target: COMPONENT-CILIUM
  - type: see_also
    target: CONCEPT-CILIUM_LOADBALANCING
  - type: see_also
    target: CONCEPT-KUBE_PROXY
---

# Cilium 1.19 won't start / features off — piecemeal kube-proxy-replacement toggles removed

## Summary

Cilium spent releases consolidating the individual kube-proxy-replacement (KPR) feature toggles into
the single `kube-proxy-replacement` switch: **deprecated in 1.18, removed in 1.19**. Any inventory or
Helm values that still set the old per-feature flags (`--enable-node-port`, `--enable-host-port`,
`--enable-external-ips`, `--enable-session-affinity`, `--enable-internal-traffic-policy`,
`--enable-svc-source-range-check`, `--enable-k8s-endpoint-slice`) break when Kubespray moves Cilium to
**1.19.3 (v2.31.0)** — the agent rejects the unknown flag, or the feature you thought you enabled is
silently governed by `kube-proxy-replacement` instead. Full jump context:
[[UPGRADE-CILIUM_1_15_TO_1_19]].

## Problem

- After upgrading to Kubespray v2.31.0 (Cilium 1.19.3), `cilium-agent` **crash-loops** with an
  unknown/removed flag error naming one of the `--enable-*` toggles.
- Or the agent starts but a service feature (NodePort, HostPort, ExternalIPs, session affinity)
  **doesn't work as before**, because it is now gated solely on `kube-proxy-replacement=true`.

## Context

- Applies to Cilium **1.19+** → Kubespray **v2.31.0** ([[COMPONENT-CILIUM]]). The flags were
  **deprecated in 1.18** (Kubespray v2.29.0/v2.30.0 — still accepted, warned) and **removed in 1.19**
  (`Documentation/operations/upgrade.rst`@v1.19.3). This is a two-step trap: it "works" on v2.29/2.30
  and breaks on v2.31.0.
- Consolidation rule: with `kube-proxy-replacement=true`, NodePort / HostPort / ExternalIPs /
  session-affinity / internal-traffic-policy / source-range-check are **enabled together** and are no
  longer individually toggleable; the standalone flags are gone.

## Diagnostics

- `kubectl -n kube-system logs ds/cilium -c cilium-agent | grep -iE "unknown flag|removed|enable-node-port"` —
  the removed flag is named in the start-up error.
- Check what's set: `kubectl -n kube-system get cm cilium-config -o yaml | grep -E "enable-node-port|enable-host-port|enable-external-ips|enable-session-affinity|kube-proxy-replacement"` —
  any of the old keys present is the culprit; `kube-proxy-replacement` should be `true`/`false`.
- Inventory side: grep your Kubespray group_vars / cilium Helm values for `cilium_*` variables mapping
  to these flags.

## Known Issues

- **Fix:** remove the individual `--enable-*` toggles from cilium config / Helm values and rely on
  **`kube-proxy-replacement`** (set `true` for the KPR feature set, `false` to run alongside
  kube-proxy). Do this **before** the v2.30.0 → v2.31.0 upgrade ([[PRACTICE-RUNBOOK_CONFIG_CHANGE]]).
- **If you ran kube-proxy-less** with these toggles individually enabled, confirm
  `kube-proxy-replacement=true` covers your set — most standalone features are now unconditional under
  KPR ([[CONCEPT-CILIUM_LOADBALANCING]], [[CONCEPT-KUBE_PROXY]]).
- **Pre-upgrade audit:** on v2.29.0/v2.30.0 (Cilium 1.18) these flags emit deprecation warnings in the
  agent log — treat those warnings as the migration to-do list before v2.31.0.

## References

- Cilium `Documentation/operations/upgrade.rst`@v1.19.3 (KPR toggle removal); @v1.18.2 (deprecation).
  Full jump [[UPGRADE-CILIUM_1_15_TO_1_19]]; component [[COMPONENT-CILIUM]]; config-change runbook
  [[PRACTICE-RUNBOOK_CONFIG_CHANGE]]; kube-proxy [[CONCEPT-KUBE_PROXY]].
