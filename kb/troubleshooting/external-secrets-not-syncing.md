---
id: TROUBLE-EXTERNAL_SECRETS_NOT_SYNCING
type: troubleshooting
title: "external-secrets: ExternalSecret not syncing to a Secret"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - externalsecret not syncing
  - secretstore not ready
  - external-secrets provider auth failed
  - target secret not created
tags:
  - troubleshooting
  - external-secrets
  - secrets
sources:
  - type: docs
    path: external-secrets troubleshooting
    url: https://external-secrets.io/latest/introduction/faq/
    note: "SecretStore/ExternalSecret status, provider auth, refreshInterval"
relations:
  - type: see_also
    target: CONCEPT-SECRETS_MANAGEMENT
  - type: see_also
    target: CONCEPT-ADDON_VAULT
---

# external-secrets: ExternalSecret not syncing to a Secret

## Summary

An `ExternalSecret` doesn't produce the target Kubernetes `Secret` (or it's stale). The chain
is **SecretStore/ClusterSecretStore → ExternalSecret → Secret**; the block is almost always
**provider authentication** or a wrong key/property reference. Read both objects' status.

## Problem

- Target `Secret` missing or empty; workload can't mount it.
- `ExternalSecret` shows `SecretSyncedError` / `Ready: False`.
- Values don't update after rotation in the backend.

## Context

- Applies to the external-secrets operator ([[CONCEPT-SECRETS_MANAGEMENT]]); providers include
  Vault ([[CONCEPT-ADDON_VAULT]]), 1Password, cloud secret managers.

## Diagnostics

1. `kubectl describe secretstore <name>` (or `clustersecretstore`) → **`Ready`**? A failing
   store (bad provider endpoint/credentials/RBAC) breaks every ExternalSecret referencing it.
2. `kubectl describe externalsecret <name>` → the sync condition and the exact provider error.
3. **Provider auth:** verify the referenced auth Secret / ServiceAccount (IRSA/Workload
   Identity) / Vault role — expired or wrong credentials are the top cause.
4. **Key/property:** the `remoteRef.key` (and `property` for JSON secrets) must match exactly;
   a typo yields "key not found".
5. **Refresh:** `refreshInterval` controls staleness — `0` disables periodic refresh; lower it
   or force reconcile to pull rotated values.
6. **RBAC/namespace:** a namespaced `SecretStore` only serves its namespace; use a
   `ClusterSecretStore` for cross-namespace.

## Known Issues

- The controller needs network egress to the provider — a blocked egress or a webhook/CA issue
  looks like an auth failure.

## References

- external-secrets FAQ/troubleshooting (above); hub: [[CONCEPT-SECRETS_MANAGEMENT]]; Vault:
  [[CONCEPT-ADDON_VAULT]].
