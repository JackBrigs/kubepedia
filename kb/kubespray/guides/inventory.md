---
id: PRACTICE-INVENTORY
type: best_practice
title: Kubespray inventory structure and host groups
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - inventory groups
tags:
  - inventory
  - ansible
sources:
  - type: docs
    path: docs/ansible/inventory.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/ansible/inventory.md
    note: "Inventory group model, node role assignment, bastion host, and a full inventory example"
relations:
  - type: see_also
    target: CONCEPT-SAMPLE_INVENTORY_LAYOUT
---

# Kubespray inventory structure and host groups

## Summary
Kubespray inventory is organized around three primary groups plus two special groups. Which group(s) a host belongs to determines its role: control plane, worker node, etcd member, or a combination. Understanding group membership is the foundation for laying out standalone vs. schedulable control planes and colocated vs. dedicated etcd.

## Context
Applies when authoring or editing the Ansible inventory before running any Kubespray playbook. Group membership decides node roles; cluster-wide variables are set under `<inventory>/group_vars/k8s_cluster/*.yml`. See the companion Ansible vars guide for how customization layers interact.

## Implementation
Three primary groups:

- **kube_node** — Kubernetes worker nodes where pods run.
- **kube_control_plane** — servers running control plane components (apiserver, scheduler, controller-manager).
- **etcd** — servers forming the etcd cluster; use at least 3 for failover.

Role composition rules:

- If a host is in both `kube_control_plane` and `kube_node`, it acts as both control plane and worker.
- A standalone, unschedulable control plane host must be in `kube_control_plane` only, not `kube_node`.
- If `kube_node` overlaps with `etcd`, etcd nodes become schedulable for workloads. Keep the groups disjoint for standalone etcd.

Two special groups:

- **calico_rr** — for advanced Calico route-reflector networking (see docs/CNI/calico.md).
- **bastion** — a jump host used when nodes are not directly reachable.

Derived group:

- **k8s_cluster** is dynamically computed as the union of `kube_node`, `kube_control_plane`, and `calico_rr`. It is used internally and as the target for whole-cluster variables in `group_vars/k8s_cluster/*.yml`.

Full inventory example (INI): per-host lines set `ansible_host` (SSH-reachable address) and `ip` (address to bind Kubernetes services on, useful when it differs from the default interface):

```ini
node1 ansible_host=95.54.0.12 ip=10.3.0.1
node2 ansible_host=95.54.0.13 ip=10.3.0.2
node3 ansible_host=95.54.0.14 ip=10.3.0.3

[kube_control_plane]
node1
node2

[etcd]
node1
node2
node3

[kube_node]
node2
node3
node4
```

Bastion host: add a `[bastion]` section pointing at the bastion's public IP so Ansible tunnels to private-only nodes.

```ShellSession
[bastion]
bastion ansible_host=x.x.x.x
```

## References
- docs/ansible/inventory.md (tag v2.31.0 1c9add4)
