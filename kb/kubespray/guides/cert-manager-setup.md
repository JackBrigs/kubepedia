---
id: PRACTICE-CERT_MANAGER_SETUP
type: best_practice
title: "cert-manager: enabling and CA setup"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - cert-manager-setup
tags:
  - operations
  - cert-manager
sources:
  - type: docs
    path: docs/advanced/cert_manager.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/advanced/cert_manager.md
    note: "digest of the tag doc"
relations:
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
---

# cert-manager: enabling and CA setup

## Summary

cert-manager is a native Kubernetes certificate controller (issues/renews certs from Let's Encrypt, Vault, a CA key pair, or self-signed). Kubespray deploys it when `cert_manager_enabled: true`.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`; cert-manager version per [[COMPONENT-CERT_MANAGER]] context (see the addons).
- Opt-in add-on.

## Implementation

Enable in the addons inventory (`k8s_cluster/addons.yml`): `cert_manager_enabled: true`. To issue TLS from your own CA, create the `ca-key-pair` Secret (Root CA cert + key) in the cluster; then configure Issuers/ClusterIssuers. For public certs, use a Let's Encrypt ClusterIssuer. See the upstream cert-manager CA configuration docs.

## References

- `docs/advanced/cert_manager.md` (tag v2.31.0 `1c9add4`).
