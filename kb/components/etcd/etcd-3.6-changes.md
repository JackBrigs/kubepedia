---
id: CONCEPT-ETCD_3_6_CHANGES
type: concept
title: "etcd 3.6 operational changes (new in Kubespray v2.31.0 for K8s 1.35)"
status: active
kubespray_version: ">=v2.31.0 <=v2.31.0"
kubernetes_version: "1.35"
component_version: "3.6.10"
verified_at: "2026-07-16"
confidence: verified
aliases:
  - etcd 3.6
  - etcd 3.5 to 3.6
  - etcd downgrade
  - etcdutl migrate
  - etcd v2 store removed
tags:
  - etcd
  - upgrade
  - control-plane
sources:
  - type: docs
    path: CHANGELOG/CHANGELOG-3.6.md
    url: https://raw.githubusercontent.com/etcd-io/etcd/main/CHANGELOG/CHANGELOG-3.6.md
    note: "etcd 3.6 changelog: downgrade support, v2 deprecation, flag graduation, feature gates"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "etcd_supported_versions: 1.35 -> 3.6.10 (tag v2.31.0)"
relations:
  - type: see_also
    target: COMPONENT-ETCD
  - type: see_also
    target: UPGRADE-V2_30_0__V2_31_0
  - type: see_also
    target: PRACTICE-ETCD_BACKUP_RESTORE
---

# etcd 3.6 operational changes (new in Kubespray v2.31.0 for K8s 1.35)

## Summary

Kubespray `v2.31.0` introduces **etcd 3.6** (`3.6.10`), but **only for Kubernetes 1.35**
— the `etcd_supported_versions` map keeps `1.33`/`1.34` on `3.5.29` and gives `1.35`
`3.6.10`. etcd 3.6 is the first minor after a long 3.5 line and brings real operational
changes: first-class **downgrade** support, removal/retirement of the legacy **v2
store**, and graduation of many `--experimental-*` flags. Treat the 3.5→3.6 move as a
genuine minor upgrade, not a patch.

## Context

- Applies to Kubespray `v2.31.0` running Kubernetes `1.35` (where etcd `3.6.10` is
  selected). Clusters on `1.33`/`1.34` stay on etcd `3.5.29`.
- etcd is managed by the `etcd` role (or kubeadm for `etcd_deployment_type: kubeadm`);
  see [[COMPONENT-ETCD]]. This note is about **3.6's own** behaviour, not Kubespray wiring.

## Implementation

**Operationally relevant 3.6 changes (from the etcd changelog):**

- **Downgrade support.** 3.6 adds proper downgrade tooling: endpoint status now reports
  `DowngradeInfo`, and `etcdutl migrate` downgrades/upgrades the **data-dir** format.
  Downgrading to 3.5 is now a supported path (previously effectively one-way).
- **Data-dir version guard (breaking).** etcd refuses to start on a data dir created by a
  **newer** version (e.g. 3.6 won't run on a 3.7+ data dir); use `etcdutl migrate` to move
  a data dir down a version.
- **v2 store / v2 discovery retired.** The legacy v2 store and v2 discovery are
  deprecated/removed; `--v2-deprecation` governs the transition. Kubernetes uses only the
  v3 API, so kubeadm/Kubespray clusters aren't affected — but don't rely on any v2 data.
- **Experimental flags graduated.** Many `--experimental-*` flags dropped the prefix
  (e.g. `--experimental-warning-unary-request-duration` →
  `--warning-unary-request-duration`); some were removed. If you pass etcd experimental
  flags through Kubespray, review them against 3.6.
- **Feature gates + metrics.** 3.6 introduces etcd **feature gates** (e.g.
  `MaxLearners` replaces the experimental flag) and a Prometheus metric to query them.

## Compatibility

- **Upgrade discipline:** snapshot etcd before upgrading to `1.35`/etcd 3.6
  ([[PRACTICE-ETCD_BACKUP_RESTORE]]); the 3.5→3.6 step is a minor version change.
  Reaching etcd 3.6 happens as part of the `v2.30.0 → v2.31.0` Kubespray upgrade **when
  the cluster is on Kubernetes 1.35** ([[UPGRADE-V2_30_0__V2_31_0]]).
- Mixed 3.5/3.6 members during a rolling upgrade should be transient — don't run a split
  cluster longer than needed.
- Downgrade is supported but still involves a data-dir migration (`etcdutl migrate`) and a
  snapshot; rehearse before doing it on production.

## References

- etcd `CHANGELOG-3.6.md` (downgrade, v2 deprecation, flag graduation, feature gates);
  `etcd_supported_versions` (`1.35 → 3.6.10`) at tag `v2.31.0`. Component:
  [[COMPONENT-ETCD]]; backup: [[PRACTICE-ETCD_BACKUP_RESTORE]].
