---
id: CONCEPT-KYVERNO_CONTROLLERS
type: concept
title: "Kyverno's four controllers — which one to blame (admission / background / reports / cleanup)"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.18.2"
verified_at: "2026-07-18"
confidence: verified
aliases:
  - kyverno controllers architecture
  - kyverno background controller
  - kyverno reports controller
  - kyverno cleanup controller
  - which kyverno pod is failing
  - kyverno generate mutateExisting logs
tags:
  - kyverno
  - concept
  - architecture
sources:
  - type: docs
    path: docs/dev/controllers/README.md
    url: https://github.com/kyverno/kyverno/blob/v1.18.2/docs/dev/controllers/README.md
    note: "generate + mutate-existing run in Background Controller; PolicyReports in Reports Controller; CleanupPolicy in Cleanup Controller (owns a webhook)"
relations:
  - type: see_also
    target: CONCEPT-ADDON_KYVERNO
  - type: see_also
    target: TROUBLE-KYVERNO_POLICY_NOT_APPLYING
  - type: see_also
    target: TROUBLE-KYVERNO_REPORTS_ETCD_SCALE
---

# Kyverno's four controllers — which one to blame (admission / background / reports / cleanup)

## Summary

Since the **v1.10/1.11 split**, Kyverno is **not one pod** — it's **four independent Deployments**, each
scaled and leader-elected separately. Most "Kyverno isn't doing X" tickets are misrouted because people
look at the admission controller for problems that live in another one. This is the map: match the
symptom to the controller, then read *that* controller's logs — scaling the admission Deployment does
nothing for a report or generate backlog.

## Context

The four controllers (`docs/dev/controllers/README.md`@v1.18.2):

| Controller | Owns | Handles | Look here when… |
|-----------|------|---------|-----------------|
| **Admission** | the mutate/validate webhook | inline validate & mutate on admission | requests are blocked / slow / `failed calling webhook` |
| **Background** | — | **generate** and **mutate-existing** rules (has *no* relationship to report scanning) | a `generate`/`mutateExisting` policy didn't create/patch resources |
| **Reports** | — | builds **PolicyReports** / background report scanning | reports are missing/stale/incomplete |
| **Cleanup** | a cleanup webhook | **CleanupPolicy** / TTL-driven deletions (CronJobs) | resources are being deleted unexpectedly, or cleanup isn't running |

- **Generate + mutate-existing live ONLY in the Background Controller** — the doc states it plainly.
  So a `generate` policy that "isn't applying" is a background-controller problem, not admission
  ([[TROUBLE-KYVERNO_POLICY_NOT_APPLYING]] covers the policy-side; this says *which pod's logs*).
- **PolicyReports are built by the Reports Controller** — missing reports ≠ admission; also the
  reports/etcd-scale flooding lives here ([[TROUBLE-KYVERNO_REPORTS_ETCD_SCALE]]).
- **CleanupPolicy runs in the Cleanup Controller** — the only component besides admission that owns a
  webhook.
- **Diagnosis rule:** identify the symptom → target the controller's Deployment and logs; each scales
  independently, so throughput problems are fixed by scaling the *right* one.

## References

- Kyverno `docs/dev/controllers/README.md`@v1.18.2. Addon [[CONCEPT-ADDON_KYVERNO]]; policy-not-applying
  [[TROUBLE-KYVERNO_POLICY_NOT_APPLYING]]; reports/etcd [[TROUBLE-KYVERNO_REPORTS_ETCD_SCALE]].
