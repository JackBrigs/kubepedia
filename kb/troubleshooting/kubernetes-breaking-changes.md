---
id: TROUBLE-KUBERNETES_BREAKING_CHANGES
type: troubleshooting
title: "kubernetes: declared breaking changes by release"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.28.0 <=1.36.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubernetes breaking changes
  - kubernetes upgrade broke
  - kubernetes action required upgrade
  - what breaks upgrading kubernetes
tags:
  - upgrade
  - breaking-change
  - kubernetes
sources:
  - type: docs
    path: kubernetes/kubernetes release notes — entries marked breaking / action required
    url: https://github.com/kubernetes/kubernetes/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubernetes: declared breaking changes by release

## Summary

**9 behaviour changes** the project itself marked as breaking or action-required, across
5 releases from 1.28.0 to 1.36.0. These are not defects: they work as designed and still break
a configuration that worked yesterday. An upgrade crossing any of them needs a decision, not just a
rollout.

## Problem

The upgrade itself usually succeeds. The damage shows up afterwards — a setting silently ignored, a
default flipped, an API version withdrawn, a variable that must now be set explicitly.

## Context

### 1.28.0

- for the custom scheduler plugin developers. Here's the breaking change in `EnqueueExtension` in the scheduling framework. The `EventsToRegister` in `EnqueueExtension` changed the return value from `ClusterEvent` to `ClusterEventWithHint`. `ClusterEventWithHint` allows each plugin to filter out more useless events via the callback function named `QueueingHintFn`. When the scheduling queue receives a cluster event, before moving each Pod from unschedulable pod pool to activeQ/backoffQ, it will call QueueingHintFn of plugins that rejected each Pod in the previous scheduling cycle. Depending on the value returned from QueueingHintFn, the scheduling queue changes how it queues each Pod: if more than one QueueingHintFn returns QueueImmediately, it queues Pod to activeQ. If no QueueingHintFn returns QueueImmediately and more than one plugin returns QueueAfterBackoff, it queues Pod to backoffQ if Pod is backing off, or to activeQ if Pod's backoff has already finished. If all QueueingHintFn return QueueSkip, it puts this pod back to the unschedulable pod pool

### 1.31.0

- The Dynamic Resource Allocation (DRA) driver's DaemonSet must be deployed with a service account that enables writing ResourceSlice and reading ResourceClaim objects.' ([#125163](https://github.com/kubernetes/kubernetes/pull/125163), [@pohly](https://github.com/pohly)) [SIG Auth, Node and Testing]
- for custom scheduler plugin developers: `EventsToRegister` in the `EnqueueExtensions` interface gets `ctx` in the parameters and `error` in the return values. Please change your plugins' implementation accordingly. ([#126113](https://github.com/kubernetes/kubernetes/pull/126113), [@googs1025](https://github.com/googs1025)) [SIG Node, Scheduling, Storage and Testing]

### 1.32.0

- ** for custom scheduler plugin developers: `PodEligibleToPreemptOthers` in the `preemption` interface now includes `ctx` in the parameters. Please update your plugins' implementation accordingly. ([#126465](https://github.com/kubernetes/kubernetes/pull/126465), [@googs1025](https://github.com/googs1025)) [SIG Scheduling]

### 1.35.0

- `failCgroupV1` will be set to true from 1.35. This means that nodes will not start on a cgroup v1 by default. This puts cgroup v1 into a deprecated state. ([#134298](https://github.com/kubernetes/kubernetes/pull/134298), [@kannon92](https://github.com/kannon92))

### 1.36.0

- kube-controller-manager: Renamed metric `volume_operation_total_errors` to `volume_operation_errors_total`. If you are using custom monitoring dashboards or alerting rules based on the `volume_operation_total_errors` metric, update them to use the new `volume_operation_errors_total` metric. ([#136399](https://github.com/kubernetes/kubernetes/pull/136399), [@tico88612](https://github.com/tico88612)) [SIG Apps, Instrumentation, Storage and Testing]
- DRA (Dynamic Resource Allocation) drivers and controllers now require granular RBAC permissions to update ResourceClaim statuses when the `DRAResourceClaimGranularStatusAuthorization` feature gate is enabled (beta in `v1.36`). Schedulers and controllers must be granted `update`/`patch` on `resourceclaims/binding`. DRA drivers must be granted `associated-node:update` or `arbitrary-node:update` (or patch equivalents) on `resourceclaims/driver`, restricted by their specific `resourceNames`. ([#134947](https://github.com/kubernetes/kubernetes/pull/134947), [@aojea](https://github.com/aojea)) [SIG API Machinery, Apps, Auth, Instrumentation, Node, Scheduling and Testing]
- Removed the integrated support for flex-volumes in kubeadm. Users were advised to migrate away from flex-volumes as recommended by SIG Storage since `v1.22`. If `kubeadm` users wish to continue using the feature, they need a custom image for the KCM that is not based on distroless, pass the KCM flag `--flex-volume-plugin-dir`, and mount the directory `/usr/libexec/kubernetes/kubelet-plugins/volume/exec` in the KCM static pod using `kubeadm`'s `extraVolumes` mechanism before upgrading to `v1.36`. Previously, `kubeadm` automatically did the mounting if the user passed the flag. ([#136423](https://github.com/kubernetes/kubernetes/pull/136423), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]
- Renamed metric `etcd_bookmark_counts` to `etcd_bookmark_total`. If you are using custom monitoring dashboards or alerting rules based on the `etcd_bookmark_counts` metric, update them to use the new `etcd_bookmark_total` metric. ([#136483](https://github.com/kubernetes/kubernetes/pull/136483), [@petern48](https://github.com/petern48)) [SIG API Machinery, Etcd, Instrumentation and Testing]


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

- Upstream releases of `kubernetes/kubernetes`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/kubernetes.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
