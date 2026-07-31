---
id: TROUBLE-KUBESPRAY_2_17_DEFECTS
type: troubleshooting
title: "kubespray 2.17: defects fixed in the 2.17 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.17.0 <2.18.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubespray 2.17 known issues
  - kubespray 2.17 fixed in
  - is this kubespray bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubespray
sources:
  - type: docs
    path: kubernetes-sigs/kubespray release notes for the 2.17 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/kubespray/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubespray 2.17: defects fixed in the 2.17 line

## Summary

**6 defects** the project fixed across **1 releases** of the 2.17 line, from 2.17.1 to
2.17.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.17.1

- [Openstack] Fix a bug where Openstack cloud provider could not be used with username/password ([#8021](https://github.com/kubernetes-sigs/kubespray/pull/8021), [@bl0m1](https://github.com/bl0m1))
- [Calico] Fix typha prometheus causing a deployment error ([#8005](https://github.com/kubernetes-sigs/kubespray/pull/8005), [@ericlake](https://github.com/ericlake))
- [Cilium] Fix operator metrics activation (`enable-metrics` key missing) ([#8000](https://github.com/kubernetes-sigs/kubespray/pull/8000), [@L3o-pold](https://github.com/L3o-pold))
- Fix CentOS7 issue with allowPrivilegeEscalation value from metrics-server ([#8014](https://github.com/kubernetes-sigs/kubespray/pull/8014), [@oomichi](https://github.com/oomichi))
- Fix k8s-certs-renew cp path wrongly using `/usr/bin/` ([#7992](https://github.com/kubernetes-sigs/kubespray/pull/7992), [@lazybetrayer](https://github.com/lazybetrayer))
- Fix containerd failed to start if apparmor is not installed ([#8011](https://github.com/kubernetes-sigs/kubespray/pull/8011), [@rtsp](https://github.com/rtsp))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.17.1**, the newest release recorded here for this line.

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
