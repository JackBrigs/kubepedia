---
id: PRACTICE-RUNBOOK_CNI_MIGRATION
type: best_practice
title: "Runbook: change the CNI plugin on a running cluster"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - cni migration runbook
  - switch cni plugin
  - calico to cilium migration
  - change kube_network_plugin
  - replace cni on running cluster
  - flannel to calico
tags:
  - runbook
  - operations
  - cni
  - networking
sources:
  - type: docs
    path: docs/CNI/cni.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/CNI/cni.md
    note: "kube_network_plugin selection; Kubespray has no in-place CNI-swap playbook"
  - type: code
    path: roles/network_plugin
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/roles/network_plugin
    note: "per-plugin subroles applied by kube_network_plugin; no removal/uninstall of the previous CNI"
relations:
  - type: part_of
    target: CONCEPT-RUNBOOKS_INDEX
  - type: depends_on
    target: VARIABLE-KUBE_NETWORK_PLUGIN
  - type: see_also
    target: ROLE-NETWORK_PLUGIN
  - type: see_also
    target: TROUBLE-KUBELET_NODE_NOTREADY_CNI
  - type: see_also
    target: PRACTICE-NETCHECK
  - type: see_also
    target: PRACTICE-ETCD_BACKUP_RESTORE
---

# Runbook: change the CNI plugin on a running cluster

## Summary

The procedure to move a cluster from one CNI to another (e.g. **Calico → Cilium**, Flannel → Calico).
The hard truth up front: **Kubespray has no in-place CNI-migration playbook** — changing
[[VARIABLE-KUBE_NETWORK_PLUGIN]] and re-running deploys the *new* plugin but does **not** cleanly
remove the old one, and two CNIs fighting over `/etc/cni/net.d` and iptables/eBPF state is an
outage. Treat this as a **disruptive** operation with a maintenance window. Follow the
[[CONCEPT-RUNBOOKS_INDEX]] spine; because a CNI swap is **not cleanly reversible in place**, the
rebuild path below is the safer default.

## Context

- **Two strategies:**
  - **Blue-green rebuild (recommended):** stand up a new cluster (or new node pool) with the target
    `kube_network_plugin`, migrate workloads, retire the old. No dual-CNI state; predictable rollback
    (keep the old cluster until cutover is verified).
  - **In-place (accept an outage):** change the variable, purge the old CNI, re-run — only when a
    rebuild is impossible. Pods have **no network** between teardown and the new CNI converging.
- **What Kubespray does / doesn't:** the `network_plugin` role ([[ROLE-NETWORK_PLUGIN]]) applies the
  subrole selected by `kube_network_plugin` ([[COMPONENT-CALICO]], [[COMPONENT-CILIUM]],
  [[COMPONENT-FLANNEL]], …). It does **not** uninstall the previous plugin's DaemonSet, CRDs,
  `/etc/cni/net.d/*.conflist`, or dataplane state — you remove those by hand.
- **Encapsulation / CIDR:** the new CNI must agree with the cluster's existing `kube_pods_subnet`
  and node routing; a mismatched pod CIDR or MTU ([[CONFIG-CNI_MTU]]) silently breaks pod-to-pod
  traffic. Stable across **v2.27.0–v2.31.0** (Cilium passthrough vars were added incrementally —
  [[CONCEPT-ESCAPE_HATCHES]]).

## Implementation

**Step 0 — Freeze, gate, back up.** Record CNI state and take the etcd snapshot
([[PRACTICE-ETCD_BACKUP_RESTORE]]) — CNI CRDs (e.g. Calico IPPools) live in etcd:

```bash
kubectl get pods -n kube-system -o wide | grep -Ei 'calico|cilium|flannel|kube-ovn'
ls /etc/cni/net.d/ ; kubectl get crds | grep -Ei 'calico|cilium|projectcalico'
```

**Step 1 — Choose the strategy.** Prefer **blue-green** for any cluster you can't take fully down.
The rest of this runbook is the **in-place** path — run it only inside an accepted outage window.

**Step 2 — Set the target plugin** in inventory group_vars ([[VARIABLE-KUBE_NETWORK_PLUGIN]]), e.g.
`kube_network_plugin: cilium`, plus the target plugin's required vars (Cilium tunnel/IPAM, Calico
encapsulation, etc.).

**Step 3 — Remove the old CNI** (Kubespray won't): delete its DaemonSet/Deployment, its CRDs, and on
**every** node clear `/etc/cni/net.d/*` for the old plugin and its dataplane state (Calico iptables
chains / Cilium eBPF maps). Skipping this is the #1 cause of a half-migrated, no-network cluster.

**Step 4 — Deploy the new CNI:**

```bash
ansible-playbook -i inventory/<cluster>/hosts.yaml kubespray/cluster.yml -b \
  --tags network    # or a full run if node-level changes are needed
```

**Step 5 — Recycle pods.** Existing pods keep their **old** network until recreated — roll every
workload (and CoreDNS) so they get new-CNI networking:

```bash
kubectl rollout restart deploy,ds,sts -A
kubectl -n kube-system rollout restart deploy coredns
```

**Step 6 — Verify** end-to-end: new CNI pods `Ready` on all nodes; nodes not stuck
`NotReady`/`cni not initialized` ([[TROUBLE-KUBELET_NODE_NOTREADY_CNI]]); pod-to-pod, pod-to-service
and DNS work — run the netcheck workload ([[PRACTICE-NETCHECK]],
[[PRACTICE-SERVICE_NETWORKING_DEBUG]]).

**Rollback.** In-place CNI migration is **not cleanly reversible** — the old dataplane state is gone.
Real rollback is either **restore the etcd snapshot + redeploy the old CNI at the previous config**,
or (why blue-green is preferred) **cut back to the still-running old cluster**. Decide which before
Step 3.

## References

- `docs/CNI/cni.md`, `roles/network_plugin/` (tag `v2.31.0`). Selector:
  [[VARIABLE-KUBE_NETWORK_PLUGIN]] / [[ROLE-NETWORK_PLUGIN]]; failure mode
  [[TROUBLE-KUBELET_NODE_NOTREADY_CNI]]; verification [[PRACTICE-NETCHECK]]; backup
  [[PRACTICE-ETCD_BACKUP_RESTORE]]; index [[CONCEPT-RUNBOOKS_INDEX]].
