---
id: TROUBLE-ETCD_3_2_DEFECTS
type: troubleshooting
title: "etcd 3.2: defects fixed in the 3.2 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.2.0 <3.3.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - etcd 3.2 known issues
  - etcd 3.2 fixed in
  - is this etcd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - etcd
sources:
  - type: docs
    path: etcd-io/etcd release notes for the 3.2 line — bug-fix entries
    url: https://github.com/etcd-io/etcd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# etcd 3.2: defects fixed in the 3.2 line

## Summary

**29 defects** the project fixed across **21 releases** of the 3.2 line, from 3.2.1 to
3.2.31. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.2.1

- Fix backend database in-memory index corruption issue on restore (only 3.2.0 is affected)

### 3.2.5

- Fix unreachable `/metrics` endpoint when `--enable-v2=false`

### 3.2.6

- Fix multiple URLs for `--listen-peer-urls` flag
- Fix `etcd_debugging_mvcc_keys_total` inconsistency

### 3.2.7

- Fix [`concurrency/stm` Put with serializable snapshot](https://github.com/etcd-io/etcd/pull/8439). Use store revision from first fetch to resolve write conflicts instead of modified revision

### 3.2.8

- Fix v2 client failover to next endpoint on mutable operation

### 3.2.11

- Fix racey grpc-go's server handler transport `WriteStatus` call to prevent [TLS-enabled etcd server crash](https://github.com/etcd-io/etcd/issues/8904)

### 3.2.12

- Fix [error message of `Revision` compactor](https://github.com/etcd-io/etcd/pull/8999) in server-side
- Add [`MaxCallSendMsgSize` and `MaxCallRecvMsgSize`](https://github.com/etcd-io/etcd/pull/9047) fields to [`clientv3.Config`](https://godoc.org/github.com/etcd-io/etcd/clientv3#Config). Fix [exceeded response size limit error in client-side](https://github.com/etcd-io/etcd/issues/9043). Address [kubernetes#51099](https://github.com/kubernetes/kubernetes/issues/51099). In previous versions(v3.2.10, v3.2.11), client response size was limited to only 4 MiB. `MaxCallSendMsgSize` default value is 2 MiB, if not configured. `MaxCallRecvMsgSize` default value is `math.MaxInt32`, if not configured

### 3.2.13

- Fix [gRPC server panic on `GracefulStop` TLS-enabled server](https://github.com/etcd-io/etcd/pull/8987)

### 3.2.14

- Fix [`mvcc/backend.defragdb` nil-pointer dereference on create bucket failure](https://github.com/etcd-io/etcd/pull/9119)

### 3.2.15

- Prevent [server panic from member update/add](https://github.com/etcd-io/etcd/pull/9174) with [wrong scheme URLs](https://github.com/etcd-io/etcd/issues/9173)

### 3.2.16

- Fix [`mvcc` "unsynced" watcher restore operation](https://github.com/etcd-io/etcd/pull/9297). "unsynced" watcher is watcher that needs to be in sync with events that have happened. That is, "unsynced" watcher is the slow watcher that was requested on old revision. "unsynced" watcher restore operation was not correctly populating its underlying watcher group. Which possibly causes [missing events from "unsynced" watchers](https://github.com/etcd-io/etcd/issues/9086). A node gets network partitioned with a watcher on a future revision, and falls behind receiving a leader snapshot after partition gets removed. When applying this snapshot, etcd watch storage moves current synced watchers to unsynced since sync watchers might have become stale during network partition. And reset synced watcher group to restart watcher routines. Previously, there was a bug when moving from synced watcher group to unsynced, thus client would miss events when the watcher was requested to the network-partitioned node

### 3.2.17

- Fix [server panic on invalid Election Proclaim/Resign HTTP(S) requests](https://github.com/etcd-io/etcd/pull/9379). Previously, wrong-formatted HTTP requests to Election API could trigger panic in etcd server. e.g. `curl -L http://localhost:2379/v3/election/proclaim -X POST -d '{"value":""}'`, `curl -L http://localhost:2379/v3/election/resign -X POST -d '{"value":""}'`
- Prevent [overflow by large `TTL` values for `Lease` `Grant`](https://github.com/etcd-io/etcd/pull/9399). `TTL` parameter to `Grant` request is unit of second. Leases with too large `TTL` values exceeding `math.MaxInt64` [expire in unexpected ways](https://github.com/etcd-io/etcd/issues/9374). Server now returns `rpctypes.ErrLeaseTTLTooLarge` to client, when the requested `TTL` is larger than *9,000,000,000 seconds* (which is >285 years). Again, etcd `Lease` is meant for short-periodic keepalives or sessions, in the range of seconds or minutes. Not for hours or days!
- Fix [v2 proxy leaky HTTP requests](https://github.com/etcd-io/etcd/pull/9336)

### 3.2.19

- Fix [`etcd_debugging_server_lease_expired_total`](https://github.com/etcd-io/etcd/pull/9557) Prometheus metric
- Fix [race conditions in v2 server stat collecting](https://github.com/etcd-io/etcd/pull/9562)

### 3.2.21

- Fix [auth storage panic when simple token provider is disabled](https://github.com/etcd-io/etcd/pull/8695)
- Fix [`mvcc` server panic from restore operation](https://github.com/etcd-io/etcd/pull/9775). Let's assume that a watcher had been requested with a future revision X and sent to node A that became network-partitioned thereafter. Meanwhile, cluster makes progress. Then when the partition gets removed, the leader sends a snapshot to node A. Previously if the snapshot's latest revision is still lower than the watch revision X, **etcd server panicked** during snapshot restore operation. Now, this server-side panic has been fixed

### 3.2.24

- Fix [lease keepalive interval updates when response queue is full](https://github.com/etcd-io/etcd/pull/9952). If `<-chan *clientv3LeaseKeepAliveResponse` from `clientv3.Lease.KeepAlive` was never consumed or channel is full, client was [sending keepalive request every 500ms](https://github.com/etcd-io/etcd/issues/9911) instead of expected rate of every "TTL / 3" duration

### 3.2.25

- Fix logic on [release lock key if cancelled](https://github.com/etcd-io/etcd/pull/10153) in `clientv3/concurrency` package

### 3.2.26

- Fix [memory leak in cache layer](https://github.com/etcd-io/etcd/pull/10327)

### 3.2.27

- Fix [`etcdctl snapshot status` to not modify snapshot file](https://github.com/etcd-io/etcd/pull/11157). For example, start etcd `v3.3.10` Write some data Use etcdctl `v3.3.10` to save snapshot Somehow, upgrading Kubernetes fails, thus rolling back to previous version etcd `v3.2.24` Run etcdctl `v3.2.24` `snapshot status` against the snapshot file saved from `v3.3.10` server Run etcdctl `v3.2.24` `snapshot restore` fails with `"expected sha256 [12..."`
- Fix bug where [db_compaction_total_duration_milliseconds metric incorrectly measured duration as 0](https://github.com/etcd-io/etcd/pull/10646)

### 3.2.28

- Fix [`wait purge file loop during shutdown`](https://github.com/etcd-io/etcd/pull/11308). Previously, during shutdown etcd could accidentally remove needed wal files, resulting in catastrophic error `etcdserver: open wal error: wal: file not found.` during startup. Now, etcd makes sure the purge file loop exits before server signals stop of the raft node

### 3.2.29

- [Fix corruption bug in defrag](https://github.com/etcd-io/etcd/pull/11613)
- Fix [`"hasleader"` metadata embedding](https://github.com/etcd-io/etcd/pull/11687). Previously, `clientv3.WithRequireLeader(ctx)` was overwriting existing context keys

### 3.2.31

- [attaching a fake root token when calling `LeaseRevoke`](https://github.com/etcd-io/etcd/pull/11691). fix a data corruption bug caused by lease expiration when authentication is enabled and upgrading cluster from etcd-3.2 to etcd-3.3


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.2.31**, the newest release recorded here for this line.

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
