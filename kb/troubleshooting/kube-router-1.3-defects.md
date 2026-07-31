---
id: TROUBLE-KUBE_ROUTER_1_3_DEFECTS
type: troubleshooting
title: "kube-router 1.3: defects fixed in the 1.3 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.3.0 <1.4.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kube-router 1.3 known issues
  - kube-router 1.3 fixed in
  - is this kube-router bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kube-router
sources:
  - type: docs
    path: cloudnativelabs/kube-router release notes for the 1.3 line — bug-fix entries
    url: https://github.com/cloudnativelabs/kube-router/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kube-router 1.3: defects fixed in the 1.3 line

## Summary

**22 defects** the project fixed across **2 releases** of the 1.3 line, from 1.3.1 to
1.3.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.3.1

- `--cleanup-config` flag should now be more comprehensive. There were a couple of bugs introduced in the 1.3 release that caused this flag to not function at all. These have been fixed. Additionally, it now cleans up most, if not all kube-router artifacts, where before it would leave some lingering parts of the Network Policy Controller
- Additional ipset locking was missing causing some errors around multiple invocations. This has been fixed
- - fix(npc): ordering of firewall / service rules (#1144) (4 days ago) <Aaron U'Ren>
- - fix: add sleeps between iptables and ipset cleanup (8 days ago) <Aaron U'Ren>
- - fix(NRC): reduce logging for egress cleanup errors (8 days ago) <Aaron U'Ren>
- - fix(NSC): actually remove IPVS definitions (8 days ago) <Aaron U'Ren>
- - fix(NSC): add exists checking to Cleanup() (8 days ago) <Aaron U'Ren>
- - fix(NPC): Cleanup() function overhaul (8 days ago) <Aaron U'Ren>
- - fix(NPC): missed ipset locking (8 days ago) <Aaron U'Ren>
- - fix(NRC): PR feedback fixes (2 weeks ago) <Aaron U'Ren>
- - fix(injectRoute): process withdrawls first (2 weeks ago) <Aaron U'Ren>
- - fix(NRC): consolidate route delete logic (2 weeks ago) <Aaron U'Ren>
- - fix(injectRoute): cleanup tunnels & routes when peer drops (2 weeks ago) <Aaron U'Ren>
- - fix: add nil checking to ipsetMutex cleanup actions (#1129) (4 weeks ago) <Aaron U'Ren>
- - fix(ci): only run build actions on non-forks (6 weeks ago) <Aaron U'Ren>
- - fix(README.md): update badge link to GitHub Actions (6 weeks ago) <Aaron U'Ren>
- - .github/workflows: Fix yaml error (6 weeks ago) <Manuel Rüger>
- - .github: Fix tag workflow (6 weeks ago) <Manuel Rüger>
- - .github: Fix Tag/Push workflow (6 weeks ago) <Manuel Rüger>

### 1.3.2

- - fix(NPC): don't rely on exit code for chain check (#1157) `<Aaron U'Ren>`
- - fix(bgp_policies_test.go): Add missing import statement to all test cases `<Lucas Mundim>`
- - fix(bgp_policies_test.go): fails if there are any unexpected statement `<Lucas Mundim>`


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.3.2**, the newest release recorded here for this line.

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
