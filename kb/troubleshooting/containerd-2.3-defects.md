---
id: TROUBLE-CONTAINERD_2_3_DEFECTS
type: troubleshooting
title: "containerd 2.3: defects fixed in the 2.3 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.3.0 <2.4.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - containerd 2.3 known issues
  - containerd 2.3 fixed in
  - is this containerd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - containerd
sources:
  - type: docs
    path: containerd/containerd release notes for the 2.3 line — bug-fix entries
    url: https://github.com/containerd/containerd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# containerd 2.3: defects fixed in the 2.3 line

## Summary

**14 defects** the project fixed across **4 releases** of the 2.3 line, from 2.3.0 to
2.3.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.3.0

- Fix binary logging driver not blocking container start on failure

### 2.3.1

- Fix bug where failed gRPC plugins were not tolerated when starting listeners
- Fix handling of out-of-range USER values in OCI spec to avoid unexpected username/group lookups
- Fix sandbox task API endpoints for non-runc runtimes and deprecate task fields in Runc options
- Fix transfer plugin error when EROFS differ is configured but mkfs.erofs is unavailable
- Fix sandbox task API endpoints for non-runc runtimes ([#13422](https://github.com/containerd/containerd/pull/13422)) [`5282d4e09`](https://github.com/containerd/containerd/commit/5282d4e09d3bc8b0957780caa7a4644fac7c86a7) Wire task address and version fields [`e44f5f9ec`](https://github.com/containerd/containerd/commit/e44f5f9ec610d95a712d230e8a19ae516e0a26ac) protos: include task API address to CreateTaskRequest
- fix: close boltdb on metadata and mount plugin close ([#13379](https://github.com/containerd/containerd/pull/13379)) [`1d601271a`](https://github.com/containerd/containerd/commit/1d601271a73a649de465ed94fa973564211b7f46) fix: close boltdb on metadata and mount plugin close
- Fix optional EROFS differ setup in transfer plugin ([#13364](https://github.com/containerd/containerd/pull/13364)) [`d666d2e42`](https://github.com/containerd/containerd/commit/d666d2e4261da664a50c7b1663461747ba8ebb2e) Refactor transfer unpack configuration setup [`ccc3bd7b9`](https://github.com/containerd/containerd/commit/ccc3bd7b90be7afce7a903391d2a34b83424c5e0) Fix optional transfer differ setup

### 2.3.2

- Fix a data race when reading shim logs on Windows
- Fix container startup failures caused by concurrent task RPC timeouts during slow container creation
- core/runtime/v2: fix race on Windows deferredPipeConnection.c in Read ([#13522](https://github.com/containerd/containerd/pull/13522)) [`62ceafff0`](https://github.com/containerd/containerd/commit/62ceafff0a9b37ab01f73d4d5acd2ff105ef4023) core/runtime/v2: fix race on Windows deferredPipeConnection.c in Read

### 2.3.3

- Fix nil pointer dereference in NRI GetIPs during pod sandbox teardown or container exit
- Fix nil pointer dereference in NRI GetIPs ([#13697](https://github.com/containerd/containerd/pull/13697)) [`36c713971`](https://github.com/containerd/containerd/commit/36c7139715fee7ff2f87f78a8b3d6fea4e2e7b35) Fix nil pointer dereference in NRI GetIPs
- test: fix flaky image timestamp check on coarse clocks ([#13643](https://github.com/containerd/containerd/pull/13643)) [`168d56783`](https://github.com/containerd/containerd/commit/168d56783608354301e6f6dfb3ceb9af342c7dde) test: fix flaky image timestamp check on coarse clocks


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.3.3**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `containerd/containerd`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/containerd.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
