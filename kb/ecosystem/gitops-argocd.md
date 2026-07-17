---
id: CONCEPT-GITOPS
type: concept
title: "GitOps on the cluster (ArgoCD)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - GitOps
  - ArgoCD
  - argocd_enabled
  - app of apps
  - declarative deployment kubernetes
  - continuous delivery kubernetes
tags:
  - gitops
  - argocd
  - deployment
  - ecosystem
sources:
  - type: code
    path: roles/kubernetes-apps/argocd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/argocd/defaults/main.yml
    note: "argocd_enabled/version/namespace — Kubespray can install ArgoCD (tag v2.31.0)"
  - type: docs
    path: Argo CD documentation
    url: https://argo-cd.readthedocs.io/
    note: "GitOps sync/self-heal, app-of-apps, sync waves (verified)"
relations:
  - type: see_also
    target: COMPONENT-ARGOCD
  - type: see_also
    target: PRACTICE-BACKUP_DR
  - type: see_also
    target: TROUBLE-RBAC_FORBIDDEN
---

# GitOps on the cluster (ArgoCD)

## Summary

GitOps means the **desired cluster state lives in Git** and a controller continuously
reconciles the cluster to match it. **ArgoCD** is the common tool and is a **Kubespray-
managed** add-on (`argocd_enabled`, off by default). Beyond installing it, the value is
the workflow: declarative Applications, drift detection, self-heal, and app-of-apps — which
also makes your workloads **recoverable from Git** (a DR win).

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`. Kubespray can install ArgoCD
  (`argocd_enabled: true`, `argocd_version`, `argocd_namespace: argocd`) —
  [[COMPONENT-ARGOCD]] — or you deploy/manage it yourself.
- GitOps is complementary to Kubespray: **Kubespray manages the cluster** (nodes, control
  plane, add-ons); **ArgoCD manages the workloads** deployed onto it.

## Implementation

**Core objects/workflow (ArgoCD):**

- **Application** — points at a Git repo/path (plain manifests, Helm, or Kustomize) and a
  target cluster/namespace; ArgoCD syncs it.
- **Sync & self-heal** — `syncPolicy.automated` (with `prune`/`selfHeal`) reconciles drift;
  manual sync for gated environments.
- **App-of-apps** — a root Application that manages child Applications, so the whole
  platform is bootstrapped from one Git entry.
- **Sync waves / hooks** — order dependent resources (CRDs before CRs, DB before app).

**Integration with the cluster:**

- ArgoCD runs in its own namespace with a ServiceAccount that needs RBAC to manage the
  resources it deploys — a Forbidden during sync is an RBAC gap
  ([[TROUBLE-RBAC_FORBIDDEN]]).
- Expose the ArgoCD API/UI via a Service/Ingress ([[CONCEPT-SERVICE_EXPOSURE]]); the
  initial admin password is generated (see [[COMPONENT-ARGOCD]]).

## Compatibility

- **DR angle:** with workloads in Git and ArgoCD reconciling, a rebuilt cluster re-applies
  everything from Git — pair this with etcd/PKI backup for full recovery
  ([[PRACTICE-BACKUP_DR]]).
- **ArgoCD vs Flux:** both are CNCF GitOps controllers; ArgoCD has a UI and app-of-apps,
  Flux is more component-based. Pick one; this KB documents the ArgoCD path (Kubespray-
  managed).
- **Version alignment:** ArgoCD version tracks its own release line (Kubespray ships
  `2.14.x`); keep it compatible with your Kubernetes version per ArgoCD's support matrix.
- **Don't GitOps the cluster itself with ArgoCD** — node/control-plane lifecycle stays with
  Kubespray; ArgoCD is for in-cluster workloads/add-ons.

## References

- Kubespray `argocd_*` defaults (`v2.31.0`); Argo CD docs. Component: [[COMPONENT-ARGOCD]];
  DR: [[PRACTICE-BACKUP_DR]]; RBAC: [[TROUBLE-RBAC_FORBIDDEN]].
