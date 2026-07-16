---
id: TAG-PRE_UPGRADE
type: ansible_tag
title: pre-upgrade (Ansible run-tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - pre-upgrade
  - --tags pre-upgrade
tags:
  - ansible-tag
  - upgrade
sources:
  - type: code
    path: playbooks/upgrade_cluster.yml
    lines: "52,86"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/upgrade_cluster.yml
    note: "role upgrade/pre-upgrade tagged pre-upgrade; control-plane then worker plays"
relations:
  - type: see_also
    target: TAG-SYSTEM_UPGRADE
  - type: see_also
    target: TAG-POST_UPGRADE
---

# pre-upgrade (Ansible run-tag)

## Summary

`pre-upgrade` runs the `upgrade/pre-upgrade` role during `upgrade-cluster.yml`. It
prepares a node for upgrade — typically cordoning and draining it so workloads move
off before the node's components are upgraded. It is the first step of the
per-node upgrade sequence (pre-upgrade → system-upgrade → post-upgrade).

## Context

- **Playbook:** `upgrade-cluster.yml`.
- **Hosts:** control-plane nodes first (`kube_control_plane`), then workers
  (`kube_node:calico_rr:!kube_control_plane`) in batches.
- Paired with [[TAG-SYSTEM_UPGRADE]] and [[TAG-POST_UPGRADE]].

## Implementation

```yaml
# playbooks/upgrade_cluster.yml
- { role: upgrade/pre-upgrade, tags: pre-upgrade }
```

The role runs before the component upgrade on each node, performing cordon/drain
and pre-checks so the upgrade proceeds safely one node at a time.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: `pre-upgrade` tags the `upgrade/pre-upgrade`
  role in `upgrade-cluster.yml`.
- **Standalone-run safety: risky.** Cordons/drains nodes (moves workloads);
  meaningful only as part of an upgrade sequence.

## References

- `playbooks/upgrade_cluster.yml:52,86` — `pre-upgrade` on control-plane and
  worker plays.
- Verified on tags v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
