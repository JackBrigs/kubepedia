---
id: TROUBLE-VAULT_SECRETS_WEBHOOK
type: troubleshooting
title: "vault-secrets-webhook: pods blocked or secrets not injected — webhook down (failurePolicy), Vault auth, annotations"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=1.21.4"
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - vault-secrets-webhook pods stuck
  - vault-env cannot authenticate
  - secrets not injected vault webhook
  - mutating webhook blocks pod creation
  - bank-vaults webhook failurePolicy
tags:
  - troubleshooting
  - security
  - vault
  - admission
sources:
  - type: external
    path: bank-vaults vault-secrets-webhook
    url: https://github.com/bank-vaults/vault-secrets-webhook
    note: "mutating webhook injects vault-env; failurePolicy scope; vault-env auth via k8s auth role"
relations:
  - type: see_also
    target: CONCEPT-ADDON_VAULT_SECRETS_WEBHOOK
  - type: see_also
    target: CONCEPT-ADDON_VAULT
  - type: see_also
    target: TROUBLE-ADMISSION_WEBHOOK_BLOCKING
  - type: see_also
    target: CONCEPT-COMPONENT_INTERACTION_FAILURES
---

# vault-secrets-webhook: pods blocked or secrets not injected — webhook down (failurePolicy), Vault auth, annotations

## Summary

The bank-vaults mutating webhook injects Vault secrets via a `vault-env` sidecar. It bites two ways: a **down webhook with `failurePolicy: Fail` blocks pod creation** in scope, or a selector/annotation mismatch (or a `vault-env` **auth** failure) means secrets are **silently not injected**.

## Problem

- Two opposite symptoms: **pods can't be created at all** (`Internal error occurred: failed calling
  webhook ... connection refused`), or pods start but the **Vault secrets aren't injected** (env still
  holds the literal `vault:...` reference).

## Context

- bank-vaults `vault-secrets-webhook` `v1.21.4` ([[CONCEPT-ADDON_VAULT_SECRETS_WEBHOOK]]); a **mutating
  admission webhook** that rewrites pods to run a `vault-env` init/sidecar which fetches secrets from
  Vault ([[CONCEPT-ADDON_VAULT]]).
- **Webhook down blocks creates (the seam):** if the webhook's `failurePolicy` is `Fail` and its pod is
  down/unreachable, the API server **refuses to create matching pods** — cluster-wide if the selector is
  broad ([[TROUBLE-ADMISSION_WEBHOOK_BLOCKING]], [[CONCEPT-COMPONENT_INTERACTION_FAILURES]]).
- **No injection:** injection only happens for pods matching the webhook's namespace/object selector and
  carrying `vault:` references (or the configured annotations). Mismatched selector / missing annotation
  → the pod is admitted unmutated, so `vault-env` never runs.
- **vault-env can't auth:** the sidecar authenticates to Vault via the configured method (usually
  Kubernetes auth). Wrong `VAULT_ADDR`, a role not bound to the pod's ServiceAccount, a bad path, or an
  unsealed-but-unreachable Vault → the container errors on startup and the pod crashloops.

## Diagnostics

```bash
kubectl get mutatingwebhookconfiguration | grep vault-secrets
kubectl -n vault-secrets-webhook get pods                       # webhook pod healthy?
kubectl -n <app-ns> logs <pod> -c vault-env                     # auth/path errors
kubectl -n <app-ns> get pod <pod> -o jsonpath='{.spec.initContainers[*].name}'  # vault-env injected?
```

## Known Issues

- **Pods blocked — fix:** restore the webhook pod; if it's an outage, scope `failurePolicy`/selector so
  only intended namespaces are gated (a broad `Fail` webhook is a cluster-wide risk). Exempt system
  namespaces from the selector.
- **No injection — fix:** confirm the namespace/pod matches the webhook selector and carries the
  expected `vault:` refs/annotations; injection is at pod creation, so recreate the workload after
  fixing the selector.
- **vault-env auth — fix:** set correct `VAULT_ADDR`; bind the Kubernetes auth **role** to the pod's
  ServiceAccount + namespace with a policy granting the secret path; verify Vault is unsealed and
  reachable ([[CONCEPT-ADDON_VAULT]]).

## References

- bank-vaults vault-secrets-webhook. Addon [[CONCEPT-ADDON_VAULT_SECRETS_WEBHOOK]]; Vault
  [[CONCEPT-ADDON_VAULT]]; webhook-blocking [[TROUBLE-ADMISSION_WEBHOOK_BLOCKING]]; seams
  [[CONCEPT-COMPONENT_INTERACTION_FAILURES]].
