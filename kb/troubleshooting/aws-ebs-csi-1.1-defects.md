---
id: TROUBLE-AWS_EBS_CSI_1_1_DEFECTS
type: troubleshooting
title: "aws-ebs-csi 1.1: defects fixed in the 1.1 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.1.0 <1.2.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - aws-ebs-csi 1.1 known issues
  - aws-ebs-csi 1.1 fixed in
  - is this aws-ebs-csi bug already fixed
tags:
  - troubleshooting
  - upgrade
  - aws-ebs-csi
sources:
  - type: docs
    path: kubernetes-sigs/aws-ebs-csi-driver release notes for the 1.1 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/aws-ebs-csi-driver/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# aws-ebs-csi 1.1: defects fixed in the 1.1 line

## Summary

**10 defects** the project fixed across **2 releases** of the 1.1 line, from 1.1.0 to
1.1.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.1.0

- fix naming mistake in clusterrolebinding, expose env var to controller via downward api ([#874](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/874), [@vdhanan](https://github.com/vdhanan))
- Fix kustomize RBAC bindings to have namespace kube-system ([#878](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/878), [@wongma7](https://github.com/wongma7))
- rename node clusterrolebinding to make auto upgrade work ([#894](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/894), [@vdhanan](https://github.com/vdhanan))
- remove hardcoded namespace for pod disruption budget ([#895](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/895), [@vdhanan](https://github.com/vdhanan))
- Only initialize the in-cluster kube client when metadata service is actually unavailable ([#897](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/897), [@chrisayoub](https://github.com/chrisayoub))
- Reduce default log level to 2 ([#903](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/903), [@wongma7](https://github.com/wongma7))
- Add pod disruption budgets that got missed in a rebase ([#906](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/906), [@krmichel](https://github.com/krmichel))
- remove WellKnownTopologyKey from PV Topology ([#912](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/912), [@Elbehery](https://github.com/Elbehery))
- Skip volume expansion if block node ([#916](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/916), [@gnufied](https://github.com/gnufied))

### 1.1.4

- Fix mount idempotency ([#1019](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/pull/1019), [@nirmalaagash](https://github.com/nirmalaagash))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.1.4**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `kubernetes-sigs/aws-ebs-csi-driver`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/aws-ebs-csi.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
