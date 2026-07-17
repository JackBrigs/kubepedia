---
id: CONCEPT-SECRETS_MANAGEMENT
type: concept
title: "Secrets management (external-secrets, sealed-secrets) vs encryption-at-rest"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - external secrets operator
  - sealed secrets
  - secrets in git
  - vault kubernetes secrets
  - gitops secrets
  - manage kubernetes secrets safely
tags:
  - secrets
  - security
  - gitops
  - ecosystem
sources:
  - type: docs
    path: External Secrets Operator / Sealed Secrets docs
    url: https://external-secrets.io/
    note: "ESO syncs from external managers; Sealed Secrets encrypts for Git; both are add-ons (verified)"
relations:
  - type: see_also
    target: PRACTICE-SECRETS_ENCRYPTION_AT_REST
  - type: see_also
    target: CONCEPT-GITOPS
  - type: see_also
    target: PRACTICE-CLUSTER_HARDENING
---

# Secrets management (external-secrets, sealed-secrets) vs encryption-at-rest

## Summary

Three **complementary** layers protect Kubernetes Secrets, each solving a different
problem: **encryption-at-rest** protects Secrets **in etcd**; **Sealed Secrets** makes a
Secret safe to **commit to Git**; **External Secrets Operator (ESO)** keeps the source of
truth in an **external secret manager** (Vault, cloud). They are not alternatives to each
other — pick per threat model, and they stack.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`. Sealed Secrets and ESO are **not** Kubespray-
  managed — install via their Helm charts (evidence: upstream docs, `verified`).
- A plain `Secret` is base64 (not encrypted) and, without encryption-at-rest, is stored
  **cleartext in etcd** — the baseline problem these tools address.

## Implementation

**1. Encryption-at-rest (already a Kubespray option).**
`kube_encrypt_secret_data: true` encrypts Secret data before it reaches etcd
([[PRACTICE-SECRETS_ENCRYPTION_AT_REST]]). Protects against etcd/disk theft. Does **not**
help you store secrets in Git.

**2. Sealed Secrets — GitOps-safe secrets.**
Encrypt a `Secret` into a `SealedSecret` CRD with the controller's public key; the
`SealedSecret` is **safe to commit to Git** and only the in-cluster controller can decrypt
it into a real `Secret`. This is how you do **GitOps of secrets** ([[CONCEPT-GITOPS]]) —
the manifest in Git is ciphertext. The controller's private key is the thing to back up.

**3. External Secrets Operator — external source of truth.**
ESO fetches secret **values from an external manager** (HashiCorp Vault, AWS/GCP/Azure
secret managers) via a `SecretStore`/`ClusterSecretStore` + `ExternalSecret`, and
materializes them as native `Secret`s that are kept in sync. Git/manifests hold only
**references**, never the value.

## Compatibility

- **They stack:** encryption-at-rest (etcd) + (Sealed Secrets **or** ESO for the Git/
  external story). ESO and Sealed Secrets solve *different* problems — ESO for a central
  vault, Sealed Secrets for self-contained Git-committable secrets.
- **RBAC:** each operator's ServiceAccount needs permission to create/manage Secrets; a
  Forbidden means an RBAC gap ([[TROUBLE-RBAC_FORBIDDEN]]).
- **PodSecurity/hardening:** these don't change the Secret consumption model — mounted/env
  Secrets still follow PodSecurity ([[PRACTICE-CLUSTER_HARDENING]]).
- **Key/vault backup:** the Sealed Secrets controller **private key** (and Vault, for ESO)
  are now critical-recovery items — back them up alongside etcd/PKI
  ([[PRACTICE-BACKUP_DR]]).

## References

- External Secrets / Sealed Secrets docs. Encryption at rest:
  [[PRACTICE-SECRETS_ENCRYPTION_AT_REST]]; GitOps: [[CONCEPT-GITOPS]]; DR: [[PRACTICE-BACKUP_DR]].
