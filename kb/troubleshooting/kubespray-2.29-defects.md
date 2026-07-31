---
id: TROUBLE-KUBESPRAY_2_29_DEFECTS
type: troubleshooting
title: "kubespray 2.29: defects fixed in the 2.29 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.29.0 <2.30.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubespray 2.29 known issues
  - kubespray 2.29 fixed in
  - is this kubespray bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubespray
sources:
  - type: docs
    path: kubernetes-sigs/kubespray release notes for the 2.29 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/kubespray/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubespray 2.29: defects fixed in the 2.29 line

## Summary

**22 defects** the project fixed across **2 releases** of the 2.29 line, from 2.29.0 to
2.29.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.29.0

- Fix Cilium installation issues (caused by templating syntax errors) when certain non-default features (encryption, etc.) are enabled (#12280, @spantaleev)
- Fix Hubble-Relay peer discovery in clusters using non-default cluster name by properly configuring clusterDomain in Cilium Helm values (#12346, @mertcancam)
- Fix cilium installation role to render cilium_config_extra_vars into helm values (#12335, @atobaum)
- Fix cilium_policy_audit_mode variable (#12569, @guoard)
- Fix error when using `kubeadm_ignore_preflight_errors: ['all']` (#12606, @VannTen)
- Fix ingress-nginx DaemonSet and Service templates rendering TCP/UDP ports as strings, which prevented correct export of TCP/UDP services via NGINX ingress controller. (#12442, @MahdadGhasemian)
- Fix invalid PodSecurity admission configuration when `kube_pod_security_use_default: false` (#12439, @AMacedoP)
- Fix scale.yml problems with cached IP facts (#12243, @fox0430)
- Fix the Cilium cluster, which is upgraded from 2.27 to 2.28 will break Fix helm release re-use message when installing repeatedly (#12254, @tico88612)
- Fix the issue of etcd node addition failure caused by incorrect ETCD_INITIAL_CLUSTER configuration. (#12342, @liuxu623)
- Fix(kubeadm): Conditionally add --skip-phases flag for v1.32.0+ (#12351, @ErikJiang)
- Fix: A timeout occurs when running the offline deployment script using Podman. (#11962, @DearJey)
- Fix: When running `./manage-offline-container-images.sh register` with using Podman, getting the image_id fails and the script is interrupted. (#11961, @DearJey)
- Fix: kubeadm secondary nodes use file discovery validation failed (#12132, @tico88612)
- Fixed a looping timeout bug when deleting an entire cluster (#12300, @chadswen)
- Fixed cilium_enable_bgp_control_plane config (#12430, @XuhuiSun95)
- Fixed packages installation on Alma/Rocky Linux when behind a proxy (#12264, @root-expert)
- Fixes a syntax error that made the '_bgp_config' an 'AnsibleUnsafeText' instead of a 'dict', which caused the "Calico | Process BGP Configuration" step to fail (#12258, @mathgaming)
- Fix netcheck etcd image tag align with the etcd current version (#12402, @wangsifei99)

### 2.29.1

- Fix Calico apiserver RBAC permissions for Kubernetes 1.33+ (#12695, @k8s-infra-cherrypick-robot)
- Fix Cilium loadBalancer.mode rendering in Kubespray values template. (#12705, @k8s-infra-cherrypick-robot)
- Fix(calico): Add missed rbac verb watch for hostendpoints (#12644, @k8s-infra-cherrypick-robot)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.29.1**, the newest release recorded here for this line.

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
