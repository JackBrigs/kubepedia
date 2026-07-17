---
id: CONCEPT-K8S_UPGRADE_SILENT_CHANGES
type: concept
title: "Silent behavior changes on Kubernetes upgrade 1.29→1.35 (feature-gate GAs, default flips, deprecations)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - silent default changes kubernetes upgrade
  - feature gates that went GA 1.29 1.30 1.31 1.32 1.33 1.34 1.35
  - what changes on kubernetes upgrade
  - kubeproxyversion field removed
  - service account secret token removed
  - nftables kube-proxy
  - in-place pod resize default
tags:
  - kubernetes
  - upgrade
  - feature-gates
  - breaking-changes
sources:
  - type: code
    path: keps/
    url: https://github.com/kubernetes/enhancements/tree/master/keps
    note: "per-KEP kep.yaml milestone (alpha/beta/stable) blocks read at master; stage transitions inside 1.29–1.35"
relations:
  - type: see_also
    target: CONCEPT-K8S_FEATURE_GATES
  - type: see_also
    target: CONCEPT-K8S_API_REMOVALS
  - type: see_also
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
  - type: see_also
    target: CONCEPT-K8S_KEPS
  - type: see_also
    target: PRACTICE-RUNBOOK_UPGRADE_ONE_MINOR
  - type: see_also
    target: CONCEPT-KUBE_PROXY
---

# Silent behavior changes on Kubernetes upgrade 1.29→1.35 (feature-gate GAs, default flips, deprecations)

## Summary

The dangerous upgrade changes are the ones that alter behavior **without any config edit** — a
feature gate reaching GA (locked on), a beta gate flipping on-by-default, or a field that stops being
populated. This is the per-version "watch list" for moving a Kubespray cluster across **K8s
1.29→1.35** (the range Kubespray v2.27.0–v2.31.0 supports), derived from each KEP's own `kep.yaml`
milestone block. It feeds the upgrade runbook ([[PRACTICE-RUNBOOK_UPGRADE_ONE_MINOR]]) and the
feature-gate/API-removal references ([[CONCEPT-K8S_FEATURE_GATES]], [[CONCEPT-K8S_API_REMOVALS]]).

## Context

**Read this per minor you cross.** Each bullet is a change that takes effect on the version shown even
if you touch nothing. Cite: `keps/sig-<area>/<n>-<slug>`@master.

### 1.29
- **NodePort** allocation now avoids the reserved static subrange (`ServiceNodePortStaticSubrange` GA)
  — fewer port conflicts. `keps/sig-network/3668-...`
- **KMS v2** encryption-at-rest GA; **KMS v1 deprecated** — migrate encryption providers.
  `keps/sig-auth/3299-...`
- **Native sidecars** on by default (`SidecarContainers`) — `initContainers` with
  `restartPolicy: Always` change startup/shutdown ordering. `keps/sig-node/753-...`
- **Taint-based eviction** moves to a separate controller (`SeparateTaintEvictionController` on).
  `keps/sig-scheduling/3902-...`
- New pod condition `PodReadyToStartContainers` on by default — automation keying on conditions may
  need updating. `keps/sig-node/3085-...`
- `ReadWriteOncePod` PV access mode GA; CRD CEL validation (`x-kubernetes-validations`) GA.
  `keps/sig-storage/2485-...`, `keps/sig-api-machinery/2876-...`

### 1.30
- **No Secret-based ServiceAccount tokens** — auto-generated SA token Secrets stop being created and
  unused legacy ones are auto-purged (`LegacyServiceAccountTokenCleanUp` GA). Tooling expecting a
  Secret per SA **breaks**. `keps/sig-auth/2799-...`
- **Structured authn/authz** config files on by default (`--authentication-config` /
  `--authorization-config`). `keps/sig-auth/3331-...`, `keps/sig-auth/3221-...`
- `ValidatingAdmissionPolicy` (in-tree CEL admission) GA; webhook `matchConditions` GA; aggregated
  discovery GA. `keps/sig-api-machinery/3488-...`
- `PodHostIPs` GA; kubelet volume-reconstruction-after-restart GA. `keps/sig-node/...`, `keps/sig-storage/3756-...`

### 1.31
- **MultiCIDRServiceAllocator** on by default — Service IP allocation moves to `ServiceCIDR`/
  `IPAddress` objects. `keps/sig-network/1880-...`
- **kube-proxy drains terminating/not-ready nodes** from LB traffic (GA) — fewer dropped connections
  during rollouts. `keps/sig-network/3836-...`
- **AppArmor API GA** — `securityContext.appArmorProfile`; **annotations deprecated**.
  `keps/sig-node/24-apparmor`
- `HonorPVReclaimPolicy` on by default (fixes PV/PVC delete-order storage leaks);
  `ConsistentListFromCache` on by default (LISTs from watch cache, lower etcd load).
  `keps/sig-storage/2644-...`, `keps/sig-api-machinery/2340-...`

### 1.32
- **StatefulSet PVCs can auto-delete** (`StatefulSetAutoDeletePVC` GA) via
  `persistentVolumeClaimRetentionPolicy` — a **data-lifecycle** change; audit before upgrading
  stateful workloads. `keps/sig-apps/1847-...`
