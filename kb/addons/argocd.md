---
id: CONCEPT-ADDON_ARGOCD
type: concept
title: "Argo CD (addon chart 8.5.7) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.31 <=1.34"
component_version: "3.1.7"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - argocd addon
  - argo-cd 8.5.7
  - argocd 3.1
tags:
  - addons
  - gitops
  - argocd
sources:
  - type: code
    path: charts/argo-cd/Chart.yaml
    url: https://raw.githubusercontent.com/argoproj/argo-helm/argo-cd-8.5.7/charts/argo-cd/Chart.yaml
    note: "kubeVersion >=1.25.0-0; appVersion v3.1.7"
  - type: docs
    path: Argo CD tested Kubernetes versions (3.1)
    url: https://argo-cd.readthedocs.io/en/release-3.1/operator-manual/tested-kubernetes-versions/
    note: "tested v1.31–v1.34"
  - type: docs
    path: 2.14→3.0 upgrade guide
    url: https://argo-cd.readthedocs.io/en/release-3.1/operator-manual/upgrading/2.14-3.0/
    note: "RBAC/tracking breaking changes in the 3.0 major"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
  - type: see_also
    target: COMPONENT-ARGOCD
  - type: see_also
    target: CONCEPT-GITOPS
---

# Argo CD (addon chart 8.5.7) — addon

## Summary

Argo CD deployed via the community `argo-cd` Helm chart **8.5.7** (app **v3.1.7**) — the
owner's independent GitOps install. **This is a different, newer deployment** than the
Kubespray-managed [[COMPONENT-ARGOCD]]; do not conflate the two versions. Chart 8.x = the
Argo CD **v3.x** major line, which carries real RBAC/tracking breaking changes vs 2.x.

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]]. Operational GitOps
  guidance: [[CONCEPT-GITOPS]].
- Overlaps Kubespray's ArgoCD add-on — the owner runs chart 8.5.7 independently, so the
  version divergence is expected (D-015 overlap rule).

## Implementation

- Chart→app: `argo-cd-8.5.7` → Argo CD **v3.1.7**; bundles redis-ha chart 4.33.7.
- Chart `kubeVersion`: **`>=1.25.0-0`** (looser than the app's tested matrix).
- Chart 8.5.7 itself only adds requests/limits on the repo-server `copyutil` initContainer;
  the substance is the **3.0 major** behaviour (below).

## Configuration

- **3.0 breaking changes to plan for** (chart 8.0.0 = app 3.0.0): fine-grained RBAC —
  `update`/`delete` now apply only to the Application, not sub-resources (new policies may be
  needed); logs RBAC enforced by default (`logs, get` now required); default resource
  tracking moved from labels to **annotations**; legacy repositories can no longer live in
  `argocd-cm` and must be **Secrets**. Read the 2.14→3.0 upgrade guide before bumping.

## Compatibility

- **Tested Kubernetes (app 3.1):** **v1.31–v1.34**. v1.29/v1.30/v1.35 are **not** listed as
  tested (the chart `kubeVersion >=1.25` is looser than reality).
- **CVE-2025-55191 / GHSA-g88p-r42r-ppp9** — DoS via a repo-credentials race, affects
  v3.1.0-rc1 through **v3.1.7** (this chart's pin), fixed in **v3.1.8**. Override the image
  to v3.1.8+ to clear it.

## Upstream issues & upgrade notes (mined 2026-07-19)

**Future upgrade context** beyond pinned **3.1.7** (from upstream releases):
- **3.4.4:** fixes an **RBAC regression for the multi-namespace (namespaced) architecture** — relevant if you run apps-in-any-namespace.
- 3.4.5 rebases onto Ubuntu 26.04 + crypto 0.53.0; 3.5.x in RC. No breaking API changes flagged in the 3.x window, but cluster-informer locking and auto-sync regressions were fixed along the way — stay on a patched 3.4.x.

## References

- `Chart.yaml`, tested-versions page, 2.14→3.0 upgrade guide (above); advisory
  GHSA-g88p-r42r-ppp9.
- Kubespray-managed sibling: [[COMPONENT-ARGOCD]]; catalog: [[CONCEPT-ADDON_CATALOG]].
