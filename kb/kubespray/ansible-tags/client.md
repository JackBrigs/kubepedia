---
id: TAG-CLIENT
type: ansible_tag
title: client (Ansible run-tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - client
  - --tags client
tags:
  - ansible-tag
  - kubectl
sources:
  - type: code
    path: playbooks/cluster.yml
    lines: "42"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/cluster.yml
    note: "role kubernetes/client tagged client; hosts kube_control_plane"
relations:
  - type: see_also
    target: TAG-CONTROL_PLANE
---

# client (Ansible run-tag)

## Summary

`client` runs the `kubernetes/client` role on control-plane hosts, which sets up
the cluster admin kubeconfig and local `kubectl` access so the control-plane node
can talk to the API server.

## Context

- **Playbook:** `cluster.yml` (the "Install the control plane" play).
- **Hosts:** `kube_control_plane`.
- Runs right after [[TAG-CONTROL_PLANE]] in the same play.

## Implementation

`playbooks/cluster.yml`:

```yaml
- { role: kubernetes/control-plane, tags: control-plane }
- { role: kubernetes/client, tags: client }
```

The `kubernetes/client` role writes the admin kubeconfig and configures `kubectl`
on the control-plane node(s).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: `client` tags the `kubernetes/client` role in
  `cluster.yml`.
- **Standalone-run safety: risky.** Writes kubeconfig/credentials; requires an
  initialized control plane.

## References

- `playbooks/cluster.yml:42` — `client` tag.
- Verified on tags v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
