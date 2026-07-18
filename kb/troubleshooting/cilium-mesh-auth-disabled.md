---
id: TROUBLE-CILIUM_MESH_AUTH_DISABLED
type: troubleshooting
title: "Cilium 1.19 forwards mutual-auth traffic unauthenticated — mesh-auth now disabled by default"
status: active
kubespray_version: ">=v2.31.0 <=v2.31.0"
kubernetes_version: ">=1.33 <=1.35"
component_version: ">=1.19.3 <=1.19.3"
verified_at: "2026-07-18"
confidence: confirmed
aliases:
  - cilium mesh-auth-enabled default off
  - authentication.enabled cilium
  - cilium mutual auth not enforced 1.19
  - cilium policy auth warning
tags:
  - cilium
  - troubleshooting
  - security
  - upgrade
sources:
  - type: docs
    path: Documentation/operations/upgrade.rst
    url: https://github.com/cilium/cilium/blob/v1.19.3/Documentation/operations/upgrade.rst
    note: "1.19: mesh-auth-enabled (Helm authentication.enabled) now disabled by default"
relations:
  - type: see_also
    target: UPGRADE-CILIUM_1_15_TO_1_19
  - type: see_also
    target: COMPONENT-CILIUM
  - type: see_also
    target: CONCEPT-CILIUM_ENCRYPTION
---

# Cilium 1.19 forwards mutual-auth traffic unauthenticated — mesh-auth now disabled by default

## Summary

In Cilium **1.19**, **`mesh-auth-enabled`** (Helm `authentication.enabled`) is now **disabled by
default**. If your CiliumNetworkPolicies use **mutual authentication** (`authentication.mode: required`),
after Kubespray moves Cilium to **1.19.3 (v2.31.0)** that traffic is **forwarded unauthenticated** and
the policies emit a **validation warning** — a silent weakening of a security control you thought was
enforced.

## Problem

- After upgrading to Kubespray v2.31.0, CiliumNetworkPolicies with `authentication.mode: required` no
  longer enforce mutual auth; traffic flows without the expected authentication.
- Cilium logs/policy status show a **warning** that mesh authentication is not enabled.

## Context

- Applies to Cilium **1.19** → Kubespray **v2.31.0** ([[UPGRADE-CILIUM_1_15_TO_1_19]]). The mutual-auth
  subsystem (mTLS-style identity handshake, related to SPIFFE/`encryption` — [[CONCEPT-CILIUM_ENCRYPTION]])
  ships **off by default** in 1.19 where it was previously enabled (`upgrade.rst`@v1.19.3).
- This is one of the three ClusterMesh/security default flips in the 1.18→1.19 jump (with
  policy-default-local-cluster on, and mesh-auth off).

## Diagnostics

- Check the setting: `kubectl -n kube-system get cm cilium-config -o yaml | grep mesh-auth` — `false`
  on 1.19 is the new default.
- Look for policy validation warnings referencing authentication in the agent/operator logs.
- Confirm you rely on it: `kubectl get cnp,ccnp -A -o yaml | grep -A2 authentication` — any
  `mode: required` means you need it on.

## Known Issues

- **Fix:** if you use mutual auth in policies, **re-enable** it explicitly — set
  `authentication.enabled=true` (Helm) / `mesh-auth-enabled=true` — and verify enforcement on a canary
  before rolling. Do this as part of the v2.30.0 → v2.31.0 upgrade plan.
- **If you don't use mutual auth:** no action; the default-off simply matches your usage.
- Treat as a **security-posture** change, not a connectivity break — traffic still flows, just without
  the auth guarantee.

## References

- Cilium `Documentation/operations/upgrade.rst`@v1.19.3 (mesh-auth default off). Full jump
  [[UPGRADE-CILIUM_1_15_TO_1_19]]; encryption/auth [[CONCEPT-CILIUM_ENCRYPTION]]; component
  [[COMPONENT-CILIUM]].
