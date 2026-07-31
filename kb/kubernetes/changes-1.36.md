---
id: CONCEPT-K8S_1_36_CHANGES
type: concept
title: Kubernetes 1.36 — operator-relevant changes
status: active
kubespray_version: null
kubernetes_version: "1.36"
component_version: null
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubernetes 1.36 changes
  - what changed in 1.36
  - 1.36 upgrade notes
  - flex volumes removed kubeadm
  - dra granular rbac resourceclaims
tags:
  - kubernetes
  - upgrade
  - release-notes
sources:
  - type: docs
    path: CHANGELOG/CHANGELOG-1.36.md
    url: https://raw.githubusercontent.com/kubernetes/kubernetes/master/CHANGELOG/CHANGELOG-1.36.md
    note: "v1.36 Urgent Upgrade Notes (ACTION REQUIRED entries) + Changes by Kind; 105 bug fixes recorded on the line"
relations:
  - type: see_also
    target: CONCEPT-K8S_1_35_CHANGES
  - type: see_also
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# Kubernetes 1.36 — operator-relevant changes

## Summary

Kubernetes `1.36` sits **above the Kubespray envelope**: no released tag ships it, and it enters the
picture only because checksums for 1.36.2/1.36.3 already exist on Kubespray `master`
([[CONCEPT-UPGRADE_HORIZON]]). Compared with the cgroup-v1 cliff of 1.35, this release is
undramatic for the node — its four action-required items are about **monitoring, RBAC and a removed
kubeadm feature**, not about whether the kubelet starts.

The one that bites silently is the pair of renamed metrics: nothing fails, dashboards simply go
blank and alerts stop firing.

## Context

- Kubernetes `1.36`; Kubespray mapping: **not shipped by any release** as of 2026-07-31, present
  only as checksums on `master`.
- Items below are the `v1.36` "ACTION REQUIRED" entries from the official changelog.

## Implementation

**Breaking / action required**

- **Metric renamed: `volume_operation_total_errors` → `volume_operation_errors_total`**
  (kube-controller-manager). Dashboards and alerting rules built on the old name silently stop
  producing data.
- **Metric renamed: `etcd_bookmark_counts` → `etcd_bookmark_total`** (API machinery). Same class of
  failure, same silence.
- **DRA now requires granular RBAC to update ResourceClaim statuses**, with the
  `DRAResourceClaimGranularStatusAuthorization` feature gate at beta in 1.36. Schedulers and
  controllers need `update`/`patch` on `resourceclaims/binding`; DRA drivers need
  `associated-node:update` or the arbitrary-node equivalent. Clusters not using DRA are unaffected;
  clusters using it lose claim updates until the roles are widened.
- **flex-volume support removed from kubeadm.** Migration away has been the recommendation since
  1.22. Continuing to use it now requires a custom KCM image that is not distroless, the
  `--flex-volume-plugin-dir` flag and the corresponding host directory mounted in — in practice this
  is a "migrate to CSI" item, not a configuration item.

**Scale of the release:** 105 bug fixes are recorded on the 1.36 line so far; the per-release index
is in `kubernetes 1.36: defects fixed in the 1.36 line`.

## Known Issues

**Renamed metrics are the failure mode of this release.** They break observability, not the cluster,
which means the damage is discovered when something else goes wrong and the dashboard that should
have shown it is empty. Grep dashboards and alert rules for both old names before upgrading.

**Nothing here is a reason to move.** With 1.36 outside every Kubespray release, adopting it means
leaving the supported envelope; the practical use of this document is to know what is waiting, and
to fix the metric names in monitoring ahead of time — that change is safe to make early, since both
names can be handled side by side.

## References

- `CHANGELOG-1.36.md`, ACTION REQUIRED entries, read 2026-07-31.
- Previous version: [[CONCEPT-K8S_1_35_CHANGES]]; envelope: [[CONCEPT-KUBERNETES_VERSION_SUPPORT]];
  what is already on `master`: [[CONCEPT-UPGRADE_HORIZON]].
