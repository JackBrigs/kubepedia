---
id: CONCEPT-HELM_IN_KUBESPRAY
type: concept
title: "Helm in Kubespray (CLI, helm-apps, and Helm-based add-ons)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - helm in kubespray
  - helm_enabled
  - helm-apps
  - which addons use helm
  - cilium helm release
tags:
  - helm
  - components
  - addons
sources:
  - type: code
    path: roles/helm-apps/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/helm-apps/tasks/main.yml
    note: "kubernetes.core.helm to deploy user charts (tag v2.31.0)"
  - type: code
    path: roles/network_plugin/cilium/tasks/apply.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/tasks/apply.yml
    note: "Cilium deployed via the cilium CLI (Helm-based release 'cilium') (tag v2.31.0)"
relations:
  - type: see_also
    target: COMPONENT-HELM
  - type: see_also
    target: TROUBLE-CILIUM_HELM_OWNERSHIP_ADOPT
  - type: see_also
    target: COMPONENT-CILIUM
---

# Helm in Kubespray (CLI, helm-apps, and Helm-based add-ons)

## Summary

Helm shows up in Kubespray in three distinct ways, often confused: (1) `helm_enabled`
installs the **Helm CLI binary** on nodes; (2) the **`helm-apps`** role deploys
**user-specified** Helm charts; and (3) a few **built-in add-ons are themselves
Helm-based** (notably **Cilium**, via the `cilium` CLI, which creates a Helm release).
Knowing which is which explains where Helm state lives and why Helm-ownership conflicts
happen.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- `helm_enabled: false` by default; the built-in Helm-based add-ons work regardless of
  `helm_enabled` (they don't need the node CLI).

## Implementation

**1. Helm CLI on nodes (`helm_enabled`).** The `kubernetes-apps/helm` role installs the
`helm` binary (version = newest in the bundled checksums map — see
[[CONCEPT-COMPONENT_VERSION_SELECTION]]). This is a convenience for operators; it does not
by itself deploy anything.

**2. `helm-apps` role (your charts).** Deploys arbitrary charts via
`kubernetes.core.helm_repository` + `kubernetes.core.helm` (`release_name`,
`release_namespace`, values). This is the supported way to have Kubespray manage extra
Helm releases.

**3. Built-in Helm-based add-ons.**

- **Cilium** — deployed with the **`cilium` CLI** (`cilium install`/`upgrade --version …
  -f cilium-values.yaml`), which creates and tracks a **Helm release named `cilium`** in
  `kube-system`. That is why a pre-existing, non-Helm-owned object blocks the install
  with an ownership error ([[TROUBLE-CILIUM_HELM_OWNERSHIP_ADOPT]]). Extra values go
  through `cilium_extra_values`.
- **kubelet-csr-approver** — installed from its Helm chart
  (`kubelet_csr_approver_chart_ref`).
- **custom_cni** — Helm-based.

## Compatibility

- Because Cilium is a Helm release, Cilium changes are made through Kubespray's values
  (`cilium_*` / `cilium_extra_values`) — not by editing the running DaemonSet, which a
  reconcile would revert.
- Helm-release objects carry ownership metadata (`app.kubernetes.io/managed-by=Helm`,
  `meta.helm.sh/release-*`); objects created outside the release can't be adopted without
  stamping that metadata ([[TROUBLE-CILIUM_HELM_OWNERSHIP_ADOPT]]).
- `helm_enabled` and the built-in add-ons are independent — you don't need `helm_enabled`
  for Cilium/kubelet-csr-approver to deploy.

## References

- `helm-apps/tasks/main.yml`, `cilium/tasks/apply.yml`, `kubelet-csr-approver` defaults at
  tag `v2.31.0`. Helm component: [[COMPONENT-HELM]]; ownership conflict:
  [[TROUBLE-CILIUM_HELM_OWNERSHIP_ADOPT]].
