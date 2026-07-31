---
id: TROUBLE-KUBESPRAY_2_24_DEFECTS
type: troubleshooting
title: "kubespray 2.24: defects fixed in the 2.24 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.24.0 <2.25.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubespray 2.24 known issues
  - kubespray 2.24 fixed in
  - is this kubespray bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubespray
sources:
  - type: docs
    path: kubernetes-sigs/kubespray release notes for the 2.24 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/kubespray/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubespray 2.24: defects fixed in the 2.24 line

## Summary

**23 defects** the project fixed across **4 releases** of the 2.24 line, from 2.24.0 to
2.24.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.24.0

- [cilium] Fix invalid hubble yaml if `cilium_hubble_tls_generate` is enabled (#10430, @toonalbers)
- [containerd] Fix invalid version check in containerd jinja-template config (#10620, @khanhngobackend)
- Fix 'kube-apiserver' tag inappropriately overwriting secrets at rest encryption token (#10460, @jwitko)
- Fix assertion for task item verify-settings (#10699, @piwinkler)
- Fix external-lb in kubelet.conf server address and kube-proxy api-server address (#10490, @ugur99)
- Fix forgotten update of etcd-servers list in apiserver manifest when scaling (#8253, @liupeng0518)
- Fix reset job for cri-o container engine (#10197, @turbosnail)
- Fix restart network task cannot be skipped (ansible boolean conversion needed) (#10512, @ErikJiang)
- Fix: add kubelet tag in task of Fetch facts to avoid kubelet config inconsistencies (#10423, @NierYYDS)
- Fixes the path of the certificates use in the etcdctl.sh wrapper when the deployment type is not kubeadm. (#10467, @RomainMou)
- Fix undefined retries variable when copying etcdctl (#10634, @ErikJiang)
- Fix download retry when get_url has no status_code (#10613, @RomainMou)
- Fix ntp installation on SLES and openSUSE (#10786, @goldyfruit)
- Fix crio_version version comparison (#10780, @ledroide)
- Fix disable swap failed in Centos/RHEL 7 (#10751, @yankay)
- Fix image pull fail with insecure-registry (#10775, @yankay)
- Refactor check_galaxy + fix version (#10729, @VannTen)
- Fix Helm installation on SLES and openSUSE (#10794, @goldyfruit)
- Fix incorrect ciliumcli binary (#10575, @tu1h)
- Fix the cluster installation on cluster using etcd clients nodes (cilium / calico / ...) (#10769, @VannTen)

### 2.24.1

- Fix logical error when checking for boostrap-os (#10953, @VannTen)

### 2.24.2

- Fix CentOS 7 yum repo baseurl update (#11364, @tico88612 )

### 2.24.3

- User has a possibility to fix nodePort of ingress-nginx service with property in addons.yaml (#11361, @k8s-infra-cherrypick-robot)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.24.3**, the newest release recorded here for this line.

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
