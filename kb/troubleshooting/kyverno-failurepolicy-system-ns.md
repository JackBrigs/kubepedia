---
id: TROUBLE-KYVERNO_FAILURE_POLICY_SYSTEM_NS
type: troubleshooting
title: "Kyverno down → whole cluster (incl. kube-system) can't create/update; only Kyverno's ns spared"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.18.2"
verified_at: "2026-07-18"
confidence: verified
aliases:
  - kyverno blocks kube-system
  - kyverno failurePolicy Fail cluster down
  - kyverno resourceFilters not excluding webhook
  - forceFailurePolicyIgnore
  - kyverno self dos
tags:
  - kyverno
  - troubleshooting
  - admission
  - policy
sources:
  - type: code
    path: charts/kyverno/templates/config/_helpers.tpl
    url: https://github.com/kyverno/kyverno/blob/v1.18.2/charts/kyverno/templates/config/_helpers.tpl
    note: "webhook namespaceSelector only excludes Kyverno's own namespace (kubernetes.io/metadata.name NotIn <ns>)"
  - type: code
    path: charts/kyverno/values.yaml
    url: https://github.com/kyverno/kyverno/blob/v1.18.2/charts/kyverno/values.yaml
    note: "config.resourceFilters lists kube-system/kube-public (policy-skip, NOT webhook-exclude, L331-348); forceFailurePolicyIgnore (L794-796)"
relations:
  - type: see_also
    target: CONCEPT-ADDON_KYVERNO
  - type: see_also
    target: TROUBLE-KYVERNO_WEBHOOK_HA
  - type: see_also
    target: TROUBLE-ADMISSION_WEBHOOK_BLOCKING
---

# Kyverno down → whole cluster (incl. kube-system) can't create/update; only Kyverno's ns spared

## Summary

A subtle but cluster-fatal default: Kyverno's admission webhook **`namespaceSelector` excludes only
Kyverno's own install namespace** — `kube-system`/`kube-public` are listed **only in
`config.resourceFilters`**, which tells Kyverno to *skip policy logic*, **not** to stop the API server
from routing those AdmissionReviews to the webhook. So with any `failurePolicy: Fail` webhook and the
Kyverno admission pods down/unready, **creates and updates cluster-wide — including `kube-system` —
are rejected**; only the Kyverno namespace keeps working. Operators assume `resourceFilters` protects
system namespaces; it does not.

## Problem

- Kyverno pods unhealthy → **everything** fails admission (`failed calling webhook ...kyverno...`),
  including control-plane/system workloads in `kube-system`.
- You had `kube-system` in `resourceFilters` and expected it to be safe — it isn't.
- The cluster can't self-heal because even system pods can't be (re)created.

## Context

- Applies to Kyverno **1.18.x** (chart 3.0.0) ([[CONCEPT-ADDON_KYVERNO]]).
- The chart injects a **single** `namespaceSelector` `matchExpressions` entry: `kubernetes.io/metadata.name
  NotIn <kyverno-ns>` (`_helpers.tpl`@v1.18.2, `kyverno.config.webhooks`). That's the *only* namespace
  the API server won't route to the webhook.
- `config.resourceFilters` (which does list `kube-system`, `kube-public`, etc. —
  `values.yaml`@v1.18.2 L331-348) is a **policy-engine skip list**, applied *after* the AdmissionReview
  already reached Kyverno. If Kyverno is down, the request never gets that far — it just fails the
  webhook call.
- This is the specific default-exclusion topology behind the generic "webhook blocks the cluster"
  problem ([[TROUBLE-KYVERNO_WEBHOOK_HA]], [[TROUBLE-ADMISSION_WEBHOOK_BLOCKING]]).

## Diagnostics

- `kubectl -n kube-system run test --image=pause` fails with a Kyverno webhook error while Kyverno is
  down → confirms system namespaces are exposed.
- `kubectl get validatingwebhookconfiguration -o yaml | grep -A3 namespaceSelector` — only the Kyverno
  ns is excluded; `failurePolicy: Fail` on the webhooks.

## Known Issues

- **Recover now (outage):** flip all Kyverno webhooks to Ignore — set
  `features.forceFailurePolicyIgnore.enabled: true` / start with `--forceFailurePolicyIgnore`
  (`values.yaml`@v1.18.2 L794-796) — or delete the ValidatingWebhookConfiguration to unblock, then fix
  Kyverno.
- **Prevent:** run Kyverno **HA** (multiple admission replicas + PDB — [[TROUBLE-KYVERNO_WEBHOOK_HA]]);
  for critical webhooks weigh `failurePolicy: Ignore` (availability > guaranteed enforcement); and
  **explicitly exclude system namespaces at the webhook level** (namespaceSelector), not just in
  `resourceFilters`.
- **Don't confuse the two lists:** `resourceFilters` = "Kyverno, ignore these"; `namespaceSelector` =
  "API server, don't even call Kyverno for these". Only the latter protects you when Kyverno is down.

## References

- Kyverno `charts/kyverno/templates/config/_helpers.tpl` + `values.yaml` (@v1.18.2). Addon
  [[CONCEPT-ADDON_KYVERNO]]; HA [[TROUBLE-KYVERNO_WEBHOOK_HA]]; generic webhook block
  [[TROUBLE-ADMISSION_WEBHOOK_BLOCKING]].
