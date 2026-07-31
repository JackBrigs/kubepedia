---
id: TROUBLE-KUBESPRAY_2_15_DEFECTS
type: troubleshooting
title: "kubespray 2.15: defects fixed in the 2.15 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.15.0 <2.16.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubespray 2.15 known issues
  - kubespray 2.15 fixed in
  - is this kubespray bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubespray
sources:
  - type: docs
    path: kubernetes-sigs/kubespray release notes for the 2.15 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/kubespray/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubespray 2.15: defects fixed in the 2.15 line

## Summary

**8 defects** the project fixed across **2 releases** of the 2.15 line, from 2.15.0 to
2.15.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.15.0

- Small Proxy fixes (add svc,svc.{{ dns_domain }} to no_proxy) (#7102)

### 2.15.1

- Correct Jinja Syntax for etcd-unsupported-arch (#6919)
- Fix ansible calico route reflector tasks in calico role (#7224)
- Fix Restart network doesn't work on Fedora CoreOS (#7271)
- Fix proxy usage when *_PROXY are present in environment (#7309)
- Fix the filename </etc/vault> is Duplicate in the reset role. (#7313)
- Fix recover-control-plane undefined 'proxy_disable_env' variable (#7326)
- Fix: added string to bool conversion for use_localhost_as_kube api load balancer (#7324)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.15.1**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `kubernetes-sigs/kubespray`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/kubespray.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
