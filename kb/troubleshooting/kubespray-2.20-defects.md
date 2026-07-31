---
id: TROUBLE-KUBESPRAY_2_20_DEFECTS
type: troubleshooting
title: "kubespray 2.20: defects fixed in the 2.20 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.20.0 <2.21.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubespray 2.20 known issues
  - kubespray 2.20 fixed in
  - is this kubespray bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubespray
sources:
  - type: docs
    path: kubernetes-sigs/kubespray release notes for the 2.20 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/kubespray/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubespray 2.20: defects fixed in the 2.20 line

## Summary

**20 defects** the project fixed across **1 releases** of the 2.20 line, from 2.20.0 to
2.20.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.20.0

- [Openstack] Fix subnet order and number of master nodes (#9159, @robinelastisys)
- Fix failure to look up user etcd when adding a user (#9016, @yankay)
- Fix Hetzner CCM cluster-cidr (wrongly set to a static value) (#9127, @ym)
- Fix calicoctl.sh path error when getting calico configuration (#9217, @tasekida)
- Fix failing tasks when calico_datastore is set to etcd (#9228, @chadswen)
- Fix missing quote in task "See if node is schedulable" (#9146, @emiran-orange)
- Fix number node name can't be added. (#9266, @cleverhu)
- Fix regex for replacing http_proxy host in RedHat Subscription Manager (#8957, @dicksontung)
- Fix some docker reset task (don't remove already uninstalled packages, ignore error on remove docker config files if already removed) (#8966, @orange-llajeanne)
- Fix the Centos/RHEL docker installation issue in ARM64 (#9047, @yankay)
- Fix the kube-vip missed SAN issue (#9099, @yankay)
- Fixed concatenate str & int in `auto_renew_certificates_systemd_calendar` (#8979, @floryut)
- Fixes the issue when it cannot correctly set the namespace for vphere-csi-driver (#9046, @eminaktas)
- Fixes vSphere CSI for vSphere CSI >= 2.4.0 on vSphere 6.7U3 (#8944, @snowball77)
- [ingress-nginx] Fix ingress-nginx RBAC rules when deployed classless (#9156, @cristicalin)
- Remove the 'etcd-unsupported-arch' args to fix the etcd issue in arm64 (#9049, @yankay)
- Fix duplicate field in ingress-nginx template (#9285, @cloud-66)
- Fix CoreDNS memory leak issue by adding `max_concurrent=1000` in the CoreDNS config (#9307, @yankay)
- Fix ansible user module create_home property (erroneously written as createhome) (#9314, @liupeng0518)
- [CI] Fix cloud_init files for different distros (#9232, @floryut)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.20.0**, the newest release recorded here for this line.

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
