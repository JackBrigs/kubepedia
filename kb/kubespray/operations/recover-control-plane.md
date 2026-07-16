---
id: PRACTICE-RECOVER_CONTROL_PLANE
type: best_practice
title: Recovering the control plane
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: verified
aliases:
  - recover control plane
  - recover-control-plane
tags:
  - recovery
  - etcd
  - operations
sources:
  - type: docs
    path: docs/operations/recover-control-plane.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/recover-control-plane.md
    note: "recover-control-plane.yml; broken_etcd / broken_kube_control_plane groups; etcd_retries"
relations:
  - type: see_also
    target: COMPONENT-ETCD
  - type: see_also
    target: TAG-CONTROL_PLANE
---

# Recovering the control plane

## Summary

The `recover-control-plane.yml` playbook restores a degraded control plane after
node failures (hardware loss, failed upgrade/patch, etcd corruption). It requires
**at least one functional** control-plane/etcd node to recover from.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- "Broken" means unrecoverable hardware failure, failure during patch/upgrade,
  etcd database corruption, or other failures leaving the control plane degraded.

## Implementation

Runbook:

1. Back up whatever you can.
2. Provision new nodes to replace the broken ones.
3. Put broken etcd nodes in the `broken_etcd` group (set `etcd_member_name` for
   each); put broken control-plane nodes in `broken_kube_control_plane`.
4. In the `etcd` and `kube_control_plane` groups, list the **surviving** nodes
   first, then the new nodes below them.
5. Run the playbook limited to those groups and raise etcd retries:

```ShellSession
ansible-playbook recover-control-plane.yml --limit etcd,kube_control_plane -e etcd_retries=10
```

The required retry count is hard to predict; increase it if recovery stalls. When
finished, the control plane (and etcd, see [[COMPONENT-ETCD]]) should be fully
working again.

## Compatibility

- Verified against `v2.31.0` docs; the recovery runbook is stable across the
  indexed range. Recovery is inherently risky — back up etcd first.

## References

- `docs/operations/recover-control-plane.md` (tag `v2.31.0` `1c9add4`).
