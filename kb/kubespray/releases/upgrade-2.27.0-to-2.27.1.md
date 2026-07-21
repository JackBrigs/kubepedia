---
id: UPGRADE-V2_27_0__V2_27_1
type: upgrade
title: "Upgrade report v2.27.0 → v2.27.1"
status: active
kubespray_version: ">=v2.27.0 <=v2.27.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-21"
confidence: confirmed
aliases:
  - v2.27.0 to v2.27.1
  - upgrade 2.27.0 2.27.1
tags:
  - upgrade
  - change-report
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main
    url: https://github.com/kubernetes-sigs/kubespray/compare/v2.27.0...v2.27.1
    note: "version deltas verified from tag code; changes from release notes"
  - type: code
    path: roles/kubernetes/control-plane/tasks/kubeadm-upgrade.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.27.1/roles/kubernetes/control-plane/tasks/kubeadm-upgrade.yml
    note: "v2.27.1 changes secondary control-plane nodes from 'kubeadm upgrade apply --force' to 'kubeadm upgrade node' and switches to --config (v1beta4 UpgradeConfiguration)"
relations:
  - type: see_also
    target: RELEASE-V2_27_1
  - type: see_also
    target: CONCEPT-COMPONENT_VERSION_SELECTION
---

# Upgrade report v2.27.0 → v2.27.1

## Summary

A **patch** upgrade on the Kubernetes 1.31 line, but it carries one change that matters more
than the version bumps: **how secondary control-plane nodes are upgraded**. Before this tag
Kubespray ran `kubeadm upgrade apply` on *every* control-plane node; v2.27.1 runs
`kubeadm upgrade node` on the non-first ones and switches the whole path to a `--config`-driven
kubeadm v1beta4 `UpgradeConfiguration`.

## Implementation

Version deltas:

| Item | v2.27.0 | v2.27.1 |
|------|-------|------|
| Kubernetes default | 1.31.4 | 1.31.9 |
| containerd | 1.7.24 | 1.7.27 |
| calico | 3.29.1 | 3.29.4 |
| runc | 1.2.3 | **1.2.6** |
| cni-plugins | 1.4.0 | 1.4.1 |
| cri-dockerd | 0.3.11 | 0.3.16 |
| cilium CLI | 0.16.0 | 0.16.24 |
| ingress-nginx | 1.12.0 | 1.12.1 |

Behaviour changes in the same tag (from the tag-to-tag diff):

- **Secondary control-plane upgrade is corrected.** In
  `roles/kubernetes/control-plane/tasks/kubeadm-upgrade.yml`, "Upgrade other control plane nodes"
  changes from `kubeadm upgrade apply -y {{ kube_version }} --force` to **`kubeadm upgrade node`**
  — the command kubeadm actually intends for non-first control-plane nodes.
- **kubeadm v1beta4 `UpgradeConfiguration`.** When `kubeadm_config_api_version` is not `v1beta3`,
  both upgrade commands stop passing individual flags (`--certificate-renewal`,
  `--ignore-preflight-errors`, `--etcd-upgrade`, `--allow-experimental-upgrades`, `--force`,
  `--patches`) and take `--config={{ kube_config_dir }}/kubeadm-config.yaml` instead. Anything you
  used to influence through those flags now has to be expressed in the generated config.
- **API-readiness check extracted** to `tasks/check-api.yml` and imported before the upgrade; the
  `retries: 3` retry loop around `kubeadm upgrade apply` is dropped.
- **New sample inventory file** `group_vars/k8s_cluster/kube_control_plane.yml` with commented
  control-plane reservations (`kube_memory_reserved`, `system_cpu_reserved`, …) — a place to put
  reservations, not a default change.
- `external_cloud_provider` accepts a new value **`manual`**, which installs no cloud-controller
  manager ([[CONCEPT-CLOUD_CONTROLLER_MANAGER]]).

## Upgrade Notes

- Same Kubernetes 1.31 line — no API removals, no kubelet/kubeadm minor jump.
- Fixes: control-plane reconfiguration on upgrades, kubeadm v1beta4 `UpgradeConfiguration`, calico
  RBAC.
- **If you carry custom kubeadm upgrade flags via inventory**, re-check them: on v1beta4 they are
  ignored in favour of the generated config.
- Snapshot etcd first ([[PRACTICE-UPGRADE_PREFLIGHT]], [[PRACTICE-ETCD_BACKUP_RESTORE]]).

## Service impact

Rolling, one control-plane node at a time — but not free.

- `upgrade-cluster.yml` runs the control plane with `serial: 1` and nodes with `serial: 20%`, so on
  an HA control plane the API stays available; on a single control-plane node the API is down for
  the duration of its upgrade.
- Each control-plane node restarts its static pods; each worker restarts kubelet and, because
  containerd (1.7.24 → 1.7.27) and runc (1.2.3 → 1.2.6) change, the container runtime is restarted
  as well — the node is briefly `NotReady`, running containers survive the restart.
- calico 3.29.1 → 3.29.4 rolls the CNI DaemonSet node by node — brief per-node datapath
  disruption.
- The `kubeadm upgrade apply` → `upgrade node` correction makes secondary control-plane nodes do
  **less** work than before, which is the safer behaviour; do not expect the old (incorrect)
  behaviour to be reproducible.

## Compatibility

- Kubernetes stays on 1.31.
- One Kubespray minor at a time ([[UPGRADE-KUBESPRAY_SEQUENTIAL]]).

## References

- Diff `v2.27.0...v2.27.1` read directly at the tags:
  `roles/kubernetes/control-plane/tasks/kubeadm-upgrade.yml` (+ `check-api.yml`),
  `roles/kubespray-defaults/defaults/main/download.yml` (component pins),
  `…/defaults/main/main.yml` (`kube_version`, `external_cloud_provider: manual`),
  `inventory/sample/group_vars/k8s_cluster/kube_control_plane.yml`.
  Per-tag components: [[RELEASE-V2_27_1]].
