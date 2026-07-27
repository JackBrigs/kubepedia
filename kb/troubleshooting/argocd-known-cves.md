---
id: TROUBLE-ARGOCD_KNOWN_CVES
type: troubleshooting
title: "Argo CD: known CVEs by shipped version (osv.dev)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: ">=2.11.0 <=2.14.21"
verified_at: "2026-07-27"
confidence: verified
aliases:
  - argocd cve
  - argo cd security
tags:
  - security
  - cve
  - argocd
  - addons
sources:
  - type: docs
    path: osv.dev API (github.com/argoproj/argo-cd/v2)
    url: https://osv.dev/list?q=github.com/argoproj/argo-cd
    note: "the 2.x module path; Kubespray ships only 2.x, so the /v2 module is the correct one to query"
relations:
  - type: see_also
    target: COMPONENT-ARGOCD
  - type: see_also
    target: UPGRADE-ARGOCD_2_11_TO_2_14
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
---

# Argo CD: known CVEs by shipped version (osv.dev)

## Summary

osv.dev reports **16 distinct advisories** across the Argo CD versions Kubespray ships (see
[COMPONENT-ARGOCD]). Here the version actually matters: **2.11.0** (v2.27.0/v2.27.1) carries **14**,
including unauthenticated DoS and unauthenticated access to sensitive settings; **2.14.21**
(v2.29.1–v2.31.0) carries **3**. Moving off the 2.11 line is the single largest CVE reduction
available anywhere in the Kubespray add-on set.

The three that remain are fixed only in **3.2.12 / 3.3.10 / 3.4.2** — the Argo CD 3.x line, which
Kubespray does not ship at any tag in the envelope.

Counts are **distinct advisories**. Argo CD 2.x lives at the Go module
`github.com/argoproj/argo-cd/v2`; querying the 3.x module path for a 2.x version returns unrelated
results.

## Problem

Argo CD holds cluster-admin-grade credentials for everything it deploys, so the extraction and
privilege-escalation classes below are not scoped to the Argo namespace.

## Context

| Component version | Kubespray | # CVEs | CVEs |
|---|---|---|---|
| 2.11.0 | v2.27.0 / v2.27.1 | 14 | CVE-2024-31989, CVE-2024-36106, CVE-2024-37152, CVE-2024-40634, CVE-2024-41666, CVE-2025-23216, CVE-2025-47933, CVE-2025-55191, CVE-2025-59531, CVE-2025-59537, CVE-2025-59538, CVE-2026-42880, CVE-2026-45737, CVE-2026-45738 |
| 2.14.5 | v2.28.0 / v2.28.1 | 9 | CVE-2025-47933, CVE-2025-55190, CVE-2025-55191, CVE-2025-59531, CVE-2025-59537, CVE-2025-59538, CVE-2026-42880, CVE-2026-45737, CVE-2026-45738 |
| 2.14.20 | v2.29.0 | 3 | CVE-2026-42880, CVE-2026-45737, CVE-2026-45738 |
| 2.14.21 | v2.29.1 / v2.30.0 / v2.31.0 | 3 | CVE-2026-42880, CVE-2026-45737, CVE-2026-45738 |

Note `CVE-2025-55190` affects 2.14.5 but **not** 2.11.0: it was introduced on the 2.13/2.14 line and
fixed in 2.14.16.

## Diagnostics

```bash
kubectl -n argocd get deploy argocd-server -o jsonpath='{.spec.template.spec.containers[*].image}'
argocd version --short
```

## Known Issues

CVEs (id — summary — fixed in):

- **CVE-2024-31989** [CVSS:3.1/AV:A/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H] — risky/missing cryptographic algorithms in the Redis cache — fixed in: `2.8.19, 2.9.15, 2.10.10, 2.11.1`
- **CVE-2024-36106** — authenticated users can enumerate clusters by name — fixed in: `2.9.17, 2.10.12, 2.11.3`
- **CVE-2024-37152** — **unauthenticated** access to sensitive settings — fixed in: `2.9.17, 2.10.12, 2.11.3`
- **CVE-2024-40634** [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H] — **unauthenticated** DoS via the `/api/webhook` endpoint — fixed in: `2.9.20, 2.10.15, 2.11.6`
- **CVE-2024-41666** [CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:L/I:L/A:L] — web terminal session does not handle revocation of user permissions — fixed in: `2.9.21, 2.10.16, 2.11.7`
- **CVE-2025-23216** [CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:N/A:N] — secret values are not scrubbed from patch errors — fixed in: `2.11.13, 2.12.10, 2.13.4`
- **CVE-2025-47933** [CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:H] — cross-site scripting on the repositories page — fixed in: `2.13.8, 2.14.13, 3.0.4`
- **CVE-2025-55190** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H] — project API token exposes repository credentials — fixed in: `2.13.9, 2.14.16, 3.0.14, 3.1.2`
- **CVE-2025-55191** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H] — repository-credentials race condition crashes the Argo CD server — fixed in: `2.14.20, 3.0.19, 3.1.8`
- **CVE-2025-59531** [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H] — **unauthenticated** server panic via a malicious Bitbucket-Server webhook payload — fixed in: `2.14.20, 3.0.19, 3.1.8`
- **CVE-2025-59537** [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H] — **unauthenticated** DoS via a malformed Gogs webhook payload — fixed in: `2.14.20, 3.0.19, 3.1.8`
- **CVE-2025-59538** [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H] — **unauthenticated** remote DoS via a malformed Azure DevOps `git.push` webhook — fixed in: `2.14.20, 3.0.19, 3.1.8`
- **CVE-2026-42880** — `ServerSideDiff` allows Kubernetes Secret extraction — fixed in: `3.2.11, 3.3.9`
- **CVE-2026-45737** — Secret extraction via `ServerSideDiff` through sensitive annotations — fixed in: `3.2.12, 3.3.10, 3.4.2`
- **CVE-2026-45738** [CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:N] — stored XSS in application link annotations enables developer-to-admin privilege escalation — fixed in: `3.2.12, 3.3.10, 3.4.2`

**Recommendation:** if you are on Kubespray v2.27.x, the Argo CD version alone justifies moving up —
four of the fourteen need **no authentication at all**. From v2.29.1 onward Kubespray ships 2.14.21
and only the three `ServerSideDiff`/XSS advisories remain; all three are fixed only in Argo CD 3.x,
which no tag in the envelope ships. Until then: disable or firewall the webhook endpoint you do not
use, and note that the two Secret-extraction advisories are reachable through `ServerSideDiff` — turn
it off if you do not need it. The version-jump path and its breaking changes:
[[UPGRADE-ARGOCD_2_11_TO_2_14]].

## References

- osv.dev (queried per version) for `github.com/argoproj/argo-cd/v2` — verified 2026-07-27.
- Component: [[COMPONENT-ARGOCD]]; upgrade path: [[UPGRADE-ARGOCD_2_11_TO_2_14]]; tracking: [[CONCEPT-SECURITY_ADVISORIES]].
