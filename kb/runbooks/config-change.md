---
id: PRACTICE-RUNBOOK_CONFIG_CHANGE
type: best_practice
title: "Runbook: apply a control-plane / kubelet config change safely"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - config change runbook
  - change kubelet setting safely
  - set apiserver flag
  - apply extra_args
  - rollout config change kubespray
  - reconfigure running cluster
tags:
  - runbook
  - operations
  - configuration
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "kubelet_config_extra_args / kubelet_custom_flags; extra_args merged, not validated"
relations:
  - type: part_of
    target: CONCEPT-RUNBOOKS_INDEX
  - type: depends_on
    target: CONCEPT-ESCAPE_HATCHES
  - type: see_also
    target: CONFIG-KUBELET_CONFIGURATION
  - type: see_also
    target: PRACTICE-GRACEFUL_UPGRADE
  - type: see_also
    target: TROUBLE-KUBEADM_UPGRADE_HEALTH_CHECK
---

# Runbook: apply a control-plane / kubelet config change safely

## Summary

The generic procedure for changing a setting on a **running** cluster — a KubeletConfiguration field,
an apiserver/controller-manager/scheduler flag, a feature gate — via Kubespray's named variables or
escape hatches ([[CONCEPT-ESCAPE_HATCHES]]), rolled out **one node at a time** so a bad value is
caught before it takes the cluster down. The danger: `*_extra_args` are **merged, not validated**, so
a wrong flag/field surfaces as a crash-loop after apply, not at edit time.

## Context

- **Pick the most specific knob** ([[CONCEPT-ESCAPE_HATCHES]] decision order): a **dedicated named
  variable** → a typed **`*_extra_args`** map → raw **`*_custom_flags` / `kubeadm_patches`** (last
  resort). The more specific, the more Kubespray validates for you.
- **Not validated = fails late.** A bad KubeletConfiguration field crash-loops the kubelet; a bad
  apiserver flag makes the static pod fail; a bad kubeadm value fails the health check
  ([[TROUBLE-KUBEADM_UPGRADE_HEALTH_CHECK]]). Use the **exact upstream name for your version** — a
  flag removed in a newer minor breaks start-up.
- **Blast radius:** control-plane changes hit static pods (one CP node at a time preserves quorum);
  kubelet changes hit every node (roll them). Scope with `--limit` to canary one node first.
- Stable across **v2.27.0–v2.31.0**.

## Implementation

**Step 0 — Freeze, gate, back up** ([[CONCEPT-RUNBOOKS_INDEX]] spine): snapshot etcd, cluster healthy,
record the current value (`kubectl get --raw /configz` for kubelet, static-pod manifests for CP
flags).

**Step 1 — Set the variable** in inventory — prefer a named var; use an escape hatch only if none
exists ([[CONFIG-KUBELET_CONFIGURATION]] for kubelet):

```yaml
# example — a KubeletConfiguration field with no dedicated var:
kubelet_config_extra_args:
  runtimeRequestTimeout: "15m"
```

**Step 2 — Canary one node** with `--limit` before touching the rest:

```bash
ansible-playbook -i inventory/<cluster>/hosts.yaml kubespray/cluster.yml -b --limit=<one-node>
```

**Step 3 — Verify the canary:** the target component restarted cleanly (kubelet `Running`, or the CP
static pod back up), the setting took effect (`kubectl get --raw /configz` / the pod's `--flag`), node
`Ready`, no crash-loop. If it fails, this is where you catch it — **one** node down, not all.

**Step 4 — Roll out to the rest**, control-plane nodes one at a time (quorum), workers in batches
([[PRACTICE-GRACEFUL_UPGRADE]] pacing):

```bash
ansible-playbook -i inventory/<cluster>/hosts.yaml kubespray/cluster.yml -b
```

**Step 5 — Verify cluster-wide:** all components healthy, the setting present everywhere, no
regressions in system pods.

**Rollback.** Config changes are reversible: **revert the variable** and re-apply the same way
(canary → roll). Because you canaried in Step 2, a bad value never reached the whole cluster. If a
control-plane node won't restart after a CP-flag change, restore its static-pod manifest / the Step 0
snapshot ([[PRACTICE-RUNBOOK_ETCD_RESTORE]] only if etcd state was touched).

## References

- kubelet node defaults, `kubespray_defaults` main.yml (tag `v2.31.0`). Escape hatches
  [[CONCEPT-ESCAPE_HATCHES]]; kubelet config [[CONFIG-KUBELET_CONFIGURATION]]; roll pacing
  [[PRACTICE-GRACEFUL_UPGRADE]]; failure seam [[TROUBLE-KUBEADM_UPGRADE_HEALTH_CHECK]]; index
  [[CONCEPT-RUNBOOKS_INDEX]].
