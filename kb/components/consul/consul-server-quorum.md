---
id: TROUBLE-CONSUL_SERVER_QUORUM
type: troubleshooting
title: "Consul server Raft quorum lost (leave_on_terminate, scale-down, PVC loss) — etcd-class outage"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=1.22.7 <=2.0.2"
verified_at: "2026-07-18"
confidence: verified
aliases:
  - consul lost quorum
  - consul no cluster leader
  - consul server statefulset notready
  - consul leave_on_terminate
  - consul scale down quorum
  - consul pvc data loss
tags:
  - consul
  - troubleshooting
  - raft
  - storage
sources:
  - type: code
    path: charts/consul/templates/server-statefulset.yaml
    url: https://github.com/hashicorp/consul-k8s/blob/v2.0.2/charts/consul/templates/server-statefulset.yaml
    note: "podManagementPolicy Parallel; readiness curls /v1/status/leader (L585-611); PVC volumeClaimTemplates (L739-749)"
  - type: code
    path: charts/consul/templates/server-config-configmap.yaml
    url: https://github.com/hashicorp/consul-k8s/blob/v2.0.2/charts/consul/templates/server-config-configmap.yaml
    note: "leave_on_terminate: true hardcoded (L69); autopilot min_quorum + disable_upgrade_migration (L70-72); retry_join headless svc"
relations:
  - type: see_also
    target: CONCEPT-CONSUL_ON_K8S
  - type: see_also
    target: COMPONENT-ETCD
  - type: see_also
    target: TROUBLE-CONSUL_CONNECT_INJECT_WEBHOOK
---

# Consul server Raft quorum lost (leave_on_terminate, scale-down, PVC loss) — etcd-class outage

## Summary

Consul servers run a **StatefulSet with Raft** — same quorum math as etcd ([[COMPONENT-ETCD]]).
`server.replicas` defaults to **1** (no fault tolerance). Two design choices bite: `leave_on_terminate:
true` is **hardcoded**, so a graceful stop makes a server **leave** the Raft pool (shrinking quorum),
and the readiness probe requires a **live leader** — so **if quorum is lost, every server pod goes
NotReady**, the `-server` Service loses endpoints, and clients + connect-inject can no longer reach
Consul (cascading into [[TROUBLE-CONSUL_CONNECT_INJECT_WEBHOOK]]).

## Problem

- `No cluster leader` in server logs; all `<release>-server-*` pods `NotReady`; the `-server` Service
  has no endpoints.
- Manually scaling the server StatefulSet down (e.g. 5→3) unexpectedly reduces fault tolerance / loses
  data.
- After deleting server PVCs: Consul comes up empty (Raft data gone) → forces ACL re-bootstrap
  ([[TROUBLE-CONSUL_ACL_BOOTSTRAP]]).

## Context

- Applies to consul-k8s **1.9.x–2.0.x** ([[CONCEPT-CONSUL_ON_K8S]]).
- **`leave_on_terminate: true` (hardcoded, `server-config-configmap.yaml`@v2.0.2 L69):** a server that
  stops gracefully *leaves* the pool. So scaling down N→M shrinks quorum to match M — "before this
  change the quorum would have remained at 3" (changelog). Losing more nodes than the new quorum
  tolerates = data loss.
- **Autopilot guards:** the chart sets `autopilot.min_quorum` (from `server.autopilotMinQuorum`) so
  autopilot won't prune servers needed for quorum, and `disable_upgrade_migration: true` (rolling, not
  blue/green) (`server-config-configmap.yaml`@v2.0.2 L70-72).
- **Readiness = leader:** the probe curls `/v1/status/leader` and requires a non-empty leader
  (`failureThreshold: 2`, `periodSeconds: 3` — `server-statefulset.yaml`@v2.0.2 L585-611). No leader →
  all pods NotReady.
- **Storage:** `volumeClaimTemplates` PVC `server.storage: 10Gi`, `storageClass: null` (cluster
  default). PVCs persist across pod restarts; **deleting them = Raft data loss**. 10Gi can fill under
  a large catalog.
- **PDB:** `server.disruptionBudget.enabled: true`, internal `maxUnavailable = 1` — a rollout drops one
  server at a time (safe for **odd** counts).
- **Join:** servers `retry_join` via the headless `-server` service DNS on `serflan.port`.

## Diagnostics

- `kubectl get pods -l component=server` — how many Ready? `kubectl logs <server-0>` → `No cluster
  leader` / raft messages.
- `consul operator raft list-peers` (with a token) — peer set and leader.
- `kubectl get pvc -l component=server` — PVCs present/bound (deleting these is the data-loss path).
- Check `server.replicas` and `server.bootstrapExpect` — a wrong `bootstrap_expect` prevents leader
  election.

## Known Issues

- **Fix (fault tolerance):** run **3 or 5** server replicas (never 1 in prod); keep the PDB enabled and
  set `autopilotMinQuorum` appropriately.
- **Fix (safe scale/rollout):** understand `leave_on_terminate` — do not scale the StatefulSet down
  casually; use `server.updatePartition` to gate rollouts. Recover a lost-quorum cluster like etcd:
  from a snapshot / `consul operator raft` peer recovery.
- **Fix (storage):** size `server.storage` for the catalog; never delete server PVCs unless you intend
  to wipe Consul (then expect ACL re-bootstrap).
- **Cascade awareness:** a quorum loss takes the `-server` Service down → the connect-inject webhook
  can't reach Consul → pod scheduling can stall ([[TROUBLE-CONSUL_CONNECT_INJECT_WEBHOOK]]).

## References

- consul-k8s `server-statefulset.yaml` + `server-config-configmap.yaml` (@v2.0.2), changelog
  (`leave_on_terminate`/quorum, autopilot). etcd analogy [[COMPONENT-ETCD]]; overview
  [[CONCEPT-CONSUL_ON_K8S]]; webhook cascade [[TROUBLE-CONSUL_CONNECT_INJECT_WEBHOOK]].
