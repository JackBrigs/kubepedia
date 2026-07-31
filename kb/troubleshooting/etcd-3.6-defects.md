---
id: TROUBLE-ETCD_3_6_DEFECTS
type: troubleshooting
title: "etcd 3.6: defects fixed in the 3.6 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.6.0 <3.7.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - etcd 3.6 known issues
  - etcd 3.6 fixed in
  - is this etcd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - etcd
sources:
  - type: docs
    path: etcd-io/etcd release notes for the 3.6 line — bug-fix entries
    url: https://github.com/etcd-io/etcd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# etcd 3.6: defects fixed in the 3.6 line

## Summary

**22 defects** the project fixed across **10 releases** of the 3.6 line, from 3.6.1 to
3.6.13. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.6.1

- [Fix the issue that `--force-new-cluster` can't remove all other members in a corner case](https://github.com/etcd-io/etcd/pull/20071)
- Fix [mvcc: avoid double decrement of watcher gauge on close/cancel race](https://github.com/etcd-io/etcd/pull/20067)
- Fix [command `etcdctl endpoint health` doesn't work when options are set via environment variables](https://github.com/etcd-io/etcd/pull/20121)

### 3.6.2

- Fix [Watch on future revision returns old events or notifications](https://github.com/etcd-io/etcd/pull/20286)

### 3.6.3

- Fix [v2store check (IsMetaStoreOnly) returns wrong result even there is no any auth data](https://github.com/etcd-io/etcd/pull/20370)

### 3.6.4

- Fix [etcdserver bootstrap failure when replaying learner promotion operation due to not exist in v3store](https://github.com/etcd-io/etcd/pull/20387)

### 3.6.5

- Fix [etcd repeatedly log the error "cannot detect storage schema version: missing confstate information"](https://github.com/etcd-io/etcd/pull/20496)
- Fix [etcd may return success for leaseRenew request even when the lease is revoked](https://github.com/etcd-io/etcd/pull/20615)
- Fix [potential data corruption when applySnapshot and defragment happen concurrently](https://github.com/etcd-io/etcd/pull/20650)

### 3.6.6

- Fix [endpoint status not retuning the correct storage quota](https://github.com/etcd-io/etcd/pull/20790)
- Fix [`--force-new-cluster can't clean up learners after creating snapshot`](https://github.com/etcd-io/etcd/pull/20896)
- Fix [duplicate metrics collector registration that caused warning messages](https://github.com/etcd-io/etcd/pull/20905)
- Fix [cannot promote member from follower when auth is enabled](https://github.com/etcd-io/etcd/pull/20874)

### 3.6.9

- Fix [Race between read index and leader change](https://github.com/etcd-io/etcd/pull/21378)
- Fix [Stale reads caused by process pausing](https://github.com/etcd-io/etcd/pull/21417)
- [server/etcdmain: fix startup deadlock in grpcproxy](https://github.com/etcd-io/etcd/pull/21354)
- Fix [slice bounds trimming single-quoted args in Argify](https://github.com/etcd-io/etcd/pull/21402)

### 3.6.10

- Fix [etcdctl endpoint command regression with option --cluster when auth is enabled](https://github.com/etcd-io/etcd/pull/21530)

### 3.6.11

- [Fixed an issue that prevented adding a new member when one member was down, even though quorum was still satisfied](https://github.com/etcd-io/etcd/pull/21667)
- Fix RBAC authorization bypass allowing read access via PrevKv or lease attachment in Put requests nested in etcd transactions (see [PR/21681](https://github.com/etcd-io/etcd/pull/21681) and [PR/21685](https://github.com/etcd-io/etcd/pull/21685))

### 3.6.13

- Fix [websocket authentication with bearer-prefixed auth tokens](https://github.com/etcd-io/etcd/pull/21932)
- Fix [CRL enforcement bypass on gRPC listener when `--listen-client-http-urls` is configured](https://github.com/etcd-io/etcd/pull/22025), refer to [security/advisories/GHSA-3wh4-j44w-pg92](https://github.com/etcd-io/etcd/security/advisories/GHSA-3wh4-j44w-pg92) for more details


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.6.13**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `etcd-io/etcd`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/etcd.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
