---
id: TROUBLE-ETCD_3_4_DEFECTS
type: troubleshooting
title: "etcd 3.4: defects fixed in the 3.4 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.4.0 <3.5.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - etcd 3.4 known issues
  - etcd 3.4 fixed in
  - is this etcd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - etcd
sources:
  - type: docs
    path: etcd-io/etcd release notes for the 3.4 line — bug-fix entries
    url: https://github.com/etcd-io/etcd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# etcd 3.4: defects fixed in the 3.4 line

## Summary

**134 defects** the project fixed across **35 releases** of the 3.4 line, from 3.4.0 to
3.4.44. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.4.0

- Rewrite [client balancer](https://github.com/etcd-io/etcd/pull/9860) with [new gRPC balancer interface](https://github.com/etcd-io/etcd/issues/9106). Upgrade [gRPC to v1.23.0](https://github.com/etcd-io/etcd/pull/10911). Improve [client balancer failover against secure endpoints](https://github.com/etcd-io/etcd/pull/10911). Fix ["kube-apiserver 1.13.x refuses to work when first etcd-server is not available" (kubernetes#72102)](https://github.com/kubernetes/kubernetes/issues/72102). Fix [gRPC panic "send on closed channel](https://github.com/etcd-io/etcd/issues/9956). [The new client balancer](https://etcd.io/docs/latest/learning/design-client/) uses an asynchronous resolver to pass endpoints to the gRPC dial function. To block until the underlying connection is up, pass `grpc.WithBlock()` to `clientv3.Config.DialOptions`
- Fix missing [`etcd_network_peer_sent_failures_total`](https://github.com/etcd-io/etcd/pull/9437) Prometheus metric count
- Fix [`etcd_debugging_server_lease_expired_total`](https://github.com/etcd-io/etcd/pull/9557) Prometheus metric
- Fix [race conditions in v2 server stat collecting](https://github.com/etcd-io/etcd/pull/9562)
- Fix bug where [db_compaction_total_duration_milliseconds metric incorrectly measured duration as 0](https://github.com/etcd-io/etcd/pull/10646)
- Fix [`mvcc` "unsynced" watcher restore operation](https://github.com/etcd-io/etcd/pull/9281). "unsynced" watcher is watcher that needs to be in sync with events that have happened. That is, "unsynced" watcher is the slow watcher that was requested on old revision. "unsynced" watcher restore operation was not correctly populating its underlying watcher group. Which possibly causes [missing events from "unsynced" watchers](https://github.com/etcd-io/etcd/issues/9086). A node gets network partitioned with a watcher on a future revision, and falls behind receiving a leader snapshot after partition gets removed. When applying this snapshot, etcd watch storage moves current synced watchers to unsynced since sync watchers might have become stale during network partition. And reset synced watcher group to restart watcher routines. Previously, there was a bug when moving from synced watcher group to unsynced, thus client would miss events when the watcher was requested to the network-partitioned node
- Fix [`mvcc` server panic from restore operation](https://github.com/etcd-io/etcd/pull/9775). Let's assume that a watcher had been requested with a future revision X and sent to node A that became network-partitioned thereafter. Meanwhile, cluster makes progress. Then when the partition gets removed, the leader sends a snapshot to node A. Previously if the snapshot's latest revision is still lower than the watch revision X, **etcd server panicked** during snapshot restore operation. Now, this server-side panic has been fixed
- Fix [server panic on invalid Election Proclaim/Resign HTTP(S) requests](https://github.com/etcd-io/etcd/pull/9379). Previously, wrong-formatted HTTP requests to Election API could trigger panic in etcd server. e.g. `curl -L http://localhost:2379/v3/election/proclaim -X POST -d '{"value":""}'`, `curl -L http://localhost:2379/v3/election/resign -X POST -d '{"value":""}'`
- Fix [revision-based compaction retention parsing](https://github.com/etcd-io/etcd/pull/9339). Previously, `etcd --auto-compaction-mode revision --auto-compaction-retention 1` was [translated to revision retention 3600000000000](https://github.com/etcd-io/etcd/issues/9337). Now, `etcd --auto-compaction-mode revision --auto-compaction-retention 1` is correctly parsed as revision retention 1
- Prevent [overflow by large `TTL` values for `Lease` `Grant`](https://github.com/etcd-io/etcd/pull/9399). `TTL` parameter to `Grant` request is unit of second. Leases with too large `TTL` values exceeding `math.MaxInt64` [expire in unexpected ways](https://github.com/etcd-io/etcd/issues/9374). Server now returns `rpctypes.ErrLeaseTTLTooLarge` to client, when the requested `TTL` is larger than *9,000,000,000 seconds* (which is >285 years). Again, etcd `Lease` is meant for short-periodic keepalives or sessions, in the range of seconds or minutes. Not for hours or days!
- Fix [expired lease revoke](https://github.com/etcd-io/etcd/pull/10693). Fix ["the key is not deleted when the bound lease expires"](https://github.com/etcd-io/etcd/issues/10686)
- Fix [`ETCD_CONFIG_FILE` env variable parsing in `etcd`](https://github.com/etcd-io/etcd/pull/10762)
- Fix [race condition in `rafthttp` transport pause/resume](https://github.com/etcd-io/etcd/pull/10826)
- Fix [server crash from creating an empty role](https://github.com/etcd-io/etcd/pull/10907). Previously, creating a role with an empty name crashed etcd server with an error code `Unavailable`. Now, creating a role with an empty name is not allowed with an error code `InvalidArgument`
- Fix [Red-Black tree to maintain black-height property](https://github.com/etcd-io/etcd/pull/10978). Previously, delete operation violates [black-height property](https://github.com/etcd-io/etcd/issues/10965)
- Fix [lease keepalive interval updates when response queue is full](https://github.com/etcd-io/etcd/pull/9952). If `<-chan *clientv3LeaseKeepAliveResponse` from `clientv3.Lease.KeepAlive` was never consumed or channel is full, client was [sending keepalive request every 500ms](https://github.com/etcd-io/etcd/issues/9911) instead of expected rate of every "TTL / 3" duration
- Fix logic on [release lock key if cancelled](https://github.com/etcd-io/etcd/pull/10153) in `clientv3/concurrency` package
- Fix [`(*Client).Endpoints()` method race condition](https://github.com/etcd-io/etcd/pull/10595)
- Fix [`etcdctl watch [key] [range_end] -- [exec-command…]`](https://github.com/etcd-io/etcd/pull/9688) parsing. Previously, `ETCDCTL_API=3 etcdctl watch foo -- echo watch event received` panicked
- Fix [`etcdctl move-leader` command for TLS-enabled endpoints](https://github.com/etcd-io/etcd/pull/9807)
- Add [timeout](https://github.com/etcd-io/etcd/pull/10301) to `etcdctl snapshot save`. User can specify timeout of `etcdctl snapshot save` command using flag `--command-timeout`. Fix etcdctl to [strip out insecure endpoints from DNS SRV records when using discovery](https://github.com/etcd-io/etcd/pull/10443)
- Fix [etcd server panic from restore operation](https://github.com/etcd-io/etcd/pull/9775). Let's assume that a watcher had been requested with a future revision X and sent to node A that became network-partitioned thereafter. Meanwhile, cluster makes progress. Then when the partition gets removed, the leader sends a snapshot to node A. Previously if the snapshot's latest revision is still lower than the watch revision X, **etcd server panicked** during snapshot restore operation. Especially, gRPC proxy was affected, since it detects a leader loss with a key `"proxy-namespace__lostleader"` and a watch revision `"int64(math.MaxInt64 - 2)"`. Now, this server-side panic has been fixed
- Fix [memory leak in cache layer](https://github.com/etcd-io/etcd/pull/10327)
- Fix [deadlock during PreVote migration process](https://github.com/etcd-io/etcd/pull/8525)
- Fix [missing learner nodes on `(n *node) ApplyConfChange`](https://github.com/etcd-io/etcd/pull/9116)
- Add [`raft.Config.MaxUncommittedEntriesSize`](https://github.com/etcd-io/etcd/pull/10167) to limit the total size of the uncommitted entries in bytes. Once exceeded, raft returns `raft.ErrProposalDropped` error. Prevent [unbounded Raft log growth](https://github.com/cockroachdb/cockroach/issues/27772). There was a bug in [PR#10167](https://github.com/etcd-io/etcd/pull/10167) but fixed via [PR#10199](https://github.com/etcd-io/etcd/pull/10199)
- Add [`raft.Ready.CommittedEntries` pagination using `raft.Config.MaxSizePerMsg`](https://github.com/etcd-io/etcd/pull/9982). This prevents out-of-memory errors if the raft log has become very large and commits all at once. Fix [correctness bug in CommittedEntries pagination](https://github.com/etcd-io/etcd/pull/10063)
- Avoid [memory allocation in Raft entry `String` method](https://github.com/etcd-io/etcd/pull/10680)
- Avoid [multiple memory allocations when merging stable and unstable log](https://github.com/etcd-io/etcd/pull/10684)
- Prevent [learners from becoming leader](https://github.com/etcd-io/etcd/pull/10822)
- Fix [restoring joint consensus](https://github.com/etcd-io/etcd/pull/11003)
- Fix [`wal` directory cleanup on creation failures](https://github.com/etcd-io/etcd/pull/10689)
- Compile with [*Go 1.12.9*](https://golang.org/doc/devel/release.html#go1.12) including [*Go 1.12.8*](https://groups.google.com/d/msg/golang-announce/65QixT3tcmg/DrFiG6vvCwAJ) security fixes

### 3.4.1

- Fix [secure server logging message](https://github.com/etcd-io/etcd/commit/8b053b0f44c14ac0d9f39b9b78c17c57d47966eb)
- Compile with [*Go 1.12.9*](https://golang.org/doc/devel/release.html#go1.12) including [*Go 1.12.8*](https://groups.google.com/d/msg/golang-announce/65QixT3tcmg/DrFiG6vvCwAJ) security fixes

### 3.4.2

- Fix [`etcdctl member add`](https://github.com/etcd-io/etcd/pull/11194) command to prevent potential timeout
- Compile with [*Go 1.12.9*](https://golang.org/doc/devel/release.html#go1.12) including [*Go 1.12.8*](https://groups.google.com/d/msg/golang-announce/65QixT3tcmg/DrFiG6vvCwAJ) security fixes
- Fix [client balancer failover against multiple endpoints](https://github.com/etcd-io/etcd/pull/11184). Fix ["kube-apiserver: failover on multi-member etcd cluster fails certificate check on DNS mismatch" (kubernetes#83028)](https://github.com/kubernetes/kubernetes/issues/83028)
- Fix [IPv6 endpoint parsing in client](https://github.com/etcd-io/etcd/pull/11211). Fix ["1.16: etcd client does not parse IPv6 addresses correctly when members are joining" (kubernetes#83550)](https://github.com/kubernetes/kubernetes/issues/83550)

### 3.4.4

- Fix [`wait purge file loop during shutdown`](https://github.com/etcd-io/etcd/pull/11308). Previously, during shutdown etcd could accidentally remove needed wal files, resulting in catastrophic error `etcdserver: open wal error: wal: file not found.` during startup. Now, etcd makes sure the purge file loop exits before server signals stop of the raft node
- [Fix corruption bug in defrag](https://github.com/etcd-io/etcd/pull/11613)
- Fix [quorum protection logic when promoting a learner](https://github.com/etcd-io/etcd/pull/11640)
- Fix bug where [etcd_debugging_mvcc_db_compaction_keys_total is always 0](https://github.com/etcd-io/etcd/pull/11400)
- Fix [NoPassword check when adding user through GRPC gateway](https://github.com/etcd-io/etcd/pull/11418) ([issue#11414](https://github.com/etcd-io/etcd/issues/11414))
- Fix bug where [some auth related messages are logged at wrong level](https://github.com/etcd-io/etcd/pull/11586)

### 3.4.5

- Fix [`"hasleader"` metadata embedding](https://github.com/etcd-io/etcd/pull/11687). Previously, `clientv3.WithRequireLeader(ctx)` was overwriting existing context keys
- Fix [`etcdctl member add`](https://github.com/etcd-io/etcd/pull/11638) command to prevent potential timeout
- Fix [`panic on error`](https://github.com/etcd-io/etcd/pull/11694) for metrics handler

### 3.4.6

- Fix [memory leak in follower nodes](https://github.com/etcd-io/etcd/pull/11731). https://github.com/etcd-io/etcd/issues/11495 https://github.com/etcd-io/etcd/issues/11730

### 3.4.8

- [Fix deadlock bug in mvcc](https://github.com/etcd-io/etcd/pull/11817)
- Fix [inconsistency between WAL and server snapshot](https://github.com/etcd-io/etcd/pull/11888). Previously, server restore fails if it had crashed after persisting raft hard state but before saving snapshot. See https://github.com/etcd-io/etcd/issues/10219 for more
- [Fix a data corruption bug by saving consistent index](https://github.com/etcd-io/etcd/pull/11652)

### 3.4.10

- Fix [`int64` convert panic in raft logger](https://github.com/etcd-io/etcd/pull/12106). Fix [kubernetes/kubernetes#91937](https://github.com/kubernetes/kubernetes/issues/91937)

### 3.4.12

- Fix [server panic in slow writes warnings](https://github.com/etcd-io/etcd/issues/12197). Fixed via [PR#12238](https://github.com/etcd-io/etcd/pull/12238)

### 3.4.14

- Fix [auth token invalid after watch reconnects](https://github.com/etcd-io/etcd/pull/12264). Get AuthToken automatically when clientConn is ready
- [Fix server panic](https://github.com/etcd-io/etcd/pull/12288) when force-new-cluster flag is enabled in a cluster which had learner node

### 3.4.15

- Fix [64 KB websocket notification message limit](https://github.com/etcd-io/etcd/pull/12402)
- Fix [`F_OFD_` constants](https://github.com/etcd-io/etcd/pull/12444)

### 3.4.16

- Fix [`--unsafe-no-fsync`](https://github.com/etcd-io/etcd/pull/12751) to still write-out data avoiding corruption (most of the time)
- Fix [incorrect metrics generated when clients cancel watches](https://github.com/etcd-io/etcd/pull/12803) back-ported from (https://github.com/etcd-io/etcd/pull/12196)

### 3.4.17

- Fix [etcdctl check datascale command](https://github.com/etcd-io/etcd/pull/11896) to work with https endpoints

### 3.4.19

- Fix [exclude the same alarm type activated by multiple peers](https://github.com/etcd-io/etcd/pull/13475)
- Fix [Defrag unsets backend options](https://github.com/etcd-io/etcd/pull/13713)
- Fix [lease leak issue due to tokenProvider isn't enabled when restoring auth store from a snapshot](https://github.com/etcd-io/etcd/pull/13206)
- Fix [the race condition between goroutine and channel on the same leases to be revoked](https://github.com/etcd-io/etcd/pull/14150)
- Fix [lessor may continue to schedule checkpoint after stepping down leader role](https://github.com/etcd-io/etcd/pull/14150)
- Fix [a bug of not refreshing expired tokens](https://github.com/etcd-io/etcd/pull/13999)

### 3.4.20

- Fix [filter learners members during autosync](https://github.com/etcd-io/etcd/pull/14236)
- Fix [Lease checkpoints don't prevent to reset ttl on leader change](https://github.com/etcd-io/etcd/pull/14253), requires enabling checkpoint persisting
- Fix [Protect rangePermCache with a RW lock correctly](https://github.com/etcd-io/etcd/pull/14230)
- Fix [raft: postpone MsgReadIndex until first commit in the term](https://github.com/etcd-io/etcd/pull/14258)
- Fix [etcdserver: resend ReadIndex request on empty apply request](https://github.com/etcd-io/etcd/pull/14269)
- Fix [remove temp files in snap dir when etcdserver starting](https://github.com/etcd-io/etcd/pull/14246)
- Fix [Etcdserver is still in progress of processing LeaseGrantRequest when it receives a LeaseKeepAliveRequest on the same leaseID](https://github.com/etcd-io/etcd/pull/14177)
- Fix [Grant lease with negative ID can possibly cause db out of sync](https://github.com/etcd-io/etcd/pull/14239)
- Fix [Allow non mutating requests pass through quotaKVServer when NOSPACE](https://github.com/etcd-io/etcd/pull/14254)

### 3.4.21

- Fix [Durability API guarantee broken in single node cluster](https://github.com/etcd-io/etcd/pull/14423)
- Fix [Panic due to nil log object](https://github.com/etcd-io/etcd/pull/14420)
- Fix [authentication data not loaded on member startup](https://github.com/etcd-io/etcd/pull/14410)
- Fix [etcdctl move-leader may fail for multiple endpoints](https://github.com/etcd-io/etcd/pull/14441)

### 3.4.22

- Fix [memberID equals zero in corruption alarm](https://github.com/etcd-io/etcd/pull/14530)
- Fix [auth invalid token and old revision errors in watch](https://github.com/etcd-io/etcd/pull/14548)
- Fix [avoid closing a watch with ID 0 incorrectly](https://github.com/etcd-io/etcd/pull/14562)
- Fix [auth: fix data consistency issue caused by recovery from snapshot](https://github.com/etcd-io/etcd/pull/14649)
- Fix [netutil: add url comparison without resolver to URLStringsEqual](https://github.com/etcd-io/etcd/pull/14577)
- Fix [Add backoff before retry when watch stream returns unavailable](https://github.com/etcd-io/etcd/pull/14581)

### 3.4.23

- Fix [Remove memberID from data corrupt alarm](https://github.com/etcd-io/etcd/pull/14853)
- Fix [nil pointer panic for readonly txn due to nil response](https://github.com/etcd-io/etcd/pull/14900)
- Fix [Refreshing token on CommonName based authentication causes segmentation violation in client](https://github.com/etcd-io/etcd/pull/14792)

### 3.4.24

- Fix [etcdserver might promote a non-started learner](https://github.com/etcd-io/etcd/pull/15097)
- Fix [aligning zap log timestamp resolution to microseconds](https://github.com/etcd-io/etcd/pull/15241). Etcd now uses zap timestamp format: `2006-01-02T15:04:05.999999Z0700` (microsecond instead of milliseconds precision)
- Fix [consistently format IPv6 addresses for comparison](https://github.com/etcd-io/etcd/pull/15188)
- Fix [etcd might send duplicated events to watch clients](https://github.com/etcd-io/etcd/pull/15275)

### 3.4.25

- Fix [server/embed: fix data race when starting both secure & insecure gRPC servers on the same address](https://github.com/etcd-io/etcd/pull/15518)
- Fix [server/auth: disallow creating empty permission ranges](https://github.com/etcd-io/etcd/pull/15621)
- Fix [wsproxy did not print log in JSON format](https://github.com/etcd-io/etcd/pull/15662)
- Fix [etcdserver may panic when parsing a JWT token without username or revision](https://github.com/etcd-io/etcd/pull/15677)
- Fix [Watch response traveling back in time when reconnecting member downloads snapshot from the leader](https://github.com/etcd-io/etcd/pull/15520)
- Fix [Requested watcher progress notifications are not synchronised with stream](https://github.com/etcd-io/etcd/pull/15697)
- Reverted the fix to [auth invalid token and old revision errors in watch](https://github.com/etcd-io/etcd/pull/15542)
- Fix [etcd docker images all tagged with amd64 architecture](https://github.com/etcd-io/etcd/pull/15681)

### 3.4.26

- Fix [LeaseTimeToLive API may return keys to clients which have no read permission on the keys](https://github.com/etcd-io/etcd/pull/15814)

### 3.4.27

- Fix [corruption check may get a `ErrCompacted` error when server has just been compacted](https://github.com/etcd-io/etcd/pull/16047)
- Fix [embed: nil pointer dereference when stopServer](https://github.com/etcd-io/etcd/pull/16195)

### 3.4.28

- Fix [Reset auth token when failing to authenticate due to auth being disabled](https://github.com/etcd-io/etcd/pull/16240)
- Fix [race condition when accessing cfg.Endpoints in dial()](https://github.com/etcd-io/etcd/pull/16857)
- Fix [invalid authority header issue in single endpoint scenario](https://github.com/etcd-io/etcd/pull/16988)

### 3.4.29

- Fix [Check if be is nil to avoid panic when be is overriden with nil](https://github.com/etcd-io/etcd/pull/17154)
- Fix [Add missing experimental-enable-lease-checkpoint-persist flag in etcd help](https://github.com/etcd-io/etcd/pull/17189)
- Fix [Don't flock snapshot files](https://github.com/etcd-io/etcd/pull/17208)

### 3.4.30

- Fix [nil pointer panicking due to using the wrong log library](https://github.com/etcd-io/etcd/pull/17270)

### 3.4.31

- Fix leases wrongly revoked by the leader by [ignoring old leader's leases revoking request](https://github.com/etcd-io/etcd/pull/17465)
- Fix [no progress notification being sent for watch that doesn't get any events](https://github.com/etcd-io/etcd/pull/17567)
- Fix [watch event loss after compaction](https://github.com/etcd-io/etcd/pull/17610)

### 3.4.32

- Fix [LeaseTimeToLive returns error if leader changed](https://github.com/etcd-io/etcd/pull/17705)
- Fix [ignore raft messages if member id mismatch](https://github.com/etcd-io/etcd/pull/17814)
- Fix [Revision decreasing after panic during compaction](https://github.com/etcd-io/etcd/pull/17864)
- Fix [initialization for epMu in client context](https://github.com/etcd-io/etcd/pull/17714)

### 3.4.33

- Fix [Memberlist results not updated when proxy node down](https://github.com/etcd-io/etcd/pull/17896)

### 3.4.34

- Fix [performance regression issue caused by the `ensureLeadership` in lease renew](https://github.com/etcd-io/etcd/pull/18440)

### 3.4.35

- Fix [watchserver related goroutine leakage](https://github.com/etcd-io/etcd/pull/18785)
- Fix [panicking occurred due to improper error handling during defragmentation](https://github.com/etcd-io/etcd/pull/18843)
- Fix [close temp file(s) in case an error happens during defragmentation](https://github.com/etcd-io/etcd/pull/18855)

### 3.4.36

- [Avoid deadlock in etcd.Close when stopping during bootstrapping](https://github.com/etcd-io/etcd/pull/19166)
- Fix [missing delete event on watch opened on same revision as compaction request](https://github.com/etcd-io/etcd/pull/19251)
- Fix [runtime panic that occurs when KeepAlive is called with a Context implemented by an uncomparable type](https://github.com/etcd-io/etcd/pull/18936)

### 3.4.38

- Fix [mvcc: avoid double decrement of watcher gauge on close/cancel race](https://github.com/etcd-io/etcd/pull/20065)
- Fix [Watch on future revision returns old events or notifications](https://github.com/etcd-io/etcd/pull/20291)
- Fix [potential data corruption when applySnapshot and defragment happen concurrently](https://github.com/etcd-io/etcd/pull/20659)
- Fix [etcd may return success for leaseRenew request even when the lease is revoked](https://github.com/etcd-io/etcd/pull/20813)

### 3.4.42

- Fix [Race between read index and leader change](https://github.com/etcd-io/etcd/pull/21385)
- Fix [Stale reads caused by process pausing](https://github.com/etcd-io/etcd/pull/21423)

### 3.4.43

- Fix [etcdctl endpoint command regression with option --cluster when auth is enabled](https://github.com/etcd-io/etcd/pull/21533)

### 3.4.44

- Fix RBAC authorization bypass allowing read access via PrevKv or lease attachment in Put requests nested in etcd transactions (see [PR/21683](https://github.com/etcd-io/etcd/pull/21683) and [PR/21688](https://github.com/etcd-io/etcd/pull/21688))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.4.44**, the newest release recorded here for this line.

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
