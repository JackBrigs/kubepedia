---
id: TROUBLE-APISERVER_ETCD_LATENCY
type: troubleshooting
title: "kube-apiserver: latency/timeouts cascading from slow etcd"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - apiserver slow etcd
  - etcdserver request timed out
  - etcd wal fsync slow
  - kubectl hangs writes stall
tags:
  - troubleshooting
  - apiserver
  - etcd
  - latency
sources:
  - type: docs
    path: apiserver/etcd troubleshooting (Azure)
    url: https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/create-upgrade-delete/troubleshoot-apiserver-etcd
    note: "etcd latency → apiserver request duration"
  - type: docs
    path: Kubernetes metrics reference
    url: https://kubernetes.io/docs/reference/instrumentation/metrics/
relations:
  - type: see_also
    target: TROUBLE-ETCD_DB_SPACE_EXCEEDED
  - type: see_also
    target: TROUBLE-ETCD_QUORUM_LOSS
  - type: see_also
    target: TROUBLE-APISERVER_APF_429
---

# kube-apiserver: latency/timeouts cascading from slow etcd

## Summary

`kubectl` hangs/times out; **writes and cache-miss reads stall** while cached reads still work.
Every write and cache-miss read hits **etcd**, which is fsync-latency sensitive — slow etcd
inflates apiserver request duration and trips APF (429/408/503).

## Problem

- `kubectl` slow/timeouts; writes fail. apiserver logs `etcdserver: request timed out`,
  `context deadline exceeded`.
- 429/408/503 rise (APF backpressure from held seats).

## Context

- Applies to Kubernetes **1.29–1.35**. Related etcd docs: space
  ([[TROUBLE-ETCD_DB_SPACE_EXCEEDED]]) and quorum ([[TROUBLE-ETCD_QUORUM_LOSS]]).

## Diagnostics

- **Key metrics:** `etcd_disk_wal_fsync_duration_seconds` and
  `etcd_disk_backend_commit_duration_seconds` (healthy p99 **<10 ms**; **disk-bound** if
  sustained >100 ms), `etcd_request_duration_seconds`,
  `apiserver_storage_db_total_size_in_bytes`.
- **Common causes:** slow/network disks (etcd needs low-latency fsync), an **oversized DB**
  (8 GB quota; >2 GB is "large"), **leaked objects** (>10k of a type), or etcd **leader
  changes**.
- **Fixes:** put etcd on **dedicated local NVMe**; enable **compaction**
  (`--auto-compaction-retention`) + periodic **defrag**; run **3 or 5** members; **offload
  Events** to a separate etcd (`--etcd-servers-overrides`); delete leaked objects and enforce
  object-count quotas/TTLs.
- The apiserver-side symptom (429) is APF reacting to held seats — [[TROUBLE-APISERVER_APF_429]].

## Known Issues

- etcd **defrag** briefly blocks that member — do one member at a time; a defrag can transiently
  spike apiserver latency ([[TROUBLE-ETCD_DB_SPACE_EXCEEDED]]).

## References

- Azure apiserver/etcd troubleshooting + metrics reference (above). etcd:
  [[TROUBLE-ETCD_DB_SPACE_EXCEEDED]], [[TROUBLE-ETCD_QUORUM_LOSS]].
