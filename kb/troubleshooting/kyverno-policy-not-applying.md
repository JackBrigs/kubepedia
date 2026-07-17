---
id: TROUBLE-KYVERNO_POLICY_NOT_APPLYING
type: troubleshooting
title: "Kyverno: mutate/generate/verifyImages policy not applying"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=1.10.0 <=1.18.2"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - kyverno mutate existing not applied
  - kyverno generate downstream not synced
  - kyverno generate infinite loop
  - kyverno verifyimages cosign fails
  - kyverno wildcard crd not found
tags:
  - troubleshooting
  - kyverno
  - policy
sources:
  - type: docs
    path: kyverno issue #13034 (mutate-existing not applied)
    url: https://github.com/kyverno/kyverno/issues/13034
    note: "mutateExistingOnPolicyUpdate required for background mutation"
  - type: docs
    path: kyverno issue #16435 (verifyImages cosign panic)
    url: https://github.com/kyverno/kyverno/issues/16435
    note: "nil-pointer in cosign RekorLogs → admission-controller crash"
relations:
  - type: see_also
    target: CONCEPT-ADDON_KYVERNO
---

# Kyverno: mutate/generate/verifyImages policy not applying

## Summary

Community-sourced Kyverno policy-behaviour issues: **mutate-existing** doesn't touch existing
resources, **generate** downstreams don't sync (or loop forever), **verifyImages** (cosign)
fails or crashes the controller, and **wildcard** policies reject newly-installed CRDs for
~15 min.

## Problem

- A mutate policy doesn't modify pre-existing objects until each is manually edited.
- `generate` + `synchronize: true` downstream isn't updated on policy change, or is updated in
  an infinite loop; cloned downstream is orphaned after the source is deleted.
- `verifyImages` fails (`UNAUTHORIZED`, Sigstore TUF timeout) or the admission-controller
  **panics/crashes** and denies all admission.
- With `kind: "*"`, a new CR of a freshly-installed CRD is denied `resource <name> not found`.

## Context

- Applies to Kyverno **1.10–1.18** ([[CONCEPT-ADDON_KYVERNO]]).

## Diagnostics

- **Mutate-existing silent:** background mutation of existing resources requires
  **`spec.mutateExistingOnPolicyUpdate: true`**; expect `object has been modified` conflicts on
  concurrent updates (issues #13034/#9174).
- **Generate not syncing:** use **`generateExisting: true`** (v1.10+) — sync triggers on
  admission events, not background scans (issue #4222). **Infinite reconcile loop:** another
  operator mutates the target (or list-key fields diff endlessly) — exclude operator-managed
  fields or disable sync for operator-owned targets (issue #8480).
- **Orphaned clone downstream:** cleanup needs `managed-by: kyverno`, but Kyverno preserves an
  existing `managed-by: Helm` value so the selector can't match — relabel the downstream before
  deleting the source (issue #9718).
- **verifyImages auth:** the admission-controller SA needs RBAC to `get` the registry-credential
  **secret** (issue #15120). **Air-gapped:** allow egress to Sigstore TUF/Rekor or configure
  offline TUF; use `ignoreTlog`/`ignoreSCT` when tlog isn't needed (issue #11518).
- **verifyImages crash (SIGSEGV):** key/cert attestor + tlog verification on new-bundle-format
  images panics in cosign `RekorLogs()` and crashes the controller → **all admission denied
  until restart** — use keyless, or disable tlog for key/cert attestors, or patch (issue #16435).
- **Wildcard CRD lag:** the GVK cache refreshes only every ~15 min — wait, target specific
  kinds, or restart Kyverno (issue #10729).

## Known Issues

- **1.15** renamed the CEL `image()` function to **`parseImageReference`** — policies using the
  old name break. **1.13** moved `validationFailureAction` to the **rule level**
  (`spec.rules.validate.failureAction`).

## References

- kyverno issues #13034/#4222/#8480/#9718/#15120/#11518/#16435/#10729 (above).
- Addon: [[CONCEPT-ADDON_KYVERNO]].
