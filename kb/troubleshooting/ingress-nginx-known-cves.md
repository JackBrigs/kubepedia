---
id: TROUBLE-INGRESS_NGINX_KNOWN_CVES
type: troubleshooting
title: "ingress-nginx: known CVEs by shipped version (osv.dev)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: ">=1.12.0 <=1.13.3"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - ingress-nginx cve
  - ingress-nginx security
  - is ingress-nginx vulnerable
tags:
  - security
  - cve
  - ingress-nginx
sources:
  - type: docs
    path: osv.dev API (k8s.io/ingress-nginx)
    url: https://osv.dev/list?q=k8s.io/ingress-nginx
    note: "version-filtered vulnerability data, queried per shipped version"
relations:
  - type: see_also
    target: COMPONENT-INGRESS_NGINX
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
---

# ingress-nginx: known CVEs by shipped version (osv.dev)

## Summary

osv.dev reports **10 distinct CVEs** affecting the ingress-nginx versions Kubespray ships across
v2.27.0–v2.31.0. The newest shipped version (1.13.3, v2.30.0) is affected by **5**;
the worst tag is v2.27.0 with 10.

Counts are distinct advisories. osv.dev returns one record per database (GHSA *and* GO) for the same
CVE, so a raw record count roughly doubles it.

## Problem

Each shipped version carries the CVEs below. osv.dev returns only vulnerabilities that affect the
queried version, so this is authoritative affectedness rather than a guess from release notes.

## Context

| Kubespray | Component version | # CVEs | CVEs |
|---|---|---:|---|
| v2.27.0 | 1.12.0 | 10 | CVE-2023-5044, CVE-2025-1097, CVE-2025-1098, CVE-2025-1974, CVE-2025-24513, CVE-2025-24514, CVE-2026-1580, CVE-2026-24512, CVE-2026-24513, CVE-2026-24514 |
| v2.27.1 | 1.12.1 | 5 | CVE-2023-5044, CVE-2026-1580, CVE-2026-24512, CVE-2026-24513, CVE-2026-24514 |
| v2.28.0 | 1.12.1 | 5 | CVE-2023-5044, CVE-2026-1580, CVE-2026-24512, CVE-2026-24513, CVE-2026-24514 |
| v2.28.1 | 1.12.1 | 5 | CVE-2023-5044, CVE-2026-1580, CVE-2026-24512, CVE-2026-24513, CVE-2026-24514 |
| v2.29.0 | 1.13.3 | 5 | CVE-2023-5044, CVE-2026-1580, CVE-2026-24512, CVE-2026-24513, CVE-2026-24514 |
| v2.29.1 | 1.13.3 | 5 | CVE-2023-5044, CVE-2026-1580, CVE-2026-24512, CVE-2026-24513, CVE-2026-24514 |
| v2.30.0 | 1.13.3 | 5 | CVE-2023-5044, CVE-2026-1580, CVE-2026-24512, CVE-2026-24513, CVE-2026-24514 |

## Diagnostics

```bash
kubectl get pods -A -o jsonpath='{range .items[*]}{range .spec.containers[*]}{.image}{"\n"}{end}{end}' \
  | grep -i ingress-nginx | sort -u
```

## Known Issues


CVEs (id — summary — fixed in):

- **CVE-2023-5044** — Ingress-nginx code injection via nginx.ingress.kubernetes.io/permanent-redirect annotation in k8s.io/ingress-nginx — fixed in: `no fix released`
- **CVE-2025-1097** — ngress-nginx controller - configuration injection via unsanitized auth-tls-match-cn annotation — fixed in: `1.11.5, 1.12.1`
- **CVE-2025-1098** — ingress-nginx controller - configuration injection via unsanitized mirror annotations — fixed in: `1.11.5, 1.12.1`
- **CVE-2025-1974** — ingress-nginx admission controller RCE escalation — fixed in: `1.11.5, 1.12.1`
- **CVE-2025-24513** — ingress-nginx controller - auth secret file path traversal vulnerability — fixed in: `1.11.5, 1.12.1`
- **CVE-2025-24514** — ingress-nginx controller - configuration injection via unsanitized auth-url annotation — fixed in: `1.11.5, 1.12.1`
- **CVE-2026-1580** — ingress-nginx's `nginx.ingress.kubernetes.io/auth-method` Ingress annotation can be used to inject configuration into nginx — fixed in: `1.13.7, 1.14.3`
- **CVE-2026-24512** — ingress-nginx's `rules.http.paths.path` Ingress field can be used to inject configuration into nginx — fixed in: `1.13.7, 1.14.3`
- **CVE-2026-24513** — ingress-nginx has Improper Check for Unusual or Exceptional Conditions — fixed in: `1.13.7, 1.14.3`
- **CVE-2026-24514** — ingress-nginx vulnerable to Allocation of Resources Without Limits or Throttling — fixed in: `1.13.7, 1.14.3`

**Recommendation:** compare the version in use against the "fixed in" column. When Kubespray pins a
version below the fix, the remedy is an explicit pin in inventory plus the matching checksum — the
same pattern as for the container runtime; see [[CONCEPT-SECURITY_INDEX]].

## References

- osv.dev queried per shipped version for `k8s.io/ingress-nginx` — verified 2026-07-31.
- Component: [[COMPONENT-INGRESS_NGINX]]; tracking: [[CONCEPT-SECURITY_ADVISORIES]].
