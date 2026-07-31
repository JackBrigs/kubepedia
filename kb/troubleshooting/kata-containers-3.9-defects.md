---
id: TROUBLE-KATA_CONTAINERS_3_9_DEFECTS
type: troubleshooting
title: "kata-containers 3.9: defects fixed in the 3.9 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.9.0 <3.10.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kata-containers 3.9 known issues
  - kata-containers 3.9 fixed in
  - is this kata-containers bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kata-containers
sources:
  - type: docs
    path: kata-containers/kata-containers release notes for the 3.9 line — bug-fix entries
    url: https://github.com/kata-containers/kata-containers/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kata-containers 3.9: defects fixed in the 3.9 line

## Summary

**10 defects** the project fixed across **1 releases** of the 3.9 line, from 3.9.0 to
3.9.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.9.0

- tests: Fix k8s test issues on s390x by @BbolroC in https://github.com/kata-containers/kata-containers/pull/10202
- helm: Several fixes, including some reasonable re-work on kata-deploy.sh script by @fidencio in https://github.com/kata-containers/kata-containers/pull/10192
- runtime: fix bad default machine_type for remote hypervisor by @squarti in https://github.com/kata-containers/kata-containers/pull/10250
- runtime: Fix runtime/cdi panic with assignment to entry in nil map by @Apokleos in https://github.com/kata-containers/kata-containers/pull/10276
- genpolicy: fix and re-enable create container UID verification by @danmihai1 in https://github.com/kata-containers/kata-containers/pull/10291
- tests: Fix indentation in the cri containerd tests by @GabyCT in https://github.com/kata-containers/kata-containers/pull/10304
- local-build: Fix unbound variable issue for lib_se.sh by @BbolroC in https://github.com/kata-containers/kata-containers/pull/10321
- ci: Fix indentation of install libseccomp script by @GabyCT in https://github.com/kata-containers/kata-containers/pull/10324
- agent: Fix CPU usage reporting for cgroup v2 in kata-agent by @alexman-stripe in https://github.com/kata-containers/kata-containers/pull/10279
- shim: Fix memory usage reporting for cgroup v2 by @alexman-stripe in https://github.com/kata-containers/kata-containers/pull/10283


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.9.0**, the newest release recorded here for this line.

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
