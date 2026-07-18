---
id: CONCEPT-K8S_STRUCTURED_AUTHN
type: concept
title: "Structured authentication config (--authentication-config, on-by-default 1.30, GA 1.34)"
status: active
kubespray_version: ">=v2.28.0 <=v2.31.0"
kubernetes_version: ">=1.30 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - structured authentication configuration
  - authentication-config file
  - multiple OIDC issuers
  - StructuredAuthenticationConfiguration
  - apiserver oidc CEL
tags:
  - kubernetes
  - auth
  - apiserver
sources:
  - type: code
    path: keps/sig-auth/3331-structured-authentication-configuration
    url: https://github.com/kubernetes/enhancements/tree/master/keps/sig-auth/3331-structured-authentication-configuration
    note: "kep.yaml milestone: alpha 1.29, beta/on-by-default 1.30, stable 1.34"
relations:
  - type: see_also
    target: CONCEPT-K8S_STRUCTURED_AUTHZ
  - type: see_also
    target: CONCEPT-K8S_UPGRADE_SILENT_CHANGES
  - type: see_also
    target: CONCEPT-K8S_FEATURE_GATES
---

# Structured authentication config (--authentication-config, on-by-default 1.30, GA 1.34)

## Summary

The API server can now take authentication config from a **`--authentication-config` YAML file**
instead of only the flat `--oidc-*` flags — enabling **multiple OIDC issuers**, **CEL** expressions to
map/validate claims, and hot-reload. `StructuredAuthenticationConfiguration` reached **beta /
on-by-default in K8s 1.30** and **GA in 1.34**, so it is available across the Kubespray range from
v2.28.0. The legacy `--oidc-*` flags still work but the file is the forward path.

## Context

- Milestone (`keps/sig-auth/3331-...` kep.yaml): alpha **1.29**, beta/on **1.30**, stable **1.34**.
- What it adds over `--oidc-*` flags: several issuers in one apiserver; CEL `claimMappings` /
  `claimValidationRules` (e.g. derive username/groups, enforce claims); file is **reloaded** without
  restart.
- Kubespray still configures OIDC via the classic flags/vars by default — this is an **escape-hatch
  upgrade path** for multi-issuer / CEL needs, set via `kube_apiserver_extra_args` +
  `kubeadm_patches` to mount the file ([[CONCEPT-K8S_FEATURE_GATES]]).
- Mutually-exclusive with `--oidc-*` flags for the same issuer — don't set both. Pairs with
  structured **authorization** ([[CONCEPT-K8S_STRUCTURED_AUTHZ]]).

## References

- `keps/sig-auth/3331-structured-authentication-configuration` (kep.yaml). Companion
  [[CONCEPT-K8S_STRUCTURED_AUTHZ]]; silent-change list [[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]]; gates
  [[CONCEPT-K8S_FEATURE_GATES]].
