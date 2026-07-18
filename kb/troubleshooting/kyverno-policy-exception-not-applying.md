---
id: TROUBLE-KYVERNO_POLICY_EXCEPTION_NOT_APPLYING
type: troubleshooting
title: "Kyverno PolicyException ignored — feature off by default and namespace-restricted"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.18.2"
verified_at: "2026-07-18"
confidence: verified
aliases:
  - kyverno policyexception not working
  - enablePolicyException
  - exceptionNamespace
  - kyverno exception ignored
tags:
  - kyverno
  - troubleshooting
  - policy
  - exceptions
sources:
  - type: code
    path: cmd/internal/flag.go
    url: https://github.com/kyverno/kyverno/blob/v1.18.2/cmd/internal/flag.go
    note: "--enablePolicyException default false; --exceptionNamespace default empty (L138-139)"
  - type: code
    path: charts/kyverno/values.yaml
    url: https://github.com/kyverno/kyverno/blob/v1.18.2/charts/kyverno/values.yaml
    note: "policyExceptions.enabled false + single-namespace restriction (L823-826)"
relations:
  - type: see_also
    target: CONCEPT-ADDON_KYVERNO
  - type: see_also
    target: TROUBLE-KYVERNO_POLICY_NOT_APPLYING
---

# Kyverno PolicyException ignored — feature off by default and namespace-restricted

## Summary

A correctly-written **`PolicyException`** can be **silently ignored** for two default reasons:
exceptions are **disabled by default** (`--enablePolicyException: false`), and even when enabled they're
accepted **only in one namespace** (`--exceptionNamespace`, empty by default) unless set to `*`. So the
exception either does nothing (feature off) or is ineffective because it lives in the "wrong" namespace.

## Problem

- A `PolicyException` is created, no errors, but the target policy still blocks/flags the resource.
- Exceptions work in one namespace but not another.

## Context

- Applies to Kyverno **1.18.x** ([[CONCEPT-ADDON_KYVERNO]]).
- **Off by default:** `--enablePolicyException` defaults to **false**; `--exceptionNamespace` defaults
  to **empty** (`cmd/internal/flag.go`@v1.18.2 L138-139). The chart mirrors this:
  `policyExceptions.enabled: false` with a single-namespace restriction (`values.yaml`@v1.18.2
  L823-826).
- **Namespace gating:** with a namespace set, exceptions are honored **only** in that namespace; set to
  `*` to allow them cluster-wide.
- Distinct from a policy simply not matching ([[TROUBLE-KYVERNO_POLICY_NOT_APPLYING]]) — here the policy
  matches and the *exception* is the thing being ignored.

## Diagnostics

- Check the flags on the admission controller: `kubectl -n <kyverno-ns> get deploy kyverno-admission-controller
  -o yaml | grep -E 'enablePolicyException|exceptionNamespace'` (or the Helm values
  `policyExceptions.*`).
- Confirm your `PolicyException` object lives in the allowed namespace (or that `*` is set).

## Known Issues

- **Fix:** enable the feature (`policyExceptions.enabled: true` / `--enablePolicyException`) **and** set
  the exception namespace appropriately (`policyExceptions.namespace` or `--exceptionNamespace`, `*` for
  cluster-wide), then place your `PolicyException` objects there.
- **Security note:** enabling exceptions cluster-wide (`*`) lets anyone who can create a `PolicyException`
  in any namespace bypass policy — scope the namespace and RBAC deliberately.

## References

- Kyverno `cmd/internal/flag.go` + `charts/kyverno/values.yaml` (@v1.18.2). Addon
  [[CONCEPT-ADDON_KYVERNO]]; policy-not-matching [[TROUBLE-KYVERNO_POLICY_NOT_APPLYING]].
