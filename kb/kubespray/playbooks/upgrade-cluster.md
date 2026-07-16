---
id: PLAYBOOK-UPGRADE_CLUSTER
type: playbook
title: upgrade-cluster.yml
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - upgrade-cluster.yml
tags:
  - playbook
  - upgrade
sources:
  - type: code
    path: playbooks/upgrade_cluster.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/upgrade_cluster.yml
    note: "graceful, serial cluster upgrade"
relations:
  - type: see_also
    target: UPGRADE-KUBESPRAY_SEQUENTIAL
  - type: see_also
    target: TAG-PRE_UPGRADE
---

# upgrade-cluster.yml

## Summary

`upgrade-cluster.yml` performs a **graceful** upgrade of an existing cluster:
control-plane nodes first, then workers in batches, cordoning/draining each node
before upgrading and uncordoning after. It requires at least one already-deployed
`kube_control_plane`.

## Implementation

Play sequence (`playbooks/upgrade_cluster.yml`):

1. Download images to the ansible cache via `kube_control_plane[0]`.
2. **Prepare nodes for upgrade** (`k8s_cluster:etcd:calico_rr`).
3. Upgrade container engine on non-cluster nodes; install/upgrade etcd.
4. **Control plane first** (`kube_control_plane`): `upgrade/pre-upgrade`
   (`pre-upgrade`) → `upgrade/system-upgrade` (`system-upgrade`) → control-plane
   roles → `upgrade/post-upgrade` (`post-upgrade`).
5. Upgrade Calico and the external cloud provider on control plane / calico_rr /
   nodes.
6. **Workers in batches** (`kube_node:calico_rr:!kube_control_plane`): the same
   pre/system/post-upgrade sequence.

Batch size is controlled by the Ansible `serial` variable (default 20% of nodes;
`serial=1` = one at a time). The full procedure and the sequential-tag rule are in
[[UPGRADE-KUBESPRAY_SEQUENTIAL]].

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: graceful per-node cordon/drain/uncordon.
- Do not skip Kubespray minors — upgrade one tag at a time.
- In `v2.29.0`/`v2.29.1` the control-plane role in this playbook still carried the
  legacy `master` tag (renamed to `control-plane` by `v2.30.0`; see
  [[TAG-CONTROL_PLANE]]).

## References

- `playbooks/upgrade_cluster.yml` (tag `v2.31.0` `1c9add4`).
- Root `upgrade-cluster.yml` imports it.
