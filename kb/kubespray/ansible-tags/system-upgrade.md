---
id: TAG-SYSTEM_UPGRADE
type: ansible_tag
title: system-upgrade (Ansible run-tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - system-upgrade
  - --tags system-upgrade
tags:
  - ansible-tag
  - upgrade
sources:
  - type: code
    path: playbooks/upgrade_cluster.yml
    lines: "53,87"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/upgrade_cluster.yml
    note: "role upgrade/system-upgrade tagged system-upgrade"
relations:
  - type: see_also
    target: TAG-PRE_UPGRADE
  - type: see_also
    target: TAG-POST_UPGRADE
---

# system-upgrade (Ansible run-tag)

## Summary

`system-upgrade` runs the `upgrade/system-upgrade` role during
`upgrade-cluster.yml`. It performs the operating-system-level upgrade step on a
node (OS package updates and, where configured, a reboot) between the pre-upgrade
drain and the post-upgrade uncordon.

## Context

- **Playbook:** `upgrade-cluster.yml`.
- **Hosts:** control-plane first, then workers in batches.
- Second step of the per-node sequence, between [[TAG-PRE_UPGRADE]] and
  [[TAG-POST_UPGRADE]].

## Implementation

```yaml
# playbooks/upgrade_cluster.yml
- { role: upgrade/system-upgrade, tags: system-upgrade }
```

The role applies system package upgrades on the drained node.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: `system-upgrade` tags the
  `upgrade/system-upgrade` role in `upgrade-cluster.yml`.
- **Standalone-run safety: risky.** Updates OS packages and may reboot; run only
  on a drained node as part of the upgrade flow.

## References

- `playbooks/upgrade_cluster.yml:53,87` — `system-upgrade` tag.
- Verified on tags v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
