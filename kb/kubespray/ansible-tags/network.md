---
id: TAG-NETWORK
type: ansible_tag
title: network (Ansible run-tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - network
  - --tags network
tags:
  - ansible-tag
  - cni
  - networking
sources:
  - type: code
    path: playbooks/cluster.yml
    lines: "56,65"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/cluster.yml
    note: "role network_plugin tagged network; calico/rr tagged ['network','calico_rr']"
  - type: code
    path: roles/network_plugin/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/tasks/main.yml
    note: "dispatches to the CNI sub-role selected by kube_network_plugin"
relations:
  - type: see_also
    target: VARIABLE-KUBE_NETWORK_PLUGIN
  - type: see_also
    target: COMPONENT-CILIUM
---

# network (Ansible run-tag)

## Summary

`network` runs the `network_plugin` role, which installs and configures the CNI
selected by [[VARIABLE-KUBE_NETWORK_PLUGIN]] (`calico` by default; `cilium` and
others are options — see [[COMPONENT-CILIUM]]). It deploys the CNI manifests/
DaemonSets so pod networking and network policy come up.

## Context

- **Playbook:** `cluster.yml` (the "Invoke kubeadm and install a CNI" play, and
  the "Install Calico Route Reflector" play).
- **Hosts:** `k8s_cluster` (and `calico_rr` for the route-reflector sub-role).
- Runs after `kubeadm` has bootstrapped the nodes.

## Implementation

`playbooks/cluster.yml`:

```yaml
- { role: network_plugin, tags: network }
...
- { role: network_plugin/calico/rr, tags: ['network', 'calico_rr'] }
```

`roles/network_plugin/tasks/main.yml` dispatches to the CNI sub-role chosen by
`kube_network_plugin`. The Calico route-reflector sub-role additionally carries
the `calico_rr` tag for targeted runs.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: `network` tags the `network_plugin` role in
  `cluster.yml`.
- **Standalone-run safety: risky.** Re-applies CNI manifests; can disrupt pod
  networking mid-change. Requires an initialized cluster (kubeadm done).

## References

- `playbooks/cluster.yml:56,65` — `network` tag on `network_plugin` and the
  Calico route reflector.
- `roles/network_plugin/tasks/main.yml` — CNI dispatch.
- Verified on tags v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
