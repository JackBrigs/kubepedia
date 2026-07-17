---
id: TROUBLE-VMAGENT_REMOTE_WRITE_FAILING
type: troubleshooting
title: "VictoriaMetrics: vmagent not ingesting / remote-write backlog"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.100.0 <=1.147.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - vmagent remote write failing
  - victoriametrics no data
  - vmagent persistentqueue growing
  - vm high cardinality
tags:
  - troubleshooting
  - victoriametrics
  - observability
  - metrics
sources:
  - type: docs
    path: vmagent troubleshooting
    url: https://docs.victoriametrics.com/vmagent/#troubleshooting
    note: "remote-write queues, scrape, cardinality"
relations:
  - type: see_also
    target: CONCEPT-ADDON_VM_K8S_STACK
  - type: see_also
    target: CONCEPT-OBSERVABILITY_STACK
---

# VictoriaMetrics: vmagent not ingesting / remote-write backlog

## Summary

Metrics are missing in VictoriaMetrics, or `vmagent`'s on-disk queue keeps growing. Usually
either **scraping** isn't discovering targets, **remote-write** to vmstorage/vmsingle is
failing (network/auth/overload), or **high cardinality** is throttling ingestion.

## Problem

- Dashboards show gaps / no data for some targets.
- `vmagent` persistent queue (`-remoteWrite.tmpDataPath`) grows; `vmagent_remotewrite_*`
  error metrics rise.
- vmstorage/vmsingle OOM or rejecting samples.

## Context

- Applies to the VM stack **1.100–1.147** (owner runs 1.115.0 —
  [[CONCEPT-ADDON_VM_K8S_STACK]], [[CONCEPT-OBSERVABILITY_STACK]]).

## Diagnostics

1. **Scrape side:** check `vmagent` `/targets` — targets `up`? Missing targets = bad
   `VMServiceScrape`/`ServiceMonitor` selector, RBAC, or namespace scoping.
2. **Remote-write side:** `vmagent` logs + `vmagent_remotewrite_errors_total` — connection
   refused/401/5xx to the storage URL. Verify the `-remoteWrite.url`, auth, and that
   vmstorage/vmsingle is healthy and not out of disk.
3. **Backlog:** a growing on-disk queue means the remote endpoint can't keep up — scale
   vmstorage/vmsingle, raise resources, or check network. Data is buffered (not lost) until
   the queue's max is hit.
4. **High cardinality:** `vm_rows`, cardinality explorer — a few label combinations
   (e.g. per-pod UID, per-request IDs) can blow up series count and throttle ingestion; drop
   or relabel offending labels.
5. **CRD drift:** `helm upgrade` does NOT update VM CRDs — a stale CRD can break new scrape
   objects; apply CRDs manually.

## Known Issues

- VM **1.115.0** is affected by a low-severity Snappy-decoder DoS (**CVE-2025-65942**, fixed
  1.122.8).

## References

- vmagent troubleshooting (above); addon: [[CONCEPT-ADDON_VM_K8S_STACK]]; hub:
  [[CONCEPT-OBSERVABILITY_STACK]].
