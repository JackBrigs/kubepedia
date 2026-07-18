---
id: CONCEPT-K8S_ADMISSION_POLICIES
type: concept
title: "CEL admission policies — ValidatingAdmissionPolicy (GA 1.30) & MutatingAdmissionPolicy (beta 1.34)"
status: active
kubespray_version: ">=v2.28.0 <=v2.31.0"
kubernetes_version: ">=1.30 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - ValidatingAdmissionPolicy
  - MutatingAdmissionPolicy
  - CEL admission
  - in-tree admission policy
  - replace admission webhook with CEL
  - AdmissionWebhookMatchConditions
tags:
  - kubernetes
  - admission
  - apiserver
  - security
sources:
  - type: code
    path: keps/sig-api-machinery/3488-cel-admission-control
    url: https://github.com/kubernetes/enhancements/tree/master/keps/sig-api-machinery/3488-cel-admission-control
    note: "kep.yaml: ValidatingAdmissionPolicy alpha 1.26, beta 1.28, stable 1.30; MutatingAdmissionPolicy (3962) beta 1.34"
relations:
  - type: see_also
    target: CONCEPT-POD_SECURITY_STANDARDS
  - type: see_also
    target: PRACTICE-CLUSTER_HARDENING
  - type: see_also
    target: CONCEPT-K8S_UPGRADE_SILENT_CHANGES
---

# CEL admission policies — ValidatingAdmissionPolicy (GA 1.30) & MutatingAdmissionPolicy (beta 1.34)

## Summary

Kubernetes now has **in-tree, CEL-based admission control** — no external webhook server needed.
**`ValidatingAdmissionPolicy`** reached **GA in 1.30** (validate/reject requests with CEL rules) and
**`MutatingAdmissionPolicy`** reached **beta in 1.34** (mutate objects with CEL, alternative to
mutating webhooks). This is a governance surface an operator can use for cheap, fail-closed policy
without running (and securing) a webhook deployment. Related: webhook `matchConditions` (CEL,
GA 1.30) to cut unnecessary webhook calls.

## Context

- Milestones: `ValidatingAdmissionPolicy` (`keps/sig-api-machinery/3488-...`) alpha **1.26** → beta
  **1.28** → stable **1.30**; `MutatingAdmissionPolicy` (`keps/sig-api-machinery/3962-...`) beta
  **1.34**; `AdmissionWebhookMatchConditions` (`keps/sig-api-machinery/3716-...`) GA **1.30**.
- **Why it matters:** a ValidatingAdmissionPolicy is evaluated **in the apiserver** (no network hop,
  no webhook availability risk), defined as a `ValidatingAdmissionPolicy` + `ValidatingAdmissionPolicyBinding`
  with CEL `validations`. Good for enforcing image registries, required labels, resource limits, etc.
  — complementing Pod Security admission ([[CONCEPT-POD_SECURITY_STANDARDS]]) and the hardening overlay
  ([[PRACTICE-CLUSTER_HARDENING]]).
- **Operator note:** these are opt-in objects you create — not a silent upgrade change — but their GA
  means you can **replace fragile validating webhooks**. MutatingAdmissionPolicy (beta 1.34) may ship
  off-by-default (post-KEP-5241) — verify the gate ([[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]]).

## References

- `keps/sig-api-machinery/{3488-cel-admission-control,3962-mutating-admission-policies,3716-admission-webhook-match-conditions}` (kep.yaml).
  PSA [[CONCEPT-POD_SECURITY_STANDARDS]]; hardening [[PRACTICE-CLUSTER_HARDENING]]; silent changes
  [[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]].
