---
id: TROUBLE-KUBE_ROUTER_2_2_DEFECTS
type: troubleshooting
title: "kube-router 2.2: defects fixed in the 2.2 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.2.0 <2.3.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kube-router 2.2 known issues
  - kube-router 2.2 fixed in
  - is this kube-router bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kube-router
sources:
  - type: docs
    path: cloudnativelabs/kube-router release notes for the 2.2 line — bug-fix entries
    url: https://github.com/cloudnativelabs/kube-router/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kube-router 2.2: defects fixed in the 2.2 line

## Summary

**10 defects** the project fixed across **3 releases** of the 2.2 line, from 2.2.0 to
2.2.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.2.0

- - fix: allow basic ICMPv6 neighbor discovery `<Aaron U'Ren>`
- - fix(getAllLocalIPs): get IPv6 & IPv4 addresses `<Aaron U'Ren>`
- - fix(NSC): ensure kube-router owns kube-router-svip `<Aaron U'Ren>`
- - fix(linux_networking.go): remove dangling IPv6 routes `<Aaron U'Ren>`
- - fix(feature_request.md): update markdown templating `<Aaron U'Ren>`
- - fix(bug_report.md): update markdown templating `<Aaron U'Ren>`
- - fix(utils.go): static /32 subnet mask reference `<Aaron U'Ren>`
- - fix: ensure that ipv6 is not disabled in kernel `<Natanael Copa>`

### 2.2.1

- fix: select ICMP version for common ICMP rules by @qbnit in https://github.com/cloudnativelabs/kube-router/pull/1713

### 2.2.2

- - fix(dsr): change grpc resolver to passthrough `<Aaron U'Ren>`


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.2.2**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `cloudnativelabs/kube-router`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/kube-router.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
