---
id: TROUBLE-KUBESPRAY_2_27_DEFECTS
type: troubleshooting
title: "kubespray 2.27: defects fixed in the 2.27 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.27.0 <2.28.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubespray 2.27 known issues
  - kubespray 2.27 fixed in
  - is this kubespray bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubespray
sources:
  - type: docs
    path: kubernetes-sigs/kubespray release notes for the 2.27 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/kubespray/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubespray 2.27: defects fixed in the 2.27 line

## Summary

**25 defects** the project fixed across **2 releases** of the 2.27 line, from 2.27.0 to
2.27.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.27.0

- [cri-o] Switch binaries to libexecdir Update youki version to 0.4.1 to fix ci. (#11584, @yankay)
- Fix CI: elastx cleanup security groups (#11411, @yankay)
- Always copy cert generation script to first etcd to pick up fixes on existing clusters (#11612, @VannTen)
- Fix Cilium agent permission can't read loadbalancerippools and secrets (#11466, @foobaar)
- Fix calico dual stack installation when using `ip` and `ip6`. (#11770, @VannTen)
- Fix collection usage for calico and other configuration depending on .sh and .conf files in Kubespray (#11707, @VannTen)
- Fix format of kubeadm-config v1beta4 (#11709, @VannTen)
- Fix kube-vip container securityContext (#11647, @KubeKyrie)
- Fix openEuler system packages installation (#11688, @VannTen)
- Fix pretty-printing (in kubectl) of nodelocaldns and coredns configmap when using `dns_upstream_forward_extra_opts` with an empty value option. (#11694, @VannTen)
- Fix spurious failure with 'localhost' when using `scale.yml --limit <some nodes>` (#11817, @VannTen)
- Fix task naming in bootstrap-os (#11714, @ErikJiang)
- Fix terraform.py on python >=3.12 (#11773, @enrico9034)
- Fix the check for cached data when using --limit (#11693, @VannTen)
- Fix the usage of --limit when using legacy groups (#11577, @VannTen)
- Fix usage of admission plugins configuration. (#11779, @VannTen)
- Fix using the default network manager in reset.yml (#11678, @KubeKyrie)
- Fix: cannot stop & remove all cri containers via remove_node.yml (#11631, @tico88612)
- Fixed: VSphere CSI and CPI drivers and are now retrieved from registry.k8s.io instead of gcr.io, as they have been deleted from the latter. Only a few recent versions are available in the new repository; if you have pinned `vsphere_csi_controller`, `vsphere_csi_driver_image_tag` or `vsphere_syncer_image_tag` to a version older than `v3.1.2`, please check if that version is available from the new repository. The same goes for `external_vsphere_cloud_controller_image_tag` which can no longer be `latest`, and should align with the running version of Kubernetes. It now defaults to `v1.31.0`. (#11564, @luringens)
- Fix `roles/download/tasks/download_file.yml` task name typo (#11684, @dmncmn)

### 2.27.1

- Fix sample inventory for the reserved resource (#11922, @k8s-infra-cherrypick-robot)
- Fix CI by exclude the `.ansible` in `.ansible-lint` Remove `ctr image pull` workaround for nerdctl (#11956, @k8s-infra-cherrypick-robot)
- Fix coredns deployment with `coredns_pod_disruption_budget: true` or `enable_nodelocaldns_secondary` (#11957, @k8s-infra-cherrypick-robot)
- Fix: When running `./manage-offline-container-images.sh register` with using Podman, getting the image_id fails and the script is interrupted. (#12314, @k8s-infra-cherrypick-robot)
- [calico] Fix kubecontrollersconfigurations list permission (#12039, @k8s-infra-cherrypick-robot)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.27.1**, the newest release recorded here for this line.

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
