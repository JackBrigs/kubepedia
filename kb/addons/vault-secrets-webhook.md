---
id: CONCEPT-ADDON_VAULT_SECRETS_WEBHOOK
type: concept
title: "vault-secrets-webhook (bank-vaults) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.21.4"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - vault-secrets-webhook
  - bank-vaults webhook
  - vault-env
tags:
  - addons
  - secrets
  - webhook
  - vault
sources:
  - type: code
    path: deploy/charts/vault-secrets-webhook/Chart.yaml
    url: https://raw.githubusercontent.com/bank-vaults/vault-secrets-webhook/v1.21.4/deploy/charts/vault-secrets-webhook/Chart.yaml
    note: "no kubeVersion constraint; appVersion v1.21.4"
  - type: code
    path: go.mod
    url: https://raw.githubusercontent.com/bank-vaults/vault-secrets-webhook/v1.21.4/go.mod
    note: "k8s.io libs v0.32.0, controller-runtime v0.19.3, admissionregistration.k8s.io/v1"
  - type: docs
    path: bank-vaults mutating-webhook docs
    url: https://bank-vaults.dev/docs/mutating-webhook/
    note: "vault-env sidecar, deploy guidance"
relations:
  - type: see_also
    target: TROUBLE-VAULT_SECRETS_WEBHOOK
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
  - type: see_also
    target: CONCEPT-ADDON_VAULT
  - type: see_also
    target: TROUBLE-ADMISSION_WEBHOOK_BLOCKING
---

# vault-secrets-webhook (bank-vaults) — addon

## Summary

The bank-vaults **vault-secrets-webhook** (chart+app **v1.21.4**, in lockstep) is a mutating
admission webhook that injects Vault secrets into pods via a `vault-env` init/sidecar. v1.21.4
is a maintenance/dependency-only release (Alpine 3.21.0, Go 1.23.4, ~50 dep bumps) — no
functional breaking changes.

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]]. Pairs with
  [[CONCEPT-ADDON_VAULT]] as the secret source.
- It is a **mutating webhook**, so it shares the cluster-wide failure class of
  [[TROUBLE-ADMISSION_WEBHOOK_BLOCKING]]: if the webhook is unreachable, pod creation can be
  blocked. Scope `namespaceSelector`/`failurePolicy` deliberately.

## Implementation

- Webhook image `:v1.21.4`; default injected sidecar `vault-env:v1.21.7` (pinned per
  release). Chart repo moved to **OCI** `oci://ghcr.io/bank-vaults/helm-charts/vault-secrets-webhook`
  — the legacy banzaicloud HTTP repo is deprecated.
- Built against `k8s.io` libraries `v0.32.0` and controller-runtime `v0.19.3`; uses the
  stable `admissionregistration.k8s.io/v1` API.

## Configuration

- Set `namespaceSelector` so only namespaces that need injection are intercepted; keep a
  sane `failurePolicy` to avoid a webhook outage blocking unrelated pods.
- Injection requires the `copy-vault-env` init container to be added by the webhook — if
  mutation is skipped, secrets are silently not injected (see Known issues).

## Compatibility

- **Kubernetes range:** no published matrix (**unverified** upper bound). Uses only stable
  admission APIs and modern k8s.io libs, so it functions across **1.29–1.35**; explicit
  1.33–1.35 support is not documented.
- **Known issues:** mutation silently skipped / no `copy-vault-env` init container
  (bank-vaults#405); cloud IAM auth breakage e.g. ECR + kube2iam (#351); OpenShift SCC /
  security-context conflicts (#307).
- **CVEs:** none found for the webhook / vault-env app at v1.21.4 (OSV empty for both Go
  modules). Transitive base-image CVEs are not individually enumerated.

## Upstream issues & upgrade notes (mined 2026-07-19)

**Future upgrade context** beyond pinned **1.21.4** (from upstream releases):
- **⚠ 1.23.1 security/behavior change:** object-supplied Vault addresses are now **validated against an allowlist (SSRF hardening)** — the **`vault-addr` annotation is no longer trusted as-is**. If you use it, set **`VAULT_ADDR_ALLOWLIST`**; loopback/private IPs are **blocked by default** unless `VAULT_ALLOW_PRIVATE_ADDR` is set. Also adds the missing `IPC_LOCK` capability to the vault-agent initContainer.
- 1.22.1 adds a `matchConditions` webhook filter and a Helm flag to enable mutations in the deploy namespace. Injection/auth troubleshooting: [[TROUBLE-VAULT_SECRETS_WEBHOOK]].

## Older-version CVEs & security history (mined 2026-07-19)

bank-vaults' own CVE record is thin; the key security change is **1.23.1's SSRF hardening** (vault-addr allowlist — see the upgrade section), so **versions below 1.23.1 trust object-supplied Vault addresses** (an SSRF vector). Older-version exposure also includes the bundled vault-env/base image. Upgrade to ≥1.23.1 and scope the webhook selector/failurePolicy.

## References

- `Chart.yaml`, `go.mod`, bank-vaults docs (above); GitHub issues #405/#351/#307.
- Catalog: [[CONCEPT-ADDON_CATALOG]]; Vault: [[CONCEPT-ADDON_VAULT]].
