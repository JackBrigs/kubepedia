---
id: TROUBLE-1PASSWORD_CONNECT
type: troubleshooting
title: "1Password Connect: secrets not served / sync failing — credentials JSON, Connect token, vault scope"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=1.7.3"
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - 1password connect not working
  - connect-sync failing
  - 1password credentials json missing
  - connect token unauthorized
  - external-secrets 1password auth
tags: [troubleshooting, secrets, 1password]
sources:
  - type: external
    path: 1Password Connect
    url: https://developer.1password.com/docs/connect/
    note: "connect-api + connect-sync; needs 1password-credentials.json secret + a Connect token; vault scope"
relations:
  - type: see_also
    target: CONCEPT-ADDON_1PASSWORD_CONNECT
  - type: see_also
    target: CONCEPT-SECRETS_MANAGEMENT
---

# 1Password Connect: secrets not served / sync failing — credentials JSON, Connect token, vault scope

## Summary

1Password Connect runs a **connect-api / connect-sync** pair that serves secrets from 1Password vaults
(usually consumed by external-secrets). Failures are almost always the **credentials JSON** secret
missing/wrong, an invalid **Connect token**, or the token lacking **access to the vault** being read.
App `v1.7.3`.

## Problem

- Consumers get `401/403` from Connect, `connect-sync` crashloops or can't authenticate, or external-
  secrets reports the 1Password provider unauthorized.

## Context

- 1Password Connect `1.7.3` ([[CONCEPT-ADDON_1PASSWORD_CONNECT]]); part of the secrets layer
  ([[CONCEPT-SECRETS_MANAGEMENT]]).
- **Credentials JSON:** connect-sync needs the `1password-credentials.json` (from `op connect server
  create`) mounted as a Secret; missing/base64-mangled → sync won't start.
- **Connect token:** clients (external-secrets) authenticate with a **Connect token** issued for that
  Connect server; a wrong/expired token → 401.
- **Vault scope:** the token is scoped to specific **vaults**; reading an item from a vault the token
  can't see → 403, even with a valid token.

## Diagnostics

```bash
kubectl -n onepassword logs deploy/onepassword-connect -c connect-sync | tail
kubectl -n onepassword get secret op-credentials -o jsonpath='{.data}' | head -c 40   # present?
kubectl -n <app-ns> describe externalsecret <name>                                     # provider auth error
```

## Known Issues

- **Credentials — fix:** recreate the `1password-credentials.json` secret exactly as produced by
  `op connect server create` (don't re-encode); restart connect-sync.
- **Token — fix:** issue a fresh Connect token for this server and update the consumer's secret.
- **Vault scope — fix:** grant the token access to the vault holding the item (scopes are per-vault).

## References

- 1Password Connect docs. Addon [[CONCEPT-ADDON_1PASSWORD_CONNECT]]; secrets
  [[CONCEPT-SECRETS_MANAGEMENT]].
