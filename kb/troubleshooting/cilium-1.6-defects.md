---
id: TROUBLE-CILIUM_1_6_DEFECTS
type: troubleshooting
title: "cilium 1.6: defects fixed in the 1.6 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.6.0 <1.7.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cilium 1.6 known issues
  - cilium 1.6 fixed in
  - is this cilium bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cilium
sources:
  - type: docs
    path: cilium/cilium release notes for the 1.6 line — bug-fix entries
    url: https://github.com/cilium/cilium/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cilium 1.6: defects fixed in the 1.6 line

## Summary

**23 defects** the project fixed across **3 releases** of the 1.6 line, from 1.6.9 to
1.6.11. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.6.9

- Avoid duplication of generated toCIDRs when using a toServices based CNP (or CCNP) (#11900, @aanm)
- CRD: fix allocation logic of identities with the same set of labels (Backport PR #11411, Upstream PR #11040, @aanm)
- Fix issue where traffic from a pod could be dropped despite allow policy when DNS L7 rules are used (Backport PR #11883, Upstream PR #11764, @joestringer)
- Fix leaking endpoint state metric (Backport PR #11933, Upstream PR #11884, @christarazi)
- Fix possible endpoint restore failure in CRD mode. (Backport PR #11266, Upstream PR #10785, @aanm)
- Fix incorrect name in sysctl_linux_test.go (Backport PR #11266, Upstream PR #10729, @christarazi)
- policy: Fix rule translation test flake (Backport PR #11933, Upstream PR #11913, @joestringer)

### 1.6.10

- endpoint: Fix data races while accessing GetIdentity() (Backport PR #12021, Upstream PR #11941, @tgraf)
- Fix bug where etcd session renew would block indefinitely, causing endpoint provision to fail (Backport PR #12341, Upstream PR #12292, @joestringer)
- Fix bug where identity allocation wouldn't cancel from api timeouts (Backport PR #12352, Upstream PR #12328, @joestringer)
- helm/operator: fix IPv6 liveness probe address for operator (Backport PR #12341, Upstream PR #12223, @Rolinh)
- ipcache: Fix deadlock when ipcache GC results in datapath reload (Backport PR #12021, Upstream PR #11950, @tgraf)
- Istio integration has been updated to release 1.5.1, with backported fix for GKE/COS. (Backport PR #12356, Upstream PR #10730, @jrajahalme)
- Fix flakey assertion on metrics (Backport PR #12021, Upstream PR #11966, @christarazi)
- ginkgo-ext: Fix data-race in Writer (Backport PR #12341, Upstream PR #12025, @gandro)

### 1.6.11

- bpf: Fix monitor aggregation for 'from-network' (Backport PR #12724, Upstream PR #12559, @joestringer)
- Fix manual endpoint regeneration via command line (Backport PR #12713, Upstream PR #12524, @christarazi)
- Fix regression to identity garbage collection due to identity allocation flag in cilium operator (#12496, @brb)
- Fix string slice type CLI arguments (Backport PR #12483, Upstream PR #12457, @JieJhih)
- Fix toGroups CRD to address validation errors (Backport PR #12483, Upstream PR #12440, @lbernail)
- Various etcd bug fixes (#12748, #12753, @tgraf)
- contrib: fix branch check in `start-backport` script (Backport PR #12483, Upstream PR #12361, @Rolinh)
- [v1.6] k8s: Fix CRD schema version to 1.15.1 (#12498, @joestringer)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.6.11**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `cilium/cilium`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/cilium.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
