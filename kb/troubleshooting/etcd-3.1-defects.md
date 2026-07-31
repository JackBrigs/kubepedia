---
id: TROUBLE-ETCD_3_1_DEFECTS
type: troubleshooting
title: "etcd 3.1: defects fixed in the 3.1 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.1.0 <3.2.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - etcd 3.1 known issues
  - etcd 3.1 fixed in
  - is this etcd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - etcd
sources:
  - type: docs
    path: etcd-io/etcd release notes for the 3.1 line — bug-fix entries
    url: https://github.com/etcd-io/etcd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# etcd 3.1: defects fixed in the 3.1 line

## Summary

**9 defects** the project fixed across **8 releases** of the 3.1 line, from 3.1.3 to
3.1.21. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.1.3

- Fix `etcd gateway` schema handling in DNS discovery
- Fix sd_notify behaviors in `gateway`, `grpc-proxy`

### 3.1.10

- Compile with [*Go 1.8.3*](https://golang.org/doc/devel/release.html#go1.8). Fix panic on `net/http.CloseNotify`

### 3.1.12

- Fix [`mvcc` "unsynced" watcher restore operation](https://github.com/etcd-io/etcd/pull/9297). "unsynced" watcher is watcher that needs to be in sync with events that have happened. That is, "unsynced" watcher is the slow watcher that was requested on old revision. "unsynced" watcher restore operation was not correctly populating its underlying watcher group. Which possibly causes [missing events from "unsynced" watchers](https://github.com/etcd-io/etcd/issues/9086). A node gets network partitioned with a watcher on a future revision, and falls behind receiving a leader snapshot after partition gets removed. When applying this snapshot, etcd watch storage moves current synced watchers to unsynced since sync watchers might have become stale during network partition. And reset synced watcher group to restart watcher routines. Previously, there was a bug when moving from synced watcher group to unsynced, thus client would miss events when the watcher was requested to the network-partitioned node

### 3.1.16

- Fix [`mvcc` server panic from restore operation](https://github.com/etcd-io/etcd/pull/9775). Let's assume that a watcher had been requested with a future revision X and sent to node A that became network-partitioned thereafter. Meanwhile, cluster makes progress. Then when the partition gets removed, the leader sends a snapshot to node A. Previously if the snapshot's latest revision is still lower than the watch revision X, **etcd server panicked** during snapshot restore operation. Now, this server-side panic has been fixed

### 3.1.17

- Fix [v3 snapshot recovery](https://github.com/etcd-io/etcd/issues/7628). A follower receives a leader snapshot to be persisted as a `[SNAPSHOT-INDEX].snap.db` file on disk. Now, server [ensures that the incoming snapshot be persisted on disk before loading it](https://github.com/etcd-io/etcd/pull/7876). Otherwise, index mismatch happens and triggers server-side panic (e.g. newer WAL entry with outdated snapshot index)

### 3.1.19

- Fix [lease keepalive interval updates when response queue is full](https://github.com/etcd-io/etcd/pull/9952). If `<-chan *clientv3LeaseKeepAliveResponse` from `clientv3.Lease.KeepAlive` was never consumed or channel is full, client was [sending keepalive request every 500ms](https://github.com/etcd-io/etcd/issues/9911) instead of expected rate of every "TTL / 3" duration

### 3.1.20

- Fix logic on [release lock key if cancelled](https://github.com/etcd-io/etcd/pull/10153) in `clientv3/concurrency` package

### 3.1.21

- Fix bug where [db_compaction_total_duration_milliseconds metric incorrectly measured duration as 0](https://github.com/etcd-io/etcd/pull/10646)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.1.21**, the newest release recorded here for this line.

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
