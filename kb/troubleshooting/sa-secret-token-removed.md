---
id: TROUBLE-K8S_SA_SECRET_TOKEN_REMOVED
type: troubleshooting
title: "ServiceAccount has no Secret / token — auto-generated SA token Secrets removed (K8s 1.24+, cleanup GA 1.30)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - serviceaccount has no secret
  - no token secret for service account
  - LegacyServiceAccountTokenCleanUp
  - sa token secret not created
  - service account secret missing after upgrade
  - imagePullSecrets automount token gone
tags:
  - kubernetes
  - troubleshooting
  - auth
  - serviceaccount
sources:
  - type: code
    path: keps/sig-auth/2799-reduction-of-secret-based-service-account-token
    url: https://github.com/kubernetes/enhancements/tree/master/keps/sig-auth/2799-reduction-of-secret-based-service-account-token
    note: "no auto-generated Secret tokens per SA; LegacyServiceAccountTokenNoAutoGeneration + CleanUp GA v1.30 (kep.yaml milestone)"
relations:
  - type: see_also
    target: CONCEPT-K8S_UPGRADE_SILENT_CHANGES
  - type: see_also
    target: CONCEPT-CLUSTER_PKI
  - type: see_also
    target: PRACTICE-RUNBOOK_UPGRADE_ONE_MINOR
---

# ServiceAccount has no Secret / token — auto-generated SA token Secrets removed (K8s 1.24+, cleanup GA 1.30)

## Summary

Kubernetes no longer creates a **Secret-based token for every ServiceAccount**, and from **1.30** it
also **auto-deletes unused legacy** token Secrets (`LegacyServiceAccountTokenCleanUp` GA). Tooling or
scripts that assumed "each ServiceAccount has a companion `*-token-*` Secret" break silently after
upgrading across the Kubespray range. The modern path is **short-lived projected tokens** (via
`TokenRequest`), not a long-lived Secret.

## Problem

- A newly created ServiceAccount has **no** `*-token-*` Secret; `kubectl get secrets` shows nothing
  for it.
- Automation that read a token from `secret/<sa>-token-xxxx` gets `NotFound`.
- After a cluster upgrade, previously-present legacy SA token Secrets **disappear** (auto-cleaned if
  unused).
- CI/external systems using a static SA token Secret suddenly fail auth.

## Context

- The auto-generation of a Secret per ServiceAccount was turned off by default in **K8s 1.24**
  (`LegacyServiceAccountTokenNoAutoGeneration`); the **cleanup** of unused legacy token Secrets
  reached **GA in 1.30** (`LegacyServiceAccountTokenCleanUp`). Both are fully in effect across the
  Kubespray range (K8s 1.29–1.35). `keps/sig-auth/2799-...`
- Pods don't need the Secret: kubelet mounts a **projected, short-lived** token automatically. The
  Secret was only ever needed by **external** consumers.

## Diagnostics

- Confirm no token Secret: `kubectl get sa <name> -o yaml` — the old `.secrets[]` list is empty/absent.
- A legacy token Secret that still exists is labeled/annotated for cleanup; check
  `kubectl get secret <name> -o jsonpath='{.metadata.labels}'` for
  `kubernetes.io/legacy-token-last-used`.
- In-use vs unused: cleanup only removes legacy tokens not used for a period — a token still used
  recently is retained (with a warning), so a broken consumer may be the one keeping it alive.

## Known Issues

- **Fix (in-cluster consumers):** use the **projected token** — mount a `serviceAccountToken`
  projected volume, or call the **TokenRequest** API; don't rely on a Secret.
- **Fix (external/long-lived need — e.g. a CI system):** explicitly create a **manually-managed**
  token Secret with `type: kubernetes.io/service-account-token` and the
  `kubernetes.io/service-account.name` annotation — this is still supported but is opt-in and will
  **not** be auto-cleaned while in use. Prefer short-lived `kubectl create token <sa>` where possible.
- **Fix (image pulls):** `imagePullSecrets` on the SA are unaffected — those are separate Secrets you
  manage; only the auto-token Secret changed.
- **Upgrade planning:** before moving a cluster forward, inventory anything reading
  `secret/<sa>-token-*` and migrate it to TokenRequest / an explicit Secret — this is a silent
  breaker ([[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]]).

## References

- `keps/sig-auth/2799-reduction-of-secret-based-service-account-token` (kep.yaml: no-auto-generation
  1.24, cleanup GA 1.30). Silent-change list [[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]]; PKI
  [[CONCEPT-CLUSTER_PKI]]; upgrade runbook [[PRACTICE-RUNBOOK_UPGRADE_ONE_MINOR]].
