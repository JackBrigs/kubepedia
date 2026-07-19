---
id: TROUBLE-ADD_NODE_GOTCHAS
type: troubleshooting
title: "Add-node gotchas — new node stays empty/NotReady (facts not run, taint, CNI, podCIDR exhausted, version skew)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - new node no pods scheduling
  - added node NotReady
  - scale.yml facts first
  - node no podCIDR
  - kube_network_node_prefix exhausted
  - new node wrong version
  - control-plane node no workloads taint
tags:
  - troubleshooting
  - node
  - scaling
  - add-node
sources:
  - type: docs
    path: docs/operations/nodes.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/nodes.md
    note: "add worker: run facts then scale.yml --limit; podCIDR from kube_network_node_prefix over kube_pods_subnet"
  - type: code
    path: scale.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/scale.yml
    note: "scale converges only the new node; hostvars/certs need facts populated cluster-wide first"
relations:
  - type: see_also
    target: PRACTICE-RUNBOOK_ADD_NODES
  - type: see_also
    target: PRACTICE-NODES_ADD_REPLACE
  - type: see_also
    target: TROUBLE-KUBEADM_VERSION_SKEW
  - type: see_also
    target: TROUBLE-KUBEADM_JOIN_NODE
  - type: see_also
    target: TROUBLE-SCHEDULER_POD_PENDING
---

# Add-node gotchas — new node stays empty/NotReady (facts not run, taint, CNI, podCIDR exhausted, version skew)

## Summary

The playbook (`scale.yml` worker / `cluster.yml` control-plane — [[PRACTICE-RUNBOOK_ADD_NODES]])
finishes green, but the new node sits **empty** (`Ready`, no pods land) or **`NotReady`**. The usual
causes are all "correct behavior, wrong expectation": **facts weren't refreshed** cluster-wide first,
a **taint** repels workloads, the **CNI DaemonSet** hasn't come up, the node **couldn't get a podCIDR**
because the node-prefix block is exhausted, or the node came up on a **different patch version** (skew).

## Problem

- New worker is `Ready` but **no pods schedule** onto it.
- New node stuck **`NotReady`** ("network plugin not ready" / no CNI).
- New node never gets a **podCIDR**; its pods stay `Pending`.
- New node joined on a **different Kubernetes patch** than the rest.

## Context

- Applies across **v2.27.0–v2.31.0**. Worker add = `scale.yml`, control-plane add = `cluster.yml`
  ([[PRACTICE-RUNBOOK_ADD_NODES]], [[PRACTICE-NODES_ADD_REPLACE]]).
- **Facts not refreshed first:** `scale.yml --limit=<new>` converges only the new node, but existing
  nodes' hostvars must already know it (cert SANs, `/etc/hosts`, etcd/nginx-proxy endpoint lists). If
  you skip the **facts** pass, the new node can join with an incomplete view. Kubespray's guidance is
  to run **`playbooks/facts.yml`** (or `cluster.yml --tags facts`) across **all** nodes **before**
  `scale.yml`.
- **Taint repels workloads:** a control-plane node carries `node-role.kubernetes.io/control-plane:NoSchedule`
  by design — general workloads won't land unless they tolerate it (this is expected, not a bug). A
  worker with a custom `node_taints` entry behaves the same. Check taints before concluding "scheduling
  is broken" ([[TROUBLE-SCHEDULER_POD_PENDING]]).
- **CNI not up:** the node is `NotReady` until its CNI DaemonSet pod is `Running`. If the CNI image
  can't be pulled (air-gap / registry / `download_run_once` host unreachable), the node stays
  `NotReady` and no pod networking exists.
- **podCIDR block exhausted:** each node gets a `/kube_network_node_prefix` slice (default `/24`) carved
  from `kube_pods_subnet`. The **max node count = 2^(node_prefix − pods_subnet_prefix)**; past that, a
  new node **cannot be assigned a podCIDR** and its pods never get IPs. This is a **planning ceiling**,
  not something scale.yml can fix at add time.
- **Version skew:** if the new node pulls a different `kube_version`/image (stale registry cache,
  different `download` host), kubelet/kube-proxy skew rules apply
  ([[TROUBLE-KUBEADM_VERSION_SKEW]]).

## Diagnostics

```bash
kubectl get node <new> -o wide                              # Ready? version matches the rest?
kubectl describe node <new> | grep -A3 -iE 'taint|podcidr'  # taints + assigned PodCIDR (empty = exhausted)
kubectl get pods -A -o wide --field-selector spec.nodeName=<new> | grep -i cni  # CNI DS running?
kubectl get events -A --field-selector involvedObject.name=<new>
```

- Empty `PodCIDR` in `describe node` → block exhausted (or IPAM not assigned yet).
- CNI pod `ImagePullBackOff` → registry/air-gap ([[TROUBLE-KUBEADM_JOIN_NODE]]).

## Known Issues

- **Empty node, has a taint — fix:** expected for control-plane; for workers, remove the stray taint
  (`kubectl taint node <new> <key>-`) or add a matching toleration. Not a scheduler fault.
- **NotReady / no CNI — fix:** ensure the CNI image is reachable from the node (mirror/registry for
  air-gap); check the CNI DaemonSet rolled a pod onto it; re-run the CNI tag if needed.
- **No podCIDR (block exhausted) — fix:** this needs a **wider `kube_pods_subnet` or larger
  `kube_network_node_prefix` block**, which is a cluster-wide re-plan (not a live add) — size the pod
  CIDR for the target node count up front ([[PRACTICE-NODES_ADD_REPLACE]]).
- **Skew — fix:** align `kube_version` and the image source so the new node matches
  ([[TROUBLE-KUBEADM_VERSION_SKEW]]).
- **Prevent:** run **`facts.yml` across all nodes first**, then `scale.yml --limit=<new>`; verify the
  new node's `PodCIDR`, taints, CNI pod, and version in one pass before handing it back.

## References

- `docs/operations/nodes.md`, `scale.yml` (tag `v2.31.0`). Runbook [[PRACTICE-RUNBOOK_ADD_NODES]];
  mechanics [[PRACTICE-NODES_ADD_REPLACE]]; join failures [[TROUBLE-KUBEADM_JOIN_NODE]]; skew
  [[TROUBLE-KUBEADM_VERSION_SKEW]]; scheduling [[TROUBLE-SCHEDULER_POD_PENDING]].
