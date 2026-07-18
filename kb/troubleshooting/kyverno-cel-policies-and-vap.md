---
id: CONCEPT-KYVERNO_CEL_POLICIES
type: concept
title: "Kyverno's new CEL policy engine (policies.kyverno.io) + auto-generated ValidatingAdmissionPolicies"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.18.2"
verified_at: "2026-07-18"
confidence: verified
aliases:
  - kyverno ValidatingPolicy MutatingPolicy
  - policies.kyverno.io
  - kyverno CEL policy webhook
  - kyverno generateValidatingAdmissionPolicy
  - kyverno auto VAP
  - vpol mpol ivpol webhook
tags:
  - kyverno
  - policy
  - admission
  - cel
sources:
  - type: code
    path: pkg/config/config.go
    url: https://github.com/kyverno/kyverno/blob/v1.18.2/pkg/config/config.go
    note: "new webhooks vpol/mpol/ivpol/gpol/nvpol for the policies.kyverno.io CEL family (L58-69)"
  - type: code
    path: charts/kyverno/values.yaml
    url: https://github.com/kyverno/kyverno/blob/v1.18.2/charts/kyverno/values.yaml
    note: "generateValidatingAdmissionPolicy.enabled TRUE by default (L797-799); generateMutatingAdmissionPolicy off (L800-802)"
relations:
  - type: see_also
    target: CONCEPT-ADDON_KYVERNO
  - type: see_also
    target: CONCEPT-K8S_ADMISSION_POLICIES
  - type: see_also
    target: CONCEPT-KYVERNO_CONTROLLERS
---

# Kyverno's new CEL policy engine (policies.kyverno.io) + auto-generated ValidatingAdmissionPolicies

## Summary

Kyverno **1.18** ships a **parallel, CEL-based policy family** under the new API group
**`policies.kyverno.io`** — `ValidatingPolicy`, `MutatingPolicy`, `ImageValidatingPolicy`,
`GeneratingPolicy` (+ namespaced variants) — each with its **own webhook** and **VAP-style semantics**,
separate from the classic `ClusterPolicy` engine. On top of that, Kyverno **by default compiles eligible
policies into native Kubernetes `ValidatingAdmissionPolicy` objects** that enforce **without the Kyverno
webhook**. Two traps: debugging the wrong webhook/engine, and seeing enforcement (or duplicate reports)
you can't trace back to Kyverno.

## Context

- Applies to Kyverno **1.18.x** ([[CONCEPT-ADDON_KYVERNO]]).
- **New CEL engine:** the `policies.kyverno.io` CRDs register their **own** webhooks —
  `vpol.validate.kyverno.svc`, `mpol.validate.kyverno.svc`, `ivpol.{validate,mutate}.kyverno.svc`,
  `gpol.validate.kyverno.svc`, and namespaced `nvpol.*` (`pkg/config/config.go`@v1.18.2 L58-69). They
  use **VAP-style `failurePolicy` + `validationActions` (Deny/Warn/Audit)** — *not* the legacy
  `validationFailureAction`. Mixing the classic `ClusterPolicy` mental model with these gives wrong
  enforcement and points you at the wrong webhook when debugging.
- **Auto-generated VAPs (on by default):** `generateValidatingAdmissionPolicy.enabled: true`
  (`values.yaml`@v1.18.2 L797-799) → eligible Kyverno policies are compiled into native
  `ValidatingAdmissionPolicy`/binding objects (see [[CONCEPT-K8S_ADMISSION_POLICIES]]) that enforce in
  the apiserver **without** calling Kyverno. Consequences: (1) enforcement continues even if the Kyverno
  webhook is down; (2) you may see duplicate reports/enforcement; (3) **uninstalling Kyverno can leave
  orphaned VAPs** still enforcing. `generateMutatingAdmissionPolicy` is **off** by default (L800-802).
- **Debugging rule:** first determine which engine a policy belongs to (classic `kyverno.io` vs new
  `policies.kyverno.io`) and whether a native VAP was generated — otherwise you inspect the wrong
  webhook/object ([[CONCEPT-KYVERNO_CONTROLLERS]] for which pod).

## References

- Kyverno `pkg/config/config.go`, `charts/kyverno/values.yaml`, `config/crds/policies.kyverno.io/`
  (@v1.18.2). Native admission policies [[CONCEPT-K8S_ADMISSION_POLICIES]]; controller map
  [[CONCEPT-KYVERNO_CONTROLLERS]]; addon [[CONCEPT-ADDON_KYVERNO]].
