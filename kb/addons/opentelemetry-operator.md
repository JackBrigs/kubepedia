---
id: CONCEPT-ADDON_OTEL_OPERATOR
type: concept
title: "OpenTelemetry Operator — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.25 <=1.35"
component_version: "0.156.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - opentelemetry-operator
  - otel operator
  - opentelemetry
tags:
  - addons
  - observability
  - tracing
  - opentelemetry
sources:
  - type: code
    path: charts/opentelemetry-operator/Chart.yaml
    url: https://raw.githubusercontent.com/open-telemetry/opentelemetry-helm-charts/opentelemetry-operator-0.120.0/charts/opentelemetry-operator/Chart.yaml
    note: "no kubeVersion; appVersion 0.156.0"
  - type: docs
    path: operator compatibility.md
    url: https://raw.githubusercontent.com/open-telemetry/opentelemetry-operator/v0.156.0/docs/getting-started/compatibility.md
    note: "supported K8s v1.25–v1.35"
relations:
  - type: see_also
    target: TROUBLE-OTEL_OPERATOR
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
---

# OpenTelemetry Operator — addon

## Summary

The OpenTelemetry Operator manages Collector and auto-instrumentation resources via CRDs.
Latest chart **0.120.0** → operator/Collector **v0.156.0**. Its supported Kubernetes window
is **v1.25–v1.35** — fully covering the base range. It **requires cert-manager** for webhook
TLS unless another cert mode is configured.

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]]. The inventory lists both
  `opentelemetry` and `opentelemetry-operator (all versions)`; this doc covers the operator.

## Implementation

- Chart→app: `opentelemetry-operator-0.120.0` → **v0.156.0** (operator + Collector), plus
  auto-instrumentation images (Java 2.29.0, .NET 1.16.0, Node.js 0.78.0, Python 0.64b0,
  Go 0.24.0).
- Chart `kubeVersion`: **none**; the effective support range is the operator's
  `compatibility.md`: **1.25–1.35** (`MIN_KUBERNETES_VERSION 1.25.0`, CI default 1.35).

## Configuration

- **cert-manager (v1) is required** for the webhook TLS by default — install it first or
  the operator webhook fails until certs are issued.
- v0.156.0: `disablePrometheusAnnotations: true` now also strips operator-stamped
  `prometheus.io/*` annotations on update (#5043).

## Compatibility

- **Breaking changes across chart 0.110→0.120:** removed `manager.featureGates` (use
  `manager.featureGatesMap`, else schema validation fails); **kube-rbac-proxy removed**
  (operator v0.142.0+): metrics moved under `manager.metrics` + `manager.ports.metricsPort`,
  default `secure: true` on 8443, deployment drops to a single container.
- **Known issues:** webhook/cert-manager readiness ordering; TargetAllocator
  scrape-target distribution/discovery.
- **CVEs (v0.156.0):** none found. GHSA-cxh2-4639-vmc5 (TargetAllocator local file read) is
  fixed in 0.152.0, so 0.156.0 is not affected.

## References

- `Chart.yaml`, `compatibility.md`, `UPGRADING.md`, v0.156.0 release notes (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]].
