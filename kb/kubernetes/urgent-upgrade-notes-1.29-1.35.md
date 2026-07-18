---
id: CONCEPT-K8S_URGENT_UPGRADE_NOTES
type: concept
title: "Kubernetes Urgent Upgrade Notes 1.29→1.35 — the 'must read before you upgrade' items"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - urgent upgrade notes kubernetes
  - must read before upgrade k8s
  - keep-terminated-pod-volumes removed
  - pod-infra-container-image removed
  - cgroups v1 hard error kubeadm 1.35
  - kubeadm admin super-admin.conf
  - kubelet cloud-config removed
tags:
  - kubernetes
  - upgrade
  - breaking-changes
sources:
  - type: docs
    path: CHANGELOG/CHANGELOG-1.29.md … 1.35.md
    url: https://github.com/kubernetes/kubernetes/tree/master/CHANGELOG
    note: "the '### Urgent Upgrade Notes' sections of each release CHANGELOG (1.29–1.35)"
relations:
  - type: see_also
    target: CONCEPT-K8S_UPGRADE_SILENT_CHANGES
  - type: see_also
    target: PRACTICE-RUNBOOK_UPGRADE_ONE_MINOR
  - type: see_also
    target: CONCEPT-K8S_CGROUP_V1_REMOVAL
  - type: see_also
    target: CONCEPT-CLUSTER_PKI
---

# Kubernetes Urgent Upgrade Notes 1.29→1.35 — the "must read before you upgrade" items

## Summary

Each Kubernetes release CHANGELOG has an **"Urgent Upgrade Notes"** section — the changes that
**require action** before/when you upgrade or the cluster breaks. This curates them for **1.29–1.35**
(the Kubespray range), filtered to what affects a self-managed / Kubespray-style cluster. It complements
the silent-default list ([[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]]): those change behavior quietly, these
**demand an explicit action**. Feed both into the upgrade runbook ([[PRACTICE-RUNBOOK_UPGRADE_ONE_MINOR]]).

## Context

Cite: `CHANGELOG/CHANGELOG-1.XX.md`@master.

### 1.29
- **kubeadm splits `admin.conf` / `super-admin.conf`:** the `admin.conf` user is moved off the
  break-glass `system:masters` group to the new RBAC group **`kubeadm:cluster-admins`** (bound to
  `cluster-admin`); the RBAC-bypass `system:masters` identity now lives in a separate
  **`super-admin.conf`**. `kubeadm upgrade apply` migrates a node to the two-file setup; `join
  --control-plane` generates only the less-privileged `admin.conf`. **Action:** decide whether to keep
  `super-admin.conf` on the host or move it somewhere safe ([[CONCEPT-CLUSTER_PKI]]). (#121305)
- **`kubeadm upgrade plan --config` no longer accepts kube-proxy/kubelet component config** — the
  legacy plan-stage migration path was removed. (#120788)

### 1.30
- **No Urgent Upgrade Notes** in the v1.30.0 CHANGELOG.

### 1.31
- **kubelet `--keep-terminated-pod-volumes` removed** (deprecated since 2017): **remove it from
  kubelet args before upgrading** or **kubelet fails to start**. (#122082)
- **RecoverVolumeExpansionFailure (alpha) PVC cleanup:** if that gate is enabled, after upgrade you
  must **clear `status.allocatedResourceStatus`** on PVCs stuck at `ControllerResizeFailed` /
  `NodeResizeFailed`. (#126108)
- *(scheduler-plugin authors only)* `SchedulerQueueingHints` changes Pod-update requeue — implement a
  QueueingHint. Low impact for stock clusters. (#122234)

### 1.32
- **No urgent notes at GA.** Pre-release caveat still worth heeding: **`InPlacePodVerticalScaling`
  checkpoint format changed** — if you use in-place resize ([[CONCEPT-K8S_IN_PLACE_POD_RESIZE]]),
  **delete `/var/lib/kubelet/pod_status_manager_state`** when upgrading the kubelet, or kubelet fails
  to start on the incompatible state file. (#126620)

### 1.33
- **CSI `IsLikelyNotMountPoint` semantics [Action Required]:** CSI driver authors must not treat
  `false` as "is a mount point"; audit driver handling. (#129370)
- **kube-proxy nftables kernel-check env var fixed:** `KUBE_PROXY_NFTABLES_SKIP_KERNEL_VERSION_CHECK`
  now skips the check only when set to a **non-empty** value. (#130401)
- **`ReduceDefaultCrashLoopBackOffDecay` (opt-in)** lowers CrashLoopBackOff to 1s/60s; review
  interaction with `KubeletCrashLoopBackOffMax`. (#130711)
- *(scheduler-plugin authors only)* action-type rename `UpdatePodTolerations`→`UpdatePodToleration`. (#129023)

### 1.34
- **apiserver/etcd metric label overhaul (monitoring break):** many apiserver / watch-cache / storage /
  etcd metrics change labels — e.g. `etcd_request_duration_seconds` swaps `type`→`resource`+`group`;
  `apiserver_cache_list_*` swap `resource_prefix`→`group`+`resource`; `apiserver_watch_events_*` swap
  `kind`→`resource`. **Action:** update dashboards / alerts / recording rules. (#131845)
- **kubelet `--cloud-config` flag removed** — remove it from kubelet args before upgrading. (#130161)
- **Static pods referencing API objects are now rejected by the kubelet** (secrets/configmaps/SA
  tokens) — they no longer silently run after mirror-pod creation fails. **Action:** audit static-pod
  manifests that depend on API objects. (#131837)
- *(scheduler-plugin authors only)* PreFilter plugins now receive the `NodeInfo` list — update the
  signature. (#130720)

### 1.35
- **kubelet `--pod-infra-container-image` flag removed [ACTION REQUIRED]:** remove it from kubelet
  config/extraArgs before upgrading kubelet or **startup fails**. kubeadm does **not** remove it if it
  was passed as an extra kubelet arg. (#133779)
- **cgroups v1 is now a HARD ERROR on kubeadm/kubelet 1.35+ [ACTION REQUIRED]:** the SystemVerification
  preflight **errors** (not warns) when cgroups v1 is detected with kubelet ≥1.35. To keep running
  cgroups v1: ignore the SystemVerification preflight error **and** set **`failCgroupV1: false`** in the
  `kube-system/kubelet-config` ConfigMap before upgrading. The real fix is to migrate nodes to
  **cgroup v2** ([[CONCEPT-K8S_CGROUP_V1_REMOVAL]]). (#134744)

**How to use.** For each minor you cross, do the listed **action** first (remove the flag, delete the
state file, migrate cgroups, update dashboards). The kubelet-flag removals (1.31/1.34/1.35) are the
classic "kubelet won't start after upgrade" cause — check your Kubespray `kubelet_*_extra_args` /
inventory for the removed flags before upgrading.

## References

- Kubernetes `CHANGELOG/CHANGELOG-1.{29..35}.md` "Urgent Upgrade Notes" (@master). Silent changes
  [[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]]; upgrade runbook [[PRACTICE-RUNBOOK_UPGRADE_ONE_MINOR]]; cgroup
  v1 [[CONCEPT-K8S_CGROUP_V1_REMOVAL]]; PKI [[CONCEPT-CLUSTER_PKI]]; in-place resize
  [[CONCEPT-K8S_IN_PLACE_POD_RESIZE]].
