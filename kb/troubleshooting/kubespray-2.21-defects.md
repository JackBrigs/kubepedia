---
id: TROUBLE-KUBESPRAY_2_21_DEFECTS
type: troubleshooting
title: "kubespray 2.21: defects fixed in the 2.21 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.21.0 <2.22.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubespray 2.21 known issues
  - kubespray 2.21 fixed in
  - is this kubespray bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubespray
sources:
  - type: docs
    path: kubernetes-sigs/kubespray release notes for the 2.21 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/kubespray/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubespray 2.21: defects fixed in the 2.21 line

## Summary

**23 defects** the project fixed across **1 releases** of the 2.21 line, from 2.21.0 to
2.21.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.21.0

- Fix a pre-upgrade node drain rescue task failure when `kube_override_hostname` is set (#9556, @chadswen)
- Fix default value for kubelet_secure_addresses (#9355, @willtrnr)
- [kube-vip] Minor changes on Kube VIP configuration parameters (and fix wrong properties) (#9414, @woutergd)
- Fix remove Cilium CNI failed because the CNI bin dependency (#9563, @yankay)
- Fix cert-manager deployment on hardening environments (#9404, @oomichi)
- Fix checksum of ciliumcli v0.12.5 for arm64 (#9614, @oomichi)
- Fix inconsistent handling of admission plugin list (`kube_apiserver_enable_admission_plugins` must be specified as a list of individual plugin names instead of a single item comma-separated list) (#9407, @willtrnr)
- Fix kube token dir permissions (#9590, @C-Romeo)
- Fix missing control plane taint in kubeadm (#9592, @yankay)
- Fix regex for comments nameserver in resolv.conf (#9523, @yankay)
- Fix reset for RedHat based distro with major version >=8 (#9537, @dougsland)
- Fix wrong cri_socket path for containerd (#9401, @maxime1907)
- Fix wrong rbac of the ClusterRole `csi-snapshotter-role` (#9610, @maxime1907)
- Fix OL9 setup - disable Centos Extras repo creation (#9483, @psvmcc)
- [Cilium] Fix the Hubble certificate being faulty because the cluster name has an hard coded value (#9340, @dcwbq)
- [Cilium] Fix tls settings not being properly set (#9457, @charlychiu)
- [Cilium] Remove trailing backslash and fix yaml indent (#9339, @reneluria)
- [Openstack] Fix a race condition in terraform causing ports to not get an IP (#9345, @bl0m1)
- [Openstack] Fix missing permissions for Openstack cloud-controller-manager (#9335, @bl0m1)
- [upcloud] Fixed issue where DNS would be blocked while using allowlist (#9510, @Xartos)
- [CI] Add check_typo job (and fix a bunch of typos) (#9361, @oomichi)
- [CI] Fix YAML format in hardening.md file (#9387, @oomichi)
- [CI] Increase the fedora memory at CI to fix the CI broken (#9640, @yankay)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.21.0**, the newest release recorded here for this line.

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
