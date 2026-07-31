---
id: TROUBLE-KUBESPRAY_2_23_DEFECTS
type: troubleshooting
title: "kubespray 2.23: defects fixed in the 2.23 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.23.0 <2.24.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubespray 2.23 known issues
  - kubespray 2.23 fixed in
  - is this kubespray bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubespray
sources:
  - type: docs
    path: kubernetes-sigs/kubespray release notes for the 2.23 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/kubespray/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubespray 2.23: defects fixed in the 2.23 line

## Summary

**41 defects** the project fixed across **4 releases** of the 2.23 line, from 2.23.0 to
2.23.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.23.0

- [local_path_provisioner] Fix invalid podhelper yaml (#10237, @MrFreezeex)
- [crio] Fix etcdctl copy operation (#10242, @ErikJiang)
- [youki] Fix youki binary download url (not requiring 'v' in version) (#10337, @ErikJiang)
- [multus] Fix loop_control template error when item is None (#10347, @nicolas-goudry)
- Update Calico to lowercase and fix broken calico link in README (#10232, @Xieql)
- Fix Dockerfile for newest directory layout (#10128, @dabeck)
- Fix Flatcar bootstrap issues (yaml module missing and ntp issue) (#10363, @tenni-paws)
- Fix argocd install not working using the kubespray docker image (#10371, @cortex3)
- Fix correctly mount ssl ca directories (#9794, @maxime1907)
- Fix etcdctl copy operation (#10230, @ErikJiang)
- Fix gce-pd-csi driver (#10208, @ashishsinghdev)
- Fix grep command without -w option causing prefix matched while adding one etcd member (#10291, @yangsenzk)
- Fix hcloud-cloud-controller-manager not working in certain setups (#10297, @cortex3)
- Fix helm (kubelet-csr-approver) installation on redhat distro (#10204, @MrFreezeex)
- Fix kubelet-csr-approver usage with upgrade-cluster.yml and missing package with helm role (#10165, @j4m3s-s)
- Fix nginxingress-class template (missing newline) (#10174, @richard-fairthorne)
- Fix problem migration problem with k8s 1.27 (#10136, @batazor)
- Fix reset_confirmation not working when inputing correct value (#10288, @somewho)
- Fix wrong path in manage-offline-files script (#9886, @Medosopher)
- Fix an issue where using Rocky Linux 8 as OS for Vagrant for testing purposes causing etcd to fail on start. (#10252, @nltimv)
- Fix ansible-lint galaxy rule (#10277, @MrFreezeex)
- Fix ansible-lint key-order error (#10314, @MrFreezeex)
- Fix outdated tag and experimental ansible-lint rules (#10254, @MrFreezeex)
- Fix metrics-server deployment to run with kubernetes 1.26+ (#10183, @mzaian)
- Fix undefined `reset_confirmation_prompt` variable in reset play (#10303, @Mishavint)
- Fix CIS Kubernetes V1.23 Benchmark item number 4.1.9 to enhance security (Change kubelet-config.yaml and kubelet.env file permissions from 640 to 600) (#10304, @satandyh)
- Fix parsing of RHSM proxy configuration (#10228, @tmurakam)
- Fix var-spacing ansible rule (#10266, @MrFreezeex)
- Fix specify owner to kube_owner in task of copy cni plugins (#10407, @NierYYDS)
- Fix typo kubelet_topoloy_manager_policy => kubelet_topology_manager_policy (#10384, @hangscer8)
- Fix recover_control_plane playbook (also add debian 12 with cilium as a new nightly test) (#10411, @floryut)
- Fix nameserver inline comments in /etc/resolv.conf (#10415, @yankay)
- [CI] fix tf-elastx_cleanup fail (#10133, @yankay)
- Resolve ansible-lint name errors (#10253, @MrFreezeex)

### 2.23.1

- [Cilium] Fix invalid hubble yaml if `cilium_hubble_tls_generate` is enabled (#10476, @toonalbers)
- [ingress-nginx] Fix nginx controller leader election RBAC permissions (#10569, @mzaian)
- Fix get currently configured nameservers error where there are inline comments in /etc/resolv.conf (#10415, @yankay)

### 2.23.2

- [containerd] Fix invalid version check in containerd jinja-template config (#10620, @khanhngobackend)
- Fix calico-node in etcd mode. (#10768, @VannTen)
- Fix download retry when get_url has no status_code (#10613, @RomainMou) (#10791, @VannTen)

### 2.23.3

- Fix hardcoded pod infra version (#10806, @ErikJiang)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.23.3**, the newest release recorded here for this line.

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
