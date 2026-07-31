---
id: TROUBLE-KUBE_ROUTER_1_4_DEFECTS
type: troubleshooting
title: "kube-router 1.4: defects fixed in the 1.4 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.4.0 <1.5.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kube-router 1.4 known issues
  - kube-router 1.4 fixed in
  - is this kube-router bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kube-router
sources:
  - type: docs
    path: cloudnativelabs/kube-router release notes for the 1.4 line — bug-fix entries
    url: https://github.com/cloudnativelabs/kube-router/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kube-router 1.4: defects fixed in the 1.4 line

## Summary

**16 defects** the project fixed across **1 releases** of the 1.4 line, from 1.4.0 to
1.4.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.4.0

- Greatly Fixed and Improved Hairpinning: Reduced the number of iptables rules when Hairpinning is enabled by ensuring it is only enabled on local nodes (see: #1208) Fixed an issue where hairpinning rules weren't being updated on service / endpoint updates (see: #1200) Fixed issue where hairpinning rules weren't being regenerated correctly (see: #1200)
- DSR Fixes Fixed an issue where sometimes FWMarks generated for DSR would collide Fixed issue where DSR mangle table definitions were not being cleaned up
- Fixed issue where peer might not be seen correctly as established due to a bad double-negative condition (see: #1184 thanks to @lx1036 )
- 2ca39f14 fix(nsc): properly check hairpinning rule
- 146786ad fix(nsc): sync hairpinning on service modification
- 8f13f069 fix(nsc): don't overwrite err & add comments
- 5101a4fe fix(nsc): remove error for lookupFWMarkByService
- bf325e16 fix(go.mod): update image-spec v1.0.2
- 4c86d3dd fix(go.mod): update containerd to v1.5.8
- b9a9246e fix(lint): don't error on deprecated protobuf funcs
- 9fd17497 fix(go.mod): add google.golang.org/protobuf v1.26.0
- 73b7c22a fix(bgp policy): sort the slice items before deep equal(#1188)
- 8e7d5852 fix(bgp): use PeerState_ESTABLISHED logic like function name(#1184)
- bee2c208 fix bug when adding ip rule for fwmark (#1178)
- 5e1d033a fix(sysctl): revert is fatal check for some conditions
- da5f8e00 fix: address minor PR feedback and misspells


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.4.0**, the newest release recorded here for this line.

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