- **kubectl `apply` uses server-side apply by default** — field-manager/conflict behavior changes for
  scripts. `keps/sig-cli/3805-ssa-default`
- `LoadBalancerIPMode` GA (VIP vs Proxy); `WatchList` on by default (streaming informers, lower
  apiserver memory); scheduler `QueueingHints` on by default; structured authorization GA.
  `keps/sig-network/1860-...`, `keps/sig-api-machinery/3157-...`, `keps/sig-scheduling/4247-...`

### 1.33
- **`status.nodeInfo.kubeProxyVersion` stops being populated** (`DisableNodeKubeProxyVersion` on) —
  tooling reading that node field breaks. `keps/sig-network/4004-...`
- **nftables kube-proxy backend GA** (`--proxy-mode=nftables`) — not default, but the recommended
  path off iptables at scale ([[CONCEPT-KUBE_PROXY]]). `keps/sig-network/3866-...`
- **In-place pod resize on by default** (`InPlacePodVerticalScaling`) — kubelet honors live
  `resources` changes via the `resize` subresource. `keps/sig-node/1287-...`
- **gitRepo volumes disabled by default** (`GitRepoVolumeDriver` off) — long-deprecated; manifests
  using gitRepo **break**. `keps/sig-storage/5040-...`
- `ServiceTrafficDistribution` / Topology Aware Routing GA; `CRDValidationRatcheting` GA;
  `SidecarContainers` GA; `RecursiveReadOnlyMounts` GA. `keps/sig-network/4444-...`, `keps/sig-api-machinery/4008-...`

### 1.34
- **DRA (structured parameters) GA** (`DynamicResourceAllocation`) — the modern GPU/device allocation
  API; needs DRA drivers. `keps/sig-node/4381-...`
- **Node swap GA** (`NodeSwap`, cgroup v2, Burstable pods) — changes memory-pressure behavior; decide
  a swap policy. `keps/sig-node/2400-...`
- **kubelet auto-detects cgroup driver from CRI** (`KubeletCgroupDriverFromCRI` GA) — manual
  `cgroupDriver` alignment becomes unnecessary (Kubespray sets it explicitly today). `keps/sig-node/4033-...`
- **Node authorizer tightened** via selectors (`AuthorizeNodeWithSelectors` GA) — custom controllers
  using node credentials may lose access. `keps/sig-auth/4601-...`
- Anonymous auth restrictable to specific endpoints GA; ordered namespace deletion (pods first) GA;
  PSA blocks host fields in probes GA (manifests may newly fail admission). `keps/sig-auth/4633-...`,
  `keps/sig-api-machinery/5080-...`, `keps/sig-auth/4940-...`
- **Policy shift (KEP 5241):** from ~1.34 new **beta** feature gates default **off** — fewer
  silent-on features after upgrade going forward. `keps/sig-architecture/5241-...`

### 1.35
- **In-place pod resize GA** (`InPlacePodVerticalScaling`). `keps/sig-node/1287-...`
- **cgroup v1 removal underway** — `RemoveCgroupV1` beta; cgroup v1 was in maintenance mode since
  1.31. Migrate nodes to **cgroup v2** ([[PRACTICE-CGROUPS]]). `keps/sig-node/5573-...`, `keps/sig-node/4569-...`
- kubelet **drop-in config dir** (`--config-dir`) GA — relevant to config management;
  `maxParallelImagePulls`, `imageMaximumGCAge` GA; `SupplementalGroupsPolicy` GA (Strict drops
  implicit image groups). `keps/sig-node/3983-...`, `keps/sig-node/3619-...`

### Deprecations / removals landing in range (need action)
- `kubeProxyVersion` node field (1.33); Secret-based SA tokens (1.30); KMS v1 (dep. 1.29); AppArmor
  annotations (1.31); gitRepo volumes (1.33 off); **in-tree cloud providers** removal completing
  in-range (needs external cloud-controller-manager) `keps/sig-cloud-provider/2395-...`; in-tree
  **Portworx**→CSI migration on/GA in-range (needs Portworx CSI driver) `keps/sig-storage/2589-...`.
- **Stricter validation that can reject previously-valid input:** `StrictIPCIDRValidation`
  (leading-zero/malformed IPs, alpha 1.33) `keps/sig-network/4858-...`; PSA host-field-in-probes
  (GA 1.34).

**Caveat.** Stages are from each KEP's `kep.yaml` milestone block (intended graduation). For a beta
gate that shipped **off** by default (increasingly common after KEP 5241 from 1.34), treat "on by
default" as unverified until confirmed against that release's `kube_features.go` — see
[[CONCEPT-K8S_FEATURE_GATES]] for the authoritative per-release gate state.

## References

- `kubernetes/enhancements` `keps/sig-*/<n>-<slug>/kep.yaml` milestone blocks (@master). Feature-gate
  detail [[CONCEPT-K8S_FEATURE_GATES]]; API removals [[CONCEPT-K8S_API_REMOVALS]]; version support
  [[CONCEPT-KUBERNETES_VERSION_SUPPORT]]; KEP index [[CONCEPT-K8S_KEPS]]; upgrade runbook
  [[PRACTICE-RUNBOOK_UPGRADE_ONE_MINOR]]; cgroups [[PRACTICE-CGROUPS]]; kube-proxy [[CONCEPT-KUBE_PROXY]].
