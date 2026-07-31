---
id: TROUBLE-CONSUL_K8S_0_6_DEFECTS
type: troubleshooting
title: "consul-k8s 0.6: defects fixed in the 0.6 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.6.0 <0.7.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - consul-k8s 0.6 known issues
  - consul-k8s 0.6 fixed in
  - is this consul-k8s bug already fixed
tags:
  - troubleshooting
  - upgrade
  - consul-k8s
sources:
  - type: docs
    path: hashicorp/consul-k8s release notes for the 0.6 line — bug-fix entries
    url: https://github.com/hashicorp/consul-k8s/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# consul-k8s 0.6: defects fixed in the 0.6 line

## Summary

**8 defects** the project fixed across **3 releases** of the 0.6 line, from 0.6.0 to
0.6.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.6.0

- Fix Gateway reference in HTTPRouteInvalidParentRefNotMatchingListenerPort (#1591, @sayboras)

### 0.6.1

- Our regex for validating path characters was updated to accurately identify "p-chars" as per RFC-3986. (#1644, @jackstine)
- An erroneous "namespace" field was present in our webhook ClusterRoleBindings and has been removed. (#1684, @tao12345666333)
- Fixed a broken test for GRPCRoute that caused an erronous failure. (#1692, @arkodg)
- Fixed usage of `net/http` default client in conformance test suite (#1617, @howardjohn)
- Fixed missing reference to NoMatchingParent in godoc (#1671, @mlavacca)

### 0.6.2

- Fix invalid HTTP redirect/rewrite examples. (#1787, @Xunzhuo)
- Fixed an issue where tests may fail erroneously on the removal of resources that are already removed. (#1745, @mlavacca)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.6.2**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `hashicorp/consul-k8s`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/consul-k8s.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
