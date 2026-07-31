---
id: TROUBLE-KUBESPRAY_2_19_DEFECTS
type: troubleshooting
title: "kubespray 2.19: defects fixed in the 2.19 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.19.0 <2.20.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubespray 2.19 known issues
  - kubespray 2.19 fixed in
  - is this kubespray bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubespray
sources:
  - type: docs
    path: kubernetes-sigs/kubespray release notes for the 2.19 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/kubespray/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubespray 2.19: defects fixed in the 2.19 line

## Summary

**42 defects** the project fixed across **2 releases** of the 2.19 line, from 2.19.0 to
2.19.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.19.0

- [Calico] Fix Wireguard support for CentOS Stream 9/RHEL 9 Beta (#8625, @ThisIsQasim)
- [Calico] fix calico-kube-controllers verbs (#8847, @irizzant)
- [MetalLB] Fix wrong port name in metallb.yml.j2 (metrics not monitoring) (#8510, @binkoni)
- [OpenStack] Fixed cluster roles for openstack cloud controller (#8638, @Xartos)
- [OpenStack] Fix templating of ansible_ssh_common_args in no_floating.yml if used as TF module (#8646, @frittentheke)
- [containerd] Fix containerd image download bug (#8894, @liupeng0518)
- CRI-O: fix unqualified-search registries (#8496, @krystianmlynek)
- Fix DNS configuration when using resolvconf_mode='host_resolvconf' during scale (#8361, @unai-ttxu)
- Fix GCP PVC creation on k8s v1.22 (#8616, @lmercl)
- Fix `0090-etchosts` file when setting `override_system_hostname=false` (#7634, @liupeng0518)
- Fix `kube-dns` service will no longer be deleted if not created by kubespray (#8565, @cyril-corbon)
- Fix an issue the kube-vip manifest with extra space. (#8831, @yankay)
- Fix an issue users cannot skip redhat registration by specifying -e rhel_enable_repos=False (#8871, @gleb108)
- Fix an issue where offline script could not output URLs of both containerd and krew. (#8379, @oomichi)
- Fix condition on kata_containers_version/kube_version check when kata_containers_enabled is false (#8804, @emiran-orange)
- Fix container engine still installed on dedicated etcd node even if `etcd_deployment_type: host` (#8386, @rtsp)
- Fix cri-o packages install for Rocky 8 (#8594, @brankomijuskovic)
- Fix etcd certificates reference to support `etcd_kubeadm_enabled: true` (#7766, @forselli-stratio)
- Fix imageRepository path for CoreDNS (ensure coredns repository namespace is kept) (#8572, @nicolas-goudry)
- Fix incorrect condition type (#8822, @cyclinder)
- Fix incorrect leader election namespace with cert-manager leading to insufficient permission (#8433, @rtsp)
- Fix issue when PodSecurityPolicy is enabled static pods are now mirrored earlier by kubelet. Problem when installing HA etcd via kubeadm. (#8744, @robinAwallace)
- Fix kubectl call before installing it when setting `first_kube_control_plane`/`joined_control_planes` (#8412, @floryut)
- Fix kubelet_kubelet_cgroups_cgroupfs pointing incorrectly to slice (#8500, @fungusakafungus)
- Fix print_hostnames of inventory.py (#8554, @oomichi)
- Fix remove-node.yaml playbook fails when host is unreachable (#8843, @oomichi)
- Fix removing `docker-ce.repo` failed (#8856, @Thearas)
- Fix the condition of drain on pre-remove task (#8634, @oomichi)
- Fix typo and duplicated declaration of ingressclasses (#8591, @spaced)
- Fix vagrant default value for parameters `local_path_provisioner_enabled`/`multi_networking` (#8650, @liupeng0518)
- Fix wrong item in mitogen contrib (#8508, @kdszoom)
- Fixed a bug where hosts with NetworkManager enabled were having their /etc/resolv.conf file edited directly instead of through NM. Fixed a bug where DNS lookup failures would cause reset.yml or scale.yml to error out when resolvconf_mode=host_resolvconf (#8575, @mac-chaffee)
- Fixed a bug where updated versions of etcd weren't being applied. Check your etcd instances to make sure their versions are what you expect. If not, restarting all etcd members should apply the update. (#8556, @mac-chaffee)
- Fixed a bug where upgrade-cluster.yaml would not apply updates to etcd-events (#8550, @mac-chaffee)
- Fixes missing checksum for kata-containers 2.2.3 on arm architectures (#8383, @Payback159)
- Fixes the etcd node removal by pointing ETCDCTL_ENDPOINTS to localhost (127.0.0.1) (#8526, @roedie)
- Prevent removing etcd member when running in check mode (#8570, @fungusakafungus)
- [Terraform-AWS] Fix error when creating subnets more than AZ (#8516, @sophalHong)
- [cert-manager] Fix missing RBAC rules for ClusterRole cert-manager-cainjector (#8444, @onock)
- [reset] fix task inclusion logic for network plugin (#8727, @cristicalin)
- [systemd-resolved] Fix DNS early and late stages (`dns_early`|`dns_late`) of cluster deployment [systemd-resolved] Add `upstream_dns_servers` to `FallbackDNS` [cluster-reset] Revert DNS configuration to early stage (for instance: only defined upstream nameservers) (#8561, @onock)

### 2.19.1

- Fix failing tasks when calico_datastore is set to etcd ([#9234](https://github.com/kubernetes-sigs/kubespray/pull/9234), [@chadswen](https://github.com/chadswen))


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.19.1**, the newest release recorded here for this line.

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
