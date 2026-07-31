---
id: TROUBLE-KUBESPRAY_2_28_DEFECTS
type: troubleshooting
title: "kubespray 2.28: defects fixed in the 2.28 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.28.0 <2.29.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubespray 2.28 known issues
  - kubespray 2.28 fixed in
  - is this kubespray bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubespray
sources:
  - type: docs
    path: kubernetes-sigs/kubespray release notes for the 2.28 line — bug-fix entries
    url: https://github.com/kubernetes-sigs/kubespray/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubespray 2.28: defects fixed in the 2.28 line

## Summary

**31 defects** the project fixed across **2 releases** of the 2.28 line, from 2.28.0 to
2.28.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.28.0

- Fix cilium network plugin config issue deploying cilium 1.17 (#11986, @pedro-peter)
- Network: Fix calico-kube-controller can't list the tiers resources (#12169, @cyclinder)
- Fix documentation for offline usage by adding the 'v' prefix in download urls (#12166, @tmurakam)
- Fix path to facts.yml in node facts refresh section (#12177, @guoard)
- Fix sample inventory for the reserved resource (#11895, @anshuman-agarwala)
- Fix CI by exclude the `.ansible` in `.ansible-lint` Remove `ctr image pull` workaround for nerdctl (#11948, @yankay)
- Fix a bug where `kubeadm_certificate_key` was not defined if control plane nodes were not in correct order (#11875, @Xartos)
- Fix a bug where custom TCP/UDP ports were not exposed by the ingress-nginx-controller container and service. (#11850, @commx)
- Fix broken calico Typha template when using both `calico_ipam_host_local` and `typha_secure` (#11917, @c-romeo)
- Fix broken dhclient hooks when using resolvconf (#11946, @kyrbrbik)
- Fix control plane pods deletion with proper shell quoting (#11943, @iptizer)
- Fix coredns deployment with `coredns_pod_disruption_budget: true` or `enable_nodelocaldns_secondary` (#11952, @RaulButuc)
- Fix hubble-ui deployment to not renders tls volume when the `cilium_hubble_tls_generate` option not configured. (#12143, @atobaum)
- Fix scale.yml problems with cached IP facts (#12020, @0ekk)
- Fix: Using the ./manage-offline-container-images.sh register command does not create a new container but registers the image in the existing container registry. (#11964, @DearJey)
- Fix: arm64 checksums for youki and kata-containers (#12173, @ErikJiang)
- Fix: missing 'v' prefix in offline image tags (#12086, @ErikJiang)
- Fix: prevent kubeadm to override coredns configuration/deployment on upgrade (#12028, @sathieu)
- Fixed an issue where the second and subsequent parameters in `kubelet_cpu_manager_policy_options` were ignored due to incorrect indentation. (#12123, @HoKim98)
- Fixed kube-vip to use `kube-vip/kube-vip-iptables` image instead of `kube-vip/kube-vip` when `lb_fwdmethod` or `kube_vip_lb_fwdmethod` is set to `masquerade` (#12145, @aviral-agarwal)
- [calico] Fix kubecontrollersconfigurations list permission (#12035, @darkobas2)

### 2.28.1

- Fix Cilium installation issues (caused by templating syntax errors) when certain non-default features (encryption, etc.) are enabled (#12283, @k8s-infra-cherrypick-robot)
- Fix Hubble-Relay peer discovery in clusters using non-default cluster name by properly configuring clusterDomain in Cilium Helm values (#12374, @k8s-infra-cherrypick-robot)
- Fix cilium installation role to render cilium_config_extra_vars into helm values (#12338, @k8s-infra-cherrypick-robot)
- Fix invalid PodSecurity admission configuration when `kube_pod_security_use_default: false` (#12478, @k8s-infra-cherrypick-robot)
- Fix the Cilium cluster, which is upgraded from 2.27 to 2.28 will break Fix helm release re-use message when installing repeatedly (#12324, @k8s-infra-cherrypick-robot)
- Fix the issue of etcd node addition failure caused by incorrect ETCD_INITIAL_CLUSTER configuration. (#12352, @k8s-infra-cherrypick-robot)
- Fix(kubeadm): Conditionally add --skip-phases flag for v1.32.0+ (#12354, @k8s-infra-cherrypick-robot)
- Fix: When running `./manage-offline-container-images.sh register` with using Podman, getting the image_id fails and the script is interrupted. (#12316, @k8s-infra-cherrypick-robot)
- Fixed cilium_enable_bgp_control_plane config (#12432, @k8s-infra-cherrypick-robot)
- Fixes a syntax error that made the '_bgp_config' an 'AnsibleUnsafeText' instead of a 'dict', which caused the "Calico | Process BGP Configuration" step to fail (#12394, @k8s-infra-cherrypick-robot)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.28.1**, the newest release recorded here for this line.

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
