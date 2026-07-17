---
id: TROUBLE-KUBEADM_JOIN_NODE
type: troubleshooting
title: "kubeadm join fails (token, discovery CA hash, API reachability)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - kubeadm join failed
  - node not joining cluster
  - discovery token ca cert hash
  - token expired kubeadm join
  - couldn't validate the identity of the API server
tags:
  - troubleshooting
  - kubeadm
  - nodes
  - join
sources:
  - type: code
    path: roles/kubernetes/kubeadm/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/kubeadm/tasks/main.yml
    note: "worker kubeadm join --ignore-preflight-errors"
  - type: code
    path: roles/kubernetes/control-plane/tasks/kubeadm-secondary.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/tasks/kubeadm-secondary.yml
    note: "secondary control-plane kubeadm join"
relations:
  - type: see_also
    target: CONCEPT-KUBESPRAY_KUBEADM_SEAM
  - type: see_also
    target: TROUBLE-KUBEADM_PREFLIGHT
---

# kubeadm join fails (token, discovery CA hash, API reachability)

## Summary

Adding a node (worker or secondary control-plane) fails at **`kubeadm join`**. Kubespray runs
join in `kubernetes/kubeadm` (worker) and `control-plane/kubeadm-secondary.yml` (CP) — a failure
is kubeadm's, surfaced by Ansible ([[CONCEPT-KUBESPRAY_KUBEADM_SEAM]]). The usual causes are a
bad/expired **token**, a wrong **discovery CA hash**, or the node can't reach the API.

## Problem

- `kubeadm join` errors: `couldn't validate the identity of the API Server`, `token … not found`
  / `token has expired`, `could not find a JWS signature`, discovery timeout.
- The new node never appears / stays `NotReady`.

## Context

- Applies to Kubespray **v2.29.0–v2.31.0** / Kubernetes **1.29–1.35**. Kubespray generates a
  fresh bootstrap token per run, so token-expiry is rarely the issue on a normal re-run.

## Diagnostics

- **API reachability:** the joining node must reach the control-plane endpoint (VIP/LB) on
  **6443** — check routing/firewall ([[TROUBLE-FIREWALL_PORTS_BLOCKED]]) and that the endpoint
  resolves. A CP join also needs etcd/2379-2380 reachability.
- **Discovery CA hash mismatch** (`couldn't validate the identity of the API Server`): the
  `--discovery-token-ca-cert-hash` must match the cluster CA — a stale hash (CA changed, or
  joining the wrong cluster) fails. Kubespray recomputes it; a mismatch usually means the node
  has stale `/etc/kubernetes` from a prior cluster — clean it
  ([[TROUBLE-KUBEADM_INIT_RETRY_FAILS]]).
- **Token expired/not found:** bootstrap tokens are short-lived; if you join manually later,
  generate a new one (`kubeadm token create --print-join-command`). On a Kubespray run the token
  is fresh.
- **Preflight on the joining node:** join runs preflight too — port/CRI/cgroup/leftover-file
  errors ([[TROUBLE-KUBEADM_PREFLIGHT]]); Kubespray passes `--ignore-preflight-errors`.
- **Secondary CP specifics:** the control-plane certs must be uploaded/available
  (`--certificate-key`); an expired upload or missing certs fails the CP join.

## Known Issues

- Re-joining a node that was removed without cleanup fails on leftovers in `/etc/kubernetes` and
  `/var/lib/etcd` — reset the node first ([[TROUBLE-KUBEADM_INIT_RETRY_FAILS]]).

## References

- `kubeadm/tasks/main.yml` + `kubeadm-secondary.yml` (v2.31.0, above); seam:
  [[CONCEPT-KUBESPRAY_KUBEADM_SEAM]]; preflight: [[TROUBLE-KUBEADM_PREFLIGHT]].
