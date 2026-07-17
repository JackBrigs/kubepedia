---
id: TROUBLE-ETCD_DB_SPACE_EXCEEDED
type: troubleshooting
title: "etcd: mvcc database space exceeded (NOSPACE alarm)"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.5.0 <=3.7.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - etcdserver mvcc database space exceeded
  - etcd NOSPACE alarm
  - etcd defrag
  - apiserver read-only etcd full
tags:
  - troubleshooting
  - etcd
  - control-plane
sources:
  - type: docs
    path: etcd maintenance (compaction/defrag/alarms)
    url: https://etcd.io/docs/latest/op-guide/maintenance/
    note: "quota-backend-bytes, compaction, defrag, disarm alarm"
relations:
  - type: see_also
    target: COMPONENT-ETCD
  - type: see_also
    target: TROUBLE-ETCD_QUORUM_LOSS
---

# etcd: mvcc database space exceeded (NOSPACE alarm)

## Summary

The API server starts failing writes with `etcdserver: mvcc: database space exceeded`. etcd
hit its backend **quota** and raised a **NOSPACE alarm**, which puts the cluster into
**read-only** until you compact, defragment, and **disarm** the alarm.

## Problem

- `kubectl apply`/writes fail cluster-wide; reads still work.
- API server logs `mvcc: database space exceeded`.
- `etcdctl endpoint status` shows the DB size near `--quota-backend-bytes`.

## Context

- Applies to etcd **3.5.x–3.7.0** (base ships 3.5.23–3.6.10 via Kubespray — [[COMPONENT-ETCD]]).
- Default quota is modest (historically ~2 GiB, often raised to 8 GiB). Space grows from
  keyspace history that hasn't been compacted, plus fragmentation.

## Diagnostics

1. Confirm the alarm: `etcdctl alarm list` → `NOSPACE`.
2. **Compact** the keyspace to the current revision:
   `rev=$(etcdctl endpoint status -w json | jq '.[0].Status.header.revision); etcdctl compact $rev`.
3. **Defragment** each member (one at a time — it briefly blocks that member):
   `etcdctl defrag --endpoints=<member>`.
4. **Disarm** the alarm: `etcdctl alarm disarm`. Writes resume.
5. Prevent recurrence: ensure **auto-compaction** is configured
   (`--auto-compaction-mode=periodic --auto-compaction-retention=8h` or revision-based) and
   consider raising `--quota-backend-bytes` (e.g. 8 GiB). An automated defrag controller can
   run periodic defrag ([[CONCEPT-ADDON_ETCD_DEFRAG_CONTROLLER]]).

## Known Issues

- Defrag on all members simultaneously can drop quorum — always **one member at a time**,
  off-peak ([[TROUBLE-ETCD_QUORUM_LOSS]]).
- A full disk is a different, harder failure — free disk before compaction can help.

## References

- etcd maintenance docs (above); component: [[COMPONENT-ETCD]]; quorum:
  [[TROUBLE-ETCD_QUORUM_LOSS]].
