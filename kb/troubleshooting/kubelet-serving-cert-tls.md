---
id: TROUBLE-KUBELET_SERVING_CERT_TLS
type: troubleshooting
title: "kubectl top / metrics-server x509 on the kubelet serving certificate"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - metrics-server x509 kubelet
  - kubectl top metrics api not available
  - cannot validate certificate for because it doesn't contain any IP SANs
  - kubelet serving certificate self-signed
  - serverTLSBootstrap
  - kubelet_rotate_server_certificates
  - kubelet-csr-approver pending CSR
tags:
  - troubleshooting
  - kubelet
  - certificates
  - metrics-server
  - tls
sources:
  - type: code
    path: roles/kubernetes-apps/kubelet-csr-approver/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/kubelet-csr-approver/defaults/main.yml
    note: "kubelet_csr_approver_enabled = kubelet_rotate_server_certificates (tag v2.31.0)"
  - type: code
    path: roles/kubernetes-apps/metrics_server/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/metrics_server/defaults/main.yml
    note: "metrics_server_kubelet_insecure_tls: true (tag v2.31.0)"
relations:
  - type: see_also
    target: CONFIG-KUBELET_CONFIGURATION
  - type: see_also
    target: VARIABLE-KUBELET_ROTATE_SERVER_CERTIFICATES
  - type: see_also
    target: COMPONENT-METRICS_SERVER
---

# kubectl top / metrics-server x509 on the kubelet serving certificate

## Summary

By default Kubespray leaves the kubelet **serving** certificate **self-signed**
(`kubelet_rotate_server_certificates: false`). `kubectl top` still works only because
metrics-server is deployed with `--kubelet-insecure-tls`
(`metrics_server_kubelet_insecure_tls: true`). Turn that verification back on without
also giving the kubelet a cluster-signed serving cert, and metrics-server (and other
kubelet-TLS clients) fail with `x509`. The proper fix is to enable server-cert rotation,
which also auto-deploys the CSR approver that signs the kubelet serving certs.

## Problem

- `kubectl top nodes` / `kubectl top pods` → `Metrics API not available` / `error: metrics
  not available yet`.
- metrics-server logs: `x509: cannot validate certificate for <node-ip> because it
  doesn't contain any IP SANs`, or `certificate signed by unknown authority`.
- Or, after enabling server-cert rotation: kubelet has no serving cert and
  `CertificateSigningRequest`s sit **Pending**.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`. Relevant defaults:
  - `kubelet_rotate_server_certificates: false` — kubelet does **not** request a
    cluster-signed serving cert; it self-signs (`serverTLSBootstrap` unset in the
    kubelet config — see [[CONFIG-KUBELET_CONFIGURATION]]).
  - `metrics_server_kubelet_insecure_tls: true` — metrics-server skips kubelet cert
    verification, so `kubectl top` works despite the self-signed cert.
  - `kubelet_csr_approver_enabled: "{{ kubelet_rotate_server_certificates }}"` — the
    kubelet-csr-approver add-on is deployed **only** when server-cert rotation is on.
- So out of the box everything works via the insecure-tls shortcut. Problems appear when
  you tighten TLS **without** wiring up proper serving certs.

## Diagnostics

- metrics-server: `kubectl -n kube-system logs deploy/metrics-server` → look for the
  `x509` line naming the kubelet cert problem.
- kubelet serving cert: on a node, inspect `/var/lib/kubelet/pki/kubelet.crt` (self-signed
  if rotation is off).
- If rotation is on: `kubectl get csr` — kubelet serving CSRs should be `Approved,Issued`;
  `Pending` means no approver is signing them.
- Confirm the knobs: `metrics_server_kubelet_insecure_tls` and
  `kubelet_rotate_server_certificates` in your inventory.

## Known Issues

**Two supported configurations — pick one, don't half-do it:**

1. **Default / insecure-tls (simplest):** keep `kubelet_rotate_server_certificates:
   false` **and** `metrics_server_kubelet_insecure_tls: true`. `kubectl top` works; the
   kubelet serving cert is not verified. Do **not** set
   `metrics_server_kubelet_insecure_tls: false` in this mode — that causes the `x509`.
2. **Verified TLS (proper):** set `kubelet_rotate_server_certificates: true`. This makes
   the kubelet request a cluster-signed serving cert (`serverTLSBootstrap: true`) **and**
   auto-enables **kubelet-csr-approver** (`kubelet_csr_approver_enabled` follows the same
   variable) to approve those CSRs. Then you may set
   `metrics_server_kubelet_insecure_tls: false` for real verification.

**Gotchas:**

- **Don't enable `serverTLSBootstrap` by hand** without an approver — the kubelet's
  serving CSRs stay `Pending`, the kubelet has no serving cert, and `kubectl logs/exec`,
  metrics, and probes to the kubelet break. Use `kubelet_rotate_server_certificates`,
  which brings the approver with it.
- The self-signed kubelet cert has **no IP SANs**, which is exactly why strict
  verification fails — verification requires the rotated, cluster-signed cert.
- This is about the kubelet **serving** cert; the kubelet **client** cert rotation is
  separate (`kubelet_rotate_certificates: true`, default on) — see
  [[VARIABLE-KUBELET_ROTATE_SERVER_CERTIFICATES]] and [[CONFIG-KUBELET_CONFIGURATION]].

## References

- kubelet-csr-approver defaults (`kubelet_csr_approver_enabled`) and metrics_server
  defaults (`metrics_server_kubelet_insecure_tls`) at tag `v2.31.0`.
- Component: [[COMPONENT-METRICS_SERVER]]; kubelet config: [[CONFIG-KUBELET_CONFIGURATION]].
