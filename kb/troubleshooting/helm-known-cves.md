---
id: TROUBLE-HELM_KNOWN_CVES
type: troubleshooting
title: "helm: known CVEs by shipped version (osv.dev)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: ">=3.18.4 <=3.18.4"
verified_at: "2026-07-16"
confidence: verified
aliases:
  - helm cve
tags:
  - security
  - cve
  - helm
sources:
  - type: docs
    path: osv.dev API (helm.sh/helm/v3)
    url: https://osv.dev/list?q=helm.sh/helm/v3
    note: "authoritative version-filtered vulnerability data"
relations:
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
---

# helm: known CVEs by shipped version (osv.dev)

## Summary

osv.dev reports **3 unique CVEs** affecting the helm versions Kubespray ships; the newest (3.18.4, v2.29.0-v2.31.0) is still affected by **3** — no fully-patched Kubespray release yet.

## Problem

Each shipped helm version carries the CVEs below (osv.dev returns only vulns affecting the queried version — authoritative affectedness).

## Context

| Version | Kubespray | # | CVEs |
|---|---|---|---|
| 3.18.4 | v2.29.0-v2.31.0 | 3 | CVE-2025-55198, CVE-2025-55199, CVE-2026-35206 |

## Diagnostics

```bash
helm version
```

## Known Issues

CVEs (id — summary — fixed in):

- **CVE-2025-55198** [CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H] — Helm May Panic Due To Incorrect YAML Content — fixed in: `3.18.5`
- **CVE-2025-55199** [CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H] — Helm Charts with Specific JSON Schema Values Can Cause Memory Exhaustion — fixed in: `3.18.5`
- **CVE-2026-35206** [CVSS:4.0/AV:L/AC:L/AT:N/PR:N/UI:P/VC:N/VI:L/VA:L/SC:N/SI:N/SA:N] — Helm Chart extraction output directory collapse via `Chart.yaml` name dot-segment — fixed in: `3.20.2`

**Recommendation:** upgrade to the newest Kubespray release (v2.29.0-v2.31.0). For CVEs still open at 3.18.4, pin/patch helm to a fixed upstream release or apply mitigation; reduce blast radius with PRACTICE-HARDENING.

## References

- osv.dev (queried per version) for `helm.sh/helm/v3` — verified 2026-07-16.
- Tracking: [[CONCEPT-SECURITY_ADVISORIES]].