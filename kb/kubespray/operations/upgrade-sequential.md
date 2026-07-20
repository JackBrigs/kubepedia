---
id: UPGRADE-KUBESPRAY_SEQUENTIAL
type: upgrade
title: Sequential Kubespray/Kubernetes upgrade procedure
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: 2026-07-20
confidence: verified
aliases:
  - kubespray upgrade
  - upgrade-cluster
  - multiple upgrades
tags:
  - upgrade
  - operations
sources:
  - type: docs
    path: docs/operations/upgrades.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/upgrades.md
    note: "graceful vs unsafe upgrade; multiple upgrades / no skipping minors; serial batch"
  - type: code
    path: playbooks/upgrade_cluster.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.0/playbooks/upgrade_cluster.yml
    note: "play ordering: control plane serial:1, workers/calico serial 20%; cordon/drain via pre/post-upgrade — evidence for the disruption profile"
relations:
  - type: see_also
    target: VARIABLE-KUBE_VERSION
  - type: see_also
    target: TAG-PRE_UPGRADE
  - type: see_also
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
---

# Sequential Kubespray/Kubernetes upgrade procedure

## Summary

Kubespray upgrades a cluster by laying components down in the same fixed order as
a fresh deploy. The cardinal rule: **do not skip minor releases — upgrade one tag
at a time** (patch releases may be skipped). Attempting to jump from an old
release straight to the latest is unsupported.

## Implementation

**Graceful upgrade** (recommended) uses a dedicated playbook that cordons, drains,
and uncordons nodes:

```ShellSession
ansible-playbook upgrade-cluster.yml -b -i inventory/.../hosts.ini -e kube_version=<next>
```

- Requires an existing cluster (≥1 `kube_control_plane` already deployed).
- Nodes are upgraded in batches; the Ansible `serial` variable controls batch size
  (default **20%** of nodes; `serial=1` = one node at a time).
- The per-node flow is [[TAG-PRE_UPGRADE]] → `system-upgrade` → `post-upgrade`
  (cordon/drain → OS upgrade → uncordon). `upgrade_node_confirm: true` pauses
  before each node.

**Unsafe upgrade** re-runs `cluster.yml` with an explicit version and
`upgrade_cluster_setup=true` (migrates static pods immediately, skips
cordon/drain):

```ShellSession
ansible-playbook cluster.yml -e kube_version=<next> -e upgrade_cluster_setup=true
```

**Multiple upgrades:** to move several releases, check out each tag in order and
run the upgrade for each — e.g. `v2.22.0 → v2.23.2 → v2.24.0` is fine;
`v2.22.0 → v2.24.0` is not. If `kube_version` is pinned in inventory, update it
(or pass `-e kube_version=...`) each step, or the upgrade stays at the pinned
version.

## Service impact

Graceful upgrade is **rolling, not zero-touch** — plan a maintenance window per
minor. Verified against play ordering in `playbooks/upgrade_cluster.yml` (v2.29.0):

- **Control plane:** upgraded `serial: 1` (one node at a time), so
  kube-apiserver / scheduler / controller-manager restart node-by-node. With ≥2
  `kube_control_plane` nodes the API stays reachable (rolling); a **single
  control-plane cluster loses the API** while its static pods are re-laid.
- **etcd:** re-run rolling; brief per-member restart, quorum preserved on a
  multi-node etcd.
- **Workers:** drained in batches (`serial`, default **20%**) with cordon →
  drain → uncordon. Every pod on a draining node is **evicted and rescheduled
  elsewhere** — single-replica workloads and those without a PodDisruptionBudget
  see **downtime**; conversely a restrictive PDB can **stall the drain**. Needs
  spare capacity to absorb the batch.
- **Node reboots:** with `system_upgrade_reboot: on-upgrade` (default) a node
  reboots when OS packages are upgraded, extending its drained window; the node
  is already cordoned, so no extra eviction.
- **Unsafe path** (`upgrade_cluster_setup=true`): skips cordon/drain and migrates
  static pods immediately — **more disruptive to workloads on each node**, no
  graceful rescheduling. Use only when that trade-off is acceptable.

Not a rollback: cluster state and objects are preserved, and running workloads
survive except during their own node's drain/reboot. Each minor is a separate
window — repeat the procedure per step.

## Upgrade Notes

- Never skip a Kubespray minor (patches are OK) — this mirrors the sequential
  support window in [[CONCEPT-KUBERNETES_VERSION_SUPPORT]].
- Individual component versions can be pinned (`kube_version`, `etcd_version`,
  `containerd_version`, …) but must stay compatible with the target release.
- Graceful upgrade needs enough spare capacity to drain nodes.

## Compatibility

- Verified against `v2.31.0` docs; the sequential-upgrade rule and the
  graceful/unsafe split are stable across the indexed range `v2.29.0`–`v2.31.0`.

## References

- `docs/operations/upgrades.md` (tag `v2.31.0` `1c9add4`) — graceful/unsafe
  upgrade, multiple upgrades, `serial`, `upgrade_cluster_setup`.
