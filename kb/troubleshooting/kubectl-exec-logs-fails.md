---
id: TROUBLE-KUBECTL_EXEC_LOGS_FAILS
type: troubleshooting
title: "kubectl exec / logs / port-forward fails (kubelet reachability)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - kubectl exec error
  - kubectl logs timeout
  - error dialing backend
  - unable to upgrade connection
  - port-forward failed
  - x509 kubelet exec
  - 10250 unreachable
tags:
  - troubleshooting
  - kubectl
  - kubelet
  - networking
sources:
  - type: docs
    path: Kubernetes kubelet authn/authz + apiserver-to-kubelet
    url: https://kubernetes.io/docs/concepts/architecture/control-plane-node-communication/
    note: "exec/logs/port-forward flow apiserver -> kubelet :10250"
relations:
  - type: see_also
    target: TROUBLE-KUBELET_SERVING_CERT_TLS
  - type: see_also
    target: TROUBLE-FIREWALL_PORTS_BLOCKED
  - type: see_also
    target: PRACTICE-NODE_NOT_READY
---

# kubectl exec / logs / port-forward fails (kubelet reachability)

## Summary

`kubectl exec`, `logs`, `port-forward`, and `top` all go **apiserver → kubelet on port
10250**. When they fail with `error dialing backend` / `unable to upgrade connection` /
timeout / `x509`, the pod is usually fine — the **apiserver-to-kubelet path** is broken:
port 10250 blocked, the kubelet's serving cert isn't trusted, or the node is unreachable.

## Problem

`kubectl exec/logs/port-forward <pod>` returns `Error from server: error dialing backend:
…` / `unable to upgrade connection` / `remote error: tls: …` / a timeout — often for pods
on **specific** nodes only.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- The apiserver connects to the kubelet's HTTPS API on **`10250`** to stream these
  commands. Anything blocking or breaking that hop fails all four verbs.

## Diagnostics

- **Which nodes?** If it fails only for pods on certain nodes, focus on those nodes'
  kubelet/network; if all nodes, a cluster-wide cause.
- **Reachability:** from a control-plane node `nc -vz <node> 10250` — is the kubelet API
  reachable? Blocked → firewall ([[TROUBLE-FIREWALL_PORTS_BLOCKED]]).
- **Node/kubelet health:** `kubectl get node <node>` (Ready?), `journalctl -u kubelet -e`
  on the node.
- **Cert errors** (`x509`) — the apiserver can't verify the kubelet serving cert; see the
  serving-cert modes ([[TROUBLE-KUBELET_SERVING_CERT_TLS]]).
- **Pod state:** `exec`/`logs` need a **running** container — a crash-looping/pending pod
  has nothing to attach to ([[TROUBLE-CRASHLOOPBACKOFF]]).

## Known Issues

Map the error to its cause:

- **`error dialing backend` / timeout** — apiserver can't reach kubelet `10250`: host
  firewall or security-group blocking the port between control-plane and node
  ([[TROUBLE-FIREWALL_PORTS_BLOCKED]]), or the node is down/NotReady
  ([[PRACTICE-NODE_NOT_READY]]).
- **`x509` / `tls`** — kubelet serving-cert trust: the default self-signed kubelet cert
  isn't verifiable if strict verification is on; use the rotated/CSR-approved serving cert
  or the insecure-tls path as appropriate ([[TROUBLE-KUBELET_SERVING_CERT_TLS]]).
- **`unable to upgrade connection: Unauthorized`** — kubelet authorization (webhook) is
  rejecting the apiserver, or RBAC for the `nodes/proxy` / `nodes/log` subresources is
  missing.
- **`container not found` / `is not running`** — the pod isn't running; fix the pod first,
  not the connection.

**Gotchas:**

- `logs` from the **apiserver** (streamed live) fails on this path, but past logs may still
  be on the node — `crictl logs` on the node bypasses the apiserver→kubelet hop for
  diagnosis.
- A working `kubectl get`/`apply` but failing `exec/logs` **confirms** it's the
  apiserver→kubelet hop (10250), not general apiserver access (6443).
- `top` failing is the same 10250 path plus metrics-server
  ([[TROUBLE-KUBELET_SERVING_CERT_TLS]]).

## References

- Kubernetes control-plane↔node communication. Ports: [[TROUBLE-FIREWALL_PORTS_BLOCKED]];
  serving cert: [[TROUBLE-KUBELET_SERVING_CERT_TLS]]; node health: [[PRACTICE-NODE_NOT_READY]].
