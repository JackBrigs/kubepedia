---
id: TROUBLE-KUBESPRAY_2_18_DEFECTS
type: troubleshooting
title: "kubespray 2.18: defects fixed in the 2.18 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.18.0 <2.19.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubespray 2.18 known issues
  - kubespray 2.18 fixed in
  - is this kubespray bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubespray
sources:
  - type: docs
    path: kubernetes-sigs/kubespray release notes for the 2.18 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/kubespray/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubespray 2.18: defects fixed in the 2.18 line

## Summary

**31 defects** the project fixed across **3 releases** of the 2.18 line, from 2.18.0 to
2.18.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.18.0

- [Openstack] Fix a bug where Openstack cloud provider could not be used with username/password ([#8021](https://github.com/kubernetes-sigs/kubespray/pull/8021), [@bl0m1](https://github.com/bl0m1))
- [Calico] Fix Kube-bench security warnings on calico controller (file ownership/permissions) ([#8072](https://github.com/kubernetes-sigs/kubespray/pull/8072), [@oomichi](https://github.com/oomichi))
- [Calico] Fix typha prometheus causing a deployment error ([#8005](https://github.com/kubernetes-sigs/kubespray/pull/8005), [@ericlake](https://github.com/ericlake))
- [Cilium] Fix operator metrics activation (`enable-metrics` key missing) ([#8000](https://github.com/kubernetes-sigs/kubespray/pull/8000), [@L3o-pold](https://github.com/L3o-pold))
- [containerd] Fix the usage of cgroupfs with containerd and introduce cgroupsfs specific variables (⚠️ `containerd_runtimes` is now `containerd_additional_runtimes` ) ([#8123](https://github.com/kubernetes-sigs/kubespray/pull/8123), [@pasqualet](https://github.com/pasqualet))
- Fix CentOS7 issue with allowPrivilegeEscalation value from metrics-server ([#8014](https://github.com/kubernetes-sigs/kubespray/pull/8014), [@oomichi](https://github.com/oomichi))
- Fix Heketi deployment logic that was broken by the ansible 3.4 upgrade ([#8118](https://github.com/kubernetes-sigs/kubespray/pull/8118), [@cristicalin](https://github.com/cristicalin))
- ~Fix `apiserver_loadbalancer_domain_name` pointing to external LB instead of dbip ([#8299](https://github.com/kubernetes-sigs/kubespray/pull/8299), [@singeleaf](https://github.com/singeleaf))~ [REVERTED]
- Fix a conflict with containerd and podman under CentOS 8.x (remove podman when installing Docker/Containerd) ([#8016](https://github.com/kubernetes-sigs/kubespray/pull/8016), [@panpan0000](https://github.com/panpan0000))
- Fix bad indentation in cert-manager when trusted internal ca is defined ([#8314](https://github.com/kubernetes-sigs/kubespray/pull/8314), [@infra-monkey](https://github.com/infra-monkey))
- Fix calico's inventory check (Check if inventory match current cluster configuration) conversion ([#8120](https://github.com/kubernetes-sigs/kubespray/pull/8120), [@juliohm1978](https://github.com/juliohm1978))
- Fix cert_manager ClusterIssuer manifest by removing deprecated ClusterIssuer ([#8064](https://github.com/kubernetes-sigs/kubespray/pull/8064), [@rtsp](https://github.com/rtsp))
- Fix cloud_provider check in preinstall task, allowing `oci` value (and removing deprecated ones) ([#8164](https://github.com/kubernetes-sigs/kubespray/pull/8164), [@oomichi](https://github.com/oomichi))
- Fix containerd failed to start if apparmor is not installed ([#8011](https://github.com/kubernetes-sigs/kubespray/pull/8011), [@rtsp](https://github.com/rtsp))
- Fix debian 9 check for apt cache update in bootstrap-os ([#8215](https://github.com/kubernetes-sigs/kubespray/pull/8215), [@floryut](https://github.com/floryut))
- Fix deploying loadbalancer to masters when bind-address is not set to 0.0.0.0 (and `loadbalancer_apiserver_localhost` is `true`) ([#8262](https://github.com/kubernetes-sigs/kubespray/pull/8262), [@Bledai](https://github.com/Bledai))
- Fix forgotten update of etcd-servers list in apiserver manifest when scaling ([#8253](https://github.com/kubernetes-sigs/kubespray/pull/8253), [@liupeng0518](https://github.com/liupeng0518))
- Fix k8s-certs-renew cp path wrongly using `/usr/bin/` ([#7992](https://github.com/kubernetes-sigs/kubespray/pull/7992), [@lazybetrayer](https://github.com/lazybetrayer))
- Fix k8scsi/csi-resizer repo (from gcr to quay) ([#8270](https://github.com/kubernetes-sigs/kubespray/pull/8270), [@oomichi](https://github.com/oomichi))
- Fix kata-containers runtime with version 2.x ([#8068](https://github.com/kubernetes-sigs/kubespray/pull/8068), [@cristicalin](https://github.com/cristicalin))
- Fix kubespray flatcar ansible_os_family and ansible_distribution for backward compatibility ([#8029](https://github.com/kubernetes-sigs/kubespray/pull/8029), [@isantospardo](https://github.com/isantospardo))
- Fix quorum check when recovering broken etcd cluster (with etcd 3.5.x) ([#8126](https://github.com/kubernetes-sigs/kubespray/pull/8126), [@floryut](https://github.com/floryut))
- Fix reset playbook for Fedora OS ([#8205](https://github.com/kubernetes-sigs/kubespray/pull/8205), [@cristicalin](https://github.com/cristicalin))
- Fix wrong baseurl for centos extra repo for Oracle Linux (missing `/os/`) ([#8208](https://github.com/kubernetes-sigs/kubespray/pull/8208), [@buker](https://github.com/buker))
- Fixes incongruence between metrics-server resources limits/requests defined in official templates ([#8088](https://github.com/kubernetes-sigs/kubespray/pull/8088), [@irizzant](https://github.com/irizzant))
- [Calico] Fix support for version 3.21.x ([#8250](https://github.com/kubernetes-sigs/kubespray/pull/8250), [@cristicalin](https://github.com/cristicalin))
- Fix resolved config when nodelocaldns is not enabled ([#8351](https://github.com/kubernetes-sigs/kubespray/pull/8351), [@liupeng0518](https://github.com/liupeng0518))

### 2.18.1

- Fix an issue where offline script could not output URLs of both containerd and krew. ([#8379](https://github.com/kubernetes-sigs/kubespray/pull/8379), [@oomichi](https://github.com/oomichi))
- Fix container engine still installed on dedicated etcd node even if `etcd_deployment_type: host` ([#8404](https://github.com/kubernetes-sigs/kubespray/pull/8404), [@rtsp](https://github.com/rtsp))

### 2.18.2

- Fix cert-manager unusable due to leader election namespace problem ([#8681](https://github.com/kubernetes-sigs/kubespray/pull/8681), [@rtsp](https://github.com/rtsp))
- Fix image_command_tool var ignored since PR #8601 ([#8684](https://github.com/kubernetes-sigs/kubespray/pull/8684), [@sathieu](https://github.com/sathieu))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.18.2**, the newest release recorded here for this line.

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
