---
id: PLAYBOOK-SCALE
type: playbook
title: scale.yml
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - scale.yml
tags:
  - playbook
  - scaling
sources:
  - type: code
    path: playbooks/scale.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/scale.yml
    note: "add worker nodes to an existing cluster"
relations:
  - type: see_also
    target: PRACTICE-NODES_ADD_REPLACE
  - type: see_also
    target: TAG-NODE
---

# scale.yml

## Summary

`scale.yml` adds new (worker) nodes to an existing cluster without disturbing the
running control plane. It runs preparation, etcd client-cert distribution, and the
node/kubeadm/network steps on the new nodes.

## Implementation

Play sequence (`playbooks/scale.yml`):

1. `boilerplate.yml` + `internal_facts.yml`.
2. **Install etcd** (`install_etcd.yml`) — distributes etcd client certs where a
   CNI needs them.
3. Download images once via `kube_control_plane[0]` (when
   `download_run_once and not download_localhost`).
4. Target the new/worker nodes to install kubelet (`node`), run `kubeadm` join,
   and apply the CNI (`network`).

Use `--limit=NODE_NAME` to restrict the run; first run `facts.yml` without a limit
to refresh the fact cache. See [[PRACTICE-NODES_ADD_REPLACE]].

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- For **removing** a node use `remove-node.yml` ([[PLAYBOOK-REMOVE_NODE]]).
- Control-plane/etcd node changes need extra care for quorum — `scale.yml` targets
  workers.

## References

- `playbooks/scale.yml` (tag `v2.31.0` `1c9add4`).
- Root `scale.yml` imports it.
