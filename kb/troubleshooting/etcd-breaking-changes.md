---
id: TROUBLE-ETCD_BREAKING_CHANGES
type: troubleshooting
title: "etcd: declared breaking changes by release"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.1.0 <=4.0.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - etcd breaking changes
  - etcd upgrade broke
  - etcd action required upgrade
  - what breaks upgrading etcd
tags:
  - upgrade
  - breaking-change
  - etcd
sources:
  - type: docs
    path: etcd-io/etcd release notes — entries marked breaking / action required
    url: https://github.com/etcd-io/etcd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# etcd: declared breaking changes by release

## Summary

**98 behaviour changes** the project itself marked as breaking or action-required, across
10 releases from 3.1.0 to 4.0.0. These are not defects: they work as designed and still break
a configuration that worked yesterday. An upgrade crossing any of them needs a decision, not just a
rollout.

## Problem

The upgrade itself usually succeeds. The damage shows up afterwards — a setting silently ignored, a
default flipped, an API version withdrawn, a variable that must now be set explicitly.

## Context

### 3.1.0

- Deprecated following gRPC metrics in favor of [go-grpc-prometheus](https://github.com/grpc-ecosystem/go-grpc-prometheus). `etcd_grpc_requests_total` `etcd_grpc_requests_failed_total` `etcd_grpc_active_streams` `etcd_grpc_unary_requests_duration_seconds`

### 3.2.0

- Increased [`--snapshot-count` default value from 10,000 to 100,000](https://github.com/etcd-io/etcd/pull/7160). Higher snapshot count means it holds Raft entries in memory for longer before discarding old entries. It is a trade-off between less frequent snapshotting and [higher memory usage](https://github.com/kubernetes/kubernetes/issues/60589#issuecomment-371977156). User lower `--snapshot-count` value for lower memory usage. User higher `--snapshot-count` value for better availabilities of slow followers (less frequent snapshots from leader)
- `clientv3.Lease.TimeToLive` returns `LeaseTimeToLiveResponse.TTL == -1` on lease not found
- `clientv3.NewFromConfigFile` is moved to `clientv3/yaml.NewConfig`
- `embed.Etcd.Peers` field is now `[]*peerListener`
- Rejects domains names for `--listen-peer-urls` and `--listen-client-urls` (3.1 only prints out warnings), since [domain name is invalid for network interface binding](https://github.com/etcd-io/etcd/issues/6336)

### 3.3.0

- Require [`google.golang.org/grpc`](https://github.com/grpc/grpc-go/releases) [**`v1.7.4`**](https://github.com/grpc/grpc-go/releases/tag/v1.7.4) or [**`v1.7.5`**](https://github.com/grpc/grpc-go/releases/tag/v1.7.5). Deprecate [`metadata.Incoming/OutgoingContext`](https://github.com/etcd-io/etcd/pull/7896). Deprecate `grpclog.Logger`, upgrade to [`grpclog.LoggerV2`](https://github.com/etcd-io/etcd/pull/8533). Deprecate [`grpc.ErrClientConnTimeout`](https://github.com/etcd-io/etcd/pull/8505) errors in `clientv3`. Use [`MaxRecvMsgSize` and `MaxSendMsgSize`](https://github.com/etcd-io/etcd/pull/8437) to limit message size, in etcd server
- Translate [gRPC status error in v3 client `Snapshot` API](https://github.com/etcd-io/etcd/pull/9038)
- v3 `etcdctl` [`lease timetolive LEASE_ID`](https://github.com/etcd-io/etcd/issues/9028) on expired lease now prints [`"lease LEASE_ID already expired"`](https://github.com/etcd-io/etcd/pull/9047). <=3.2 prints `"lease LEASE_ID granted with TTL(0s), remaining(-1s)"`
- Replace [gRPC gateway](https://github.com/grpc-ecosystem/grpc-gateway) endpoint `/v3alpha` with [`/v3beta`](https://github.com/etcd-io/etcd/pull/8880). To deprecate [`/v3alpha`](https://github.com/etcd-io/etcd/issues/8125) in v3.4. In v3.3, `curl -L http://localhost:2379/v3alpha/kv/put -X POST -d '{"key": "Zm9v", "value": "YmFy"}'` still works as a fallback to `curl -L http://localhost:2379/v3beta/kv/put -X POST -d '{"key": "Zm9v", "value": "YmFy"}'`, but `curl -L http://localhost:2379/v3alpha/kv/put -X POST -d '{"key": "Zm9v", "value": "YmFy"}'` won't work in v3.4. Use `curl -L http://localhost:2379/v3beta/kv/put -X POST -d '{"key": "Zm9v", "value": "YmFy"}'` instead
- Change `etcd --auto-compaction-retention` flag to [accept string values](https://github.com/etcd-io/etcd/pull/8563) with [finer granularity](https://github.com/etcd-io/etcd/issues/8503). Now that `etcd --auto-compaction-retention` accepts string values, etcd configuration YAML file `auto-compaction-retention` field must be changed to `string` type. Previously, `--config-file etcd.config.yaml` can have `auto-compaction-retention: 24` field, now must be `auto-compaction-retention: "24"` or `auto-compaction-retention: "24h"`. If configured as `etcd --auto-compaction-mode periodic --auto-compaction-retention "24h"`, the time duration value for `etcd --auto-compaction-retention` flag must be valid for [`time.ParseDuration`](https://golang.org/pkg/time/#ParseDuration) function in Go

### 3.3.14

- Rewrite [client balancer](https://github.com/etcd-io/etcd/pull/9860) with [new gRPC balancer interface](https://github.com/etcd-io/etcd/issues/9106). Upgrade [gRPC to v1.23.0](https://github.com/etcd-io/etcd/pull/10911). Improve [client balancer failover against secure endpoints](https://github.com/etcd-io/etcd/pull/10911). Fix ["kube-apiserver 1.13.x refuses to work when first etcd-server is not available" (kubernetes#72102)](https://github.com/kubernetes/kubernetes/issues/72102). [The new client balancer](https://etcd.io/docs/latest/learning/design-client/) uses an asynchronous resolver to pass endpoints to the gRPC dial function. to block until the underlying connection is up, pass `grpc.WithBlock()` to `clientv3.Config.DialOptions`
- Require [*Go 1.12+*](https://github.com/etcd-io/etcd/pull/10045)
- Compile with [*Go 1.12.9*](https://golang.org/doc/devel/release.html#go1.12) including [*Go 1.12.8*](https://groups.google.com/d/msg/golang-announce/65QixT3tcmg/DrFiG6vvCwAJ) security fixes
- Migrate dependency management tool from `glide` to [Go module](https://github.com/etcd-io/etcd/pull/10063). <= 3.3 puts `vendor` directory under `cmd/vendor` directory to [prevent conflicting transitive dependencies](https://github.com/etcd-io/etcd/issues/4913). 3.4 moves `cmd/vendor` directory to `vendor` at repository root. Remove recursive symlinks in `cmd` directory. Now `go get/install/build` on `etcd` packages (e.g. `clientv3`, `tools/benchmark`) enforce builds with etcd `vendor` directory
- Deprecated `latest` [release container](https://console.cloud.google.com/gcr/images/etcd-development/GLOBAL/etcd) tag. **`docker pull gcr.io/etcd-development/etcd:latest` would not be up-to-date**
- Deprecated [minor](https://semver.org/) version [release container](https://console.cloud.google.com/gcr/images/etcd-development/GLOBAL/etcd) tags. `docker pull gcr.io/etcd-development/etcd:v3.3` would still work but may be stale. **`docker pull gcr.io/etcd-development/etcd:v3.4` would not work**. Use **`docker pull gcr.io/etcd-development/etcd:v3.3.14`** instead, with the exact patch version
- Deprecated [ACIs from official release](https://github.com/etcd-io/etcd/pull/9059). [AppC was officially suspended](https://github.com/appc/spec#-disclaimer-), as of late 2016. [`acbuild`](https://github.com/containers/build#this-project-is-currently-unmaintained) is not maintained anymore. `*.aci` files are not available from `v3.4` release

### 3.3.15

- Revert "Migrate dependency management tool from `glide` to [Go module](https://github.com/etcd-io/etcd/pull/10063)". Now, etcd >= v3.3.15 uses `glide` for dependency management. See [kubernetes#81434](https://github.com/kubernetes/kubernetes/pull/81434) for more contexts

### 3.3.23

- Fix [incorrect package dependency when etcd clientv3 used as libary](https://github.com/etcd-io/etcd/issues/12068)
- Changed behavior on [existing dir permission](https://github.com/etcd-io/etcd/pull/11798). Previously, the permission was not checked on existing data directory and the directory used for automatically generating self-signed certificates for TLS connections with clients. Now a check is added to make sure those directories, if already exist, has a desired permission of 700 on Linux and 777 on Windows

### 3.4.0

- Rewrite [client balancer](https://github.com/etcd-io/etcd/pull/9860) with [new gRPC balancer interface](https://github.com/etcd-io/etcd/issues/9106). Upgrade [gRPC to v1.23.0](https://github.com/etcd-io/etcd/pull/10911). Improve [client balancer failover against secure endpoints](https://github.com/etcd-io/etcd/pull/10911). Fix ["kube-apiserver 1.13.x refuses to work when first etcd-server is not available" (kubernetes#72102)](https://github.com/kubernetes/kubernetes/issues/72102). Fix [gRPC panic "send on closed channel](https://github.com/etcd-io/etcd/issues/9956). [The new client balancer](https://etcd.io/docs/latest/learning/design-client/) uses an asynchronous resolver to pass endpoints to the gRPC dial function. To block until the underlying connection is up, pass `grpc.WithBlock()` to `clientv3.Config.DialOptions`
- Require [*Go 1.12+*](https://github.com/etcd-io/etcd/pull/10045). Compile with [*Go 1.12.9*](https://golang.org/doc/devel/release.html#go1.12) including [*Go 1.12.8*](https://groups.google.com/d/msg/golang-announce/65QixT3tcmg/DrFiG6vvCwAJ) security fixes
- Migrate dependency management tool from `glide` to [Go module](https://github.com/etcd-io/etcd/pull/10063). <= 3.3 puts `vendor` directory under `cmd/vendor` directory to [prevent conflicting transitive dependencies](https://github.com/etcd-io/etcd/issues/4913). 3.4 moves `cmd/vendor` directory to `vendor` at repository root. Remove recursive symlinks in `cmd` directory. Now `go get/install/build` on `etcd` packages (e.g. `clientv3`, `tools/benchmark`) enforce builds with etcd `vendor` directory
- Deprecated `latest` [release container](https://console.cloud.google.com/gcr/images/etcd-development/GLOBAL/etcd) tag. **`docker pull gcr.io/etcd-development/etcd:latest` would not be up-to-date**
- Deprecated [minor](https://semver.org/) version [release container](https://console.cloud.google.com/gcr/images/etcd-development/GLOBAL/etcd) tags. `docker pull gcr.io/etcd-development/etcd:v3.3` would still work. **`docker pull gcr.io/etcd-development/etcd:v3.4` would not work**. Use **`docker pull gcr.io/etcd-development/etcd:v3.4.x`** instead, with the exact patch version
- Deprecated [ACIs from official release](https://github.com/etcd-io/etcd/pull/9059). [AppC was officially suspended](https://github.com/appc/spec#-disclaimer-), as of late 2016. [`acbuild`](https://github.com/containers/build#this-project-is-currently-unmaintained) is not maintained anymore. `*.aci` files are not available from `v3.4` release
- Move [`"github.com/coreos/etcd"`](https://github.com/etcd-io/etcd/issues/9965) to [`"github.com/etcd-io/etcd"`](https://github.com/etcd-io/etcd/issues/9965). Change import path to `"go.etcd.io/etcd"`. e.g. `import "go.etcd.io/etcd/raft"`
- Make [`ETCDCTL_API=3 etcdctl` default](https://github.com/etcd-io/etcd/issues/9600). Now, `etcdctl set foo bar` must be `ETCDCTL_API=2 etcdctl set foo bar`. Now, `ETCDCTL_API=3 etcdctl put foo bar` could be just `etcdctl put foo bar`
- Make [`etcd --enable-v2=false` default](https://github.com/etcd-io/etcd/pull/10935)
- Make [`embed.DefaultEnableV2` `false` default](https://github.com/etcd-io/etcd/pull/10935)
- **Deprecated `etcd --ca-file` flag**. Use [`etcd --trusted-ca-file`](https://github.com/etcd-io/etcd/pull/9470) instead (`etcd --ca-file` flag has been marked deprecated since v2.1)
- **Deprecated `etcd --peer-ca-file` flag**. Use [`etcd --peer-trusted-ca-file`](https://github.com/etcd-io/etcd/pull/9470) instead (`etcd --peer-ca-file` flag has been marked deprecated since v2.1)
- **Deprecated `pkg/transport.TLSInfo.CAFile` field**. Use [`pkg/transport.TLSInfo.TrustedCAFile`](https://github.com/etcd-io/etcd/pull/9470) instead (`CAFile` field has been marked deprecated since v2.1)
- Exit on [empty hosts in advertise URLs](https://github.com/etcd-io/etcd/pull/8786). Address [advertise client URLs accepts empty hosts](https://github.com/etcd-io/etcd/issues/8379). e.g. exit with error on `--advertise-client-urls=http://:2379`. e.g. exit with error on `--initial-advertise-peer-urls=http://:2380`
- Exit on [shadowed environment variables](https://github.com/etcd-io/etcd/pull/9382). Address [error on shadowed environment variables](https://github.com/etcd-io/etcd/issues/8380). e.g. exit with error on `ETCD_NAME=abc etcd --name=def`. e.g. exit with error on `ETCD_INITIAL_CLUSTER_TOKEN=abc etcd --initial-cluster-token=def`. e.g. exit with error on `ETCDCTL_ENDPOINTS=abc.com ETCDCTL_API=3 etcdctl endpoint health --endpoints=def.com`
- Change [`etcdserverpb.AuthRoleRevokePermissionRequest/key,range_end` fields type from `string` to `bytes`](https://github.com/etcd-io/etcd/pull/9433)
- Deprecating `etcd_debugging_mvcc_db_total_size_in_bytes` Prometheus metric (to be removed in v3.5). Use [`etcd_mvcc_db_total_size_in_bytes`](https://github.com/etcd-io/etcd/pull/9819) instead
- Deprecating `etcd_debugging_mvcc_put_total` Prometheus metric (to be removed in v3.5). Use [`etcd_mvcc_put_total`](https://github.com/etcd-io/etcd/pull/10962) instead
- Deprecating `etcd_debugging_mvcc_delete_total` Prometheus metric (to be removed in v3.5). Use [`etcd_mvcc_delete_total`](https://github.com/etcd-io/etcd/pull/10962) instead
- Deprecating `etcd_debugging_mvcc_range_total` Prometheus metric (to be removed in v3.5). Use [`etcd_mvcc_range_total`](https://github.com/etcd-io/etcd/pull/10968) instead
- Deprecating `etcd_debugging_mvcc_txn_total`Prometheus metric (to be removed in v3.5). Use [`etcd_mvcc_txn_total`](https://github.com/etcd-io/etcd/pull/10968) instead
- Rename `etcdserver.ServerConfig.SnapCount` field to `etcdserver.ServerConfig.SnapshotCount`, to be consistent with the flag name `etcd --snapshot-count`
- Rename `embed.Config.SnapCount` field to [`embed.Config.SnapshotCount`](https://github.com/etcd-io/etcd/pull/9745), to be consistent with the flag name `etcd --snapshot-count`
- Change [`embed.Config.CorsInfo` in `*cors.CORSInfo` type to `embed.Config.CORS` in `map[string]struct{}` type](https://github.com/etcd-io/etcd/pull/9490)
- Deprecated [`embed.Config.SetupLogging`](https://github.com/etcd-io/etcd/pull/9572). Now logger is set up automatically based on [`embed.Config.Logger`, `embed.Config.LogOutputs`, `embed.Config.Debug` fields](https://github.com/etcd-io/etcd/pull/9572)
- Rename [`etcd --log-output` to `etcd --log-outputs`](https://github.com/etcd-io/etcd/pull/9624) to support multiple log outputs. **`etcd --log-output`** will be deprecated in v3.5
- Rename [**`embed.Config.LogOutput`** to **`embed.Config.LogOutputs`**](https://github.com/etcd-io/etcd/pull/9624) to support multiple log outputs
- Change [**`embed.Config.LogOutputs`** type from `string` to `[]string`](https://github.com/etcd-io/etcd/pull/9579) to support multiple log outputs. Now that `etcd --log-outputs` accepts multiple writers, etcd configuration YAML file `log-outputs` field must be changed to `[]string` type. Previously, `etcd --config-file etcd.config.yaml` can have `log-outputs: default` field, now must be `log-outputs: [default]`
- Deprecating [`etcd --debug`](https://github.com/etcd-io/etcd/pull/10947) flag. Use `etcd --log-level=debug` flag instead. v3.5 will deprecate `etcd --debug` flag in favor of `etcd --log-level=debug`
- Change v3 `etcdctl snapshot` exit codes with [`snapshot` package](https://github.com/etcd-io/etcd/pull/9118/commits/df689f4280e1cce4b9d61300be13ca604d41670a). Exit on error with exit code 1 (no more exit code 5 or 6 on `snapshot save/restore` commands)
- Deprecated [`grpc.ErrClientConnClosing`](https://github.com/etcd-io/etcd/pull/10981). `clientv3` and `proxy/grpcproxy` now does not return `grpc.ErrClientConnClosing`. `grpc.ErrClientConnClosing` has been [deprecated in gRPC >= 1.10](https://github.com/grpc/grpc-go/pull/1854). Use `clientv3.IsConnCanceled(error)` or `google.golang.org/grpc/status.FromError(error)` instead
- Deprecated [gRPC gateway](https://github.com/grpc-ecosystem/grpc-gateway) endpoint `/v3beta` with [`/v3`](https://github.com/etcd-io/etcd/pull/9298). Deprecated [`/v3alpha`](https://github.com/etcd-io/etcd/pull/9298). To deprecate [`/v3beta`](https://github.com/etcd-io/etcd/issues/9189) in v3.5. In v3.4, `curl -L http://localhost:2379/v3beta/kv/put -X POST -d '{"key": "Zm9v", "value": "YmFy"}'` still works as a fallback to `curl -L http://localhost:2379/v3/kv/put -X POST -d '{"key": "Zm9v", "value": "YmFy"}'`, but `curl -L http://localhost:2379/v3beta/kv/put -X POST -d '{"key": "Zm9v", "value": "YmFy"}'` won't work in v3.5. Use `curl -L http://localhost:2379/v3/kv/put -X POST -d '{"key": "Zm9v", "value": "YmFy"}'` instead
- Change [`wal` package function signatures](https://github.com/etcd-io/etcd/pull/9572) to support [structured logger and logging to file](https://github.com/etcd-io/etcd/issues/9438) in server-side. Previously, `Open(dirpath string, snap walpb.Snapshot) (*WAL, error)`, now `Open(lg *zap.Logger, dirpath string, snap walpb.Snapshot) (*WAL, error)`. Previously, `OpenForRead(dirpath string, snap walpb.Snapshot) (*WAL, error)`, now `OpenForRead(lg *zap.Logger, dirpath string, snap walpb.Snapshot) (*WAL, error)`. Previously, `Repair(dirpath string) bool`, now `Repair(lg *zap.Logger, dirpath string) bool`. Previously, `Create(dirpath string, metadata []byte) (*WAL, error)`, now `Create(lg *zap.Logger, dirpath string, metadata []byte) (*WAL, error)`
- Remove [`pkg/cors` package](https://github.com/etcd-io/etcd/pull/9490)
- Move internal packages to `etcdserver`. `"github.com/coreos/etcd/alarm"` to `"go.etcd.io/etcd/etcdserver/api/v3alarm"`. `"github.com/coreos/etcd/compactor"` to `"go.etcd.io/etcd/etcdserver/api/v3compactor"`. `"github.com/coreos/etcd/discovery"` to `"go.etcd.io/etcd/etcdserver/api/v2discovery"`. `"github.com/coreos/etcd/etcdserver/auth"` to `"go.etcd.io/etcd/etcdserver/api/v2auth"`. `"github.com/coreos/etcd/etcdserver/membership"` to `"go.etcd.io/etcd/etcdserver/api/membership"`. `"github.com/coreos/etcd/etcdserver/stats"` to `"go.etcd.io/etcd/etcdserver/api/v2stats"`. `"github.com/coreos/etcd/error"` to `"go.etcd.io/etcd/etcdserver/api/v2error"`. `"github.com/coreos/etcd/rafthttp"` to `"go.etcd.io/etcd/etcdserver/api/rafthttp"`. `"github.com/coreos/etcd/snap"` to `"go.etcd.io/etcd/etcdserver/api/snap"`. `"github.com/coreos/etcd/store"` to `"go.etcd.io/etcd/etcdserver/api/v2store"`
- Change [snapshot file permissions](https://github.com/etcd-io/etcd/pull/9977): On Linux, the snapshot file changes from readable by all (mode 0644) to readable by the user only (mode 0600)
- Change [`pkg/adt.IntervalTree` from `struct` to `interface`](https://github.com/etcd-io/etcd/pull/10959). See [`pkg/adt` README](https://github.com/etcd-io/etcd/tree/main/pkg/adt) and [`pkg/adt` godoc](https://godoc.org/go.etcd.io/etcd/pkg/adt)
- Release branch `/version` defines version `3.4.x-pre`, instead of `3.4.y+git`. Use `3.4.5-pre`, instead of `3.4.4+git`

### 3.4.10

- Changed behavior on [existing dir permission](https://github.com/etcd-io/etcd/pull/11798). Previously, the permission was not checked on existing data directory and the directory used for automatically generating self-signed certificates for TLS connections with clients. Now a check is added to make sure those directories, if already exist, has a desired permission of 700 on Linux and 777 on Windows

### 3.5.0

- `go.etcd.io/etcd` Go packages have moved to `go.etcd.io/etcd/{api,pkg,raft,client,etcdctl,server,raft,tests}/v3` to follow the [Go modules](https://github.com/golang/go/wiki/Modules) conventions
- `go.etcd.io/clientv3/snapshot` SnapshotManager class have moved to `go.etcd.io/clientv3/etcdctl`. The method `snapshot.Save` to download a snapshot from the remote server was preserved in 'go.etcd.io/clientv3/snapshot`
- `go.etcd.io/client' package got migrated to 'go.etcd.io/client/v2'
- Changed behavior of clientv3 API [MemberList](https://github.com/etcd-io/etcd/pull/11639). Previously, it is directly served with server's local data, which could be stale. Now, it is served with linearizable guarantee. If the server is disconnected from quorum, `MemberList` call will fail
- [gRPC gateway](https://github.com/grpc-ecosystem/grpc-gateway) only supports [`/v3`](TODO) endpoint. Deprecated [`/v3beta`](https://github.com/etcd-io/etcd/pull/9298). `curl -L http://localhost:2379/v3beta/kv/put -X POST -d '{"key": "Zm9v", "value": "YmFy"}'` doesn't work in v3.5. Use `curl -L http://localhost:2379/v3/kv/put -X POST -d '{"key": "Zm9v", "value": "YmFy"}'` instead
- **`etcd --experimental-enable-v2v3` flag remains experimental and to be deprecated.** v2 storage emulation feature will be deprecated in the next release. etcd 3.5 is the last version that supports V2 API. Flags `--enable-v2` and `--experimental-enable-v2v3` [are now deprecated](https://github.com/etcd-io/etcd/pull/12940) and will be removed in etcd v3.6 release
- **`etcd --experimental-backend-bbolt-freelist-type` flag has been deprecated.** Use **`etcd --backend-bbolt-freelist-type`** instead. The default type is hashmap and it is stable now
- **`etcd --debug` flag has been deprecated.** Use **`etcd --log-level=debug`** instead
- Remove [`embed.Config.Debug`](https://github.com/etcd-io/etcd/pull/10947)
- **`etcd --log-output` flag has been deprecated.** Use **`etcd --log-outputs`** instead
- **`etcd --logger=zap --log-outputs=stderr`** is now the default
- **`etcd --logger=capnslog` flag value has been deprecated.**
- **`etcd --logger=zap --log-outputs=default` flag value is not supported.**. Use `etcd --logger=zap --log-outputs=stderr`. Or, use `etcd --logger=zap --log-outputs=systemd/journal` to send logs to the local systemd journal. Previously, if etcd parent process ID (PPID) is 1 (e.g. run with systemd), `etcd --logger=capnslog --log-outputs=default` redirects server logs to local systemd journal. And if write to journald fails, it writes to `os.Stderr` as a fallback. However, even with PPID 1, it can fail to dial systemd journal (e.g. run embedded etcd with Docker container). Then, [every single log write will fail](https://github.com/etcd-io/etcd/pull/9729) and fall back to `os.Stderr`, which is inefficient. To avoid this problem, systemd journal logging must be configured manually
- **`etcd --log-outputs=stderr`** is now the default
- **`etcd --log-package-levels` flag for `capnslog` has been deprecated.** Now, **`etcd --logger=zap --log-outputs=stderr`** is the default
- **`[CLIENT-URL]/config/local/log` endpoint has been deprecated, as is `etcd --log-package-levels` flag.** `curl http://127.0.0.1:2379/config/local/log -XPUT -d '{"Level":"DEBUG"}'` won't work. Please use `etcd --logger=zap --log-outputs=stderr` instead
- Deprecated `etcd_debugging_mvcc_db_total_size_in_bytes` Prometheus metric. Use `etcd_mvcc_db_total_size_in_bytes` instead
- Deprecated `etcd_debugging_mvcc_put_total` Prometheus metric. Use `etcd_mvcc_put_total` instead
- Deprecated `etcd_debugging_mvcc_delete_total` Prometheus metric. Use `etcd_mvcc_delete_total` instead
- Deprecated `etcd_debugging_mvcc_txn_total` Prometheus metric. Use `etcd_mvcc_txn_total` instead
- Deprecated `etcd_debugging_mvcc_range_total` Prometheus metric. Use `etcd_mvcc_range_total` instead
- Main branch `/version` outputs `3.5.0-pre`, instead of `3.4.0+git`
- Changed `proxy` package function signature to [support structured logger](https://github.com/etcd-io/etcd/pull/11614). Previously, `NewClusterProxy(c *clientv3.Client, advaddr string, prefix string) (pb.ClusterServer, <-chan struct{})`, now `NewClusterProxy(lg *zap.Logger, c *clientv3.Client, advaddr string, prefix string) (pb.ClusterServer, <-chan struct{})`. Previously, `Register(c *clientv3.Client, prefix string, addr string, ttl int)`, now `Register(lg *zap.Logger, c *clientv3.Client, prefix string, addr string, ttl int) <-chan struct{}`. Previously, `NewHandler(t *http.Transport, urlsFunc GetProxyURLs, failureWait time.Duration, refreshInterval time.Duration) http.Handler`, now `NewHandler(lg *zap.Logger, t *http.Transport, urlsFunc GetProxyURLs, failureWait time.Duration, refreshInterval time.Duration) http.Handler`
- Changed `pkg/flags` function signature to [support structured logger](https://github.com/etcd-io/etcd/pull/11616). Previously, `SetFlagsFromEnv(prefix string, fs *flag.FlagSet) error`, now `SetFlagsFromEnv(lg *zap.Logger, prefix string, fs *flag.FlagSet) error`. Previously, `SetPflagsFromEnv(prefix string, fs *pflag.FlagSet) error`, now `SetPflagsFromEnv(lg *zap.Logger, prefix string, fs *pflag.FlagSet) error`
- ClientV3 supports [grpc resolver API](https://github.com/etcd-io/etcd/blob/main/client/v3/naming/resolver/resolver.go). Endpoints can be managed using [endpoints.Manager](https://github.com/etcd-io/etcd/blob/main/client/v3/naming/endpoints/endpoints.go) Previously supported [GRPCResolver was decomissioned](https://github.com/etcd-io/etcd/pull/12675). Use [resolver](https://github.com/etcd-io/etcd/blob/main/client/v3/naming/resolver/resolver.go) instead
- Turned on [--pre-vote by default](https://github.com/etcd-io/etcd/pull/12770). Should prevent disrupting RAFT leader by an individual member
- [ETCD_CLIENT_DEBUG env](https://github.com/etcd-io/etcd/pull/12786): Now supports log levels (debug, info, warn, error, dpanic, panic, fatal). Only when set, overrides application-wide grpc logging settings
- [Embed Etcd.Close()](https://github.com/etcd-io/etcd/pull/12828) needs to called exactly once and closes Etcd.Err() stream
- [Embed Etcd does not override global/grpc logger](https://github.com/etcd-io/etcd/pull/12861) be default any longer. If desired, please call `embed.Config::SetupGlobalLoggers()` explicitly
- [Embed Etcd custom logger should be configured using simpler builder `NewZapLoggerBuilder`](https://github.com/etcd-io/etcd/pull/12973)
- Client errors of `context cancelled` or `context deadline exceeded` are exposed as `codes.Canceled` and `codes.DeadlineExceeded`, instead of `codes.Unknown`

### 4.0.0

- [Secure etcd by default](https://github.com/etcd-io/etcd/issues/9475)?
- Deprecate [`etcd --proxy*`](TODO) flags; **no more v2 proxy**
- Deprecate [v2 storage backend](https://github.com/etcd-io/etcd/issues/9232); **no more v2 store**. v2 API is still supported via [v2 emulation](TODO)
- `clientv3.Client.KeepAlive(ctx context.Context, id LeaseID) (<-chan *LeaseKeepAliveResponse, error)` is now [`clientv4.Client.KeepAlive(ctx context.Context, id LeaseID) <-chan *LeaseKeepAliveResponse`](TODO). Similar to `Watch`, [`KeepAlive` does not return errors](https://github.com/etcd-io/etcd/issues/7488). If there's an unknown server error, kill all open channels and create a new stream on the next `KeepAlive` call
- Rename `github.com/coreos/client` to `github.com/coreos/clientv2`
- [`etcd --experimental-initial-corrupt-check`](TODO) has been deprecated. Use [`etcd --initial-corrupt-check`](TODO) instead
- [`etcd --experimental-corrupt-check-time`](TODO) has been deprecated. Use [`etcd --corrupt-check-time`](TODO) instead


## Diagnostics

```bash
# which version is actually deployed
kubectl get nodes -o wide
helm list -A
```

Cross the list above against the range you are moving through, not only the target version.

## Known Issues

Entries are verbatim from upstream release notes and filtered mechanically: lines shorter than
45 characters and duplicates are dropped, because section headings and list fragments reach the
extractor looking like entries. If a release you care about appears empty here, read its notes
upstream before concluding that nothing changed.

## References

- Upstream releases of `etcd-io/etcd`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/etcd.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
