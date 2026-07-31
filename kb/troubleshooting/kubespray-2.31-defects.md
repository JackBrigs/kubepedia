---
id: TROUBLE-KUBESPRAY_2_31_DEFECTS
type: troubleshooting
title: "kubespray 2.31: defects fixed in the 2.31 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.31.0 <2.32.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubespray 2.31 known issues
  - kubespray 2.31 fixed in
  - is this kubespray bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubespray
sources:
  - type: docs
    path: kubernetes-sigs/kubespray release notes for the 2.31 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/kubespray/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubespray 2.31: defects fixed in the 2.31 line

## Summary

**11 defects** the project fixed across **1 releases** of the 2.31 line, from 2.31.0 to
2.31.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.31.0

- Fix OCI CCM deployment failure caused by incorrect template filename in lookup (#13151, @amoghazy)
- Fix broken NO_PROXY variable (#12981, @VannTen)
- Fix calico missing RBAC permissions for kube-controller-manager to access tiers in manifest installs, which was preventing proper resource garbage collection. (#13100, @guoard)
- Fix calico missing staged policy permissions for api server (#13101, @guoard)
- Fix cilium_enable_prometheus variable having no effect by wiring it to the Helm values template. (#13142, @yankay)
- Fix crash when CiliumBGPAdvertisement is defined without a labels key. (#13149, @karimzakzouk)
- Fix drain tasks failing with UNREACHABLE when drain_timeout exceeds the Ansible SSH connection timeout by using async/poll. (#13081, @0xMH)
- Fix terraform openstack compute `image_id` and update `openstack_blockstorage_volume_v3` (#12910, @HauptJ)
- Fixed Gateway API v1.4.1 unexpected checksum change and add test (#13006, @labaq)
- Fixed openeuler metalink 24.03LTS wrong url (#13144, @tico88612)
- The internal kube-config used by control plane components on control plane nodes now points to the local apiserver (default kubeadm behavior) This fixes the incorrect version skew between control plane components and apiserver during upgrade (#12870, @VannTen)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.31.0**, the newest release recorded here for this line.

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
