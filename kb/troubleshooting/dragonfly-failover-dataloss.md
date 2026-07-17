---
id: TROUBLE-DRAGONFLY_FAILOVER_DATALOSS
type: troubleshooting
title: "Dragonfly operator: failover data loss / replica readiness / auth / TLS"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=1.28.1"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - dragonfly failover data loss
  - dragonfly replica ready during full sync
  - dragonfly healthcheck wrong port
  - dragonfly noauth admin port
  - dragonfly maxmemory not set
tags:
  - troubleshooting
  - dragonfly
  - data
  - cache
sources:
  - type: docs
    path: dragonfly-operator issue #289 (failover data loss)
    url: https://github.com/dragonflydb/dragonfly-operator/issues/289
    note: "SLAVEOF to terminating master → data loss"
  - type: docs
    path: dragonfly-operator PR #467 (replication-ready gate)
    url: https://github.com/dragonflydb/dragonfly-operator/pull/467
    note: "readiness ignores replication sync state"
relations:
  - type: see_also
    target: CONCEPT-ADDON_DRAGONFLY
---

# Dragonfly operator: failover data loss / replica readiness / auth / TLS

## Summary

Community-sourced Dragonfly-operator risks — several can cause **data loss**. During failover
the operator may replicate from a **terminating master**, or mark a **replica Ready mid-sync**
so a drain removes the master before sync completes. Plus health-check port, auth, TLS-log and
`--maxmemory` gotchas.

## Problem

- Data lost after a master pod termination / node drain.
- Replica shows Ready while still doing a full sync.
- Pods fail health checks after an operator upgrade (wrong port).
- `NOAUTH Authentication required` on internal `SLAVE OF NO ONE`.
- TLS port logs flooded with `ssl3_get_record:wrong version number`.

## Context

- Applies to dragonfly-operator ≥1.1.x / datastore **≥1.28.1** (owner runs op 1.1.11 / db
  1.28.1 — [[CONCEPT-ADDON_DRAGONFLY]]).

## Diagnostics

- **Failover data loss:** the operator reads the terminating master's IP and issues
  `SLAVEOF <old-master>` to the replica (flush + full re-replication) without checking
  `deletionTimestamp`; if the master dies before sync finishes, data is lost — **enable PVC
  snapshotting** to mitigate (issue #289).
- **Replica Ready mid-sync:** readiness ignores replication state, so a drain (`PDB
  maxUnavailable=1`) can remove the master mid-sync — use the replication-aware readiness gate
  `dragonflydb.io/replication-ready` (PR #467) or enable snapshots (issue #465).
- **Health-check wrong port (after upgrade):** port autodetect can pick e.g. UDP 8125 — set
  **`HEALTHCHECK_PORT=6379`** explicitly (issue #173).
- **NOAUTH:** with auth enabled and `admin_nopass=false`, the operator's admin-port client has
  no creds — keep the admin port passwordless (default `admin_nopass=true`) (issue #133).
- **TLS wrong-version logs:** health probes connect plaintext to the TLS port; align the CA
  between serving and client certs (issue #145 / dragonfly #4171).
- **maxmemory:** `--maxmemory` is not auto-set from K8s requests; set it relative to the
  container limit (Dragonfly may refuse to start without it).

## Known Issues

- **Datastore 1.28.1 is affected by 3 CVEs** (CVE-2026-62357/-54341/-47206) — override
  `spec.image` to ≥1.40 ([[CONCEPT-ADDON_DRAGONFLY]]).
- **Future landmines:** datastore **1.31.0** memory-growth/OOM regression; **1.35.0** restart
  loop (`accept system:22`) — avoid those versions.

## References

- dragonfly-operator issues #289/#465/#173/#133/#145, PR #467 (above).
- Addon: [[CONCEPT-ADDON_DRAGONFLY]].
