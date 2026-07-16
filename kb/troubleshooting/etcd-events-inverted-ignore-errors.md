---
id: TROUBLE-ETCD_EVENTS_INVERTED_IGNORE_ERRORS
type: troubleshooting
title: Inverted ignore_errors condition for etcd-events service startup causes false failures
status: active
kubespray_version: ">=v2.29.1 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - etcd-events false failure on scale
tags:
  - etcd
  - scale
  - control-plane
sources:
  - type: github_pr
    url: https://github.com/kubernetes-sigs/kubespray/pull/13343
    note: "PR fixing the inverted ignore_errors condition for etcd-events service startup (merged 2026-07-07, Issue #13342)"
relations: []
---

# Inverted ignore_errors condition for etcd-events service startup causes false failures

## Summary
When `etcd_events_cluster_setup: true`, adding or scaling control-plane nodes can produce false
playbook failures on etcd-events service startup even though the etcd-events cluster is healthy.
The `ignore_errors` condition for the etcd-events service is inverted relative to the parallel
task for the main etcd. The fix is merged only into master after v2.31.0 and is not in any
released tag yet.

## Problem
False failures of the playbook when adding / scaling control-plane nodes with
`etcd_events_cluster_setup: true` enabled. The `etcd-events` service startup task reports an error
even though the etcd-events cluster is healthy.

## Context
- Affected Kubespray versions: v2.29.1, v2.30.0, v2.31.0 (all indexed versions).
- Fixed versions: none released yet. The fix is in master and will land in the next tag after
  v2.31.0.
- Trigger conditions: scaling / adding control-plane nodes with `etcd_events_cluster_setup: true`.

## Diagnostics
- Symptom: the etcd-events service startup task fails during a scale/add-control-plane run while
  the etcd-events cluster is actually healthy.
- Confirm the etcd-events cluster is healthy via `etcdctl endpoint health` against the events
  endpoints; if healthy, the reported startup failure is the false failure described here.
- Inspect `roles/etcd/tasks/configure.yml` line 96 in the tag: the bug is present in all indexed
  versions:
  - `v2.29.1:roles/etcd/tasks/configure.yml:96`
  - `v2.30.0:roles/etcd/tasks/configure.yml:96`
  - `v2.31.0:roles/etcd/tasks/configure.yml` (line 96 in the tag working tree)
  - All show `ignore_errors: "{{ etcd_events_cluster_is_healthy.rc != 0 }}"` (nearby line 85 for
    the main etcd uses the correct `== 0`).

## Known Issues
- Root cause: in `roles/etcd/tasks/configure.yml`, the `ignore_errors` condition for the
  etcd-events service is inverted relative to the parallel main-etcd task:
  - main etcd (correct): `ignore_errors: "{{ etcd_cluster_is_healthy.rc == 0 }}"` — errors are
    ignored when the cluster is already healthy (rc == 0);
  - etcd-events (bug): `ignore_errors: "{{ etcd_events_cluster_is_healthy.rc != 0 }}"` — uses
    `!= 0`, so on a healthy cluster (rc == 0) errors are NOT ignored and a harmless startup
    failure surfaces as a real error.
- Fix: PR [#13343](https://github.com/kubernetes-sigs/kubespray/pull/13343) "Fix inverted
  ignore_errors condition for etcd-events service startup" (commit `63bdde2ad`, merged
  2026-07-07, Issue #13342) changes the condition to `== 0`. The defect was introduced long ago
  (commit `7516fe1`, 2021) and is present in all indexed versions. The fix is merged into master
  **after** the v2.31.0 tag and is not part of any released tag yet (verified: commit `63bdde2ad`
  is not an ancestor of v2.31.0).
- Workaround: when scaling control-plane with `etcd_events_cluster_setup: true`, ignore this
  single etcd-events startup failure if the etcd-events cluster is actually healthy (check
  `etcdctl endpoint health` for the events endpoints); or locally patch line 96 to use `== 0`.

## References
- https://github.com/kubernetes-sigs/kubespray/pull/13343
- Migrated from Kubepedia 0.1.0 cache: etcd-events-inverted-ignore-errors-v2.31.0.md
