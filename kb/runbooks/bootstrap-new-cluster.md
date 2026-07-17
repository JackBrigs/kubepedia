---
id: PRACTICE-RUNBOOK_BOOTSTRAP
type: best_practice
title: "Runbook: bootstrap a new cluster (cluster.yml)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - bootstrap runbook
  - deploy new cluster kubespray
  - cluster.yml first run
  - initial cluster deployment
  - fresh install kubespray
tags:
  - runbook
  - operations
  - bootstrap
sources:
  - type: docs
    path: docs/getting_started/getting-started.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/getting_started/getting-started.md
    note: "inventory, cluster.yml, kube_network_plugin, first deploy"
  - type: code
    path: cluster.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/cluster.yml
    note: "full-cluster convergence playbook"
relations:
  - type: part_of
    target: CONCEPT-RUNBOOKS_INDEX
  - type: depends_on
    target: PRACTICE-INVENTORY
  - type: depends_on
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
  - type: see_also
    target: PRACTICE-ARCHITECTURE_COMPATIBILITY
  - type: see_also
    target: VARIABLE-KUBE_NETWORK_PLUGIN
  - type: see_also
    target: PRACTICE-CLUSTER_ACCESS
---

# Runbook: bootstrap a new cluster (cluster.yml)

## Summary

The ordered first-deploy procedure: prepare inventory and host prerequisites, pick the versions and
CNI, run `cluster.yml`, and verify. Bootstrap is the one operation whose rollback is trivial — there
is no state to lose — so the risk is a **wrong-but-converged** cluster (bad CIDR, wrong CNI,
undersized control plane), which is far cheaper to fix now than after workloads land.

## Context

- **`cluster.yml` is idempotent and re-runnable** — the same playbook converges a fresh cluster and
  reconciles an existing one. Bootstrap = its first run.
- **Decide before you run** (changing these later is a migration, not an edit): pod/service CIDRs
  (`kube_pods_subnet`, `kube_service_addresses`), CNI ([[VARIABLE-KUBE_NETWORK_PLUGIN]]), container
  runtime, and the Kubernetes version (tag default vs pinned `kube_version` —
  [[CONCEPT-KUBERNETES_VERSION_SUPPORT]]).
- **Control-plane count:** deploy **3** `kube_control_plane` / `etcd` for HA from the start —
  growing from 1 to 3 later is the harder add-node path.
- Stable across **v2.27.0–v2.31.0**; the target Kubernetes minor and component versions come from the
  chosen tag's release doc.

## Implementation

**Step 0 — Host prerequisites** (all nodes): supported OS/arch
([[PRACTICE-ARCHITECTURE_COMPATIBILITY]]), kernel modules and sysctls
([[PRACTICE-KERNEL_REQUIREMENTS]]), required ports open between roles
([[PRACTICE-PORT_REQUIREMENTS]]), SSH + sudo from the control host, swap off.

**Step 1 — Inventory** ([[PRACTICE-INVENTORY]]): define `kube_control_plane`, `etcd`, `kube_node`
groups; set CIDRs, CNI, runtime, and `kube_version` (or leave unset for the tag default). Sanity:

```bash
ansible -i inventory/<cluster>/hosts.yaml all -m ping
```

**Step 2 — Refresh facts** (cheap, avoids stale-fact surprises):

```bash
ansible-playbook -i inventory/<cluster>/hosts.yaml kubespray/facts.yml
```

**Step 3 — Deploy:**

```bash
ansible-playbook -i inventory/<cluster>/hosts.yaml kubespray/cluster.yml -b
```

**Step 4 — Get admin access** ([[PRACTICE-CLUSTER_ACCESS]]): copy
`/etc/kubernetes/admin.conf` from a control-plane node to your kubeconfig (rewrite the server to a
reachable address / the API VIP).

**Step 5 — Verify** ([[PRACTICE-CLUSTER_HEALTH_CHECKS]]): all nodes `Ready`, all `kube-system` pods
`Running`, CoreDNS answering, and pod-to-pod + pod-to-service connectivity via the netcheck workload
([[PRACTICE-NETCHECK]]).

**Rollback.** Nothing to preserve on a fresh deploy — if the result is wrong, **reset and redeploy**
([[PRACTICE-RUNBOOK_RESET]]) with corrected inventory rather than trying to mutate CIDR/CNI in place.

## References

- `docs/getting_started/`, `cluster.yml` (tag `v2.31.0`). Prereqs:
  [[PRACTICE-ARCHITECTURE_COMPATIBILITY]], [[PRACTICE-KERNEL_REQUIREMENTS]],
  [[PRACTICE-PORT_REQUIREMENTS]]; inventory [[PRACTICE-INVENTORY]]; access [[PRACTICE-CLUSTER_ACCESS]];
  index [[CONCEPT-RUNBOOKS_INDEX]].
