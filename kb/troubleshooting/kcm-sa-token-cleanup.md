---
id: TROUBLE-KCM_SA_TOKEN_CLEANUP
type: troubleshooting
title: "Legacy ServiceAccount token secrets auto-invalidated/deleted (1.29+)"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - legacy service account token deleted
  - legacy-token-invalid-since
  - sa token secret cleanup 1.29
  - auto-generated service account token deleted
tags:
  - troubleshooting
  - controller-manager
  - serviceaccount
  - auth
sources:
  - type: docs
    path: legacy SA token cleaner issue
    url: https://github.com/kubernetes/kubernetes/issues/120447
    note: "referenced-by-pod check incomplete"
  - type: docs
    path: KEP-2799 (reduction of secret-based SA tokens)
    url: https://github.com/kubernetes/enhancements/blob/master/keps/sig-auth/2799-reduction-of-secret-based-service-account-token/README.md
    note: "LegacyServiceAccountTokenCleanUp default-on from 1.29"
relations:
  - type: see_also
    target: CONCEPT-TROUBLESHOOTING_MAP
---

# Legacy ServiceAccount token secrets auto-invalidated/deleted (1.29+)

## Summary

Apps that rely on **long-lived, auto-generated ServiceAccount token Secrets** may break after
upgrading to **1.29+**: the `legacy-serviceaccount-token-cleaner` marks unused legacy tokens
invalid and eventually **deletes** them. This is intended behaviour (KEP-2799) — migrate to
bound/projected tokens.

## Problem

- Auth failures for a workload that mounted a classic SA token Secret.
- kcm log: `"Delete auto-generated service account token" secret="<ns>/<name>"` — sometimes for
  a secret still referenced by an active pod.

## Context

- `LegacyServiceAccountTokenCleanUp` is **beta and on by default from 1.29**. On upgrade,
  unused legacy token secrets get labeled `kubernetes.io/legacy-token-invalid-since` and are
  later deleted.

## Diagnostics

- **Expected:** the cleaner invalidates then deletes legacy token secrets **not used** for a
  configurable period. Check the `kubernetes.io/legacy-token-invalid-since` label; a token used
  again is un-invalidated.
- **The bug:** the "referenced by a pod" check was incomplete, so a secret **still mounted** by
  an active pod could be deleted (issue #120447) — if a workload lost its token, recreate the
  Secret.
- **Fix forward — migrate off legacy tokens:** use the **TokenRequest API** / **projected
  bound** ServiceAccount tokens (auto-rotated, audience-scoped) instead of static Secret
  tokens. Tune `--legacy-service-account-token-clean-up-period` if you need more runway.

## Known Issues

- CI/integrations that hardcode a specific SA token Secret name are the usual victims — move
  them to bound tokens or an explicitly-created, `kubernetes.io/service-account-token` Secret
  you manage.

## References

- kcm issue #120447 + KEP-2799 (above).
