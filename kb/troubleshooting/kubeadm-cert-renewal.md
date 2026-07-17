---
id: TROUBLE-KUBEADM_CERT_RENEWAL
type: troubleshooting
title: "Control-plane cert renewal via the seam (kubeadm certs renew)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - kubeadm certs renew all
  - k8s-certs-renew.sh
  - control plane certificate expired
  - kubeadm certs check-expiration
  - renew certs kubespray
  - certs valid 100 years myth
tags:
  - troubleshooting
  - kubeadm
  - certificates
  - control-plane
sources:
  - type: code
    path: roles/kubernetes/control-plane/templates/k8s-certs-renew.sh.j2
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/templates/k8s-certs-renew.sh.j2
    note: "Kubespray ships a renew script → kubeadm certs renew all"
  - type: docs
    path: kubeadm certificate management
    url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/
relations:
  - type: see_also
    target: CONCEPT-KUBESPRAY_KUBEADM_SEAM
  - type: see_also
    target: CONCEPT-CLUSTER_PKI
  - type: see_also
    target: CONCEPT-K8S_1_29_CHANGES
---

# Control-plane cert renewal via the seam (kubeadm certs renew)

## Summary

Control-plane certificate renewal is **kubeadm's** job, and Kubespray deploys a script
(`k8s-certs-renew.sh`) that runs **`kubeadm certs renew all`**. Two things bite operators: certs
that quietly **expire** (kubeadm renews CP certs on every upgrade, but a cluster that never
upgrades for ~a year expires), and the fact that **kubeadm does not restart the control-plane
static pods** after renewal — you must.

## Problem

- CP components fail TLS: `x509: certificate has expired or is not yet valid` on apiserver/etcd/
  kubelet client certs; `kubectl` stops working after ~1 year with no upgrades.
- After renewing certs, components still present the **old** cert.

## Context

- Applies to Kubespray **v2.29.0–v2.31.0** / Kubernetes **1.29–1.35**. kubeadm-managed CP certs
  live in `/etc/kubernetes/pki`; default validity is **1 year** (the CA is 10 years). PKI layout:
  [[CONCEPT-CLUSTER_PKI]].

## Diagnostics

- **Check first:** `kubeadm certs check-expiration` lists every cert + its expiry and whether
  it's externally managed.
- **Renew:** run **`kubeadm certs renew all`** (what Kubespray's `k8s-certs-renew.sh` does) — or
  run the Kubespray upgrade play, which renews on the way. Renewal uses the existing CA (no CA
  change, so nodes keep trusting).
- **Restart the CP static pods** after renewal — kubeadm **doesn't** do it: move the manifests
  out/in of `/etc/kubernetes/manifests` (or `crictl rm`/reboot) so apiserver/controller-manager/
  scheduler/etcd reload the new certs. This is the step most people miss.
- **admin.conf / super-admin.conf (1.29+):** kubeadm split the admin credential — `admin.conf`
  (bound to `kubeadm:cluster-admins`) and the break-glass `super-admin.conf`
  ([[CONCEPT-K8S_1_29_CHANGES]]); renew/regenerate the one you actually use.
- **kubelet client cert** rotates automatically (bootstrap); the **kubelet serving** cert is a
  separate path ([[TROUBLE-KUBELET_SERVING_CERT_ROTATION]]).

## Known Issues

- **Externally-managed / custom CA:** `kubeadm certs renew` can't renew certs signed by an
  external CA — re-issue them out-of-band.
- Let CP certs get close to expiry across all masters and you can lose the whole control plane at
  once — monitor `check-expiration` or upgrade regularly (each upgrade renews).

## References

- `k8s-certs-renew.sh.j2` (v2.31.0) + kubeadm cert docs (above); PKI: [[CONCEPT-CLUSTER_PKI]];
  seam: [[CONCEPT-KUBESPRAY_KUBEADM_SEAM]]; 1.29 admin split: [[CONCEPT-K8S_1_29_CHANGES]].
