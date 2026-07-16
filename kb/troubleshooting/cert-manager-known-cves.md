---
id: TROUBLE-CERT_MANAGER_KNOWN_CVES
type: troubleshooting
title: "cert-manager: known CVEs by shipped version (osv.dev)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: ">=1.15.3 <=1.15.3"
verified_at: "2026-07-16"
confidence: verified
aliases:
  - cert-manager cve
tags:
  - security
  - cve
  - cert-manager
sources:
  - type: docs
    path: osv.dev API (github.com/cert-manager/cert-manager)
    url: https://osv.dev/list?q=github.com/cert-manager/cert-manager
    note: "authoritative version-filtered vulnerability data"
relations:
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
---

# cert-manager: known CVEs by shipped version (osv.dev)

## Summary

osv.dev reports **1 unique CVEs** affecting the cert-manager versions Kubespray ships; the newest (1.15.3, v2.29.0-v2.31.0) is still affected by **1** — no fully-patched Kubespray release yet.

## Problem

Each shipped cert-manager version carries the CVEs below (osv.dev returns only vulns affecting the queried version — authoritative affectedness).

## Context

| Version | Kubespray | # | CVEs |
|---|---|---|---|
| 1.15.3 | v2.29.0-v2.31.0 | 1 | CVE-2024-12401 |

## Diagnostics

```bash
kubectl -n cert-manager get deploy -o jsonpath='{.items[*].spec.template.spec.containers[*].image}'
```

## Known Issues

CVEs (id — summary — fixed in):

- **CVE-2024-12401** [CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:N/VA:L/SC:N/SI:N/SA:N] — cert-manager ha a potential slowdown / DoS when parsing specially crafted PEM inputs — fixed in: `1.12.14, 1.15.4, 1.16.2`

**Recommendation:** upgrade to the newest Kubespray release (v2.29.0-v2.31.0). For CVEs still open at 1.15.3, pin/patch cert-manager to a fixed upstream release or apply mitigation; reduce blast radius with PRACTICE-HARDENING.

## References

- osv.dev (queried per version) for `github.com/cert-manager/cert-manager` — verified 2026-07-16.
- Tracking: [[CONCEPT-SECURITY_ADVISORIES]].