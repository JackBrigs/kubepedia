---
id: TAG-RESET
type: ansible_tag
title: reset (Ansible run-tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - reset
  - --tags reset
tags:
  - ansible-tag
  - reset
  - destructive
sources:
  - type: code
    path: playbooks/reset.yml
    lines: "9,35"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/reset.yml
    note: "hosts etcd:k8s_cluster:calico_rr; role reset tagged reset"
  - type: code
    path: playbooks/remove_node.yml
    lines: "51"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/remove_node.yml
    note: "role reset tagged reset, when reset_nodes | default(True)"
relations:
  - type: see_also
    target: TAG-CONTROL_PLANE
  - type: see_also
    target: TAG-ETCD
---

# reset (Ansible run-tag)

## Summary

`reset` runs the `reset` role, which **tears a node back down**: it stops and
removes Kubernetes, etcd, the container runtime state, CNI, and Kubespray-managed
configuration/certificates, returning the host toward a pre-install state. It is
used by `reset.yml` (whole cluster) and by `remove-node.yml` (per node).

## Context

- **Playbooks:** `reset.yml` and `remove-node.yml` (gated by `reset_nodes`).
- **Hosts:** `etcd:k8s_cluster:calico_rr`.
- This is the most destructive tag in Kubespray.

## Implementation

```yaml
# playbooks/reset.yml
- hosts: etcd:k8s_cluster:calico_rr
  roles:
    - { role: reset, tags: reset }

# playbooks/remove_node.yml
- { role: reset, tags: reset, when: reset_nodes | default(True) | bool }
```

The `reset` role removes cluster services, unmounts and deletes data
directories, and cleans up network interfaces created by the CNI. `reset.yml`
prompts for confirmation before proceeding.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: `reset` tags the `reset` role in `reset.yml`
  and `remove-node.yml`.
- **Standalone-run safety: unsafe (destructive).** Running `--tags reset`
  destroys cluster state on the targeted hosts. Never run it as a casual subset;
  it is not idempotent-safe against a healthy cluster — it removes it.

## References

- `playbooks/reset.yml:9,35` — hosts and `reset` tag.
- `playbooks/remove_node.yml:51` — `reset` tag gated on `reset_nodes`.
- Verified on tags v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
