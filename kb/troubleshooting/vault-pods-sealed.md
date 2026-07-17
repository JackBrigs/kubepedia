---
id: TROUBLE-VAULT_PODS_SEALED
type: troubleshooting
title: "Vault: pods 0/1, cluster sealed after restart"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.15.0 <=1.23.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - vault pods 0/1
  - vault sealed
  - vault auto-unseal
  - vault not ready readiness sealed
tags:
  - troubleshooting
  - vault
  - secrets
sources:
  - type: docs
    path: Vault on Kubernetes (Helm) run guide
    url: https://developer.hashicorp.com/vault/docs/deploy/kubernetes/helm/run
    note: "seal/unseal, HA storage, injector"
relations:
  - type: see_also
    target: CONCEPT-ADDON_VAULT
---

# Vault: pods 0/1, cluster sealed after restart

## Summary

Vault pods show **`0/1` Ready** and the UI/API returns "Vault is sealed". Vault **starts
sealed** by design after every restart; until it is **unsealed** it does not serve. Either
provide unseal keys or (recommended) configure **auto-unseal**.

## Problem

- Vault pods `0/1 Running`, readiness never passes.
- `vault status` shows `Sealed: true`.
- Apps using the Agent Injector don't get secrets (Vault unavailable).

## Context

- Applies to Vault **1.15–1.23** via the Helm chart (owner runs 1.21.2 —
  [[CONCEPT-ADDON_VAULT]]). Readiness intentionally fails while sealed.

## Diagnostics

- **Fresh install:** initialize once — `vault operator init` — store the unseal keys + root
  token securely, then unseal.
- **After a restart (manual seal):** `vault operator unseal` with the threshold of keys on
  each pod (Raft/HA: unseal every member).
- **Production fix — auto-unseal:** configure a `seal` stanza (cloud KMS / Transit) so pods
  auto-unseal on restart and readiness passes without manual steps.
- **HA/Raft stuck `Pending` (not sealed):** the server needs a working `StorageClass`/PVC —
  check storage, not seal state.

## Known Issues

- **Do not lose the unseal keys / recovery keys** — without them a sealed Vault (or KMS
  outage with Transit unseal) is unrecoverable. Keep a break-glass copy.
- The **Agent Injector** webhook TLS/CA must be correct or injection silently fails even once
  Vault is unsealed.

## References

- Vault Helm run guide (above); addon: [[CONCEPT-ADDON_VAULT]].
