---
id: TROUBLE-KEDA_SCALEDOBJECT_NOT_SCALING
type: troubleshooting
title: "KEDA: ScaledObject not scaling / HPA stuck"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.17.0 <=2.20.1"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - keda not scaling
  - scaledobject no external metric
  - keda triggerauthentication failing
  - keda scaler error
tags:
  - troubleshooting
  - keda
  - autoscaling
sources:
  - type: docs
    path: KEDA troubleshooting / FAQ
    url: https://keda.sh/docs/latest/troubleshooting/
    note: "ScaledObject status, operator/metrics-server logs, scaler errors"
relations:
  - type: see_also
    target: CONCEPT-ADDON_KEDA
  - type: see_also
    target: TROUBLE-HPA_NOT_SCALING
---

# KEDA: ScaledObject not scaling / HPA stuck

## Summary

A `ScaledObject` is created but the workload doesn't scale (or won't leave zero). KEDA
translates triggers into an HPA fed by its metrics adapter; the block is usually a
**scaler/trigger auth** error, a **metrics-server/adapter** problem, or `minReplicaCount`
semantics. Read the `ScaledObject` status and KEDA logs.

## Problem

- Replicas stay flat despite load; or scale-to-zero never wakes on events.
- `ScaledObject` shows `Ready: False` / `Fallback` conditions.
- HPA exists but reports `unable to get external metric`.

## Context

- Applies to KEDA **2.17–2.20** (owner runs 2.17.2 — [[CONCEPT-ADDON_KEDA]]). It drives a
  standard HPA — [[TROUBLE-HPA_NOT_SCALING]] still applies.

## Diagnostics

1. `kubectl describe scaledobject <name>` — conditions and the created HPA name; look for
   scaler errors in the events.
2. **Scaler/trigger config:** verify the trigger metadata (queue name, connection, query) and
   the **`TriggerAuthentication`** secret/identity — a bad credential yields "scaler error"
   and no metric.
3. **Metrics adapter:** `kubectl get apiservice v1beta1.external.metrics.k8s.io` should be
   `Available`; check `keda-operator-metrics-apiserver` logs. If the APIService is down, the
   HPA can't read external metrics.
4. **Scale-to-zero:** `minReplicaCount: 0` needs an **activating** trigger value; if the
   scaler can't reach the source it never activates. `idleReplicaCount`/`cooldownPeriod`
   affect wake/idle behaviour.
5. **Operator health:** `keda-operator` logs for reconcile errors.

## Known Issues

- **KEDA 2.17.2** has a Vault-credential path-traversal CVE (**CVE-2025-68476**, fixed
  2.17.3) — relevant if using the Vault trigger-auth provider.
- KEDA follows an **N-2 Kubernetes** support policy (2.17 tested 1.30–1.32); running outside
  the tested window can cause metric-API oddities.

## References

- KEDA troubleshooting (above); addon: [[CONCEPT-ADDON_KEDA]]; HPA basics:
  [[TROUBLE-HPA_NOT_SCALING]].
