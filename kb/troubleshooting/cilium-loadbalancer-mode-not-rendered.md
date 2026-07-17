---
id: TROUBLE-CILIUM_LOADBALANCER_MODE_NOT_RENDERED
type: troubleshooting
title: Cilium loadBalancer.mode not applied due to lowercase helm-values key
status: active
kubespray_version: "v2.29.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - cilium loadbalancer mode ignored
tags:
  - cilium
  - loadbalancer
sources:
  - type: github_pr
    url: https://github.com/kubernetes-sigs/kubespray/pull/12705
    note: "Cherry-pick fixing the helm-values key to camelCase loadBalancer"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# Cilium loadBalancer.mode not applied due to lowercase helm-values key

## Summary
When installing Cilium via Kubespray, the configured load-balancing mode (`cilium_loadbalancer_mode`, e.g. `dsr` or `hybrid`) was silently ignored and Cilium kept the default `snat` mode, because the helm-values section key was written as lowercase `loadbalancer:` instead of camelCase `loadBalancer:`. Fixed in v2.29.1.

## Problem
When installing Cilium through Kubespray, the configured balancing mode (`cilium_loadbalancer_mode`, e.g. `dsr` or `hybrid`) was not actually applied — Cilium kept running in the default mode (`snat`) despite the inventory setting.

## Context
- Affected versions: v2.29.0.
- Fixed versions: v2.29.1.
- Users of v2.29.0 who set `cilium_loadbalancer_mode` should upgrade to v2.29.1.

## Diagnostics
- Confirm Cilium runs in `snat` mode at runtime despite `cilium_loadbalancer_mode` being set to `dsr`/`hybrid`.
- Inspect the rendered `roles/network_plugin/cilium/templates/values.yaml.j2`: the section key `loadbalancer:` (lowercase `b`) is ignored by the Cilium helm chart, which expects camelCase `loadBalancer:`.

## Known Issues
Root cause: in the Cilium helm-values template the section key was written as `loadbalancer:` (lowercase `b`). The Cilium helm chart expects the camelCase key `loadBalancer:`, so the entire section (including `mode`) was silently ignored. File: `roles/network_plugin/cilium/templates/values.yaml.j2`.

Fix: original Issue #12666. PR #12705 (cherry-pick of the original #12701 "Fixes #12666", commit `3c0cff983`) corrected the key to camelCase:

```diff
-loadbalancer:
+loadBalancer:
   mode: {{ cilium_loadbalancer_mode }}
```

Confirmed in tag v2.29.1: `roles/network_plugin/cilium/templates/values.yaml.j2:30` contains `loadBalancer:` and line 31 `mode: {{ cilium_loadbalancer_mode }}`. Commit `3c0cff983` falls within the `v2.29.0..v2.29.1` range.

## References
- https://github.com/kubernetes-sigs/kubespray/pull/12705
- Migrated from Kubepedia 0.1.0 cache: cilium-loadbalancer-mode-not-rendered-v2.29.1.md
