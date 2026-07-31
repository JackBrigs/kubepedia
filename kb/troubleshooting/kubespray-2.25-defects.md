---
id: TROUBLE-KUBESPRAY_2_25_DEFECTS
type: troubleshooting
title: "kubespray 2.25: defects fixed in the 2.25 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.25.0 <2.26.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubespray 2.25 known issues
  - kubespray 2.25 fixed in
  - is this kubespray bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubespray
sources:
  - type: docs
    path: kubernetes-sigs/kubespray release notes for the 2.25 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/kubespray/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubespray 2.25: defects fixed in the 2.25 line

## Summary

**26 defects** the project fixed across **2 releases** of the 2.25 line, from 2.25.0 to
2.25.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.25.0

- Prevent nodelocaldns to be OOM-killed (#11056, @sathieu)
- Fix secondary coredns missing var (#10821, @VannTen)
- Fixed typos in inventory/sample/group_vars/k8s_cluster (#10911, @arahmangulov)
- Fix ClusterRole for Calico >=v1.26.x with Calico API Server installed (#11089, @RaSerge)
- Fix ansible parameter ssh_args in ansible.cfg file not work (#10981, @joy717)
- Fix boostrap for Amazon Linux (#11139, @VannTen)
- Fix crio registries config file when using slashes in the registry path (#11030, @pedro-peter)
- Fix file loss during download (#10779, @ErikJiang)
- Fix kubespray-defaults: Check for boostrap-os FQCN (#11073, @KubeKyrie)
- Fix local path provisioner image repo in sample inventory. (#11180, @tico88612)
- Fix logical error when checking for boostrap-os (#10867, @VannTen)
- Fix lsattr command error when kubelet has symbolic link (#11074, @KubeKyrie)
- Fix network manage service of Debian 12 (#11058, @KubeKyrie)
- Fix nginx controller leader election RBAC (#10913, @VannTen)
- Fix python regex matching problem when finding docker packages (#11075, @KubeKyrie)
- Fix waiting for MetalLB controller (#10858, @flxbwr)
- Fix(kubernetes): taint nodes on cluster upgrade (#10705, @maxime1907)
- Fix: config hostname as string type in kubeadmConfig rendering (#10997, @ErikJiang)
- Fixes running `recover-control-plane.yml` with offline broken etcd nodes. (#10660, @yuha0)
- Revert OCCM standard dnsPolicy to ClusterFirst to fix #10914 which was introduced with #10618 and make dnsPolicy configurable to furthermore support #10618 (#11168, @Payback159)
- [etcd] fixes wrong distributed tracing flag for etcd (#11175, @ugur99)
- Correct the POLY1305 cipher suites by adding the suffix _SHA256 (#10641, @yckaolalala)

### 2.25.1

- User has a possibility to fix nodePort of ingress-nginx service with property in addons.yaml (#11339, @k8s-infra-cherrypick-robot)
- [calico] Update default calico to v3.27.4 [calico] Fix high cpu load due to XDP program in iptables (#11476, @mzaian)
- Always copy cert generation script to first etcd to pick up fixes on existing clusters (#11616, @k8s-infra-cherrypick-robot)
- Fix: cannot stop & remove all cri containers via remove_node.yml (#11638, @k8s-infra-cherrypick-robot)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.25.1**, the newest release recorded here for this line.

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
