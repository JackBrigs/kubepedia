---
id: TAG-KUBEADM
type: ansible_tag
title: kubeadm (Ansible run-tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - kubeadm
  - --tags kubeadm
tags:
  - ansible-tag
  - kubeadm
  - node
sources:
  - type: code
    path: playbooks/cluster.yml
    lines: "52"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/cluster.yml
    note: "role kubernetes/kubeadm tagged kubeadm; hosts k8s_cluster"
  - type: code
    path: roles/kubernetes/kubeadm/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/kubeadm/tasks/main.yml
    note: "kubeadm join / node bootstrap; kubeadm_etcd_node.yml"
relations:
  - type: see_also
    target: TAG-CONTROL_PLANE
  - type: see_also
    target: CONFIG-KUBEADM_CONFIG_API_VERSION
---

# kubeadm (Ansible run-tag)

## Summary

`kubeadm` runs the `kubernetes/kubeadm` role, which performs the node-side kubeadm
step: it bootstraps each node into the cluster (kubeadm join / kubelet bootstrap
config) so the API server, kubelet, and CNI can come up. It complements
[[TAG-CONTROL_PLANE]] (which runs kubeadm on the control-plane nodes).

## Context

- **Playbook:** `cluster.yml` (the "Invoke kubeadm and install a CNI" play).
- **Hosts:** `k8s_cluster`.
- Runs after `node` and `control-plane`, immediately before the CNI (`network`).

## Implementation

`playbooks/cluster.yml`:

```yaml
- { role: kubernetes/kubeadm, tags: kubeadm}
```

`roles/kubernetes/kubeadm/tasks/main.yml` runs the kubeadm bootstrap for nodes;
`kubeadm_etcd_node.yml` handles etcd-node specifics. The kubeadm configuration
format is `v1beta4` (see [[CONFIG-KUBEADM_CONFIG_API_VERSION]]).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: `kubeadm` tags the `kubernetes/kubeadm` role in
  `cluster.yml`.
- **Standalone-run safety: risky.** Drives kubeadm join and writes kubelet
  bootstrap config; requires a reachable, initialized control plane.

## References

- `playbooks/cluster.yml:52` — `kubeadm` tag.
- `roles/kubernetes/kubeadm/tasks/main.yml` — node bootstrap.
- Verified on tags v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
