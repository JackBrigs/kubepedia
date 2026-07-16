---
id: TAG-NODE_TAINT
type: ansible_tag
title: node-taint (Ansible run-tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - node-taint
  - --tags node-taint
tags:
  - ansible-tag
  - node
sources:
  - type: code
    path: playbooks/cluster.yml
    lines: "54"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/cluster.yml
    note: "role kubernetes/node-taint tagged node-taint; hosts k8s_cluster"
relations:
  - type: see_also
    target: TAG-NODE
---

# node-taint (Ansible run-tag)

## Summary

`node-taint` runs the `kubernetes/node-taint` role, which applies node taints
(e.g. control-plane / dedicated-role taints and any configured custom taints) to
cluster nodes via the API server.

## Context

- **Playbook:** `cluster.yml` (the "Invoke kubeadm and install a CNI" play).
- **Hosts:** `k8s_cluster`.
- Runs after nodes have joined, alongside `node-label`.

## Implementation

`playbooks/cluster.yml`:

```yaml
- { role: kubernetes/node-taint, tags: node-taint }
```

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: `node-taint` tags the `kubernetes/node-taint`
  role in `cluster.yml`.
- **Standalone-run safety: risky.** Applies taints via the API server; requires a
  reachable, joined cluster. Handy for re-applying taints in isolation, but taints
  affect scheduling immediately.

## References

- `playbooks/cluster.yml:54` — `node-taint` tag.
- Verified on tags v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
