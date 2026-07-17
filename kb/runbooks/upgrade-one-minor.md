---
id: PRACTICE-RUNBOOK_UPGRADE_ONE_MINOR
type: best_practice
title: "Runbook: upgrade the cluster by one Kubespray minor"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - upgrade runbook
  - how to upgrade kubespray safely
  - upgrade-cluster.yml step by step
  - one minor upgrade procedure
  - safe cluster upgrade
  - upgrade rollback
tags:
  - runbook
  - operations
  - upgrade
sources:
  - type: docs
    path: docs/operations/upgrades.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/upgrades.md
    note: "graceful (upgrade-cluster.yml, serial, drain), unsafe (upgrade_cluster_setup), multiple upgrades"
  - type: code
    path: playbooks/upgrade_cluster.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/upgrade_cluster.yml
    note: "serial: control-plane 1, workers 20%; pre_upgrade/post_upgrade drain hooks"
relations:
  - type: part_of
    target: CONCEPT-RUNBOOKS_INDEX
  - type: depends_on
    target: PRACTICE-UPGRADE_PREFLIGHT
  - type: depends_on
    target: UPGRADE-KUBESPRAY_SEQUENTIAL
  - type: see_also
    target: PRACTICE-GRACEFUL_UPGRADE
  - type: see_also
    target: PRACTICE-ETCD_BACKUP_RESTORE
  - type: see_also
    target: TROUBLE-KUBEADM_UPGRADE_HEALTH_CHECK
  - type: see_also
    target: CONCEPT-K8S_API_REMOVALS
---

# Runbook: upgrade the cluster by one Kubespray minor

## Summary

The end-to-end, ordered procedure to move a running cluster **up exactly one Kubespray minor**
(e.g. `v2.30.0 → v2.31.0`) with a drain-safe rollout and a defined rollback. It **orders and links**
the existing mechanics — it does not restate them: preflight ([[PRACTICE-UPGRADE_PREFLIGHT]]),
the one-minor rule ([[UPGRADE-KUBESPRAY_SEQUENTIAL]]), graceful drain/serial
([[PRACTICE-GRACEFUL_UPGRADE]]), and the etcd backup anchor ([[PRACTICE-ETCD_BACKUP_RESTORE]]).
Follow the [[CONCEPT-RUNBOOKS_INDEX]] safety spine: freeze → gate → back up → execute one unit →
verify → rollback.

## Context

- **One minor only.** `v2.30.0 → v2.31.0` is valid; `v2.29.0 → v2.31.0` is **not** — check out each
  tag in order and run this runbook once per step ([[UPGRADE-KUBESPRAY_SEQUENTIAL]]). Patch hops
  (`vX.Y.0 → vX.Y.1`) are fine.
- **Use `upgrade-cluster.yml`, not `cluster.yml`.** The upgrade playbook is the drain-aware path
  (cordon → drain → upgrade → uncordon, control-plane `serial: 1` to preserve etcd/API quorum). Only
  fall back to the **unsafe** path (`cluster.yml -e upgrade_cluster_setup=true`, no drain) when you
  have accepted the disruption.
- **Version deltas across the range** (envelope v2.27.0–v2.31.0): worker `serial` default is `20%`;
  each step's target Kubernetes minor and component bumps live in that step's `RELEASE-V*` /
  `UPGRADE-V*__V*` doc — read the target release's breaking changes before running.
- **Capacity.** Draining needs somewhere for pods to go; a too-strict PodDisruptionBudget stalls the
  drain until `drain_timeout`. Confirm spare capacity and PDB headroom first.

## Implementation

**Step 0 — Freeze & record** (rollback reference point):

```bash
kubectl get nodes,pods -A -o wide > /var/backups/pre-upgrade-state.txt
git -C kubespray describe --tags            # current tag
grep -r kube_version inventory/<cluster>/   # is kube_version pinned?
```

**Step 1 — Preflight gate.** Run the full checklist — do not proceed on any ❌
([[PRACTICE-UPGRADE_PREFLIGHT]]): cluster healthy now, certs valid for the window
([[PRACTICE-CERTIFICATE_EXPIRY]]), and the target release's **API removals / feature-gate**
changes reviewed against your manifests and flags ([[CONCEPT-K8S_API_REMOVALS]],
[[CONCEPT-K8S_FEATURE_GATES]]).

**Step 2 — Back up etcd, off-node** (the rollback anchor — [[PRACTICE-ETCD_BACKUP_RESTORE]]):

```bash
etcdctl snapshot save /var/backups/etcd-pre-<target>.db
etcdutl snapshot status /var/backups/etcd-pre-<target>.db --write-out=table
# copy the snapshot OFF the node, alongside the cluster PKI
```

**Step 3 — Check out the target tag and align the version:**

```bash
git -C kubespray checkout <target-tag>       # exactly one minor above current
pip install -r kubespray/requirements.txt    # collections/pins move between tags
# if kube_version is pinned in inventory, bump it to the target (else the tag default is used)
```

**Step 4 — Execute, one node at a time, paced.** Start cautious; watch the first control-plane and
first worker before letting it roll ([[PRACTICE-GRACEFUL_UPGRADE]]):

```bash
ansible-playbook -i inventory/<cluster>/hosts.yaml kubespray/upgrade-cluster.yml -b \
  -e upgrade_node_confirm=true        # pause before each node (drop once you trust the roll)
# faster, still safe once confident:  -e serial=1   (or the default 20% for workers)
```

**Step 5 — Verify after each node** (the roll pauses if you set confirm/pause): node `Ready`,
system pods `Running`, a smoke workload reschedules ([[PRACTICE-CLUSTER_HEALTH_CHECKS]]). If the
run **halts at a control-plane node with a kubeadm health-check timeout**, that is the kubeadm
seam, not Kubespray — diagnose with [[TROUBLE-KUBEADM_UPGRADE_HEALTH_CHECK]] before retrying.

**Step 6 — Post-upgrade confirmation:** all nodes on the new version
(`kubectl get nodes -o wide`), no leftover `NotReady`/`CrashLoopBackOff`, and the target's
component versions match the release doc ([[RELEASE-V2_31_0]] for the top of the range).

**Rollback.** There is **no in-place downgrade** of a Kubernetes minor. If verification fails and
you cannot fix forward:

1. Stop the roll (the drain model means only upgraded nodes changed — the rest are still on the old
   version).
2. Restore the **Step 2 etcd snapshot** and rebuild the control plane at the **previous tag**
   ([[PRACTICE-RUNBOOK_ETCD_RESTORE]] / [[PRACTICE-RECOVER_CONTROL_PLANE]]).
3. Re-run at the old tag to bring partially-upgraded nodes back to a consistent version.

This is why Step 2 is non-negotiable: without the snapshot, a failed minor upgrade has no clean
reversal.

## References

- `docs/operations/upgrades.md`, `playbooks/upgrade_cluster.yml` (tag `v2.31.0`). Ordered from:
  preflight [[PRACTICE-UPGRADE_PREFLIGHT]], sequencing [[UPGRADE-KUBESPRAY_SEQUENTIAL]], drain
  mechanics [[PRACTICE-GRACEFUL_UPGRADE]], backup [[PRACTICE-ETCD_BACKUP_RESTORE]]; failure seam
  [[TROUBLE-KUBEADM_UPGRADE_HEALTH_CHECK]]; index [[CONCEPT-RUNBOOKS_INDEX]].
