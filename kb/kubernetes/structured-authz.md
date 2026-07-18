---
id: CONCEPT-K8S_STRUCTURED_AUTHZ
type: concept
title: "Structured authorization config (--authorization-config, on-by-default 1.30, GA 1.32)"
status: active
kubespray_version: ">=v2.28.0 <=v2.31.0"
kubernetes_version: ">=1.30 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - structured authorization configuration
  - authorization-config file
  - ordered webhooks
  - StructuredAuthorizationConfig
  - authorizer CEL
tags:
  - kubernetes
  - auth
  - apiserver
sources:
  - type: code
    path: keps/sig-auth/3221-structured-authorization-configuration
    url: https://github.com/kubernetes/enhancements/tree/master/keps/sig-auth/3221-structured-authorization-configuration
    note: "kep.yaml milestone: alpha 1.29, beta/on-by-default 1.30, stable 1.32"
relations:
  - type: see_also
    target: CONCEPT-K8S_STRUCTURED_AUTHN
  - type: see_also
    target: PRACTICE-RBAC_LEAST_PRIVILEGE
  - type: see_also
    target: CONCEPT-K8S_UPGRADE_SILENT_CHANGES
---

# Structured authorization config (--authorization-config, on-by-default 1.30, GA 1.32)

## Summary

The API server can take an **`--authorization-config` YAML file** defining an **ordered chain of
authorizers** (Node, RBAC, Webhook, …) with **CEL** `matchConditions` per webhook — replacing the
single `--authorization-mode` list. `StructuredAuthorizationConfig` reached **beta/on-by-default in
1.30** and **GA in 1.32**. It lets you place multiple webhooks in a defined order, short-circuit with
CEL, and set failure policies — impossible with the flat flag.

## Context

- Milestone (`keps/sig-auth/3221-...` kep.yaml): alpha **1.29**, beta/on **1.30**, stable **1.32**.
- Over `--authorization-mode`: ordered authorizers, per-webhook `matchConditions` (CEL) to skip
  irrelevant requests, explicit `timeout`/`failurePolicy`, and reload without restart.
- Kubespray sets `authorization_modes: ['Node','RBAC']` via the flag by default
  ([[PRACTICE-RBAC_LEAST_PRIVILEGE]]); the config file is the path when you need **multiple ordered
  webhooks** (e.g. an external policy engine before RBAC). Mount via `kube_apiserver_extra_args` +
  `kubeadm_patches`.
- Pairs with structured authentication ([[CONCEPT-K8S_STRUCTURED_AUTHN]]).

## References

- `keps/sig-auth/3221-structured-authorization-configuration` (kep.yaml). Companion
  [[CONCEPT-K8S_STRUCTURED_AUTHN]]; RBAC [[PRACTICE-RBAC_LEAST_PRIVILEGE]]; silent changes
  [[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]].
