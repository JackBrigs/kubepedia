---
id: TROUBLE-ETCD_3_3_DEFECTS
type: troubleshooting
title: "etcd 3.3: defects fixed in the 3.3 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.3.0 <3.4.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - etcd 3.3 known issues
  - etcd 3.3 fixed in
  - is this etcd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - etcd
sources:
  - type: docs
    path: etcd-io/etcd release notes for the 3.3 line — bug-fix entries
    url: https://github.com/etcd-io/etcd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# etcd 3.3: defects fixed in the 3.3 line

## Summary

**60 defects** the project fixed across **20 releases** of the 3.3 line, from 3.3.0 to
3.3.26. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.3.0

- Use [`coreos/bbolt`](https://github.com/coreos/bbolt/releases) to replace [`boltdb/bolt`](https://github.com/boltdb/bolt#project-status). Fix [etcd database size grows until `mvcc: database space exceeded`](https://github.com/etcd-io/etcd/issues/8009)
- Fix [range/put/delete operation metrics](https://github.com/etcd-io/etcd/pull/8054) with transaction. `etcd_debugging_mvcc_range_total` `etcd_debugging_mvcc_put_total` `etcd_debugging_mvcc_delete_total` `etcd_debugging_mvcc_txn_total`
- Fix [`etcd_debugging_mvcc_keys_total`](https://github.com/etcd-io/etcd/pull/8390) on restore
- Fix [`etcd_debugging_mvcc_db_total_size_in_bytes`](https://github.com/etcd-io/etcd/pull/8120) on restore. Also change to [`prometheus.NewGaugeFunc`](https://github.com/etcd-io/etcd/pull/8150)
- Add [health balancer](https://github.com/etcd-io/etcd/pull/8545) to fix [watch API hangs](https://github.com/etcd-io/etcd/issues/7247), improve [endpoint switch under network faults](https://github.com/etcd-io/etcd/issues/7941)
- Add [`MaxCallSendMsgSize` and `MaxCallRecvMsgSize`](https://github.com/etcd-io/etcd/pull/9047) fields to [`clientv3.Config`](https://godoc.org/github.com/coreos/etcd/clientv3#Config). Fix [exceeded response size limit error in client-side](https://github.com/etcd-io/etcd/issues/9043). Address [kubernetes#51099](https://github.com/kubernetes/kubernetes/issues/51099). In previous versions(v3.2.10, v3.2.11), client response size was limited to only 4 MiB. `MaxCallSendMsgSize` default value is 2 MiB, if not configured. `MaxCallRecvMsgSize` default value is `math.MaxInt32`, if not configured
- Fix ["put at-most-once" violation](https://github.com/etcd-io/etcd/pull/8335)
- Fix [`WatchResponse.Canceled`](https://github.com/etcd-io/etcd/pull/8283) on [compacted watch request](https://github.com/etcd-io/etcd/issues/8231)
- Fix [`concurrency/stm` `Put` with serializable snapshot](https://github.com/etcd-io/etcd/pull/8439). Use store revision from first fetch to resolve write conflicts instead of modified revision
- Fix [`etcdctl snapshot status` to not modify snapshot file](https://github.com/etcd-io/etcd/pull/8815). For example, start etcd `v3.3.10` Write some data Use etcdctl `v3.3.10` to save snapshot Somehow, upgrading Kubernetes fails, thus rolling back to previous version etcd `v3.2.24` Run etcdctl `v3.2.24` `snapshot status` against the snapshot file saved from `v3.3.10` server Run etcdctl `v3.2.24` `snapshot restore` fails with `"expected sha256 [12..."`
- Fix [Snapshot API error handling](https://github.com/etcd-io/etcd/commit/dbd16d52fbf81e5fd806d21ff5e9148d5bf203ab)
- Fix [KV API `PrevKv` flag handling](https://github.com/etcd-io/etcd/pull/8366)
- Fix [KV API `KeysOnly` flag handling](https://github.com/etcd-io/etcd/pull/8552)
- Support [websocket for bi-directional streams](https://github.com/etcd-io/etcd/pull/8257). Fix [`Watch` API with gRPC gateway](https://github.com/etcd-io/etcd/issues/8237)
- Fix [backend database in-memory index corruption](https://github.com/etcd-io/etcd/pull/8127) issue on restore (only 3.2.0 is affected)
- Fix [watch restore from snapshot](https://github.com/etcd-io/etcd/pull/8427)
- Fix [`mvcc/backend.defragdb` nil-pointer dereference on create bucket failure](https://github.com/etcd-io/etcd/pull/9119)
- Fix [server crash](https://github.com/etcd-io/etcd/pull/8010) on [invalid transaction request from gRPC gateway](https://github.com/etcd-io/etcd/issues/7889)
- Prevent [server panic from member update/add](https://github.com/etcd-io/etcd/pull/9174) with [wrong scheme URLs](https://github.com/etcd-io/etcd/issues/9173)
- Fix [`grpc.Server` panic on `GracefulStop`](https://github.com/etcd-io/etcd/pull/8987) with [TLS-enabled server](https://github.com/etcd-io/etcd/issues/8916)
- Fix ["multiple peer URLs cannot start" issue](https://github.com/etcd-io/etcd/issues/8383)
- Fix server-side auth so [concurrent auth operations do not return old revision error](https://github.com/etcd-io/etcd/pull/8442)

### 3.3.1

- Fix [`mvcc` "unsynced" watcher restore operation](https://github.com/etcd-io/etcd/pull/9281). "unsynced" watcher is watcher that needs to be in sync with events that have happened. That is, "unsynced" watcher is the slow watcher that was requested on old revision. "unsynced" watcher restore operation was not correctly populating its underlying watcher group. Which possibly causes [missing events from "unsynced" watchers](https://github.com/etcd-io/etcd/issues/9086). A node gets network partitioned with a watcher on a future revision, and falls behind receiving a leader snapshot after partition gets removed. When applying this snapshot, etcd watch storage moves current synced watchers to unsynced since sync watchers might have become stale during network partition. And reset synced watcher group to restart watcher routines. Previously, there was a bug when moving from synced watcher group to unsynced, thus client would miss events when the watcher was requested to the network-partitioned node

### 3.3.2

- Fix [server panic on invalid Election Proclaim/Resign HTTP(S) requests](https://github.com/etcd-io/etcd/pull/9379). Previously, wrong-formatted HTTP requests to Election API could trigger panic in etcd server. e.g. `curl -L http://localhost:2379/v3/election/proclaim -X POST -d '{"value":""}'`, `curl -L http://localhost:2379/v3/election/resign -X POST -d '{"value":""}'`
- Fix [revision-based compaction retention parsing](https://github.com/etcd-io/etcd/pull/9339). Previously, `etcd --auto-compaction-mode revision --auto-compaction-retention 1` was [translated to revision retention 3600000000000](https://github.com/etcd-io/etcd/issues/9337). Now, `etcd --auto-compaction-mode revision --auto-compaction-retention 1` is correctly parsed as revision retention 1
- Prevent [overflow by large `TTL` values for `Lease` `Grant`](https://github.com/etcd-io/etcd/pull/9399). `TTL` parameter to `Grant` request is unit of second. Leases with too large `TTL` values exceeding `math.MaxInt64` [expire in unexpected ways](https://github.com/etcd-io/etcd/issues/9374). Server now returns `rpctypes.ErrLeaseTTLTooLarge` to client, when the requested `TTL` is larger than *9,000,000,000 seconds* (which is >285 years). Again, etcd `Lease` is meant for short-periodic keepalives or sessions, in the range of seconds or minutes. Not for hours or days!
- Fix [v2 proxy leaky HTTP requests](https://github.com/etcd-io/etcd/pull/9336)

### 3.3.4

- Fix [`etcd_debugging_server_lease_expired_total`](https://github.com/etcd-io/etcd/pull/9557) Prometheus metric
- Fix [race conditions in v2 server stat collecting](https://github.com/etcd-io/etcd/pull/9562)

### 3.3.5

- Fix [`etcdctl watch [key] [range_end] -- [exec-command…]`](https://github.com/etcd-io/etcd/pull/9688) parsing. Previously, `ETCDCTL_API=3 ./bin/etcdctl watch foo -- echo watch event received` panicked

### 3.3.6

- Fix [auth storage panic on server lease revoke routine with JWT token](https://github.com/etcd-io/etcd/issues/9695)
- Fix [`mvcc` server panic from restore operation](https://github.com/etcd-io/etcd/pull/9775). Let's assume that a watcher had been requested with a future revision X and sent to node A that became network-partitioned thereafter. Meanwhile, cluster makes progress. Then when the partition gets removed, the leader sends a snapshot to node A. Previously if the snapshot's latest revision is still lower than the watch revision X, **etcd server panicked** during snapshot restore operation. Now, this server-side panic has been fixed

### 3.3.7

- Fix [`etcdctl move-leader` command for TLS-enabled endpoints](https://github.com/etcd-io/etcd/pull/9807)

### 3.3.9

- Fix [lease keepalive interval updates when response queue is full](https://github.com/etcd-io/etcd/pull/9952). If `<-chan *clientv3LeaseKeepAliveResponse` from `clientv3.Lease.KeepAlive` was never consumed or channel is full, client was [sending keepalive request every 500ms](https://github.com/etcd-io/etcd/issues/9911) instead of expected rate of every "TTL / 3" duration

### 3.3.10

- Fix logic on [release lock key if cancelled](https://github.com/etcd-io/etcd/pull/10153) in `clientv3/concurrency` package

### 3.3.11

- Fix [memory leak in cache layer](https://github.com/etcd-io/etcd/pull/10327)

### 3.3.13

- Fix bug where [db_compaction_total_duration_milliseconds metric incorrectly measured duration as 0](https://github.com/etcd-io/etcd/pull/10646)
- Fix [`(*Client).Endpoints()` method race condition](https://github.com/etcd-io/etcd/pull/10595)

### 3.3.14

- Fix [race condition in `rafthttp` transport pause/resume](https://github.com/etcd-io/etcd/pull/10826)
- Fix [gRPC panic "send on closed channel](https://github.com/etcd-io/etcd/issues/9956) by upgrading [`google.golang.org/grpc`](https://github.com/grpc/grpc-go/releases) from [**`v1.7.5`**](https://github.com/grpc/grpc-go/releases/tag/v1.7.5) to [**`v1.23.0`**](https://github.com/grpc/grpc-go/releases/tag/v1.23.0)
- Rewrite [client balancer](https://github.com/etcd-io/etcd/pull/9860) with [new gRPC balancer interface](https://github.com/etcd-io/etcd/issues/9106). Upgrade [gRPC to v1.23.0](https://github.com/etcd-io/etcd/pull/10911). Improve [client balancer failover against secure endpoints](https://github.com/etcd-io/etcd/pull/10911). Fix ["kube-apiserver 1.13.x refuses to work when first etcd-server is not available" (kubernetes#72102)](https://github.com/kubernetes/kubernetes/issues/72102). [The new client balancer](https://etcd.io/docs/latest/learning/design-client/) uses an asynchronous resolver to pass endpoints to the gRPC dial function. to block until the underlying connection is up, pass `grpc.WithBlock()` to `clientv3.Config.DialOptions`
- Fix [Red-Black tree to maintain black-height property](https://github.com/etcd-io/etcd/pull/10978). Previously, delete operation violates [black-height property](https://github.com/etcd-io/etcd/issues/10965)
- Compile with [*Go 1.12.9*](https://golang.org/doc/devel/release.html#go1.12) including [*Go 1.12.8*](https://groups.google.com/d/msg/golang-announce/65QixT3tcmg/DrFiG6vvCwAJ) security fixes

### 3.3.15

- Compile with [*Go 1.12.9*](https://golang.org/doc/devel/release.html#go1.12) including [*Go 1.12.8*](https://groups.google.com/d/msg/golang-announce/65QixT3tcmg/DrFiG6vvCwAJ) security fixes

### 3.3.16

- Fix [`etcdctl member add`](https://github.com/etcd-io/etcd/pull/11194) command to prevent potential timeout
- Compile with [*Go 1.12.9*](https://golang.org/doc/devel/release.html#go1.12) including [*Go 1.12.8*](https://groups.google.com/d/msg/golang-announce/65QixT3tcmg/DrFiG6vvCwAJ) security fixes
- Fix [client balancer failover against multiple endpoints](https://github.com/etcd-io/etcd/pull/11184). Fix ["kube-apiserver: failover on multi-member etcd cluster fails certificate check on DNS mismatch" (kubernetes#83028)](https://github.com/kubernetes/kubernetes/issues/83028)
- Fix [IPv6 endpoint parsing in client](https://github.com/etcd-io/etcd/pull/11211). Fix ["1.16: etcd client does not parse IPv6 addresses correctly when members are joining" (kubernetes#83550)](https://github.com/kubernetes/kubernetes/issues/83550)

### 3.3.18

- Fix [`wait purge file loop during shutdown`](https://github.com/etcd-io/etcd/pull/11308). Previously, during shutdown etcd could accidentally remove needed wal files, resulting in catastrophic error `etcdserver: open wal error: wal: file not found.` during startup. Now, etcd makes sure the purge file loop exits before server signals stop of the raft node

### 3.3.19

- Fix [`"hasleader"` metadata embedding](https://github.com/etcd-io/etcd/pull/11687). Previously, `clientv3.WithRequireLeader(ctx)` was overwriting existing context keys
- [Fix corruption bug in defrag](https://github.com/etcd-io/etcd/pull/11613)
- Fix [`etcdctl member add`](https://github.com/etcd-io/etcd/pull/11638) command to prevent potential timeout
- Fix [`panic on error`](https://github.com/etcd-io/etcd/pull/11694) for metrics handler

### 3.3.21

- [Fix deadlock bug in mvcc](https://github.com/etcd-io/etcd/pull/11817)
- Fix [inconsistency between WAL and server snapshot](https://github.com/etcd-io/etcd/pull/11888). Previously, server restore fails if it had crashed after persisting raft hard state but before saving snapshot. See https://github.com/etcd-io/etcd/issues/10219 for more
- [Fix a data corruption bug by saving consistent index](https://github.com/etcd-io/etcd/pull/11652)

### 3.3.23

- Fix [watch stream got closed if one watch request is not permitted](https://github.com/etcd-io/etcd/pull/11758)

### 3.3.24

- Fix [`int64` convert panic in raft logger](https://github.com/etcd-io/etcd/pull/12106). Fix [kubernetes/kubernetes#91937](https://github.com/kubernetes/kubernetes/issues/91937)

### 3.3.26

- Fix [auth token invalid after watch reconnects](https://github.com/etcd-io/etcd/pull/12264). Get AuthToken automatically when clientConn is ready
- Fix [constant](https://github.com/etcd-io/etcd/pull/12440) for linux locking


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.3.26**, the newest release recorded here for this line.

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
