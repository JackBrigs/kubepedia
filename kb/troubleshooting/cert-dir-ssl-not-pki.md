---
id: TROUBLE-CERT_DIR_SSL_NOT_PKI
type: troubleshooting
title: "Myth: 'copy CA into /etc/kubernetes/pki' — Kubespray uses /etc/kubernetes/ssl"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - kubeadm expects pki directory
  - copy CA to /etc/kubernetes/pki
  - certificatesDir kubespray
  - certificate directory ssl vs pki
  - init first master certificate stuck
tags:
  - troubleshooting
  - certificates
  - kubeadm
  - myth
sources:
  - type: code
    path: roles/kubernetes/control-plane/templates/kubeadm-config.v1beta4.yaml.j2
    lines: "124"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/templates/kubeadm-config.v1beta4.yaml.j2
    note: "certificatesDir: {{ kube_cert_dir }} => /etc/kubernetes/ssl (kubeadm is told to use ssl, not pki)"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_cert_dir: {{ kube_config_dir }}/ssl (re-verified; community advice to copy CA into pki is outdated)"
relations:
  - type: see_also
    target: CONCEPT-CLUSTER_PKI
  - type: see_also
    target: CONCEPT-KUBEADM_CONFIG
  - type: see_also
    target: PRACTICE-KUBEADM_JOIN_FAILURES
---

# Myth: "copy CA into /etc/kubernetes/pki" — Kubespray uses /etc/kubernetes/ssl

## Summary

A widely-repeated community "fix" claims that **kubeadm expects certificates in
`/etc/kubernetes/pki` but Kubespray puts them in `/etc/kubernetes/ssl`, so you must create
`pki/` and copy the CA there**. This is a **myth / outdated advice**. Kubespray tells
kubeadm to use its own directory via the generated `certificatesDir: /etc/kubernetes/ssl`
in the kubeadm config — so kubeadm looks in `ssl`, not `pki`. Manually copying certs into
`pki/` is unnecessary and can mask the real problem.

## Problem

You hit a stuck deploy (e.g. "kubeadm | Initialize first control plane") or a certificate
error and find advice online to `mkdir /etc/kubernetes/pki` and copy the CA there. You're
unsure whether Kubespray is misconfigured.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- Kubespray's `kube_cert_dir` default is **`{{ kube_config_dir }}/ssl`** =
  `/etc/kubernetes/ssl`, and the generated **kubeadm config** sets
  `certificatesDir: {{ kube_cert_dir }}` — i.e. kubeadm is explicitly pointed at
  `/etc/kubernetes/ssl`. There is no mismatch; kubeadm and Kubespray agree on `ssl`.

## Diagnostics

- Confirm on a control-plane node: `grep certificatesDir /etc/kubernetes/kubeadm-config.yaml`
  → it reads `/etc/kubernetes/ssl`.
- The etcd/apiserver/CA certs live under `/etc/kubernetes/ssl/` (and `ssl/etcd/` for etcd)
  — that is the correct, expected location, not a bug.

## Known Issues

- **Do not** create `/etc/kubernetes/pki` and copy the CA there to "fix" a stuck init — it
  addresses a non-problem and can leave stale/duplicate certs. Kubespray manages certs in
  `ssl/`.
- If the first-control-plane init is genuinely stuck, the cause is elsewhere — the kubelet
  not coming up, a failed preflight, a runtime issue, etc.
  ([[PRACTICE-KUBEADM_JOIN_FAILURES]]). Diagnose that, not the cert directory.
- Vanilla kubeadm (outside Kubespray) does default to `/etc/kubernetes/pki`; the confusion
  comes from applying vanilla-kubeadm folklore to a Kubespray cluster, where
  `certificatesDir` is overridden. Trust the generated `certificatesDir`.

## References

- `kubeadm-config.v1beta4.yaml.j2:124` (`certificatesDir: {{ kube_cert_dir }}`) and
  `kube_cert_dir` default at tag `v2.31.0`. PKI lifecycle: [[CONCEPT-CLUSTER_PKI]]; kubeadm
  config: [[CONCEPT-KUBEADM_CONFIG]].
