---
id: UPGRADE-ARGOCD_2_11_TO_2_14
type: upgrade
title: "Argo CD upgrade 2.11 → 2.14 across Kubespray v2.27.0–v2.31.0 (cumulative breaking changes)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=2.11.0 <=2.14.21"
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - argocd upgrade breaking changes
  - argocd 2.11 to 2.14
  - argocd self-heal backoff default
  - argocd ignoreResourceUpdatesEnabled
  - argocd redis ecr registry
  - argocd kubernetes compatibility
tags:
  - argocd
  - gitops
  - upgrade
  - breaking-changes
sources:
  - type: docs
    path: docs/operator-manual/upgrading/
    url: https://github.com/argoproj/argo-cd/tree/v2.14.21/docs/operator-manual/upgrading
    note: "per-minor upgrade guides 2.11-2.12 / 2.12-2.13 / 2.13-2.14 read at tags v2.12.0/v2.13.0/v2.14.21"
  - type: docs
    path: docs/operator-manual/tested-kubernetes-versions.md
    url: https://github.com/argoproj/argo-cd/blob/v2.14.5/docs/operator-manual/tested-kubernetes-versions.md
    note: "Argo CD 2.11 tested k8s v1.25–v1.29; 2.14 tested v1.28–v1.31"
relations:
  - type: see_also
    target: COMPONENT-ARGOCD
  - type: see_also
    target: TROUBLE-ARGOCD_REDIS_ECR_AIRGAP
  - type: depends_on
    target: UPGRADE-KUBESPRAY_SEQUENTIAL
  - type: see_also
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
---

# Argo CD upgrade 2.11 → 2.14 across Kubespray v2.27.0–v2.31.0 (cumulative breaking changes)

## Summary

Kubespray pins Argo CD **2.11.0** in v2.27.0 and **2.14.x** from v2.28.0 onward (effective
**2.14.20/2.14.21** by the computed-checksum resolution — [[COMPONENT-ARGOCD]]). Because Kubespray
jumps **2.11 → 2.14 in one step**, every breaking change introduced across **2.12, 2.13 and 2.14
applies cumulatively**. Argo CD is **disabled by default** (`argocd_enabled: false`), so this only
matters if you enable it — but if you do, the jump crosses three minors of upstream changes at once.

## Implementation

- Kubespray applies the upstream Argo CD `install.yaml` manifest for the pinned version into the
  `argocd` namespace ([[COMPONENT-ARGOCD]]); upgrading = applying the newer manifest on a cluster
  upgrade. There is no Kubespray-managed data migration — Argo CD's own upgrade notes below are the
  checklist.
- **Version by Kubespray tag:** 2.11.0 (v2.27.0) → 2.14.20 (v2.29.0) → 2.14.21 (v2.29.1+). Moving
  v2.27.0 → v2.28.0+ is the 2.11 → 2.14 jump.

## Upgrade Notes

### 2.11 → 2.12 (`docs/operator-manual/upgrading/2.11-2.12.md`@v2.12.0)

- **Registry move (biggest for Kubespray):** bundled `redis-ha` chart moved the **redis** and
  **haproxy** images from **DockerHub → AWS ECR**. Air-gapped / mirrored / policy-restricted installs
  must pre-mirror the ECR images or pods won't pull — see [[TROUBLE-ARGOCD_REDIS_ECR_AIRGAP]].
- **ApplicationSet SSA/CRD:** selector fields (`.spec.generators[].selector`, `.cluster.selector`,
  `.clusterDecisionResource.labelSelector`, matrix/merge selectors) became
  `x-kubernetes-map-type: atomic` — with server-side apply, a **single** field manager must own both
  `matchLabels` and `matchExpressions`.
- **Config:** repo-server excludes hidden Git dirs by default (`reposerver.include.hidden.directories:
  "false"`); new `webhook.maxPayloadSizeMB`, event-label keys in argocd-cm. Bundled Helm 3.14→3.15.

### 2.12 → 2.13 (`docs/operator-manual/upgrading/2.12-2.13.md`@v2.13.0)

- **Self-heal timing (default change):** `controller.self.heal.timeout.seconds` default **5 → 2** and
  self-heal became **exponential backoff** (`controller.self.heal.backoff.factor: "3"`,
  `...backoff.cap.seconds: "300"`).
- **Stricter LDAP:** Dex → v2.39.0 tightened LDAP username/password validation (EscapeFilter) —
  logins with special characters may start failing.
- **ApplicationSet policy:** `applicationsetcontroller.policy` default `"sync"` → `""`; new
  `applicationsetcontroller.enable.policy.override` gates per-AppSet policy override.
- **RBAC:** Flux CR actions/health checks added — update RBAC if you drive Flux CRs.
- Minor: manual Job name postfix `-YYYYMMDDHHmm` → `-YYMMDDHHmm`; downloaded logs `.txt` → `.log`.

### 2.13 → 2.14 (`docs/operator-manual/upgrading/2.13-2.14.md`@v2.14.21)

- **CVE / API sanitization (GHSA-786q-9hcg-v9ff):** the project API response now **strips
  project-scoped repository and cluster credentials** — tooling that read those fields no longer
  receives them.
- **Default change:** `resource.ignoreResourceUpdatesEnabled` **false → true** — Argo CD now ignores
  resource-update-only events by default (external cluster state changes surface more slowly).
- **TLS hardened:** default `server.tls.ciphers` / `reposerver.tls.ciphers` drop
  `TLS_RSA_WITH_AES_256_GCM_SHA384` — clients relying on it fail TLS.
- **New (alpha):** source/manifest **hydrator** (`hydrator.enabled`) + a new **commit-server**
  component. Bundled Helm → 3.16.

## Compatibility

- **Kubernetes compatibility per Argo CD version** (`tested-kubernetes-versions.md`): Argo CD **2.11**
  tested on k8s **v1.25–v1.29**; **2.14** tested on **v1.28–v1.31**. Kubespray's range spans ~k8s
  1.29–1.35, so **Argo CD 2.14.x is not tested above k8s v1.31** — running it on Kubespray targets at
  **k8s 1.32+** is outside Argo CD's tested matrix (untested upstream, not necessarily broken —
  [[CONCEPT-KUBERNETES_VERSION_SUPPORT]]).
- **Cumulative jump:** all 2.12/2.13/2.14 breaking items apply together on the v2.27.0→v2.28.0 move.
  Highest-impact for a Kubespray (often offline) install: (1) redis/haproxy **DockerHub→ECR**
  pre-mirror; (2) self-heal exponential backoff; (3) `ignoreResourceUpdatesEnabled` flip;
  (4) stricter LDAP if SSO uses Dex/LDAP; (5) narrowed TLS ciphers.
- **CVE scope:** only **GHSA-786q-9hcg-v9ff** is documented in the in-repo upgrade guides for this
  range; other CVEs fixed in 2.11.x/2.12.x/2.13.x patches are not enumerated there (unverified here).

## References

- Argo CD `docs/operator-manual/upgrading/{2.11-2.12,2.12-2.13,2.13-2.14}.md` (@v2.12.0/v2.13.0/
  v2.14.21) and `tested-kubernetes-versions.md`. Component [[COMPONENT-ARGOCD]]; air-gap gotcha
  [[TROUBLE-ARGOCD_REDIS_ECR_AIRGAP]]; sequencing [[UPGRADE-KUBESPRAY_SEQUENTIAL]].
