---
id: TROUBLE-ETCD_3_5_DEFECTS
type: troubleshooting
title: "etcd 3.5: defects fixed in the 3.5 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.5.0 <3.6.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - etcd 3.5 known issues
  - etcd 3.5 fixed in
  - is this etcd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - etcd
sources:
  - type: docs
    path: etcd-io/etcd release notes for the 3.5 line — bug-fix entries
    url: https://github.com/etcd-io/etcd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# etcd 3.5: defects fixed in the 3.5 line

## Summary

**130 defects** the project fixed across **30 releases** of the 3.5 line, from 3.5.0 to
3.5.32. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.5.0

- [Fix corruption bug in defrag](https://github.com/etcd-io/etcd/pull/11613)
- Fix [quorum protection logic when promoting a learner](https://github.com/etcd-io/etcd/pull/11640)
- [Fix deadlock bug in mvcc](https://github.com/etcd-io/etcd/pull/11817)
- Fix [inconsistency between WAL and server snapshot](https://github.com/etcd-io/etcd/pull/11888). Previously, server restore fails if it had crashed after persisting raft hard state but before saving snapshot. See https://github.com/etcd-io/etcd/issues/10219 for more. Add [missing CRC checksum check in WAL validate method otherwise causes panic](https://github.com/etcd-io/etcd/pull/11924). See https://github.com/etcd-io/etcd/issues/11918
- [Fix invalid Go type in etcdserverpb](https://github.com/etcd-io/etcd/pull/12000)
- Fix [server panic in slow writes warnings](https://github.com/etcd-io/etcd/issues/12197). Fixed via [PR#12238](https://github.com/etcd-io/etcd/pull/12238)
- [Fix server panic](https://github.com/etcd-io/etcd/pull/12288) when force-new-cluster flag is enabled in a cluster which had learner node
- Fix [client balancer failover against multiple endpoints](https://github.com/etcd-io/etcd/pull/11184). Fix [`"kube-apiserver: failover on multi-member etcd cluster fails certificate check on DNS mismatch"`](https://github.com/kubernetes/kubernetes/issues/83028)
- Fix [IPv6 endpoint parsing in client](https://github.com/etcd-io/etcd/pull/11211). Fix ["1.16: etcd client does not parse IPv6 addresses correctly when members are joining" (kubernetes#83550)](https://github.com/kubernetes/kubernetes/issues/83550)
- Fix [errors caused by grpc changing balancer/resolver API](https://github.com/etcd-io/etcd/pull/11564). This change is compatible with grpc >= [v1.26.0](https://github.com/grpc/grpc-go/releases/tag/v1.26.0), but is not compatible with < v1.26.0 version
- Fix [`"hasleader"` metadata embedding](https://github.com/etcd-io/etcd/pull/11687). Previously, `clientv3.WithRequireLeader(ctx)` was overwriting existing context keys
- Fix [watch leak caused by lazy cancellation](https://github.com/etcd-io/etcd/pull/11850). When clients cancel their watches, a cancel request will now be immediately sent to the server instead of waiting for the next watch event
- Fix [auth token invalid after watch reconnects](https://github.com/etcd-io/etcd/pull/12264). Get AuthToken automatically when clientConn is ready
- Fix [memory leak in follower nodes](https://github.com/etcd-io/etcd/pull/11731). https://github.com/etcd-io/etcd/issues/11495 https://github.com/etcd-io/etcd/issues/11730
- Fix `etcdctl member add` command to prevent potential timeout. ([PR#11194](https://github.com/etcd-io/etcd/pull/11194) and [PR#11638](https://github.com/etcd-io/etcd/pull/11638))
- Fix [`panic on error`](https://github.com/etcd-io/etcd/pull/11694) for metrics handler
- [Fix grpc watch proxy hangs when failed to cancel a watcher](https://github.com/etcd-io/etcd/pull/12030)
- Fix [NoPassword check when adding user through GRPC gateway](https://github.com/etcd-io/etcd/pull/11418) ([issue#11414](https://github.com/etcd-io/etcd/issues/11414))
- Fix bug where [some auth related messages are logged at wrong level](https://github.com/etcd-io/etcd/pull/11586)
- [Fix a data corruption bug by saving consistent index](https://github.com/etcd-io/etcd/pull/11652)
- Fix [a bug of not refreshing expired tokens](https://github.com/etcd-io/etcd/pull/13308)

### 3.5.1

- Fix [self-signed-cert-validity parameter cannot be specified in the config file](https://github.com/etcd-io/etcd/pull/13237)
- Fix [ensure that cluster members stored in v2store and backend are in sync](https://github.com/etcd-io/etcd/pull/13348)
- [Fix etcd client sends invalid :authority header](https://github.com/etcd-io/etcd/issues/13192)

### 3.5.2

- Fix [exclude the same alarm type activated by multiple peers](https://github.com/etcd-io/etcd/pull/13476)
- Fix [Lease checkpoints don't prevent to reset ttl on leader change](https://github.com/etcd-io/etcd/pull/13508), requires enabling checkpoint persisting
- Fix [assertion failed due to tx closed when recovering v3 backend from a snapshot db](https://github.com/etcd-io/etcd/pull/13501)
- Fix [segmentation violation(SIGSEGV) error due to premature unlocking of watchableStore](https://github.com/etcd-io/etcd/pull/13541)

### 3.5.3

- Fix [Provide a better liveness probe for when etcd runs as a Kubernetes pod](https://github.com/etcd-io/etcd/pull/13706)
- Fix [inconsistent log format](https://github.com/etcd-io/etcd/pull/13864)
- Fix [Inconsistent revision and data occurs](https://github.com/etcd-io/etcd/pull/13908)
- Fix [Etcdserver is still in progress of processing LeaseGrantRequest when it receives a LeaseKeepAliveRequest on the same leaseID](https://github.com/etcd-io/etcd/pull/13932)
- Fix [consistent_index coming from snapshot is overwritten by the old local value](https://github.com/etcd-io/etcd/pull/13933)
- Fix [Defrag unsets backend options](https://github.com/etcd-io/etcd/pull/13701)

### 3.5.4

- Fix [etcd panic on startup (auth enabled)](https://github.com/etcd-io/etcd/pull/13946)

### 3.5.5

- Fix [do not overwrite authTokenBundle on dial](https://github.com/etcd-io/etcd/pull/14132)
- Fix [IsOptsWithPrefix returns false even if WithPrefix() is included](https://github.com/etcd-io/etcd/pull/14187)
- Fix [unexpected error during txn](https://github.com/etcd-io/etcd/issues/14110)
- Fix [lease leak issue due to tokenProvider isn't enabled when restoring auth store from a snapshot](https://github.com/etcd-io/etcd/pull/13205)
- Fix [the race condition between goroutine and channel on the same leases to be revoked](https://github.com/etcd-io/etcd/pull/14087)
- Fix [lessor may continue to schedule checkpoint after stepping down leader role](https://github.com/etcd-io/etcd/pull/14087)
- Fix [Restrict the max size of each WAL entry to the remaining size of the WAL file](https://github.com/etcd-io/etcd/pull/14127)
- Fix [Protect rangePermCache with a RW lock correctly](https://github.com/etcd-io/etcd/pull/14227)
- Fix [memberID equals zero in corruption alarm](https://github.com/etcd-io/etcd/pull/14272)
- Fix [Durability API guarantee broken in single node cluster](https://github.com/etcd-io/etcd/pull/14424)
- Fix [etcd fails to start after performing alarm list operation and then power off/on](https://github.com/etcd-io/etcd/pull/14429)
- Fix [authentication data not loaded on member startup](https://github.com/etcd-io/etcd/pull/14409)
- Fix [etcdctl move-leader may fail for multiple endpoints](https://github.com/etcd-io/etcd/pull/14434)

### 3.5.6

- Fix [auth invalid token and old revision errors in watch](https://github.com/etcd-io/etcd/pull/14547)
- Fix [avoid closing a watch with ID 0 incorrectly](https://github.com/etcd-io/etcd/pull/14563)
- Fix [auth: fix data consistency issue caused by recovery from snapshot](https://github.com/etcd-io/etcd/pull/14648)
- Fix [revision might be inconsistency between members when etcd crashes during processing defragmentation operation](https://github.com/etcd-io/etcd/pull/14733)
- Fix [timestamp in inconsistent format](https://github.com/etcd-io/etcd/pull/14799)
- Fix [Failed resolving host due to lost DNS record](https://github.com/etcd-io/etcd/pull/14573)
- Fix [Add backoff before retry when watch stream returns unavailable](https://github.com/etcd-io/etcd/pull/14582)
- Fix [stack overflow error in double barrier](https://github.com/etcd-io/etcd/pull/14658)
- Fix [Refreshing token on CommonName based authentication causes segmentation violation in client](https://github.com/etcd-io/etcd/pull/14790)

### 3.5.7

- Fix [Remove memberID from data corrupt alarm](https://github.com/etcd-io/etcd/pull/14852)
- Fix [Allow non mutating requests pass through quotaKVServer when NOSPACE](https://github.com/etcd-io/etcd/pull/14884)
- Fix [nil pointer panic for readonly txn due to nil response](https://github.com/etcd-io/etcd/pull/14899)
- Fix [The last record which was partially synced to disk isn't automatically repaired](https://github.com/etcd-io/etcd/pull/15069)
- Fix [etcdserver might promote a non-started learner](https://github.com/etcd-io/etcd/pull/15096)
- Reverted the fix to [auth invalid token and old revision errors in watch](https://github.com/etcd-io/etcd/pull/14995)

### 3.5.8

- Fix [Watch response traveling back in time when reconnecting member downloads snapshot from the leader](https://github.com/etcd-io/etcd/pull/15515)
- Fix [race when starting both secure & insecure gRPC servers on the same address](https://github.com/etcd-io/etcd/pull/15517)
- Fix [server/auth: disallow creating empty permission ranges](https://github.com/etcd-io/etcd/pull/15619)
- Fix [aligning zap log timestamp resolution to microseconds](https://github.com/etcd-io/etcd/pull/15240). Etcd now uses zap timestamp format: `2006-01-02T15:04:05.999999Z0700` (microsecond instead of milliseconds precision)
- Fix [wsproxy did not print log in JSON format](https://github.com/etcd-io/etcd/pull/15661)
- Fix [etcdserver may panic when parsing a JWT token without username or revision](https://github.com/etcd-io/etcd/pull/15676)
- Fix [Requested watcher progress notifications are not synchronised with stream](https://github.com/etcd-io/etcd/pull/15695)
- Fix [consistently format IPv6 addresses for comparison](https://github.com/etcd-io/etcd/pull/15187)
- Fix [etcd might send duplicated events to watch clients](https://github.com/etcd-io/etcd/pull/15274)
- Fix [etcd docker images all tagged with amd64 architecture](https://github.com/etcd-io/etcd/pull/15612)

### 3.5.9

- Fix [LeaseTimeToLive API may return keys to clients which have no read permission on the keys](https://github.com/etcd-io/etcd/pull/15815)

### 3.5.10

- Fix [`--socket-reuse-port` and `--socket-reuse-address` not able to be set in configuration file](https://github.com/etcd-io/etcd/pull/16435)
- Fix [corruption check may get a `ErrCompacted` error when server has just been compacted](https://github.com/etcd-io/etcd/pull/16048)
- Fix [Hash and HashKV have duplicated RESTful API](https://github.com/etcd-io/etcd/pull/16490)
- Fix [Memberlist results not updated when proxy node down](https://github.com/etcd-io/etcd/pull/15907)
- Fix [Multiple endpoints with same prefix got mixed up](https://github.com/etcd-io/etcd/pull/15939)
- Fix [Unexpected blocking when barrier waits on a nonexistent key](https://github.com/etcd-io/etcd/pull/16188)
- Fix [Reset auth token when failing to authenticate due to auth being disabled](https://github.com/etcd-io/etcd/pull/16241)
- Fix [panic in etcd validate secure endpoints](https://github.com/etcd-io/etcd/pull/16565)

### 3.5.11

- Fix distributed tracing by ensuring `--experimental-distributed-tracing-sampling-rate` configuration option is available to [set tracing sample rate](https://github.com/etcd-io/etcd/pull/16951)
- Fix [url redirects while checking peer urls during new member addition](https://github.com/etcd-io/etcd/pull/16986)

### 3.5.12

- Fix [not validating database consistent index, and panicking on nil backend](https://github.com/etcd-io/etcd/pull/17151)
- Fix [needlessly flocking snapshot files when deleting](https://github.com/etcd-io/etcd/pull/17206)
- Fix [delete inconsistencies in read buffer](https://github.com/etcd-io/etcd/pull/17230)

### 3.5.13

- Fix leases wrongly revoked by the leader by [ignoring old leader's leases revoking request](https://github.com/etcd-io/etcd/pull/17425)
- Fix [no progress notification being sent for watch that doesn't get any events](https://github.com/etcd-io/etcd/pull/17566)
- Fix [watch event loss after compaction](https://github.com/etcd-io/etcd/pull/17612)

### 3.5.14

- Fix [LeaseTimeToLive returns error if leader changed](https://github.com/etcd-io/etcd/pull/17704)
- Fix [ignore raft messages if member id mismatch](https://github.com/etcd-io/etcd/pull/17813)
- Fix [Revision decreasing after panic during compaction](https://github.com/etcd-io/etcd/pull/17865)
- Fix [initialization for mu in client context](https://github.com/etcd-io/etcd/pull/17699)

### 3.5.15

- Fix [add prometheus metric registration for metric `etcd_disk_wal_write_duration_seconds`](https://github.com/etcd-io/etcd/pull/18174)
- Fix [noisy logs from simple auth token expiration by reducing log level to debug](https://github.com/etcd-io/etcd/pull/18245)

### 3.5.16

- Fix [performance regression issue caused by the `ensureLeadership` in lease renew](https://github.com/etcd-io/etcd/pull/18439)

### 3.5.17

- Fix [watchserver related goroutine leakage](https://github.com/etcd-io/etcd/pull/18784)
- Fix [risk of a partial write txn being applied](https://github.com/etcd-io/etcd/pull/18799)
- Fix [panicking occurred due to improper error handling during defragmentation](https://github.com/etcd-io/etcd/pull/18842)
- Fix [close temp file(s) in case an error happens during defragmentation](https://github.com/etcd-io/etcd/pull/18854)

### 3.5.18

- Avoid deadlock in etcd.Close when stopping during bootstrapping, see https://github.com/etcd-io/etcd/pull/19167 and https://github.com/etcd-io/etcd/pull/19258
- Fix [missing delete event on watch opened on same revision as compaction request](https://github.com/etcd-io/etcd/pull/19249)
- Fix [runtime panic that occurs when KeepAlive is called with a Context implemented by an uncomparable type](https://github.com/etcd-io/etcd/pull/18937)

### 3.5.19

- Fix [performance regression due to uncertain compaction sleep interval](https://github.com/etcd-io/etcd/pull/19405)

### 3.5.20

- Fix [the learner promotion changes not being persisted into v3store (bbolt)](https://github.com/etcd-io/etcd/pull/19563)
- Fix [command `etcdctl member promote` doesn't support json output](https://github.com/etcd-io/etcd/pull/19602)
- Fix [grpcproxy can get stuck in and endless loop causing high CPU usage](https://github.com/etcd-io/etcd/pull/19562)

### 3.5.22

- Fix [the compaction pause duration metric is not emitted for every compaction batch](https://github.com/etcd-io/etcd/pull/19771)
- Fix [mvcc: avoid double decrement of watcher gauge on close/cancel race](https://github.com/etcd-io/etcd/pull/20066)
- Fix [Watch on future revision returns old events or notifications](https://github.com/etcd-io/etcd/pull/20290)
- Fix [`--force-new-cluster` can't remove all other members in a corner case](https://github.com/etcd-io/etcd/pull/20339)
- Fix [v2store check (IsMetaStoreOnly) returns wrong result even there is no any auth data](https://github.com/etcd-io/etcd/pull/20357)

### 3.5.23

- Fix [etcd may return success for leaseRenew request even when the lease is revoked](https://github.com/etcd-io/etcd/pull/20616)
- Fix [potential data corruption when applySnapshot and defragment happen concurrently](https://github.com/etcd-io/etcd/pull/20653)

### 3.5.24

- Fix [Learner promotion not being persisted into v3store may be propagated across multiple upgrades](https://github.com/etcd-io/etcd/pull/20797)

### 3.5.25

- Fix [`--force-new-cluster can't clean up learners after creating snapshot`](https://github.com/etcd-io/etcd/pull/20896)

### 3.5.26

- Fix [zombie members in v3store](https://github.com/etcd-io/etcd/pull/20995)
- [Fix a typo of 'etcdctl snapshot restore' command](https://github.com/etcd-io/etcd/pull/20948)

### 3.5.28

- Fix [Race between read index and leader change](https://github.com/etcd-io/etcd/pull/21387)
- Fix [Stale reads caused by process pausing](https://github.com/etcd-io/etcd/pull/21421)
- Fix [cannot promote member from follower when auth is enabled](https://github.com/etcd-io/etcd/pull/21494)
- [server/etcdmain: fix startup deadlock in grpcproxy](https://github.com/etcd-io/etcd/pull/21356)
- Fix [slice bounds trimming single-quoted args in Argify](https://github.com/etcd-io/etcd/pull/21403)

### 3.5.29

- Fix [etcdctl endpoint command regression with option --cluster when auth is enabled](https://github.com/etcd-io/etcd/pull/21532)

### 3.5.30

- [Fixed an issue that prevented adding a new member when one member was down, even though quorum was still satisfied](https://github.com/etcd-io/etcd/pull/21669)
- Fix RBAC authorization bypass allowing read access via PrevKv or lease attachment in Put requests nested in etcd transactions (see [PR/21682](https://github.com/etcd-io/etcd/pull/21682) and [PR/21687](https://github.com/etcd-io/etcd/pull/21687))

### 3.5.32

- Fix [websocket authentication with bearer-prefixed auth tokens](https://github.com/etcd-io/etcd/pull/21935)
- Fix [CRL enforcement bypass on gRPC listener when `--listen-client-http-urls` is configured](https://github.com/etcd-io/etcd/pull/22021), refer to [security/advisories/GHSA-3wh4-j44w-pg92](https://github.com/etcd-io/etcd/security/advisories/GHSA-3wh4-j44w-pg92) for more details
- Avoid logging for JWT token for a case of failed parsing ([#21993](https://github.com/etcd-io/etcd/pull/21993))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.5.32**, the newest release recorded here for this line.

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
