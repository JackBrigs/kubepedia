---
id: TROUBLE-CONSUL_K8S_0_7_DEFECTS
type: troubleshooting
title: "consul-k8s 0.7: defects fixed in the 0.7 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.7.0 <0.8.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - consul-k8s 0.7 known issues
  - consul-k8s 0.7 fixed in
  - is this consul-k8s bug already fixed
tags:
  - troubleshooting
  - upgrade
  - consul-k8s
sources:
  - type: docs
    path: hashicorp/consul-k8s release notes for the 0.7 line — bug-fix entries
    url: https://github.com/hashicorp/consul-k8s/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# consul-k8s 0.7: defects fixed in the 0.7 line

## Summary

**9 defects** the project fixed across **2 releases** of the 0.7 line, from 0.7.0 to
0.7.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.7.0

- Removes GRPCRoute method match defaulting to allow for matching all requests, or matching only by header. (#1753, @skriss)
- Update route validation to comply with RFC-3986 "p-char" characters. (#1644, @jackstine)
- Illegal names like " " will be not allowed for query param name in HTTPQueryParamMatch. (#1796, @gyohuangxin)
- Webhook: Port is now considered when validating that ParentRefs are unique (#1995, @howardjohn)
- Fixes for mesh conformance tests (#2017, @keithmattix)
- Fix description of ReferenceGrant example in documentation by making it use the correct resources. (#1864, @matteoolivi)
- Fix grammar mistake in ReferenceGrant implementation guidelines. (#1865, @matteoolivi)

### 0.7.1

- Fixed an issues causing conformance tests to fail when using IPv6 addresses. (#2024, @howardjohn)
- Fixes to port and scheme redirect tests: Tests now send HTTPS requests with consistent SNI and Host, Gateway now has the correct SANs. (#2039, @sunjaybhatia)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.7.1**, the newest release recorded here for this line.

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
