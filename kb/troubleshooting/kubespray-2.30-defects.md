---
id: TROUBLE-KUBESPRAY_2_30_DEFECTS
type: troubleshooting
title: "kubespray 2.30: defects fixed in the 2.30 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.30.0 <2.31.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubespray 2.30 known issues
  - kubespray 2.30 fixed in
  - is this kubespray bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubespray
sources:
  - type: docs
    path: kubernetes-sigs/kubespray release notes for the 2.30 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/kubespray/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubespray 2.30: defects fixed in the 2.30 line

## Summary

**10 defects** the project fixed across **1 releases** of the 2.30 line, from 2.30.0 to
2.30.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.30.0

- Fixed `kube_vip_version` variable for managing kube-vip version instead of `kube_vip_image_tag` (#12835, @ThisIsQasim)
- Fix(cilium): prevent installation failure with unprivileged agent (#12628, @r3m8)
- Fix Calico apiserver RBAC permissions for Kubernetes 1.33+ (#12654, @rickerc)
- Fix Cilium loadBalancer.mode rendering in Kubespray values template. (#12701, @intojhanurag)
- Fix RBAC for calico using the etcd datastore (#12828, @LawiK974)
- Fix automatic certs renew with systemd timer (#12876, @VannTen)
- Fix broken upgrade path/control plane node rotation for cluster using calico in etcd datastore mode with separate etcd. `etcd_cert_dir_mode` is deleted (always use `0700`) (#12908, @VannTen)
- Fix kubeadm init retry after first failure on cluster creation (#12785, @VannTen)
- Fix(calico): Add missed rbac verb watch for hostendpoints (#12641, @jmeza-xyz)
- Fixed an issue in the config.json.j2 template where the CRI-O registry authentication configuration could render invalid JSON when multiple `crio_registry_auth` entries were defined, resulting in duplicate top-level `auths` keys in the generated config. (#12845, @accuROAMC)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.30.0**, the newest release recorded here for this line.

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
