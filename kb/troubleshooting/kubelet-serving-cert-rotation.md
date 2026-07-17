---
id: TROUBLE-KUBELET_SERVING_CERT_ROTATION
type: troubleshooting
title: "kubelet: serving cert rotation silently skipped → :10250 TLS failures"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: probable
aliases:
  - kubelet serving cert not rotating
  - kubelet-serving CSR not auto-approved
  - certificate expired 10250
  - rotate-server-certificates
tags:
  - troubleshooting
  - kubelet
  - certificates
  - tls
sources:
  - type: docs
    path: kubelet serving-cert rotation skip issue
    url: https://github.com/kubernetes/kubernetes/issues/138763
    note: "rotation returns without rescheduling when template nil"
  - type: docs
    path: Certificate rotation
    url: https://kubernetes.io/docs/tasks/tls/certificate-rotation/
relations:
  - type: see_also
    target: TROUBLE-KUBELET_SERVING_CERT_TLS
  - type: see_also
    target: CONCEPT-CLUSTER_PKI
---

# kubelet: serving cert rotation silently skipped → :10250 TLS failures

## Summary

On a subset of **long-lived nodes** the kubelet serving certificate **never rotates** — no CSR,
no error — and eventually expires, breaking TLS on **:10250** (metrics-server, `kubectl
top`/`logs`/`exec`). A transient empty node status at the rotation deadline wedges the loop for
the node's lifetime.

## Problem

- `kubelet_certificate_manager_server_rotation_seconds_count` stays **0** for 38+ days on some
  nodes; no `kubelet-serving` CSR submitted; then serving-cert expiry → x509 on :10250.

## Context

- Applies to Kubernetes **1.29–1.35** (reported 1.34.4, EKS/Bottlerocket, ~15–20% of long-lived
  nodes; **root cause not maintainer-confirmed** — `confidence: probable`, issue #138763). The
  x509-at-use symptom overlaps [[TROUBLE-KUBELET_SERVING_CERT_TLS]].

## Diagnostics

- **Mechanism:** the rotation routine does `if getTemplate() == nil { return }` **without
  rescheduling** — if the node informer transiently returns empty `status.addresses` exactly at
  the rotation deadline, the loop exits and never re-enters for that node.
- **Prerequisite often missed:** `kubernetes.io/kubelet-serving` CSRs are **NOT auto-approved**
  by default — you need an **approver controller** (e.g. a signer that approves node-serving
  CSRs), plus `--rotate-server-certificates` on the kubelet.
- **Mitigation (bug open):** **recycle long-lived nodes** before the rotation window (cap node
  lifetime — e.g. Karpenter `expireAfter ~35d`); verify `--rotate-server-certificates` is on and
  an approver exists.

## Known Issues

- Distinct from the metrics-server x509 caused by an **unsigned/self-signed** serving cert
  ([[TROUBLE-KUBELET_SERVING_CERT_TLS]]) — here the cert simply **expired** because rotation
  stalled.

## References

- k8s issue #138763 + cert-rotation docs (above); at-use symptom:
  [[TROUBLE-KUBELET_SERVING_CERT_TLS]]; PKI: [[CONCEPT-CLUSTER_PKI]].
