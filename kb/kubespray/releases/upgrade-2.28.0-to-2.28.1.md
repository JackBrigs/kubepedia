---
id: UPGRADE-V2_28_0__V2_28_1
type: upgrade
title: "Upgrade report v2.28.0 → v2.28.1"
status: active
kubespray_version: ">=v2.28.0 <=v2.28.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-21"
confidence: confirmed
aliases:
  - v2.28.0 to v2.28.1
  - upgrade 2.28.0 2.28.1
tags:
  - upgrade
  - change-report
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main
    url: https://github.com/kubernetes-sigs/kubespray/compare/v2.28.0...v2.28.1
    note: "version deltas verified from tag code; changes from release notes"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.28.1/roles/kubespray_defaults/defaults/main/main.yml
    note: "adds kubeadm_upgrade_node_phases_skip (inherits kubeadm_init_phases_skip on k8s >= 1.32)"
  - type: code
    path: roles/network_plugin/cilium/tasks/apply.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.28.1/roles/network_plugin/cilium/tasks/apply.yml
    note: "v2.28.1 introduces the 'cilium version' probe and install|upgrade branch (v2.28.0 always ran install)"
relations:
  - type: see_also
    target: RELEASE-V2_28_1
  - type: see_also
    target: CONCEPT-COMPONENT_VERSION_SELECTION
---

# Upgrade report v2.28.0 → v2.28.1

## Summary

A **patch** upgrade in numbering only. The component deltas are small and stay on Kubernetes
1.32, but this tag also changes **how** two things are managed — Cilium gains an upgrade path
and Argo CD moves to checksum-driven versioning — and adds a new kubeadm phase-skip variable.
Read it as a behaviour change, not just bug fixes.

## Implementation

Version deltas:

| Item | v2.28.0 | v2.28.1 |
|------|-------|------|
| Kubernetes default | 1.32.5 | 1.32.8 |
| etcd | 3.5.16 | 3.5.22 |
| containerd | 2.0.5 | 2.0.6 |
| cilium | 1.17.3 | **1.17.7** |
| calico | 3.29.3 | 3.29.5 |

Mechanism changes in the same tag (from the tag-to-tag diff, not the release notes):

- **etcd version stops being a hard-coded map.** `etcd_supported_versions` for 1.30/1.31/1.32
  changes from the literal `3.5.16` to a computed
  `(etcd_binary_checksums['amd64'].keys() | select('version', '3.6', '<'))[0]` — i.e. the newest
  pre-3.6 etcd in the checksum table. That is where `3.5.22` comes from; future checksum additions
  move it again without a variable change ([[CONCEPT-COMPONENT_VERSION_SELECTION]]).
- **Cilium gains an upgrade path.** `tasks/apply.yml` starts probing `cilium version` and choosing
  `install` vs `upgrade`; before this tag it always ran `cilium install`. A one-shot cleanup for
  manifest-era objects (`tasks/remove_old_resources.yml`, `cilium_remove_old_resources`, default
  `false`) is added too — details in [[UPGRADE-CILIUM_1_15_TO_1_19]].
- **Argo CD versioning moves to the shared download machinery:** `argocd_install_url` leaves the
  role defaults and `argocd_version` becomes the first key of `argocd_install_checksums.no_arch`
  ([[UPGRADE-ARGOCD_2_11_TO_2_14]]).
- **New variable `kubeadm_upgrade_node_phases_skip`** (`kubespray_defaults/defaults/main/main.yml`):
  phases skipped when upgrading a **secondary** control-plane node; on Kubernetes ≥ 1.32 it
  additionally inherits `kubeadm_init_phases_skip`.

## Upgrade Notes

- Same Kubernetes 1.32 line — no API removals, no kubelet/kubeadm minor jump.
- Fixes: Cilium install/templating & `loadBalancer.mode`, Cilium BGP control-plane, calico BGP,
  external etcd member removal.
- **If you run Cilium**, this is the tag where re-running Kubespray stops re-installing and starts
  upgrading the release. Verify the release state before the run.
- **If you run Argo CD**, an inventory pin of `argocd_version` now needs a matching checksum entry.

## Service impact

A patch upgrade is still a rolling restart of the cluster, not a config-only change.

- `upgrade-cluster.yml` processes the control plane with `serial: 1` and nodes with
  `serial: 20%`, draining and rebooting per its own settings — so the API stays available on an HA
  control plane, and workloads move as nodes are drained
  ([[PRACTICE-RUNBOOK_UPGRADE_ONE_MINOR]]).
- The kubelet/kubeadm patch bump restarts kubelet and the control-plane static pods node by node;
  etcd 3.5.16 → 3.5.22 restarts etcd members one at a time.
- containerd 2.0.5 → 2.0.6 restarts the runtime on each node (`Restart containerd`): the node is
  briefly `NotReady`, running containers survive.
- **Cilium 1.17.3 → 1.17.7 restarts the agent DaemonSet.** Datapath disruption on a Cilium upgrade
  is real but brief per node; the role waits for all `k8s-app=cilium` pods to be ready before
  continuing.
- Take an etcd snapshot first ([[PRACTICE-ETCD_BACKUP_RESTORE]]) — a patch tag is not a reason to
  skip it.

## Compatibility

- Kubernetes stays on 1.32.
- One Kubespray minor at a time ([[UPGRADE-KUBESPRAY_SEQUENTIAL]]).

## References

- Diff `v2.28.0...v2.28.1` read directly at the tags:
  `roles/kubespray_defaults/defaults/main/download.yml` (cilium 1.17.3→1.17.7, computed
  `etcd_supported_versions`, argocd download entry), `…/defaults/main/main.yml`
  (`kubeadm_upgrade_node_phases_skip`), `roles/network_plugin/cilium/tasks/apply.yml` +
  `remove_old_resources.yml`, `roles/kubernetes-apps/argocd/defaults/main.yml`.
  Per-tag components: [[RELEASE-V2_28_1]].
