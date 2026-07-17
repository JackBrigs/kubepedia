---
id: TROUBLE-ARGOCD_UPGRADE_3_RBAC
type: troubleshooting
title: "Argo CD 2→3 upgrade: users lose access / permission denied"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.0.0 <=3.4.5"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - argocd 3.0 rbac broke
  - argocd permission denied after upgrade
  - argocd logs rbac
  - argocd resource tracking annotations
tags:
  - troubleshooting
  - argocd
  - gitops
  - upgrade
  - rbac
sources:
  - type: docs
    path: Argo CD 2.14→3.0 upgrade guide
    url: https://argo-cd.readthedocs.io/en/release-3.1/operator-manual/upgrading/2.14-3.0/
    note: "fine-grained RBAC, logs RBAC, tracking method changes"
relations:
  - type: see_also
    target: CONCEPT-ADDON_ARGOCD
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
  - type: see_also
    target: TROUBLE-RBAC_FORBIDDEN
---

# Argo CD 2→3 upgrade: users lose access / permission denied

## Summary

After upgrading Argo CD across the **2.x → 3.x** boundary (chart 8.x = app 3.x), users
suddenly get "permission denied", cannot see sub-resources, or pod logs disappear from the
UI. This is expected: 3.0 tightened RBAC and changed defaults. Adjust the RBAC policy and
resource-tracking config to match.

## Problem

Symptoms right after the 3.x upgrade:

- Users who could act before now get `permission denied` on sync/delete.
- Application resource trees show fewer resources, or "logs" tab is empty/denied.
- Apps show as OutOfSync/unknown because tracking labels changed to annotations.

## Context

- Applies to Argo CD **3.0.0–3.4.5** (owner runs 3.1.7 — [[CONCEPT-ADDON_ARGOCD]]).
- The 3.0 major deliberately changed RBAC and tracking; the chart upgrade alone does not warn
  you interactively.

## Diagnostics

- Fine-grained RBAC: `update`/`delete` now apply **only to the Application**, not its
  sub-resources — sub-resource actions need explicit new policies.
- **Logs RBAC enforced by default:** viewing pod logs now requires an explicit `logs, get`
  policy that was implicit before.
- **Resource tracking moved labels → annotations** by default — a mismatch with the previous
  tracking method makes apps read as OutOfSync until reconciled/aligned.
- Legacy repositories can no longer live in `argocd-cm` — they must be **Secrets**.

## Known Issues

- Also on 3.1.x: **CVE-2025-55191** (DoS via repo-credentials race) affects ≤3.1.7 — fixed
  3.1.8. Bundle the security bump with the RBAC fix. General RBAC-denial triage:
  [[TROUBLE-RBAC_FORBIDDEN]].

## References

- Argo CD 2.14→3.0 upgrade guide (above); addon: [[CONCEPT-ADDON_ARGOCD]]; horizon:
  [[CONCEPT-UPGRADE_HORIZON]].
