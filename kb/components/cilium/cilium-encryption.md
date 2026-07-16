---
id: CONCEPT-CILIUM_ENCRYPTION
type: concept
title: "Cilium transparent encryption in Kubespray (IPsec / WireGuard)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium encryption
  - cilium ipsec
  - cilium wireguard
  - cilium_encryption_enabled
  - transparent encryption cilium
  - node encryption
tags:
  - cilium
  - encryption
  - security
  - networking
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "cilium_encryption_enabled/_type/_node_encryption defaults (tag v2.31.0)"
  - type: code
    path: roles/network_plugin/cilium/tasks/check.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/tasks/check.yml
    note: "encryption preflight: ipsec key required; wireguard kernel >=5.6 (tag v2.31.0)"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
  - type: see_also
    target: TROUBLE-CILIUM_CONFIG_VALIDATION
  - type: see_also
    target: CONCEPT-CILIUM_DATAPATH
---

# Cilium transparent encryption in Kubespray (IPsec / WireGuard)

## Summary

Cilium can transparently encrypt pod-to-pod traffic with **IPsec** or **WireGuard**. It
is **off by default**; enabling it requires picking a type and satisfying that type's
prerequisites (an IPsec key, or a WireGuard-capable kernel). Kubespray's preflight
enforces these, so a misconfigured encryption setup fails **before** deploy rather than
silently sending cleartext.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`, `kube_network_plugin: cilium`.
- Defaults (`cilium/defaults/main.yml`):
  - `cilium_encryption_enabled: false` — master switch.
  - `cilium_encryption_type: "ipsec"` — `ipsec` (default) or `wireguard`.
  - `cilium_encryption_node_encryption: false` — also encrypt host/node traffic (not just
    pod-to-pod).

## Implementation

**IPsec:**

- Requires **`cilium_ipsec_key`** to be defined (a secret) — the preflight aborts without
  it ([[TROUBLE-CILIUM_CONFIG_VALIDATION]]).
- Key rotation and algorithm are managed through the Cilium IPsec secret.

**WireGuard:**

- Requires kernel **≥ 5.6.0** (in-kernel WireGuard) — Kubespray's preflight asserts this;
  older kernels fail the check.
- Simpler key management than IPsec (Cilium handles keys), often the preferred choice on
  modern kernels.

**Common guards (from `check.yml`):**

- `cilium_encryption_type` must be exactly `ipsec` or `wireguard`.
- If `cilium_ipsec_enabled` is set, `cilium_encryption_type` must be `ipsec` (the two must
  agree).
- `cilium_encryption_node_encryption: true` extends coverage to node traffic — verify your
  environment tolerates the added scope.

## Compatibility

- Encryption adds per-packet overhead; enable it where the threat model needs it, not
  reflexively.
- Switching encryption type or enabling it on a running cluster is a datapath change —
  roll it out carefully and confirm flows still pass (Hubble helps — see
  [[CONCEPT-CILIUM_HUBBLE]]).
- Encryption interacts with the datapath/routing mode ([[CONCEPT-CILIUM_DATAPATH]]);
  validate on a non-prod cluster first.

## References

- `cilium/defaults/main.yml` and `cilium/tasks/check.yml` at tag `v2.31.0`. Preflight:
  [[TROUBLE-CILIUM_CONFIG_VALIDATION]]; component: [[COMPONENT-CILIUM]].
