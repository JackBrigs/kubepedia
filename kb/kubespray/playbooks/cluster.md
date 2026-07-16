---
id: PLAYBOOK-CLUSTER
type: playbook
title: cluster.yml
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cluster.yml
tags:
  - playbook
  - install
sources:
  - type: code
    path: playbooks/cluster.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/cluster.yml
    note: "top-level cluster deploy playbook"
relations:
  - type: see_also
    target: TAG-ETCD
  - type: see_also
    target: TAG-CONTROL_PLANE
  - type: see_also
    target: TAG-NETWORK
---

# cluster.yml

## Summary

`cluster.yml` is the main playbook that deploys a full Kubernetes cluster from
scratch. It lays components down in a fixed order across the inventory groups.
The root `cluster.yml` imports `playbooks/cluster.yml`.

## Implementation

Play sequence (`playbooks/cluster.yml`):

1. **Prepare for etcd install** (`k8s_cluster:etcd`) — `kubernetes/preinstall`
   (`preinstall`), `container-engine` (`container-engine`, when
   `deploy_container_engine`), `download` (`download`, when not `skip_downloads`).
2. **Install etcd** — imports `install_etcd.yml` (role `etcd`, tags `etcd` /
   `etcd-secrets`).
3. **Install Kubernetes nodes** (`k8s_cluster`) — `kubernetes/node` (`node`).
4. **Install the control plane** (`kube_control_plane`) —
   `kubernetes/control-plane` (`control-plane`), `kubernetes/client` (`client`),
   `kubernetes-apps/cluster_roles` (`cluster-roles`).
5. **Invoke kubeadm and install a CNI** (`k8s_cluster`) — `kubernetes/kubeadm`
   (`kubeadm`), `node-label`, `node-taint`, `network_plugin` (`network`).
6. **Install Kubernetes apps** (`kube_control_plane`) — external cloud/policy/
   ingress controllers, external provisioner, `kubernetes-apps` (`apps`).
7. **Apply resolv.conf** once cluster DNS is up (`resolvconf`).

Every stage is tag-scoped (see the corresponding `TAG-*` docs), so partial runs
are possible with `--tags`.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: the play order and tags above are stable.
- For upgrades of an existing cluster use `upgrade-cluster.yml`
  ([[PLAYBOOK-UPGRADE_CLUSTER]]); to add nodes use `scale.yml`
  ([[PLAYBOOK-SCALE]]).

## References

- `playbooks/cluster.yml` (tag `v2.31.0` `1c9add4`).
- Root `cluster.yml` imports it.
