---
id: PRACTICE-RUNBOOK_RESET
type: best_practice
title: "Runbook: reset / tear down a cluster or node (reset.yml)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - reset runbook
  - reset.yml
  - tear down cluster kubespray
  - wipe node kubernetes
  - clean redeploy
  - destroy cluster
tags:
  - runbook
  - operations
  - teardown
sources:
  - type: docs
    path: docs/getting_started/getting-started.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/getting_started/getting-started.md
    note: "reset.yml wipes k8s/etcd/CNI/runtime state; interactive confirmation prompt"
  - type: code
    path: reset.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/reset.yml
    note: "reset role: stop services, remove certs/manifests/etcd data, flush iptables/CNI"
relations:
  - type: part_of
    target: CONCEPT-RUNBOOKS_INDEX
  - type: depends_on
    target: PRACTICE-ETCD_BACKUP_RESTORE
  - type: see_also
    target: ROLE-RESET
  - type: see_also
    target: TAG-RESET
  - type: see_also
    target: PRACTICE-RUNBOOK_BOOTSTRAP
---

# Runbook: reset / tear down a cluster or node (reset.yml)

## Summary

`reset.yml` **destroys** cluster state — it stops services and removes Kubernetes/etcd data, certs,
static manifests, CNI config and iptables/eBPF rules ([[ROLE-RESET]]) — returning hosts to a
near-clean state for a fresh deploy. It is **irreversible**: the only rollback is a **restore from
backup** or a **redeploy**. Treat it as the most dangerous runbook here and gate it behind an etcd
snapshot ([[PRACTICE-ETCD_BACKUP_RESTORE]]) and an explicit scope.

## Context

- **What it wipes:** kubelet/etcd/runtime services, `/etc/kubernetes`, etcd data dir, CNI state
  (`/etc/cni/net.d`, interfaces), and runtime state — via the `reset` tags
  ([[TAG-RESET]], [[TAG-RESET_CONTAINERD]]). It does **not** un-patch the OS or remove packages.
- **Interactive by default:** `reset.yml` prompts for confirmation. In automation you pass
  `-e reset_confirmation=yes` — which is exactly why it's dangerous; never wire that into a pipeline
  that could target a live cluster.
- **Scope with `--limit`** to reset a **subset** of nodes (e.g. one bad node before re-adding) rather
  than the whole cluster. Without a limit, it targets everything in the inventory.
- Stable across **v2.27.0–v2.31.0**.

## Implementation

**Step 0 — Back up anything you might want** ([[PRACTICE-ETCD_BACKUP_RESTORE]] + any PVs / app data).
After reset it is gone.

**Step 1 — Confirm the target.** Double-check the inventory and `--limit` — a missing `--limit` means
**the entire cluster**:

```bash
ansible -i inventory/<cluster>/hosts.yaml <target-group-or-node> --list-hosts
```

**Step 2 — Reset:**

```bash
# whole cluster (interactive prompt):
ansible-playbook -i inventory/<cluster>/hosts.yaml kubespray/reset.yml -b
# a single node, non-interactive:
ansible-playbook -i inventory/<cluster>/hosts.yaml kubespray/reset.yml -b \
  --limit=<node> -e reset_confirmation=yes
```

**Step 3 — Verify the wipe:** on the target(s), no kubelet/etcd/containerd cluster state — `crictl
ps` empty of cluster pods, `/etc/kubernetes` gone, no `cni0`/CNI interfaces lingering. A leftover CNI
interface or iptables rule is the usual cause of a broken **re-deploy**.

**Step 4 — Redeploy or re-add** as intended: full rebuild via [[PRACTICE-RUNBOOK_BOOTSTRAP]], or a
single reset node back in via [[PRACTICE-RUNBOOK_ADD_NODES]].

**Rollback.** None in place — reset is destructive by design. Recovery is **restore the etcd snapshot
into a freshly deployed control plane** ([[PRACTICE-RUNBOOK_ETCD_RESTORE]]) or accept the clean
redeploy. This is why Step 0 is mandatory.

## References

- `reset.yml`, reset role (tag `v2.31.0`). Role detail [[ROLE-RESET]]; backup gate
  [[PRACTICE-ETCD_BACKUP_RESTORE]]; redeploy [[PRACTICE-RUNBOOK_BOOTSTRAP]]; index
  [[CONCEPT-RUNBOOKS_INDEX]].
