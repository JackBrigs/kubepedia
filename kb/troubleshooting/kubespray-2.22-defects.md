---
id: TROUBLE-KUBESPRAY_2_22_DEFECTS
type: troubleshooting
title: "kubespray 2.22: defects fixed in the 2.22 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.22.0 <2.23.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubespray 2.22 known issues
  - kubespray 2.22 fixed in
  - is this kubespray bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubespray
sources:
  - type: docs
    path: kubernetes-sigs/kubespray release notes for the 2.22 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/kubespray/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubespray 2.22: defects fixed in the 2.22 line

## Summary

**33 defects** the project fixed across **3 releases** of the 2.22 line, from 2.22.0 to
2.22.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.22.0

- Fix kube-bench 1.2.20 to enhance security (Ensure that the --audit-log-maxbackup argument is set to 10) (#9939, @yankay)
- Fix kube-bench 1.1.19 to enhance security (Change Kubernetes Cert directory and file ownership is set to root:root) (#9937, @yankay)
- Fix kube-bench 4.1.1 to enhance security (Change kubelet systemd init file from 644 to 600) (#9934, @yankay)
- Fix kubernetes-app/argocd: download related things with the download role (#9786, @pli01)
- [cri-o] Fix install order -> first runc then crictl (#9780, @mvandergiesen)
- [cri-o] Fix missed double quotes in cri-o config (#10040, @turbosnail)
- [cri-o] Fix CRI-O amd64 v1.26.0 wrong archive checksum (#9872, @panguicai008)
- [cri-o] Fix cri-o restart if config change (#10057, @MrFreezeex)
- [Calico] Fix installation while applying CRD (#10068, @hangscer8)
- [Cilium] Fix Hubble relay configuration (#9876, @prashantchitta)
- [Cilium] Fix the configuration of TLS for hubble (#9880, @utam0k)
- [multus] fix multus include error (#10105, @darkobas2)
- Fix sidebar documentation (#9988, @lijin-union)
- Fix `cert_manager_trusted_internal_ca` manifest failing when dns policy is set (#9922, @peschmae)
- Fix `containerd_insecure_registries` => move `with_item` to `with_dict` (#9729, @lengrongfu)
- Fix allow unsupported distribution (#9904, @ErikJiang)
- Fix cilium's hubble ui configuration (#9735, @j4m3s-s)
- Fix comma-separated-list splitting of `kubelet_enforce_node_allocatable` variable (#9694, @Tristan971)
- Fix ingress url not found issue (#9789, @JaneLiuL)
- Fix playbook names to support import via galaxy (#10021, @dkasanic)
- Fix restart k8s components, checking yml files instead of manifest (#9962, @liupeng0518)
- Fix uniontech OS installation failure (#9862, @ErikJiang)
- [etcd] fix make-ssl-etcd.sh.j2; move pem files only if any new certs exist (#9974, @2k0ri)
- [vSphere-csi-driver] Fixes the run of the `cluster.yml` playbook when `vsphere_csi_namespace` is set to non-default (#9946, @eugene-marchanka)
- Fix(contrib/terraform): do not set ansible_ssh_port to 22 (#9828, @maxime1907)
- Fix arithmetic outside of jinja (#10106, @MrFreezeex)
- Fix CI broken by flannel-cni-plugin docker hub rate limit (#10083, @yankay)
- [CI] Fix CentOS Extras repo url for Oracle Linux 7 aarch64 (#9791, @bin456789)
- [CI] Fix tests for files lookup path for custom-cni (#10088, @j4m3s-s)

### 2.22.1

- Fix metrics-server deployment to run with kubernetes 1.26+ (#10183, @mzaian)
- Fix Update MetalLB deployment, wait for resource. (#9995, @Jeroen0494)

### 2.22.2

- Fix hardcoded pod infra version (#10805, @ErikJiang)
- [Multus] Fix loop_control template error when item is None (#10347, @nicolas-goudry)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.22.2**, the newest release recorded here for this line.

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
