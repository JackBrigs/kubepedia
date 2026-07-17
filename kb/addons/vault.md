---
id: CONCEPT-ADDON_VAULT
type: concept
title: "Vault (HashiCorp) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.31 <=1.35"
component_version: "1.21.2"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - vault
  - hashicorp vault
  - vault helm chart
  - vault 0.32.0
tags:
  - addons
  - secrets
  - vault
sources:
  - type: code
    path: Chart.yaml
    url: https://raw.githubusercontent.com/hashicorp/vault-helm/v0.32.0/Chart.yaml
    note: "kubeVersion >=1.20.0-0; appVersion 1.21.2 (NOT 1.21.4)"
  - type: docs
    path: vault-helm v0.32.0 release
    url: https://github.com/hashicorp/vault-helm/releases/tag/v0.32.0
    note: "tested against K8s 1.31–1.35 (Kind v0.31.0)"
  - type: docs
    path: HashiCorp advisory
    url: https://discuss.hashicorp.com/t/vault-1-21-4-1-20-9-1-19-15-and-1-16-31-released/77217
    note: "CVE-2026-1229 fixed in 1.21.4"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
  - type: see_also
    target: CONCEPT-ADDON_VAULT_SECRETS_WEBHOOK
  - type: see_also
    target: CONCEPT-SECRETS_MANAGEMENT
---

# Vault (HashiCorp) — addon

## Summary

HashiCorp Vault deployed via the official `vault-helm` chart **0.32.0** — an
independently-installed platform addon (not Kubespray-managed). **Version note:** chart
0.32.0 pins **appVersion `1.21.2`**, *not* `1.21.4` as listed in the inventory — verify the
running image before relying on `1.21.4` behaviour or CVE status. The chart also defaults
`vault-k8s 1.7.2` (Agent Injector) and `vault-csi-provider 1.7.0`.

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]].
- Deployed by the Vault Helm chart, independent of Kubespray.
- Vault is stateful and **starts sealed** — it needs init + unseal (or auto-unseal) before
  it serves; this shapes every operational failure mode below.

## Implementation

- Chart→app: `vault-helm v0.32.0` → Vault **1.21.2** (raw `Chart.yaml`). If the inventory
  intends 1.21.4, the image tag must be overridden (`server.image.tag`); the chart alone
  does not ship 1.21.4.
- Chart `kubeVersion`: **`>=1.20.0-0`** (floor only, no upper bound).
- 0.32.0 is a feature/bugfix release — **no breaking changes**. Notable: NetworkPolicy
  template now includes namespace config (GH-1152); guard against duplicate `disable_mlock`
  HCL (GH-1154); OpenShift service-ca automation (GH-1165).

## Configuration

- **HA/Raft** needs a working `StorageClass` or the server pods stay `Pending`.
- Choose an **auto-unseal** path (cloud KMS / transit) in production so pod restarts don't
  wedge on manual unseal.
- The **Agent Injector** (vault-k8s) is a mutating webhook — its TLS/CA-bundle must be
  correct or injection silently fails (see [[CONCEPT-ADDON_VAULT_SECRETS_WEBHOOK]] for a
  webhook alternative).

## Compatibility

- **Tested Kubernetes:** 1.31–1.35 per the v0.32.0 release notes. 1.29–1.30 satisfy the
  chart floor but are **below the tested floor** (not officially validated).
- **CVE-2026-1229** (bundled `cloudflare/circl`) is fixed **only in Vault 1.21.4**, so the
  shipped **1.21.2 is affected** — override the image to 1.21.4+ to clear it. (CVE-2026-34986
  / -39883 / -39829 were already fixed in 1.21.2.)
- Upgrades are not fully automated: unseal after restart, leader upgraded last.

## References

- `vault-helm` v0.32.0 `Chart.yaml` + release notes; HashiCorp 1.21.4 advisory (all above).
- Deploy/run guide: https://developer.hashicorp.com/vault/docs/deploy/kubernetes/helm/run
- Catalog: [[CONCEPT-ADDON_CATALOG]].
