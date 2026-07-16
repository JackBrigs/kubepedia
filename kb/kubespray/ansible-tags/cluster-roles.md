---
id: TAG-CLUSTER_ROLES
type: ansible_tag
title: cluster-roles (Ansible run-tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - cluster-roles
  - --tags cluster-roles
tags:
  - ansible-tag
  - rbac
sources:
  - type: code
    path: playbooks/cluster.yml
    lines: "43"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/cluster.yml
    note: "role kubernetes-apps/cluster_roles tagged cluster-roles; hosts kube_control_plane"
relations:
  - type: see_also
    target: TAG-CONTROL_PLANE
---

# cluster-roles (Ansible run-tag)

## Summary

`cluster-roles` runs the `kubernetes-apps/cluster_roles` role, which applies the
RBAC ClusterRoles and ClusterRoleBindings Kubespray needs (e.g. node bindings,
add-on permissions) to the cluster.

## Context

- **Playbook:** `cluster.yml` (the "Install the control plane" play).
- **Hosts:** `kube_control_plane`.
- Runs after the control plane and client are up (needs a reachable API server).

## Implementation

`playbooks/cluster.yml`:

```yaml
- { role: kubernetes-apps/cluster_roles, tags: cluster-roles }
```

The role applies RBAC manifests via `kubectl`/the API server from the
control-plane node.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: `cluster-roles` tags the
  `kubernetes-apps/cluster_roles` role in `cluster.yml`.
- **Standalone-run safety: risky.** Applies RBAC objects to a running cluster;
  requires a reachable API server.

## References

- `playbooks/cluster.yml:43` — `cluster-roles` tag.
- Verified on tags v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
