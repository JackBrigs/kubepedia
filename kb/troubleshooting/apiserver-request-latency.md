---
id: TROUBLE-APISERVER_REQUEST_LATENCY
type: troubleshooting
title: "kube-apiserver: request latency from audit / admission"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - apiserver slow create update
  - audit log backpressure
  - admission webhook latency
  - apiserver_admission_webhook_admission_duration_seconds
tags:
  - troubleshooting
  - apiserver
  - audit
  - admission
  - latency
sources:
  - type: docs
    path: Auditing (modes / batching)
    url: https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/
    note: "blocking vs batch, buffer/throttle"
  - type: docs
    path: apiserver admission metrics
    url: https://kubernetes.io/docs/reference/instrumentation/metrics/
relations:
  - type: see_also
    target: TROUBLE-ADMISSION_WEBHOOK_BLOCKING
  - type: see_also
    target: TROUBLE-APISERVER_APF_429
---

# kube-apiserver: request latency from audit / admission

## Summary

Create/update requests are slow across the board and the delay is in **audit** or **admission**
— both run synchronously in the request path, so a slow audit backend or a slow
plugin/webhook/CEL condition inflates every matching request's latency.

## Problem

- All create/update requests slow; latency localized to audit or admission (not etcd).
- In `blocking` audit mode, response is delayed until the audit event is processed; in `batch`
  mode, audit events silently drop on buffer overflow.

## Context

- Applies to Kubernetes **1.29–1.35**. Webhook **blocking** (fail-closed) is a separate class
  ([[TROUBLE-ADMISSION_WEBHOOK_BLOCKING]]); this doc is about **latency**.

## Diagnostics

**Audit backpressure:**

- `--audit-log-mode`/`--audit-webhook-mode`: **`blocking`/`blocking-strict`** couple each
  request's latency to the audit backend (strict also *fails* the request if audit fails at
  RequestReceived); **`batch`** buffers up to `--audit-webhook-batch-buffer-size` (default
  10000) and **drops** on overflow. Metrics: `apiserver_audit_event_total`,
  `apiserver_audit_error_total`, `apiserver_audit_requests_rejected_total`.
- **Fix:** prefer **`batch`**; tune `--audit-webhook-batch-max-size` / `-max-wait` /
  `-throttle-qps`/`-burst`; increase the buffer if dropping; **narrow the audit Policy**
  (`Metadata` not `RequestResponse` for chatty resources). Reserve `blocking-strict` for
  completeness-over-availability.

**Admission latency:**

- Metrics pinpoint it: `apiserver_admission_step_admission_duration_seconds`,
  `apiserver_admission_controller_admission_duration_seconds` (per built-in plugin, label
  `name`), **`apiserver_admission_webhook_admission_duration_seconds`** (per webhook),
  `apiserver_admission_match_condition_evaluation_seconds` (CEL match conditions).
- **Fix:** narrow webhook match scope (namespace/objectSelector, specific resources/verbs);
  tight `timeoutSeconds`; fast/HA backend; `failurePolicy: Ignore` for non-critical; prefer
  in-process **ValidatingAdmissionPolicy** (CEL) over external webhooks.

## Known Issues

- A slow webhook is both a latency source *and* (fail-closed) an availability risk — see
  [[TROUBLE-ADMISSION_WEBHOOK_BLOCKING]].

## References

- Audit docs + admission metrics (above); APF interaction: [[TROUBLE-APISERVER_APF_429]].
