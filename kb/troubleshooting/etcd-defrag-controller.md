---
id: TROUBLE-ETCD_DEFRAG_CONTROLLER
type: troubleshooting
title: "etcd-defrag-controller: latency spikes / defrag not reclaiming space — stop-the-world, one member at a time"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "0.0.7"
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - etcd defrag latency
  - etcd defrag controller
  - defrag stop the world
  - etcd space not reclaimed
tags:
  - troubleshooting
  - etcd
  - maintenance
sources:
  - type: external
    path: etcd_defrag_controller
    url: https://github.com/kaasops/etcd-defrag-controller
    note: "defrag is a blocking per-member op that reclaims space after compaction; run one member at a time"
relations:
  - type: see_also
    target: CONCEPT-ADDON_ETCD_DEFRAG_CONTROLLER
  - type: see_also
    target: COMPONENT-ETCD
  - type: see_also
    target: TROUBLE-ETCD_DB_SPACE_EXCEEDED
---

# etcd-defrag-controller: latency spikes / defrag not reclaiming space — stop-the-world, one member at a time

## Summary

The controller automates `etcdctl defrag`, which reclaims disk after compaction. The catch: **defrag is a stop-the-world, blocking operation per member** — while a member defrags it doesn't serve, so a mistimed or all-at-once defrag causes **API latency spikes** or a transient quorum wobble. Chart/app `v0.0.7`.

## Problem

- etcd/API **latency spikes** correlated with defrag runs, or the etcd DB **doesn't shrink** despite the controller running.

## Context

- etcd-defrag-controller `0.0.7` ([[CONCEPT-ADDON_ETCD_DEFRAG_CONTROLLER]]) over etcd ([[COMPONENT-ETCD]]).
- **Blocking op:** each member is unavailable during its own defrag; the controller should defrag **one member at a time**, never simultaneously, and ideally off leader/peak.
- **Space only frees after compaction:** defrag reclaims what compaction freed — if the DB is genuinely full of live keys, defrag won't shrink it ([[TROUBLE-ETCD_DB_SPACE_EXCEEDED]]).

## Diagnostics

```bash
kubectl -n <ns> logs deploy/etcd-defrag-controller | tail
etcdctl endpoint status --write-out=table   # DB size per member before/after
```

## Known Issues

- **Latency — fix:** ensure serialized, one-member-at-a-time defrag; schedule off-peak; keep the interval sane (defrag isn't needed constantly).
- **No shrink — fix:** confirm compaction runs first (auto-compaction retention); defrag after compaction actually reclaims. If the DB is space-exceeded from live data, address quota/keys ([[TROUBLE-ETCD_DB_SPACE_EXCEEDED]]).

## References

Upstream project (see `sources`). Catalog entry [[CONCEPT-ADDON_ETCD_DEFRAG_CONTROLLER]].
