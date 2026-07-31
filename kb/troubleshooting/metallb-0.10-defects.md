---
id: TROUBLE-METALLB_0_10_DEFECTS
type: troubleshooting
title: "metallb 0.10: defects fixed in the 0.10 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.10.0 <0.11.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - metallb 0.10 known issues
  - metallb 0.10 fixed in
  - is this metallb bug already fixed
tags:
  - troubleshooting
  - upgrade
  - metallb
sources:
  - type: docs
    path: metallb/metallb release notes for the 0.10 line — bug-fix entries
    url: https://github.com/metallb/metallb/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# metallb 0.10: defects fixed in the 0.10 line

## Summary

**5 defects** the project fixed across **3 releases** of the 0.10 line, from 0.10.1 to
0.10.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.10.1

- Fix the images in `manifests/metallb.yaml` to refer to the images for the release tag instead of the `main` branch. ([Issue #874](https://github.com/metallb/metallb/issues/874))

### 0.10.2

- Fix a missing RBAC update in the manifests used by the helm chart. ([Issue #878](https://github.com/metallb/metallb/issues/878))

### 0.10.3

- helm: fix validation of imagePullSecrets ([Issue #897](https://github.com/metallb/metallb/issues/897))
- Resolve issue in EndpointSlice support that caused excessive log spam. ([Issue #899](https://github.com/metallb/metallb/issues/899)) ([Issue #901](https://github.com/metallb/metallb/issues/901)) ([Issue #978](https://github.com/metallb/metallb/issues/978))
- layer2: Fix a race condition when sending gratuitous ARP or NDP messages where an error on a removed interface would cause MetalLB to skip sending the same message out on the rest of the list of interfaces. ([Issue #681](https://github.com/metallb/metallb/issues/681))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.10.3**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `metallb/metallb`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/metallb.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
