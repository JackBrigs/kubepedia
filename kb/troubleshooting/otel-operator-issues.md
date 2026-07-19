---
id: TROUBLE-OTEL_OPERATOR
type: troubleshooting
title: "OpenTelemetry Operator: Collector not reconciled / auto-instrumentation not injecting (cert-manager, webhook)"
status: active
kubespray_version: null
kubernetes_version: ">=1.25 <=1.35"
component_version: ">=0.156.0"
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - opentelemetry operator webhook
  - otel collector not created
  - otel auto-instrumentation not working
  - otel operator needs cert-manager
  - opentelemetrycollector crd
tags:
  - troubleshooting
  - observability
  - opentelemetry
  - admission
sources:
  - type: external
    path: opentelemetry-operator
    url: https://github.com/open-telemetry/opentelemetry-operator
    note: "requires cert-manager for webhook TLS by default; Instrumentation injection via pod annotation"
relations:
  - type: see_also
    target: CONCEPT-ADDON_OTEL_OPERATOR
  - type: see_also
    target: CONCEPT-ADDON_CERT_MANAGER
  - type: see_also
    target: TROUBLE-WEBHOOK_CERT_MANAGER_ORDERING
  - type: see_also
    target: CONCEPT-COMPONENT_INTERACTION_FAILURES
---

# OpenTelemetry Operator: Collector not reconciled / auto-instrumentation not injecting (cert-manager, webhook)

## Summary

The OTel Operator reconciles Collectors and injects auto-instrumentation through **admission webhooks** that need **cert-manager** TLS by default. If cert-manager isn't ready the webhook has no cert and nothing reconciles; injection additionally needs a per-pod annotation and an `Instrumentation` CR.

## Problem

- An `OpenTelemetryCollector` CR is created but **no Collector pod appears**, or the operator logs
  webhook/TLS errors.
- **Auto-instrumentation** doesn't happen — pods start without the injected init container / SDK env.

## Context

- OTel Operator `v0.156.0` ([[CONCEPT-ADDON_OTEL_OPERATOR]]); supports K8s 1.25–1.35.
- **cert-manager dependency:** by default the operator's admission/conversion webhooks get TLS from
  **cert-manager** ([[CONCEPT-ADDON_CERT_MANAGER]]). If cert-manager isn't installed/ready, the webhook
  has no serving cert → the operator can't validate/convert CRs → Collectors aren't reconciled. This is
  the classic cert-manager↔webhook ordering seam ([[TROUBLE-WEBHOOK_CERT_MANAGER_ORDERING]],
  [[CONCEPT-COMPONENT_INTERACTION_FAILURES]]).
- **Auto-instrumentation** is opt-in per pod via an annotation
  (`instrumentation.opentelemetry.io/inject-<lang>: "true"`) that references an `Instrumentation` CR in
  a reachable namespace; the mutating webhook injects the SDK. No annotation / missing CR / webhook down
  → no injection.

## Diagnostics

```bash
kubectl -n opentelemetry-operator-system logs deploy/opentelemetry-operator-controller-manager | tail
kubectl get validatingwebhookconfiguration,mutatingwebhookconfiguration | grep opentelemetry
kubectl get certificate -A | grep opentelemetry        # cert-manager issued the webhook cert?
kubectl get opentelemetrycollector,instrumentation -A
```

## Known Issues

- **Webhook/TLS — fix:** install and make cert-manager healthy **before** the operator (or configure a
  non-cert-manager cert source); confirm the webhook `Certificate` is `Ready` and the
  webhookconfiguration `caBundle` is populated.
- **Collector not created — fix:** with the webhook healthy, `kubectl describe` the CR for admission
  errors (invalid config/mode); the operator only builds the Collector once the CR validates.
- **No injection — fix:** add the `inject-<lang>` annotation to the **pod template** (not just the
  Deployment metadata), ensure the referenced `Instrumentation` CR exists and is reachable, and confirm
  the mutating webhook is `Running`. Injection happens at pod creation — restart the workload after
  adding the annotation.

## References

- opentelemetry-operator upstream. Addon [[CONCEPT-ADDON_OTEL_OPERATOR]]; cert-manager
  [[CONCEPT-ADDON_CERT_MANAGER]]; webhook ordering [[TROUBLE-WEBHOOK_CERT_MANAGER_ORDERING]].
