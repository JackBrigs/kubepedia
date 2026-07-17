---
id: TROUBLE-KYVERNO_UPGRADE
type: troubleshooting
title: "Kyverno upgrade: no raw-YAML path, CRD limits, breaking field moves"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=1.10.0 <=1.18.2"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - kyverno upgrade breaks
  - kyverno crd annotations too long
  - kyverno 1.10 no upgrade path
  - kyverno 1.12.0 etcd growth
  - kyverno validationfailureaction moved
tags:
  - troubleshooting
  - kyverno
  - upgrade
  - policy
sources:
  - type: docs
    path: kyverno issue #8589 (CRD annotations too long)
    url: https://github.com/kyverno/kyverno/issues/8589
    note: "client-side apply blows 256KB annotation limit"
  - type: docs
    path: kyverno v1.10.0 release notes
    url: https://github.com/kyverno/kyverno/releases/tag/v1.10.0
    note: "controller split; no raw-YAML upgrade path"
relations:
  - type: see_also
    target: CONCEPT-ADDON_KYVERNO
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# Kyverno upgrade: no raw-YAML path, CRD limits, breaking field moves

## Summary

Kyverno upgrades break more often than most addons. The recurring traps: **no raw-YAML
upgrade path** across the 1.10 split, **CRDs that exceed the 256 KB annotation limit** under
client-side apply, **Helm never upgrading CRDs**, and **policy fields relocated** between
minors. Read the target minor's notes first.

## Problem

- Helm fails: `clusterpolicies.kyverno.io is invalid: metadata.annotations: Too long: must
  have at most 262144 bytes`.
- Controllers silently hit stale/renamed CRD fields after an upgrade.
- After bumping, policies stop enforcing or reports vanish.
- etcd grows uncontrollably right after upgrading to 1.12.0.

## Context

- Applies to Kyverno **1.10–1.18** ([[CONCEPT-ADDON_KYVERNO]]); the upgrade-horizon layer is
  [[CONCEPT-UPGRADE_HORIZON]].

## Diagnostics

- **CRD "annotations too long":** client-side apply adds a `last-applied-configuration`
  annotation that overflows on Kyverno's large CRDs — use **server-side apply** or
  `kubectl create/replace`, and **manage CRDs separately** (issues #8589/#14378).
- **Helm doesn't upgrade CRDs:** `helm upgrade` never touches CRDs — `kubectl apply` the new
  CRDs **before** upgrading, and verify CRD versions after (issue #13931).
- **1.10 controller split:** there is **no raw-YAML upgrade path** and only a limited Helm path
  — **back up policies or scale Kyverno to zero first**, then install fresh; the split also
  needs new aggregated-ClusterRole label values.
- **1.12.0 etcd growth:** 1.12.0 has ephemeralreports/etcd-growth bugs — **upgrade straight to
  1.12.4+**. 1.12 also graduated storage APIs to **v2** (Helm migration hooks) and hardened
  RBAC (wildcards removed) — controllers may lose CR access.
- **1.13 field relocation:** `spec.validationFailureAction` moved to
  **`spec.rules.validate.failureAction`** (and `failurePolicy`/`webhookTimeoutSeconds`
  migrated); PolicyException default-enable was removed (CVE-2024-48921) — enable per namespace.
- **1.15 CEL rename:** `image()` → `parseImageReference`. **1.16:** `UpdateRequest v1beta1`
  became **unserved**.

## Known Issues

- Leftover webhook configs after a failed/ArgoCD uninstall deadlock the cluster
  ([[TROUBLE-KYVERNO_WEBHOOK_HA]]).
- Upgrading also closes the large 1.15–1.18 CVE wave — run the newest patch
  ([[CONCEPT-ADDON_KYVERNO]] / [[CONCEPT-CVE_REMEDIATION]]).

## References

- kyverno issue #8589, v1.10.0 release notes (above); issues #14378/#13931; release tags
  v1.12.0/v1.13.0/v1.15.0/v1.16.0. Addon: [[CONCEPT-ADDON_KYVERNO]].
