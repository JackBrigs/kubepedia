---
id: TAG-POST_UPGRADE
type: ansible_tag
title: post-upgrade (Ansible run-tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - post-upgrade
  - --tags post-upgrade
tags:
  - ansible-tag
  - upgrade
sources:
  - type: code
    path: playbooks/upgrade_cluster.yml
    lines: "64"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/upgrade_cluster.yml
    note: "role upgrade/post-upgrade tagged post-upgrade"
relations:
  - type: see_also
    target: TAG-PRE_UPGRADE
  - type: see_also
    target: TAG-SYSTEM_UPGRADE
---

# post-upgrade (Ansible run-tag)

## Summary

`post-upgrade` runs the `upgrade/post-upgrade` role during `upgrade-cluster.yml`.
It finalizes the per-node upgrade — typically uncordoning the node so it becomes
schedulable again after its components and OS have been upgraded.

## Context

- **Playbook:** `upgrade-cluster.yml`.
- **Hosts:** control-plane first, then workers in batches.
- Final step of the per-node sequence, after [[TAG-PRE_UPGRADE]] and
  [[TAG-SYSTEM_UPGRADE]].

## Implementation

```yaml
# playbooks/upgrade_cluster.yml
- { role: upgrade/post-upgrade, tags: post-upgrade }
```

The role runs after the node's components are upgraded, restoring the node to a
schedulable state (uncordon) and any post-upgrade checks.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: `post-upgrade` tags the `upgrade/post-upgrade`
  role in `upgrade-cluster.yml`.
- **Standalone-run safety: risky.** Uncordons nodes; only meaningful after the
  preceding upgrade steps.

## References

- `playbooks/upgrade_cluster.yml:64` — `post-upgrade` tag.
- Verified on tags v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
