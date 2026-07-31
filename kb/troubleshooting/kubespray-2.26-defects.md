---
id: TROUBLE-KUBESPRAY_2_26_DEFECTS
type: troubleshooting
title: "kubespray 2.26: defects fixed in the 2.26 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.26.0 <2.27.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubespray 2.26 known issues
  - kubespray 2.26 fixed in
  - is this kubespray bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubespray
sources:
  - type: docs
    path: kubernetes-sigs/kubespray release notes for the 2.26 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/kubespray/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubespray 2.26: defects fixed in the 2.26 line

## Summary

**20 defects** the project fixed across **2 releases** of the 2.26 line, from 2.26.0 to
2.26.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.26.0

- User has a possibility to fix nodePort of ingress-nginx service with property in addons.yaml (#11310, @mochizuki875)
- [calico] add calico support v3.27.4 to fix high cpu load due to XDP program in iptables (#11476, @ehsan310)
- [containerd] fixes wrong templating for tracing config (#11372, @ugur99) [runc] Upgrade to v1.1.13 (#11413, @mzaian)
- Fix Hetzner kubernetes group names (#11232, @jmaccabee13)
- Fix: skip multus when not defined (#10934, @darkobas2)
- Fix CI with fail docker pull in gitlab runner by change DOCKER_HOST (#11315, @yankay)
- Fix etcd not starting up when using a custom access address (#11388, @derselbst)
- Fix the Auto Bump PR is blocked by the label `do-not-merge/release-note-label-needed` by adding dependabot `release-note-none` label. (#11256, @yankay)
- Fix kube_reserved so it only controls kubeReservedCgroup . (#11367, @rptaylor)
- Fix error in boostrap-os when git does not handle symlinks (#11508, @VannTen)
- Fix static kube-apiserver advertise address based on first control plane (#11457, @Seljuke)
- Fix incorrect member matching when removing etcd nodes (#11488, @ErikJiang)
- Fix double pop of access_ip (#11435, @rptaylor)
- Fix use super-admin.conf for kube-vip on first master when it exists to support initial k8s v1.29+ installation with kube-vip enabled (#11422, @Seljuke)
- Fix openstack cleanup by change the delete security_group order (#11299, @yankay)

### 2.26.1

- Always copy cert generation scripts to first etcd to pick up fixes on existing clusters (#11615, @k8s-infra-cherrypick-robot)
- Fix: cannot stop & remove all cri containers via remove_node.yml (#11637, @k8s-infra-cherrypick-robot)
- Fix kubecontrollersconfigurations list permission (#12038, @k8s-infra-cherrypick-robot)
- Fix manage-offline-container-images.sh get image_id (#12315, @k8s-infra-cherrypick-robot)
- Fix PodSecurity Admission "empty" definition handling (#12477, @k8s-infra-cherrypick-robot)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.26.1**, the newest release recorded here for this line.

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
