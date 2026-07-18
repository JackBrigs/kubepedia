---
id: TROUBLE-K8S_KMS_V1_DEPRECATED
type: troubleshooting
title: "KMS v1 encryption provider deprecated — migrate to KMS v2 (GA 1.29)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - KMS v1 deprecated
  - migrate KMS v2
  - KMSv2 encryption at rest
  - kms provider apiVersion v1 warning
  - encryption provider migration
tags:
  - kubernetes
  - troubleshooting
  - security
  - encryption
sources:
  - type: code
    path: keps/sig-auth/3299-kms-v2-improvements
    url: https://github.com/kubernetes/enhancements/tree/master/keps/sig-auth/3299-kms-v2-improvements
    note: "kep.yaml: KMSv2 stable 1.29; KMS v1 deprecated"
relations:
  - type: see_also
    target: PRACTICE-SECRETS_ENCRYPTION_AT_REST
  - type: see_also
    target: PRACTICE-RUNBOOK_SECRETS_ENCRYPTION
  - type: see_also
    target: CONCEPT-K8S_UPGRADE_SILENT_CHANGES
---

# KMS v1 encryption provider deprecated — migrate to KMS v2 (GA 1.29)

## Summary

The **KMS v2** encryption-at-rest provider reached **GA in K8s 1.29**, and **KMS v1 is deprecated**.
Clusters using an external KMS to encrypt Secrets in etcd via a `kms:` provider with **`apiVersion:
v1`** should migrate to **`v2`** — v2 is faster (local KEK caching, no per-object KMS call), supports
key-ID rotation tracking, and is the only version that will remain. Kubespray's built-in
`secretbox`/`aescbc` providers ([[PRACTICE-SECRETS_ENCRYPTION_AT_REST]]) are unaffected — this is only
for external-KMS setups.

## Problem

- apiserver logs a **deprecation warning** for KMS provider `apiVersion: v1`.
- Planning to keep encryption working long-term but the config still references the v1 KMS plugin.
- High KMS call volume / latency on Secret reads (v1 calls KMS per object; v2 caches a local KEK).

## Context

- Milestone (`keps/sig-auth/3299-...` kep.yaml): `KMSv2` **stable 1.29** (with `KMSv2KDF`). v1 remains
  functional but deprecated across the Kubespray range (K8s 1.29–1.35).
- v2 changes the on-disk envelope (DEK-per-write encrypted by a cached KEK) — **migration re-encrypts
  data**, so it follows the same rewrite discipline as enabling encryption.

## Diagnostics

- Inspect the EncryptionConfiguration on control-plane nodes: a `providers:` entry
  `kms: { apiVersion: v1, ... }` is the deprecated one; `apiVersion: v2` is current.
- Confirm the external KMS plugin binary supports the v2 gRPC API (`KeyManagementService` v2) before
  switching.

## Known Issues

- **Fix (migration):** deploy a **v2-capable** KMS plugin, add the **v2** provider **first** in the
  providers list (writes use the first provider) while keeping the v1 provider in the list for
  **reads**, then **re-encrypt all Secrets** (`kubectl get secrets -A -o json | kubectl replace -f -`),
  and only then remove the v1 provider — the same order-sensitive procedure as
  [[PRACTICE-RUNBOOK_SECRETS_ENCRYPTION]].
- **Snapshot etcd first** — you are changing how control-plane state is written.
- **Not using external KMS?** Ignore this — Kubespray's `secretbox`/`aescbc`/`aesgcm` providers are
  not KMS and are unaffected ([[PRACTICE-SECRETS_ENCRYPTION_AT_REST]]).

## References

- `keps/sig-auth/3299-kms-v2-improvements` (kep.yaml stable 1.29). Encryption mechanics
  [[PRACTICE-SECRETS_ENCRYPTION_AT_REST]]; enable/rotate runbook [[PRACTICE-RUNBOOK_SECRETS_ENCRYPTION]];
  silent changes [[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]].
