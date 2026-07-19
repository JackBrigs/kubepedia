---
id: CONCEPT-ADDON_KYVERNO
type: concept
title: "Kyverno (policy engine) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=1.10.0 <=1.18.2"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - kyverno
  - kyverno policy engine
  - kyverno admission controller
tags:
  - addons
  - policy
  - admission
  - security
sources:
  - type: docs
    path: Kyverno release notes (per vX.Y.0 tag)
    url: https://github.com/kyverno/kyverno/releases
    note: "breaking changes verified from tagged release pages"
  - type: docs
    path: Kyverno high-availability / architecture
    url: https://kyverno.io/docs/high-availability/
    note: "split controllers (admission/background/reports/cleanup) since 1.10"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
  - type: see_also
    target: TROUBLE-ADMISSION_WEBHOOK_BLOCKING
---

# Kyverno (policy engine) — addon

## Summary

Kyverno is a Kubernetes-native **policy engine** (validate / mutate / generate / verifyImages /
cleanup) implemented as admission webhooks + controllers. The stable line spans **1.0 →
1.18.2** (latest). **Correction to a common belief:** the monolith was split into separate
**admission / background / reports / cleanup** controllers in **1.10**, *not* 1.12. Kyverno
upgrades are frequently breaking — read the per-minor notes before bumping.

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]]. Owner's exact version was
  not specified — this doc tracks the version history; confirm the deployed tag.
- As an admission engine it shares the cluster-wide webhook blast radius
  ([[TROUBLE-ADMISSION_WEBHOOK_BLOCKING]]) — `failurePolicy`/selectors matter a lot.

## Implementation

