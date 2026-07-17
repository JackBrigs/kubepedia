---
id: TROUBLE-ARGOCD_REDIS_ECR_AIRGAP
type: troubleshooting
title: "Argo CD 2.12+ redis/haproxy moved DockerHub→ECR — pull fails in air-gapped/mirrored clusters"
status: active
kubespray_version: ">=v2.28.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=2.12.0 <=2.14.21"
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - argocd redis imagepullbackoff
  - argocd haproxy ecr
  - argocd redis-ha dockerhub to ecr
  - argocd air-gapped image pull
  - redis-ha public.ecr.aws
tags:
  - argocd
  - troubleshooting
  - offline
  - registry
sources:
  - type: docs
    path: docs/operator-manual/upgrading/2.11-2.12.md
    url: https://github.com/argoproj/argo-cd/blob/v2.12.0/docs/operator-manual/upgrading/2.11-2.12.md
    note: "redis-ha chart 4.22.3→4.26.6; redis & haproxy image registry moved DockerHub→ECR"
relations:
  - type: see_also
    target: UPGRADE-ARGOCD_2_11_TO_2_14
  - type: see_also
    target: COMPONENT-ARGOCD
  - type: see_also
    target: PRACTICE-OFFLINE_ENVIRONMENT
  - type: see_also
    target: TROUBLE-IMAGEPULLBACKOFF
---

# Argo CD 2.12+ redis/haproxy moved DockerHub→ECR — pull fails in air-gapped/mirrored clusters

## Summary

When Argo CD's bundled `redis-ha` chart was upgraded (4.22.3 → 4.26.6) in **2.12**, the **redis** and
**haproxy** images moved from **DockerHub to AWS ECR** (`public.ecr.aws/...`). On a cluster that pulls
only from a private mirror or enforces an image-registry allow-list (Cosign/admission policy), the
redis-ha pods hit `ImagePullBackoff` or are **denied admission** after upgrading Argo CD across the
2.11→2.14 gap. Kubespray installs are frequently offline/mirrored, so this is the single most likely
break when enabling Argo CD on v2.28.0+.

## Problem

- After upgrading Argo CD (Kubespray v2.27.0 → v2.28.0+, i.e. 2.11 → 2.14.x), `argocd-redis-ha-*`
  and `argocd-redis-ha-haproxy-*` pods are `ImagePullBackOff` / `ErrImagePull`.
- Or the pods are **rejected at admission** by an image-signature / approved-registry policy that
  doesn't include AWS ECR.
- Argo CD itself (server/repo-server/controller) may be up, but sync/HA is degraded because Redis HA
  is down.

## Context

- Applies to Argo CD **2.12+** (so Kubespray **v2.28.0–v2.31.0**, which ships 2.14.x —
  [[COMPONENT-ARGOCD]] / [[UPGRADE-ARGOCD_2_11_TO_2_14]]). Kubespray pins Argo CD 2.11.0 in v2.27.0
  where the images were still on DockerHub; the move bites on the jump to v2.28.0+.
- Root cause: the bundled `redis-ha` Helm chart bump changed the default image registry for the redis
  and haproxy images to ECR (`docs/operator-manual/upgrading/2.11-2.12.md`@v2.12.0). Non-HA mode
  (single `argocd-redis`) uses a different image and may be unaffected — this specifically hits the
  **redis-ha** deployment.

## Diagnostics

- Find the failing image: `kubectl -n argocd get pods | grep redis` then
  `kubectl -n argocd describe pod <redis-ha-pod>` → look at the `Image:` and the pull error (host is
  an ECR/`public.ecr.aws` registry your mirror doesn't have).
- Confirm it's a registry/policy issue vs network: `kubectl -n argocd get events --field-selector
  reason=Failed` — `ImagePullBackOff` (missing in mirror) vs a policy `denied` message (admission).

## Known Issues

- **Fix (mirrored/offline — [[PRACTICE-OFFLINE_ENVIRONMENT]]):** mirror the ECR redis-ha images into
  your private registry **before** upgrading, and override the chart image registry/repository so the
  pods pull from the mirror ([[TROUBLE-IMAGEPULLBACKOFF]] for the general mirror/override pattern).
- **Fix (policy-restricted):** add the AWS ECR registry to the Cosign / approved-registry allow-list
  before upgrading, or re-sign the mirrored images under your own registry.
- **Pre-upgrade check:** diff the redis-ha image references between the 2.11 and 2.14 install
  manifests and pre-stage every new image — the redis and haproxy images are the ones that moved.
- This is an **upgrade-time** break: a fresh 2.14 install on a properly-mirrored cluster is fine once
  the ECR images are mirrored; the surprise is that a working 2.11 install breaks on upgrade because
  the image source changed underneath it.

## References

- Argo CD `docs/operator-manual/upgrading/2.11-2.12.md`@v2.12.0 (redis-ha chart bump + ECR move).
  Upgrade overview [[UPGRADE-ARGOCD_2_11_TO_2_14]]; component [[COMPONENT-ARGOCD]]; offline mirroring
  [[PRACTICE-OFFLINE_ENVIRONMENT]]; general pull-fail [[TROUBLE-IMAGEPULLBACKOFF]].
