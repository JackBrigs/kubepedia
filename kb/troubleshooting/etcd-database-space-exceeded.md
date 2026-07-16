---
id: TROUBLE-ETCD_DB_SPACE_EXCEEDED
type: troubleshooting
title: "etcd 'mvcc: database space exceeded' — API writes fail"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - etcd-database-space-exceeded
tags:
  - troubleshooting
  - operations
  - etcd
sources:
  - type: docs
    url: https://etcd.io/docs/latest/op-guide/maintenance/
    note: "etcd maintenance (compaction/defrag/quota)"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd 'mvcc: database space exceeded' — API writes fail

## Summary

The API server starts rejecting writes and etcd logs `mvcc: database space exceeded`. etcd went read-only after hitting its storage quota (`etcd_quota_backend_bytes`, default 2 GiB).

## Problem

etcd keeps a revision history; without regular auto-compaction + defragmentation the backend DB grows past `etcd_quota_backend_bytes` and etcd raises a NOSPACE alarm, blocking writes.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0` clusters. This is a general Kubernetes/component operational issue (not tied to one Kubespray version); the relevant tunables are noted in Known Issues.

## Diagnostics

```bash
etcdctl endpoint status --write-out=table   # DB SIZE near the quota?
etcdctl alarm list                          # NOSPACE alarm present?
```

## Known Issues

Compact and defragment, then disarm the alarm: `etcdctl compact <rev>`, `etcdctl defrag` (one member at a time, see PRACTICE-ETCD_BACKUP_RESTORE), `etcdctl alarm disarm`. Prevent recurrence with auto-compaction and, if needed, a larger `etcd_quota_backend_bytes`.

## References

- https://etcd.io/docs/latest/op-guide/maintenance/ — etcd maintenance (compaction/defrag/quota) (verified behavior, 2026-07-16).
