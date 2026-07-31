---
id: TROUBLE-KATA_CONTAINERS_3_5_DEFECTS
type: troubleshooting
title: "kata-containers 3.5: defects fixed in the 3.5 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.5.0 <3.6.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kata-containers 3.5 known issues
  - kata-containers 3.5 fixed in
  - is this kata-containers bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kata-containers
sources:
  - type: docs
    path: kata-containers/kata-containers release notes for the 3.5 line — bug-fix entries
    url: https://github.com/kata-containers/kata-containers/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kata-containers 3.5: defects fixed in the 3.5 line

## Summary

**10 defects** the project fixed across **1 releases** of the 3.5 line, from 3.5.0 to
3.5.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.5.0

- passfd-io: fix FIFO opening and vsock handling by @Tim-Zhang in https://github.com/kata-containers/kata-containers/pull/9335
- build: Fix tarball not building correctly in docker by @JakubLedworowski in https://github.com/kata-containers/kata-containers/pull/9549
- doc: fix missing document link by @cncal in https://github.com/kata-containers/kata-containers/pull/9528
- build: fix the confusing build message if yq doesn't exist in GOPATH/bin by @cncal in https://github.com/kata-containers/kata-containers/pull/9582
- runtime-rs: fix the issue of the leak of dead shim by @lifupan in https://github.com/kata-containers/kata-containers/pull/9598
- db: fix the issue of failed to init pci root bus by @lifupan in https://github.com/kata-containers/kata-containers/pull/9596
- deploy: Fix wrong pushing of artifacts by @zvonkok in https://github.com/kata-containers/kata-containers/pull/9616
- build: nvidia-gpu: Fix cache usage of the headers tarball by @fidencio in https://github.com/kata-containers/kata-containers/pull/9622
- runtime-rs: Fix constructing the RTC struct by @emanuellima1 in https://github.com/kata-containers/kata-containers/pull/9571
- kata-deploy: Fix tdx_not_supported call by @ldoktor in https://github.com/kata-containers/kata-containers/pull/9629


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.5.0**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `kata-containers/kata-containers`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/kata-containers.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
