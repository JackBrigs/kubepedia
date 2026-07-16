---
id: PLAYBOOK-RESET
type: playbook
title: reset.yml
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - reset.yml
tags:
  - playbook
  - reset
  - destructive
sources:
  - type: code
    path: playbooks/reset.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/reset.yml
    note: "tears the whole cluster back down"
relations:
  - type: see_also
    target: TAG-RESET
---

# reset.yml

## Summary

`reset.yml` tears an entire cluster back down: it runs the `reset` role on
`etcd:k8s_cluster:calico_rr`, removing Kubernetes, etcd, container-runtime state,
CNI, and Kubespray-managed configuration/certificates. It is the most destructive
playbook and prompts for confirmation first.

## Implementation

`playbooks/reset.yml`: hosts `etcd:k8s_cluster:calico_rr`, role `reset`
(tag `reset`, see [[TAG-RESET]]). The role stops/removes cluster services,
unmounts and deletes data directories, and cleans up CNI network interfaces.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Destructive and not reversible.** Intended for wiping a cluster; to remove a
  single node instead use `remove-node.yml` ([[PLAYBOOK-REMOVE_NODE]]).

## References

- `playbooks/reset.yml` (tag `v2.31.0` `1c9add4`).
- Root `reset.yml` imports it.
