---
id: TROUBLE-KYVERNO_WEBHOOK_HA
type: troubleshooting
title: "Kyverno: webhook blocks cluster / latency / HA leader flapping"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=1.10.0 <=1.18.2"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - kyverno failurepolicy fail blocks cluster
  - kyverno webhook timeout latency
  - kyverno leftover webhook configs
  - kyverno leadership lost crashloop
tags:
  - troubleshooting
  - kyverno
  - webhooks
  - policy
sources:
  - type: docs
    path: kyverno issue #2962 (fail-closed blocks cluster)
    url: https://github.com/kyverno/kyverno/issues/2962
    note: "Kyverno down + failurePolicy Fail rejects all ops"
  - type: docs
    path: kyverno issue #8635 (admission latency under load)
    url: https://github.com/kyverno/kyverno/issues/8635
    note: "client-go QPS throttling; raise clientRateLimit*"
relations:
  - type: see_also
    target: CONCEPT-ADDON_KYVERNO
  - type: see_also
    target: TROUBLE-ADMISSION_WEBHOOK_BLOCKING
---

# Kyverno: webhook blocks cluster / latency / HA leader flapping

## Summary

Community-sourced Kyverno webhook/HA failures — the most dangerous being **fail-closed
deadlock**: when Kyverno is down and `failurePolicy: Fail`, its webhook rejects **every**
resource operation cluster-wide (even pod deletion / taint removal), which can prevent
self-healing.

## Problem

- All API operations rejected when Kyverno pods are unavailable (`failurePolicy: Fail`).
- Admission latency jumps (>3s), webhook timeouts, apiserver `context deadline exceeded` under
  load spikes.
- After a node/network outage, `node.kubernetes.io/unreachable` taints never clear (bootstrap
  deadlock).
- Controllers CrashLoopBackOff with `leadership lost, stopped leading`.

## Context

- Applies to Kyverno **1.10–1.18** ([[CONCEPT-ADDON_KYVERNO]]); a specialization of the
  webhook blast radius [[TROUBLE-ADMISSION_WEBHOOK_BLOCKING]].

## Diagnostics

- **Fail-closed deadlock (emergency):** delete the Kyverno validating (and if needed mutating)
  webhook configs — e.g. `kubectl delete validatingwebhookconfiguration
  kyverno-resource-validating-webhook-cfg` — then restart Kyverno. Taints auto-clear and pods
  schedule (issues #2962, #11893).
- **Prevent it:** `failurePolicy: Ignore` for non-critical policies; exclude `kube-system` and
  Kyverno's namespace via `namespaceSelector`/`objectSelector`.
- **Latency/timeouts under load:** default client-go QPS 5 / burst 10 throttles the controller
  during admission/informer spikes — raise **`--clientRateLimitQPS`** and
  **`--clientRateLimitBurst`**, scale admission replicas, tune the webhook timeout (issue #8635).
- **Leader flapping / CrashLoop:** cold-start informer LIST bursts exhaust the client-go rate
  limiter so the lease-renewal PUT misses its deadline (`context deadline exceeded` on the
  lease) — raise the same `clientRateLimit*` flags (issue #15998). Note: non-leader
  background/cleanup replicas exiting on changeover is the leader-only-active HA model
  (issue #13010) — a single replica avoids the ~5-min restart churn.

## Known Issues

- **Uninstall/upgrade leftovers:** webhook configs can remain after uninstall (esp. ArgoCD,
  which ignores Helm `pre-delete` hooks) → fail-closed deadlock. Modern charts ship empty
  (`webhooks: []`) configs so they're GC'd; emergency `--forceFailurePolicyIgnore` or manual
  delete (issues #9551/#8390).

## References

- kyverno issues #2962/#11893/#8635/#15998/#13010/#9551 (above); addon:
  [[CONCEPT-ADDON_KYVERNO]]; webhook class: [[TROUBLE-ADMISSION_WEBHOOK_BLOCKING]].
