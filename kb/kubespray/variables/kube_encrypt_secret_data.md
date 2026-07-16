---
id: VARIABLE-KUBE_ENCRYPT_SECRET_DATA
type: variable
title: kube_encrypt_secret_data
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - kube_encrypt_secret_data
tags:
  - security
  - hardening
  - apiserver
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    lines: "197 (v2.31.0)"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "kube_encrypt_secret_data: false (default, unchanged v2.29.0–v2.31.0)"
relations:
  - type: see_also
    target: TAG-CONTROL_PLANE
---

# kube_encrypt_secret_data

## Summary

`kube_encrypt_secret_data` enables encryption at rest for Kubernetes Secrets in
etcd. The default is `false` across `v2.29.0`–`v2.31.0`; enabling it configures
the API server's `EncryptionConfiguration`.

## Implementation

Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` (`false`,
unchanged across all four tags). When `true`, Kubespray generates an encryption
config and points the API server at it so Secret data is encrypted in etcd.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: default `false`.
- A hardening control: recommended for production. Enabling it after install
  requires re-writing existing Secrets to encrypt them.

## References

- `roles/kubernetes/control-plane/defaults/main/main.yml` — default (L194 in
  v2.29.0, L197 in v2.31.0; shifts by tag).
- Tags: v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
