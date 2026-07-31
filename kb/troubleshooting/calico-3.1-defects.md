---
id: TROUBLE-CALICO_3_1_DEFECTS
type: troubleshooting
title: "calico 3.1: defects fixed in the 3.1 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.1.0 <3.2.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - calico 3.1 known issues
  - calico 3.1 fixed in
  - is this calico bug already fixed
tags:
  - troubleshooting
  - upgrade
  - calico
sources:
  - type: docs
    path: projectcalico/calico release notes for the 3.1 line — bug-fix entries
    url: https://github.com/projectcalico/calico/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# calico 3.1: defects fixed in the 3.1 line

## Summary

**6 defects** the project fixed across **1 releases** of the 3.1 line, from 3.1.0 to
3.1.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.1.0

- Fix a bug where IPs could be assigned from disabled IP pools. [libcalico-go #806](https://github.com/projectcalico/libcalico-go/pull/806) (@ozdanborne)
- Fix a bug where profiles were periodically and unnecessarily reprogrammed by kube-controllers. [libcalico-go #805](https://github.com/projectcalico/libcalico-go/pull/805) (@caseydavenport)
- Fix a bug where nodes were periodically and unnecessarily processed by kube-controllers. [kube-controllers #216](https://github.com/projectcalico/kube-controllers/pull/216) (@caseydavenport)
- Fix a rare bug where a node could in some circumstances advertise /26 blocks that it didn't own [calico #1712](https://github.com/projectcalico/calico/pull/1712) (@caseydavenport)
- Fix an interaction between failsafe inbound/outbound ports and do-not-track policy that resulted in failsafe ports being blocked if do-not-track policy was added. [felix #1718](https://github.com/projectcalico/felix/pull/1718) (@fasaxc)
- Fix bug in icmp validation where ipVersion was required for all icmp rules. [calicoctl #1814](https://github.com/projectcalico/calicoctl/pull/1814) (@ozdanborne)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.1.0**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `projectcalico/calico`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/calico.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
