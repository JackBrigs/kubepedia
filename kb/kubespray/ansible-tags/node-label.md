---
id: TAG-NODE_LABEL
type: ansible_tag
title: node-label (Ansible run-tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - node-label
  - --tags node-label
tags:
  - ansible-tag
  - node
sources:
  - type: code
    path: playbooks/cluster.yml
    lines: "53"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/cluster.yml
    note: "role kubernetes/node-label tagged node-label; hosts k8s_cluster"
relations:
  - type: see_also
    target: TAG-NODE
---

# node-label (Ansible run-tag)

## Summary

`node-label` runs the `kubernetes/node-label` role, which applies node labels
(from `node_labels` and Kubespray-managed labels) to cluster nodes via the API
server.

## Context

- **Playbook:** `cluster.yml` (the "Invoke kubeadm and install a CNI" play).
- **Hosts:** `k8s_cluster`.
- Runs after nodes have joined (kubeadm), so the API server can accept the label
  changes.

## Implementation

`playbooks/cluster.yml`:

```yaml
- { role: kubernetes/node-label, tags: node-label }
```

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: `node-label` tags the `kubernetes/node-label`
  role in `cluster.yml`.
- **Standalone-run safety: risky.** Applies labels to nodes via the API server;
  requires a reachable, joined cluster. Useful for re-applying labels in
  isolation.

## References

- `playbooks/cluster.yml:53` — `node-label` tag.
- Verified on tags v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
