---
id: TROUBLE-CILIUM_CONFIG_VALIDATION
type: troubleshooting
title: Cilium config validation aborts the deploy
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium check failed
  - cilium_encryption_type invalid
  - cilium_ipsec_key
  - cilium identity allocation mode
tags:
  - troubleshooting
  - cilium
  - cni
  - preflight
sources:
  - type: code
    path: roles/network_plugin/cilium/tasks/check.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/tasks/check.yml
    note: "Cilium preflight assertions (tag v2.31.0)"
relations:
  - type: see_also
    target: TROUBLE-KUBESPRAY_PREFLIGHT_FAILS
  - type: see_also
    target: COMPONENT-CILIUM
  - type: see_also
    target: TROUBLE-NFTABLES_KERNEL_TOO_LOW
---

# Cilium config validation aborts the deploy

## Summary

When `kube_network_plugin: cilium`, Kubespray runs `network_plugin/cilium/tasks/check.yml`
before deploying and aborts on any invalid Cilium setting. Each assertion pins a
specific `cilium_*` variable to a legal value/range; the failure message names the
variable. This document lists every in-range Cilium precondition and its fix.

## Problem

The run stops during the Cilium role on a task like `Stop if bad Cilium …` /
`Check Cilium encryption …`, with a message naming a `cilium_*` variable, before the
CNI is installed.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0` with `kube_network_plugin: cilium` (or
  `cilium_deploy_additionally`).
- Cilium is the only CNI indexed in this KB (owner decision); other plugins have their
  own `check.yml`.

## Diagnostics

| Assertion | Rule | Fix |
|-----------|------|-----|
| min version | `cilium_version >= 1.15` (`cilium_min_version_required`) | set a supported `cilium_version` |
| identity mode | `cilium_identity_allocation_mode ∈ {crd, kvstore}` | use `crd` (default) or `kvstore` |
| encryption type | `cilium_encryption_type ∈ {ipsec, wireguard}` (when `cilium_encryption_enabled`) | fix the typo/value |
| ipsec key | `cilium_ipsec_key` defined when `cilium_encryption_type: ipsec` | provide the IPsec key secret |
| ipsec consistency | if `cilium_ipsec_enabled`, `cilium_encryption_type` must be `ipsec` | align the two variables |
| wireguard kernel | kernel `>= 5.6.0` for WireGuard encryption | upgrade kernel or use ipsec |
| cluster id | `1 <= cilium_cluster_id <= 255` (when defined) | pick an ID in range (ClusterMesh) |
| hubble buffer | `cilium_hubble_event_buffer_capacity ∈ {2^n − 1}` in `[1, 65535]` | use `4095`, `8191`, `16383`, … |

Also relevant (from the shared preinstall check): Cilium requires kernel `>= 4.9.17`
generally — see [[TROUBLE-KUBESPRAY_PREFLIGHT_FAILS]].

## Known Issues

- `cilium_hubble_event_buffer_capacity` must be a **power of two minus one** — a value
  like `10000` fails; use the nearest `2^n − 1` (e.g. `8191`).
- The kernel checks parse `ansible_kernel` up to the first `-`; back-ported distro
  kernels can report a misleadingly low base version.
- These are config-validation guards, not runtime diagnostics — for a deployed Cilium
  that misbehaves, see the Cilium diagnostics runbook and [[COMPONENT-CILIUM]].
- Bypassing with `ignore_assert_errors` does not apply to all of these (some run
  unconditionally); fix the variable instead.

## References

- `network_plugin/cilium/tasks/check.yml` at tag `v2.31.0`.
- Preflight overview: [[TROUBLE-KUBESPRAY_PREFLIGHT_FAILS]]; component: [[COMPONENT-CILIUM]].
