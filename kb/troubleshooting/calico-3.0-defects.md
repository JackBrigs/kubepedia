---
id: TROUBLE-CALICO_3_0_DEFECTS
type: troubleshooting
title: "calico 3.0: defects fixed in the 3.0 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.0.0 <3.1.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - calico 3.0 known issues
  - calico 3.0 fixed in
  - is this calico bug already fixed
tags:
  - troubleshooting
  - upgrade
  - calico
sources:
  - type: docs
    path: projectcalico/calico release notes for the 3.0 line — bug-fix entries
    url: https://github.com/projectcalico/calico/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# calico 3.0: defects fixed in the 3.0 line

## Summary

**13 defects** the project fixed across **3 releases** of the 3.0 line, from 3.0.2 to
3.0.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.0.2

- Fixed a bug where Calico would silently lose its connection to etcd and never recover when the etcd server was terminated. [libcalico-go #780](https://github.com/projectcalico/libcalico-go/pull/780) (@caseydavenport)
- Fixed a bug when multiple nodes are restarted simultaneously and swap IP addresses [calico #1681](https://github.com/projectcalico/calico/pull/1681) (@caseydavenport)
- Fixed a route scan issue where upon startup bird did not notice that tunneled routes needed to be updated to be non-tunneled. [calico #1679](https://github.com/projectcalico/calico/pull/1679) (@caseydavenport)
- Enable Kubernetes node references for automatic cleanup of Node resources in etcd. [calico #1678](https://github.com/projectcalico/calico/pull/1678) (@caseydavenport)
- Fixed a panic when BGP is disabled. [calico #1674](https://github.com/projectcalico/calico/pull/1674) (@tmjd)
- Kubernetes self-hosted manifests now enable BGP IP address auto-detection by default. [calico #1588](https://github.com/projectcalico/calico/pull/1588) (@caseydavenport)

### 3.0.3

- Improved error messages when failing to initialize a connection to etcd [libcalico-go #794](https://github.com/projectcalico/libcalico-go/pull/794) (@ozdanborne)
- Ignore hidden files when checking for etcd certificates to copy over when installing CNI. [cni-plugin #473](https://github.com/projectcalico/cni-plugin/pull/473) (@tmjd)

### 3.0.4

- Fixes a bug where the calico/cni container would ignore termination signals. [cni-plugin #487](https://github.com/projectcalico/cni-plugin/pull/487) (@ketkulka)
- Closes a number of race conditions and failure scenarios in IPAM block allocation and releasing. [libcalico-go #819](https://github.com/projectcalico/libcalico-go/pull/819) (@caseydavenport)
- Improves log output around IPAM block allocation and releasing. [libcalico-go #819](https://github.com/projectcalico/libcalico-go/pull/819) (@caseydavenport)
- Fixes a bug where IPs could be assigned from disabled IP pools. [libcalico-go #819](https://github.com/projectcalico/libcalico-go/pull/819) (@ozdanborne)
- Fixes a rare bug where a node could, in some circumstances, advertise /26 blocks that it didn't own [calico #1751](https://github.com/projectcalico/calico/pull/1751) (@caseydavenport)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.0.4**, the newest release recorded here for this line.

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
