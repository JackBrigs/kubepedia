---
id: TAG-NODE
type: ansible_tag
title: node (Ansible run-tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - node
  - --tags node
tags:
  - ansible-tag
  - kubelet
  - node
sources:
  - type: code
    path: playbooks/cluster.yml
    lines: "32"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/cluster.yml
    note: "role kubernetes/node tagged node; hosts k8s_cluster"
  - type: code
    path: roles/kubernetes/node/tasks
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/roles/kubernetes/node/tasks
    note: "install.yml, kubelet.yml, loadbalancer/{haproxy,kube-vip,nginx-proxy}.yml"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
  - type: see_also
    target: COMPONENT-KUBE_VIP
---

# node (Ansible run-tag)

## Summary

`node` runs the `kubernetes/node` role on every cluster node: it installs kubelet
and the kubelet service, and sets up the node-local API-server load balancer
(nginx-proxy / haproxy / kube-vip) that worker nodes use to reach the control
plane. kubelet's version equals `kube_version` (see
[[CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS]]).

## Context

- **Playbook:** `cluster.yml` (the "Install Kubernetes nodes" play).
- **Hosts:** `k8s_cluster` (all control-plane and worker nodes).
- Runs before the control plane and kubeadm plays.

## Implementation

`playbooks/cluster.yml`:

```yaml
- { role: kubernetes/node, tags: node }
```

Task files include `install.yml`, `kubelet.yml`, and the local load-balancer
options under `loadbalancer/` (`nginx-proxy.yml`, `haproxy.yml`, `kube-vip.yml`;
see [[COMPONENT-KUBE_VIP]]). The role installs the kubelet binary and unit and
configures the node's access to the API server.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: `node` tags the `kubernetes/node` role in
  `cluster.yml`.
- **Standalone-run safety: risky.** Installs/reconfigures kubelet and the
  node load balancer; can restart kubelet. Depends on `download` and
  `container-engine` having run.

## References

- `playbooks/cluster.yml:32` — `node` tag.
- `roles/kubernetes/node/tasks/` — kubelet install and node load balancer.
- Verified on tags v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