- **Architecture (since 1.10):** four Deployments — admission-controller (webhook),
  background-controller (generate/mutate-existing + UpdateRequests), reports-controller
  (PolicyReports), cleanup-controller (cleanup policies). Each has its own RBAC/role; give the
  background/reports controllers enough memory (they're the OOM-prone ones).
- **Latest app:** 1.18.2 (2026-07-10). Chart repo `kyverno/charts`: **chart 3.0.0 = app
  1.10.0**, latest **chart 3.8.2 = app 1.18.2** (chart-minor ≈ app-minor from 3.0). A direct
  chart **2.x → 3.x** upgrade is **unsupported** (manual steps required).

## Configuration

- Scope `failurePolicy` + `namespaceSelector`/`objectSelector` to exclude `kube-system` and
  Kyverno's own namespace, so a Kyverno outage can't block the whole cluster
  ([[TROUBLE-KYVERNO_WEBHOOK_HA]]).
- Manage the **CRDs separately** (server-side apply) — client-side apply blows the 256 KB
  annotation limit ([[TROUBLE-KYVERNO_UPGRADE]]).
- At scale, cap report/UpdateRequest growth ([[TROUBLE-KYVERNO_REPORTS_ETCD_SCALE]]).

## Compatibility

- **Kubernetes compatibility (N-2 policy, ~3 months patch support per minor):**

  | Kyverno | K8s range | Status |
  |---------|-----------|--------|
  | 1.13.x | 1.28–1.31 | EOL |
  | 1.14.x | 1.29–1.32 | EOL |
  | 1.15.x | 1.30–1.33 | EOL |
  | 1.16.x | 1.31–1.34 | supported |
  | 1.17.x | 1.32–1.35 | supported |
  | 1.18.x | 1.33–1.35 | supported (current) |

  Everything **≤1.15 is EOL**. Kyverno 1.14+ generates **ValidatingAdmissionPolicy** (CEL)
  objects — needs a K8s version with VAP.
- **Notable breaking changes by minor** (from the release tags):
  - **1.10** — controller split (no raw-YAML upgrade path; Helm-only with manual steps),
    generate fields immutable, `generate.apiVersion` required, subresource match
    `Parent/subresource`, GenerateRequest→UpdateRequest, implicit `docker.io` removed.
  - **1.11** — PolicyReports per-resource (named by UID); Cosign 2.0 (Rekor URL required);
    PolicyExceptions/CleanupPolicies → beta (cleanup no longer uses CronJobs); CLI restructure
    (`manifest`→`create`).
  - **1.12** — API storage versions → **v2** (auto CRD-migration hooks); RBAC hardening
    (wildcards removed); PolicyException now evaluates existing resources. **Upgrade to
    1.12.4+** (1.12.0 has ephemeralreports/etcd-growth bugs).
  - **1.13** — `validationFailureAction` moved **policy-level → rule-level**; PolicyException
    default enablement removed (**CVE-2024-48921** / GHSA-qjvc-p88j-j9rm); VAP v1alpha1→v1beta1;
    admission/background report types removed.
  - **1.14** — VAP → v1; new CEL-first `ValidatingPolicy`/`ImageValidatingPolicy`; namespace-
    selector bypass fix.
  - **1.15** — CEL `image()` renamed **`parseImageReference`**; new CEL Mutating/Generating/
    Deleting policies; VAP generation on by default.
  - **1.16** — `UpdateRequest v1beta1` marked **unserved**; standalone CRDs chart.
  - **1.17** — VAP/MAP reporting switched **opt-out → opt-in**; Cosign v3.
  - **1.18** — no breaking changes flagged; admission-controller memory autoscaling.
- **CVEs (Kyverno has ~21 core advisories — run the latest patch):** the biggest concentration
  is a **2026 wave in 1.15–1.18** (apiCall SSRF, ServiceAccount-token leakage, cross-namespace
  reads, generate-based escalation). Highlights:
  - **CVE-2026-54523 / GHSA-79gf-7frw-68m9** (**Critical 9.6**) — unvalidated namespace in CEL
    `generator.apply()` lets the background-controller create RoleBindings in **any namespace
    incl. kube-system → cluster-admin escalation**. Affected **≤1.18.1, fixed 1.18.2**.
  - **CVE-2026-22039** (Critical) — namespaced apiCall reads cross-namespace secrets as the
    Kyverno SA; fixed 1.15.3 / 1.16.3. Follow-up CVE-2026-41068 fixed 1.17.2.
  - **CVE-2026-4789 / GHSA-rggm-jjmc-3394** (High) — SSRF via CEL `http.Get/Post`; fixed 1.16.4
    (1.18 blocks loopback/metadata + disables namespaced HTTP by default).
  - SA-token leakage set (CVE-2026-41323/-40868, GHSA-8wfp…) — all fixed **1.16.4**.
  - **GHSA-gg4x-fgg2-h9w9** (Critical) enforce-bypass via double PolicyExceptions — fixed 1.13.0;
    **CVE-2024-48921** (PolicyException any-namespace override) — fixed **1.13.0**.
  - DoS: forEach-mutation panic (CVE-2026-41485, fixed 1.17.2/1.16.4), JMESPath OOM
    (CVE-2026-23881), namespace-selector bypass on lister error (CVE-2025-46342, fixed 1.13.5/1.14.0).
  - Older image-verify bypasses: CVE-2022-47633 (fixed 1.8.5), CVE-2023-47630 (fixed 1.10.5/1.11.0).

## Upstream issues & upgrade notes (mined 2026-07-19)

**Upstream (Kyverno 1.18.2, from release notes):**
- **Security fix:** namespace-boundary enforcement added to `generator.apply()` — generate policies can no longer cross namespace boundaries. Ensure you're on **1.18.2+**.
- Dynamic watchers now restart background reporting on **`410 Gone`** (fixes stalled reports); required validation no longer aborts on non-matching images.
- No breaking changes in this patch; the big webhook/HA and CEL considerations remain (see the Kyverno troubleshooting/upgrade docs).

## References

- Kyverno release tags + HA/architecture docs (above). Troubleshooting:
  [[TROUBLE-KYVERNO_WEBHOOK_HA]], [[TROUBLE-KYVERNO_REPORTS_ETCD_SCALE]],
  [[TROUBLE-KYVERNO_POLICY_NOT_APPLYING]], [[TROUBLE-KYVERNO_UPGRADE]]. Catalog:
  [[CONCEPT-ADDON_CATALOG]].
