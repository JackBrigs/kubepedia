---
id: PLAYBOOK-RECOVER_CONTROL_PLANE
type: playbook
title: recover-control-plane.yml
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - recover-control-plane.yml
tags:
  - playbook
  - recovery
sources:
  - type: code
    path: playbooks/recover-control-plane.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/recover-control-plane.yml
    note: "recover a degraded control plane / etcd"
relations:
  - type: see_also
    target: PRACTICE-RECOVER_CONTROL_PLANE
---

# recover-control-plane.yml

## Summary

`recover-control-plane.yml` restores a degraded control plane after node failures
(hardware loss, failed upgrade, etcd corruption). It rebuilds etcd membership and
the control plane from at least one surviving node.

## Implementation

The operator places broken nodes in the `broken_etcd` /
`broken_kube_control_plane` groups (setting `etcd_member_name` for etcd), lists
surviving nodes first in the `etcd` / `kube_control_plane` groups, then runs the
playbook limited to those groups, usually with a raised `etcd_retries`:

```ShellSession
ansible-playbook recover-control-plane.yml --limit etcd,kube_control_plane -e etcd_retries=10
```

The full runbook is in [[PRACTICE-RECOVER_CONTROL_PLANE]].

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- Requires at least one functional control-plane/etcd node. Recovery is risky —
  back up etcd first.

## References

- `playbooks/recover-control-plane.yml` (tag `v2.31.0` `1c9add4`).
