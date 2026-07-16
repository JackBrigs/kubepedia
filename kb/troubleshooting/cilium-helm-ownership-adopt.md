---
id: TROUBLE-CILIUM_HELM_OWNERSHIP_ADOPT
type: troubleshooting
title: "Cilium install fails: Helm can't adopt existing resource (invalid ownership metadata)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - invalid ownership metadata
  - cannot be imported into the current release
  - missing key app.kubernetes.io/managed-by must be set to Helm
  - meta.helm.sh/release-name
  - cilium-operator-tlsinterception-secrets exists
  - cilium-operator-ingress-secrets
  - cilium-operator-gateway-secrets
  - cilium-secrets namespace role conflict
  - Unable to install Cilium
tags:
  - troubleshooting
  - cilium
  - helm
  - upgrade
  - cni
sources:
  - type: docs
    path: Helm resource-adoption ownership metadata
    url: https://helm.sh/docs/faq/#automatically-rolling-back-releases
    note: "Helm requires app.kubernetes.io/managed-by=Helm + meta.helm.sh/release-{name,namespace} to adopt an existing object"
  - type: issue
    path: field-verified resolution (operator report)
    url: https://github.com/kubernetes-sigs/kubespray
    note: "fix confirmed working on a real Kubespray Cilium upgrade; error emitted by Helm during the cilium install"
  - type: code
    path: install/kubernetes/cilium/templates/cilium-operator/role.yaml
    url: https://raw.githubusercontent.com/cilium/cilium/v1.19.3/install/kubernetes/cilium/templates/cilium-operator/role.yaml
    note: "Cilium chart defines Role cilium-operator-tlsinterception-secrets in tls.secretsNamespace (default cilium-secrets) when secret-sync/TLS is enabled"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
  - type: see_also
    target: COMPONENT-HELM
  - type: see_also
    target: TROUBLE-CILIUM_CONFIG_VALIDATION
---

# Cilium install fails: Helm can't adopt existing resource (invalid ownership metadata)

## Summary

Kubespray installs/upgrades Cilium through **Helm**. If an object that the Cilium chart
wants to manage **already exists but was not created by this Helm release**, Helm
refuses to take it over and aborts the install with `invalid ownership metadata`. The
fix is to stamp the object with the Helm **ownership label + annotations** so Helm can
adopt it, then re-run — no delete required.

## Problem

The Cilium deploy fails with (example seen on a real upgrade):

```
Unable to install Cilium: Unable to continue with install: Role
"cilium-operator-tlsinterception-secrets" in namespace "cilium-secrets" exists and
cannot be imported into the current release: invalid ownership metadata; label
validation error: missing key "app.kubernetes.io/managed-by": must be set to "Helm";
annotation validation error: missing key "meta.helm.sh/release-name": must be set to
"cilium"; annotation validation error: missing key "meta.helm.sh/release-namespace":
must be set to "kube-system"
```

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0` with `kube_network_plugin: cilium`
  (Helm-based Cilium install).
- **What this specific object is (verified from the Cilium chart).**
  `cilium-operator-tlsinterception-secrets` is a namespaced **`Role`** the Cilium chart
  (`cilium-operator/role.yaml`) creates so the **cilium-operator** can `create/delete/
  update/patch` **secrets** in the TLS secrets namespace (`tls.secretsNamespace.name`,
  default **`cilium-secrets`**). It is rendered only when Cilium's **secret-sync / TLS
  interception** is active (`secretSyncEnabled`) — i.e. features like **Ingress**,
  **Gateway API**, or **TLS** handling that need the operator to sync TLS secrets into
  `cilium-secrets`. Sibling Roles from the same template: `cilium-operator-ingress-secrets`
  (Ingress) and `cilium-operator-gateway-secrets` (Gateway API) — expect the identical
  conflict on those if you use those features.
- **Why the conflict happens:** the object already exists but was **not** created by the
  current Helm release — e.g. by a **previous Cilium version** (the RBAC was added/renamed
  across versions), by the **operator at runtime**, a **Cilium CLI / manual** install, or
  a different Helm `release-name`/`release-namespace`. Such an object lacks the three
  ownership keys Helm needs to adopt it, so the chart install/upgrade aborts. This is why
  it surfaces most often during a **Cilium version upgrade**.
- **Note on namespaces:** the object lives in `cilium-secrets`, but the required
  `meta.helm.sh/release-namespace` is **`kube-system`** — that annotation names where
  the *Helm release* is tracked (Kubespray installs Cilium as release `cilium` in
  `kube-system`), not where the object sits. Always copy the exact
  `release-name`/`release-namespace` values **from the error message**.

## Diagnostics

- Read the error: it names the **kind**, **name**, **namespace**, and the exact
  expected `release-name` / `release-namespace` values.
- Inspect the offending object's metadata:
  `kubectl -n cilium-secrets get role cilium-operator-tlsinterception-secrets -o yaml`
  → confirm the `app.kubernetes.io/managed-by` label and `meta.helm.sh/*` annotations
  are missing or wrong.
- If several objects are affected, Helm reports them one at a time — expect to repeat
  the fix per object until the install proceeds.

## Known Issues

**Fix (field-verified) — adopt the object into the release:**

```bash
kubectl -n cilium-secrets label role cilium-operator-tlsinterception-secrets \
  app.kubernetes.io/managed-by=Helm \
  --overwrite

kubectl -n cilium-secrets annotate role cilium-operator-tlsinterception-secrets \
  meta.helm.sh/release-name=cilium \
  meta.helm.sh/release-namespace=kube-system \
  --overwrite
```

Then re-run the Cilium install (re-run `cluster.yml`/`upgrade-cluster.yml`, or the
`--tags=cilium`-scoped run). Helm now sees the object as its own and adopts it.

- **Values come from the error, not from this doc** — use whatever `kind/name`,
  `release-name`, and `release-namespace` Helm printed. Different feature/version →
  different object name (e.g. other `cilium-*` Roles/Secrets/ServiceAccounts).
- **Alternative:** delete the conflicting object and let Helm recreate it
  (`kubectl -n cilium-secrets delete role cilium-operator-tlsinterception-secrets`).
  Adoption (label/annotate) is safer — it preserves the object and any data; deletion is
  fine for stateless/regeneratable objects but risky for populated Secrets.
- **Prevention:** don't mix a manual/CLI Cilium install with the Kubespray Helm-managed
  one; keep a single ownership source. This class of error is generic to Helm — the same
  adopt-by-metadata fix applies to any `invalid ownership metadata` conflict.

## References

- Helm ownership metadata (`app.kubernetes.io/managed-by`, `meta.helm.sh/release-name`,
  `meta.helm.sh/release-namespace`) — Helm resource-adoption requirement.
- Cilium component / config: [[COMPONENT-CILIUM]], [[TROUBLE-CILIUM_CONFIG_VALIDATION]];
  Helm in Kubespray: [[COMPONENT-HELM]].
