---
id: PRACTICE-SECRETS_ENCRYPTION_AT_REST
type: best_practice
title: "Encrypting Secret data at rest (provider choice)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - secrets-encryption-at-rest
tags:
  - operations
  - security
sources:
  - type: docs
    path: docs/operations/encrypting-secret-data-at-rest.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/encrypting-secret-data-at-rest.md
    note: "digest of the tag doc"
relations:
  - type: see_also
    target: VARIABLE-KUBE_ENCRYPT_SECRET_DATA
---

# Encrypting Secret data at rest (provider choice)

## Summary

Kubespray can enable encryption of Kubernetes Secrets at rest in etcd. When enabled, Kubespray's default provider is **secretbox** (XSalsa20/Poly1305). Alternatives: `identity` (no encryption), `aesgcm`, `aescbc`, `kms`.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- Enabled via [[VARIABLE-KUBE_ENCRYPT_SECRET_DATA]] (default `false`).

## Implementation

Provider trade-offs (from the doc): `identity` = none; `aesgcm` must be rotated every ~200k writes; `aescbc` not recommended (padding-oracle); `kms` is the official recommendation but needs an external KMS. Kubespray defaults to `secretbox` as a safe general choice. Enabling after install requires rewriting existing Secrets so they get encrypted. See [[PRACTICE-HARDENING]].

## References

- `docs/operations/encrypting-secret-data-at-rest.md` (tag v2.31.0 `1c9add4`).
