---
id: CONCEPT-ADDON_PATCH_PRIORITY
type: concept
title: "Addon security patch priority — what to fix first (from the upstream CVE sweep)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - what to patch first
  - addon cve priority
  - security remediation order
  - critical addon vulnerabilities
  - patch priority matrix
tags:
  - concept
  - security
  - cve
  - addons
  - index
sources:
  - type: analysis
    path: kubepedia/addon upstream CVE sweep (forward + backward), mined 2026-07-19
    note: "ranked from the per-addon 'Upstream issues' and 'Older-version CVEs' sections"
relations:
  - type: see_also
    target: CONCEPT-SECURITY_INDEX
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
  - type: see_also
    target: CONCEPT-CVE_REMEDIATION
---

# Addon security patch priority — what to fix first (from the upstream CVE sweep)

## Summary

A single **actionable ranking** of the addon-security findings from the upstream CVE sweep (forward +
backward, mined 2026-07-19). Fix top-down. Each item names the CVE, the fixed version, and — where it
matters more than a version bump — the **config hardening** or **migration** that actually removes the
risk. Details and sources live in each addon's `Upstream issues` / `Older-version CVEs` sections.

## Context

### P0 — drop everything (CVSS ~10 / RCE / cluster-takeover)

| Addon | Issue | Fix |
|---|---|---|
| **Kyverno** | **CVE-2026-22039 (CVSS 10)** cross-namespace priv-esc via policy `apiCall` (+ **CVE-2026-4789** SSRF → cloud metadata creds, **CVE-2026-41068** ConfigMap-loader variant) — envelope floor 1.10 is exposed | **≥1.16.3 / ≥1.18.2** |
| **Argo CD** | **CVE-2025-55190 (CVSS 10.0)** project-scoped API token retrieves **repository credentials** | **2.13.9 / 2.14.16 / 3.0.14 / 3.1.2+** + scope project tokens |
| **ingress-nginx** | **CVE-2025-1974 "IngressNightmare"** (unauth RCE via admission) **+** the 2023 annotation-injection set (**CVE-2023-5044/5043**, controller can read all cluster Secrets) | **≥1.12.1**, **`allow-snippet-annotations: false`**, `--enable-annotation-validation`, restrict Ingress RBAC |
| **Envoy Gateway** | **CVE-2026-53713 (CRITICAL)** Lua path-traversal → secret disclosure **+ CVE-2026-53714** xDS auth bypass — **the pinned 1.6.0 is vulnerable** | **≥1.8.1** |
| **GPU Operator** | **CVE-2024-0132 (CRITICAL)** TOCTOU container escape / host-FS access (if running **<24.6.1**) | **≥24.6.2** (libnvidia-container ≥1.16.2) |

### P1 — high (auth bypass / secret disclosure / privilege)

| Addon | Issue | Fix |
|---|---|---|
| **Vault** | **CVE-2025-13357** LDAP `deny_null_bind=false` auth bypass; **CVE-2025-11621** AWS-auth account-ID bypass; **HCSEC-2025-22** batch (token elevation, operator RCE, MFA bypass…) | 1.16.28 / 1.19.12 / 1.20.6 / **1.21.x**; audit LDAP/AWS auth config |
| **cert-manager** | **GHSA-8rvj-mm4h-c258 (High)** ACME Challenge/Order RBAC + **CVE-2026-25518** DNS-01 panic DoS | **1.19.6 / 1.20.3+** |
| **vault-secrets-webhook** | **<1.23.1** trusts object-supplied `vault-addr` (SSRF) | **≥1.23.1** + set `VAULT_ADDR_ALLOWLIST` |
| **OTel Operator** | **CVE-2026-47701** ServiceMonitor `bearerTokenFile` arbitrary file read (**<0.152.0**) | **≥0.152.0** |
| **tbot / Teleport** | **<18.9.2** AWS app-access SSRF (+ other 18.x hardening) | **≥18.9.2**, track 18.x |
| **KEDA** | **CVE-2025-68476** Vault-cred path-traversal (shipped **2.17.2** affected) | **≥2.17.3** |

### P2 — medium / hardening

- **VictoriaMetrics:** `vmrestore` path traversal (CVE-2026-61625), snappy-decoder DoS (CVE-2025-65942) → 1.146.0 / 1.136.12 / 1.122.25.
- **Capsule:** tenant-isolation regex-bypass advisories → **≥0.13.8**.
- **Gigapipe/qryn:** reflected XSS **<4.3.1** → **≥4.3.1** + front with auth.
- **Alertmanager:** stored XSS **0.25.0** → **0.25.1** (override the chart `image.tag`).
- **Velero:** very old (**<1.4.3/1.5.2**) restore-PV-mismatch (CVE-2020-3996).

### Replace / migrate (no patch exists — frozen or dead upstream)

- **RabbitMQ (Bitnami chart):** images frozen in `bitnamilegacy` since 2025-08-28, **no CVE patches** → migrate to the **RabbitMQ Cluster Operator**.
- **Kubernetes Dashboard:** repo archived, no fixes → migrate to **Headlamp**.
- **kvm-device-plugin:** upstream dead since 2020 → maintained KVM plugin / current **KubeVirt**.
- **Spegel:** the `0.0.1` pin is a phantom → move to **0.7.x** (mind containerd 1.7/2.0 drop).

### Config hardening (do regardless of version)

- **ingress-nginx:** `allow-snippet-annotations: false`, annotation validation on, tighten who can edit Ingress.
- **Admission webhooks** (Kyverno, vault-secrets-webhook, cert-manager, OTel): scope `failurePolicy`/selector so a down webhook can't block pod creation cluster-wide, and exempt system namespaces.
- **RBAC as the boundary:** kubernetes-mcp and any dashboard act as their ServiceAccount — minimize that SA's RBAC.

## References

- Ranked from the per-addon `Upstream issues & upgrade notes` and `Older-version CVEs & security
  history` sections (sweep dated 2026-07-19). Security layer: [[CONCEPT-SECURITY_INDEX]]; CVE workflow:
  [[CONCEPT-CVE_REMEDIATION]]; catalog: [[CONCEPT-ADDON_CATALOG]].
