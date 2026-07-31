---
id: TROUBLE-KUBESPRAY_BREAKING_CHANGES
type: troubleshooting
title: "kubespray: declared breaking changes by release"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.1.0 <=2.31.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubespray breaking changes
  - kubespray upgrade broke
  - kubespray action required upgrade
  - what breaks upgrading kubespray
tags:
  - upgrade
  - breaking-change
  - kubespray
sources:
  - type: docs
    path: kubernetes-sigs/kubespray release notes — entries marked breaking / action required
    url: https://github.com/kubernetes-sigs/kubespray/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubespray: declared breaking changes by release

## Summary

**29 behaviour changes** the project itself marked as breaking or action-required, across
10 releases from 2.1.0 to 2.31.0. These are not defects: they work as designed and still break
a configuration that worked yesterday. An upgrade crossing any of them needs a decision, not just a
rollout.

## Problem

The upgrade itself usually succeeds. The damage shows up afterwards — a setting silently ignored, a
default flipped, an API version withdrawn, a variable that must now be set explicitly.

## Context

### 2.1.0

- Only systemd based Linux OS distributions supported from now on
- Requires users to sync `groups_vars/all.yaml`

### 2.1.1

- Support for etcd3 backend for kube-apiserver. (Note that existing installs will not auto-upgrade.)
- docker_dns mode is now the default. Hosts cannot resolve pod network domains with this configuration, but it is less vulnerable to outside changes to host /etc/resolv.conf
- kube-apiserver now listens on port 6443 by default
- This release works only with Ansible version 2.2.1.0. All other versions are unsupported
- This release only works with Jinja2 version >=2.8. Earlier versions will have issues rendering templates

### 2.1.2

- Versions of Docker above 1.13.x do not work. As a result, newer CoreOS releases will not work

### 2.15.0

- users that relies on the default value of calico_datastore needs to explicitly configure their datastore choice

### 2.25.0

- BREAKING CHANGE: This script is introduced to facilitate living documentation and its administration. This leads to a restructuring in the documentation at https://kubespray.io/#/ to simplify the automatic creation of links, as the structure in the sidebar changes. (#11128, @Payback159)

### 2.27.0

- Change `kubeadm_patches` format to use an array of inline patch instead of patch files. See [the example](roles/kubernetes/kubeadm_common/defaults/main.yml) for new format. (#11521, @VannTen)
- Removes the generation of static tokens for every node in the cluster when `kube_token_auth: true` (#11567, @VannTen)
- The `kubelet_node_{config_extra_args,custom_flags}` are removed. Use `kubelet_{config_extra_args,custom_flags}` in `<your_inventory>/group_vars/kube_node.yml`. The `{kube,system}_master_{cpu,memory,ephemeral-storage,pid}` are removed. Use the `{kube,system}_{cpu,memory,ephemeral-storage,pid}` variables in `<your_inventory>/group_vars/kube_control_plane.yml. `kubelet_custom_flags` can no longer be a string, an array is required. (#10643, @VannTen)
- `k8s_cluster` group is now automatically defined, it can be removed from your inventory if you're not using it for group_vars (#11559, @VannTen)
- `kubeadm_ignore_preflight_errors` is introduced to ignore specific preflight checks from kubeadm. The previous was effectively `all`, so some errors might surface during upgrade, in which cases, users should add the ones they choose to ignore to that variable. (#11710, @VannTen)
- Running kubespray with --limit without cached facts is no longer supported. Improves the scaling for large clusters. (#11598, @VannTen)

### 2.28.0

- Krew installation support is removed (#11824, @VannTen)
- You should remove the leading 'v' of all explicit version of components deployed by kubespray (most notably `kube_version`) (#11890, @VannTen)
- `etcd_kubeadm_enabled` (was deprecated) is removed. You should remove it from your inventory (#11901, @VannTen) `gateway_api_experimental_channel` is deprecated, please use `gateway_api_channel` and set `experimental`. (#11763, @tico88612)

### 2.29.0

- /etc/hosts/ is no longer populated with all cluster nodes (#12382, @VannTen)
- Add support for `coredns_affinity` to change affinity of coredns deployments, defaulting to the upstream coredns deployment's one. The `coredns` deployment's node affinity has been removed, so the `coredns` pods will no longer be scheduled into control-planes by default. (#11994, @HoKim98)
- Remove support for weave network plugin (#12230, @anshuman-agarwala)
- The tag 'master' is removed, replaced by the tag 'control-plane' (#12228, @VannTen)
- `conntrack_modules` is removed; the list of conntrack modules to try to load is instead hardcoded, since there is no reason to have any other values. (#12475, @VannTen)
- drop support for cri-o on ubuntu20. (#12233, @VannTen)

### 2.30.0

- `containerd_discard_unpacked_layers` is now applied only for containerd < 2.1 to avoid warnings with the Transfer Service used in newer versions. (#12821, @guoard) Cilium `k8sServiceHost` and `k8sServicePort` are now derived from `kube_apiserver_global_endpoint` instead of being auto-detected, so users must ensure this endpoint is correctly set and reachable from all nodes. (#12624, @r3m8)

### 2.31.0

- Make kubernetes v1.35 default. cgroup V1 is no longer supported upstream by default, and must be enabled with `kubelet_fail_cgroup_v1: false`. (#12812, @mzaian)
- Support for ingress-nginx ingress controller is removed, as the project has been retired by upstream (#12767, @jmeza-xyz)
- The Kubernetes Dashboard addon has been removed from Kubespray because the upstream project is being archived and is no longer maintained. The configuration `dashboard_enabled: true` is no longer supported. (#12858, @neo502721) Adds automated validation role to detect removed variables at playbook start. Playbooks will abort on `removed vars`. Users must migrate away from the listed removed variables to avoid playbook failures. (#12942, @Srishti-j18) Replace ssh_bastion_confing__name with ssh_bastion_config_name (#13046, @scolley31)


## Diagnostics

```bash
# which version is actually deployed
kubectl get nodes -o wide
helm list -A
```

Cross the list above against the range you are moving through, not only the target version.

## Known Issues

Entries are verbatim from upstream release notes and filtered mechanically: lines shorter than
45 characters and duplicates are dropped, because section headings and list fragments reach the
extractor looking like entries. If a release you care about appears empty here, read its notes
upstream before concluding that nothing changed.

## References

- Upstream releases of `kubernetes-sigs/kubespray`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/kubespray.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
