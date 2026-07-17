---
id: PRACTICE-RUNBOOK_COLD_START
type: best_practice
title: "Runbook: cold-start recovery after full power loss"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - cold start runbook
  - cluster power loss recovery
  - full cluster reboot
  - bring cluster back after outage
  - etcd quorum after reboot
  - all nodes down recovery
tags:
  - runbook
  - operations
  - disaster-recovery
sources:
  - type: docs
    path: docs/operations/recover-control-plane.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/recover-control-plane.md
    note: "recover-control-plane.yml for members that do not rejoin after outage"
relations:
  - type: part_of
    target: CONCEPT-RUNBOOKS_INDEX
  - type: see_also
    target: COMPONENT-ETCD
  - type: see_also
    target: PRACTICE-RECOVER_CONTROL_PLANE
  - type: see_also
    target: PRACTICE-RUNBOOK_ETCD_RESTORE
  - type: see_also
    target: PRACTICE-CLUSTER_HEALTH_CHECKS
---

# Runbook: cold-start recovery after full power loss

## Summary

When **every** node went down at once (power/datacenter outage), the cluster usually recovers on its
own once machines boot — but in a specific **order**: **etcd must regain quorum first**, then the
control plane, then workers. This runbook is the ordered bring-up and the checks at each layer, plus
the escalation path when etcd or the control plane doesn't come back on its own. Most cold-starts
need no playbook; the risk is thrashing the control plane before etcd has a leader.

## Context

- **etcd is the gate.** The API server is useless until etcd has quorum ((N/2)+1 members). Don't
  chase apiserver errors while etcd is still forming — fix etcd first ([[COMPONENT-ETCD]]).
- **Static pods self-heal:** kubelet restarts the control-plane static pods automatically once it and
  etcd are up — you rarely start them by hand. Give kubelet a few minutes before intervening.
- **Order matters:** power on / verify **etcd nodes → control-plane → workers**. Bringing workers up
  first just fills them with `NotReady`/pending until the control plane answers.
- **Clocks:** a large time skew after outage breaks TLS and etcd — confirm NTP/chrony is syncing on
  boot. Stable across **v2.27.0–v2.31.0**.

## Implementation

**Step 1 — Power on etcd nodes first** and wait for quorum. On an etcd node
([[PRACTICE-RUNBOOK_ETCD_BACKUP]] env for etcdctl):

```bash
etcdctl endpoint health --cluster        # all members healthy?
etcdctl endpoint status --write-out=table  # one leader, matching raft index?
```

Do not proceed until there is a **leader** and a healthy majority.

**Step 2 — Bring up the control plane.** Power on control-plane nodes; give kubelet a few minutes to
restart the static pods, then:

```bash
kubectl get --raw='/readyz?verbose'      # apiserver ready?
kubectl get pods -n kube-system          # apiserver/cm/scheduler Running
```

**Step 3 — Bring up workers.** Power them on; they re-register and `NotReady` clears as CNI/kubelet
re-init ([[PRACTICE-CLUSTER_HEALTH_CHECKS]]).

**Step 4 — Verify** ([[PRACTICE-CLUSTER_HEALTH_CHECKS]]): all nodes `Ready`, system pods `Running`,
CoreDNS answering, workloads rescheduled. Expect a settling period as controllers reconcile.

**Escalation — a member won't come back:**

- **An etcd member fails to rejoin** (data corruption on unclean shutdown) but **quorum survives** →
  replace that member with [[PRACTICE-RECOVER_CONTROL_PLANE]].
- **Quorum is lost** (majority of etcd members corrupt/gone) → this is a **restore**, not a boot:
  go to [[PRACTICE-RUNBOOK_ETCD_RESTORE]] with your latest snapshot.

**Rollback.** N/A — cold-start is recovery, not a change. The backstop for the unrecoverable case
(lost quorum) is the etcd snapshot ([[PRACTICE-RUNBOOK_ETCD_RESTORE]]), which is why
[[PRACTICE-RUNBOOK_ETCD_BACKUP]] runs on a schedule.

## References

- `docs/operations/recover-control-plane.md` (tag `v2.31.0`). etcd [[COMPONENT-ETCD]]; member
  replacement [[PRACTICE-RECOVER_CONTROL_PLANE]]; restore [[PRACTICE-RUNBOOK_ETCD_RESTORE]]; backup
  [[PRACTICE-RUNBOOK_ETCD_BACKUP]]; index [[CONCEPT-RUNBOOKS_INDEX]].
