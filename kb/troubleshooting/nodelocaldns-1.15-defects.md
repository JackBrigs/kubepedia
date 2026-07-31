---
id: TROUBLE-NODELOCALDNS_1_15_DEFECTS
type: troubleshooting
title: "nodelocaldns 1.15: defects fixed in the 1.15 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.15.0 <1.16.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - nodelocaldns 1.15 known issues
  - nodelocaldns 1.15 fixed in
  - is this nodelocaldns bug already fixed
tags:
  - troubleshooting
  - upgrade
  - nodelocaldns
sources:
  - type: docs
    path: kubernetes/dns release notes for the 1.15 line — bug-fix entries
    url: https://github.com/kubernetes/dns/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# nodelocaldns 1.15: defects fixed in the 1.15 line

## Summary

**5 defects** the project fixed across **3 releases** of the 1.15 line, from 1.15.1 to
1.15.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.15.1

- node-cache 1.15.1 fixes a bug found in coreOS setup where the ip address on the nodelocaldns interface would not get assigned correctly. Fixes https://github.com/kubernetes/dns/issues/282
- kube-dns 1.15.1 images now support specifying hostnames in stubDomains. Fixes https://github.com/kubernetes/dns/issues/82

### 1.15.2

- Rebase images to latest debian-base that contains CVE fixes (https://github.com/kubernetes/dns/pull/294, https://github.com/kubernetes/dns/pull/296)
- Fixed some bugs in node-cache with iptables (https://github.com/kubernetes/dns/pull/291)

### 1.15.4

- Change dnsmasq compile-image to debian (fixes #308)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.15.4**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `kubernetes/dns`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/nodelocaldns.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
