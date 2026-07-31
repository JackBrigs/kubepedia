---
id: TROUBLE-COREDNS_1_9_DEFECTS
type: troubleshooting
title: "coredns 1.9: defects fixed in the 1.9 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.9.0 <1.10.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - coredns 1.9 known issues
  - coredns 1.9 fixed in
  - is this coredns bug already fixed
tags:
  - troubleshooting
  - upgrade
  - coredns
sources:
  - type: docs
    path: coredns/coredns release notes for the 1.9 line — bug-fix entries
    url: https://github.com/coredns/coredns/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# coredns 1.9: defects fixed in the 1.9 line

## Summary

**9 defects** the project fixed across **3 releases** of the 1.9 line, from 1.9.1 to
1.9.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.9.1

- plugin/grpc: Fix healthy proxy error case (https://github.com/coredns/coredns/pull/5168)
- plugin/k8s_external: Fix external nsAddrs when CoreDNS Service has no External IPs (https://github.com/coredns/coredns/pull/4891)
- plugin/secondary: Fix startup transfer failure wrong zone logged (https://github.com/coredns/coredns/pull/5085)

### 1.9.2

- plugin/cache: fix cache poisoning exploit (https://github.com/coredns/coredns/pull/5174)
- plugin/etcd: fix multi record TXT lookups (https://github.com/coredns/coredns/pull/5293)
- plugin/kubernetes: fix k8s start up timeout ticker (https://github.com/coredns/coredns/pull/5361)
- plugin/template: fix rcode option documentation (https://github.com/coredns/coredns/pull/5328)

### 1.9.4

- plugin/rewrite: fix a crash in rewrite plugin when rule type is missing (https://github.com/coredns/coredns/pull/5459)
- plugin/rewrite: fix out-of-index issue in rewrite plugin (https://github.com/coredns/coredns/pull/5462)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.9.4**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `coredns/coredns`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/coredns.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
