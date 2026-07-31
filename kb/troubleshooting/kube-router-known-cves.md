---
id: TROUBLE-KUBE_ROUTER_KNOWN_CVES
type: troubleshooting
title: "kube-router: known CVEs by shipped version (osv.dev)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: ">=2.0.0 <=2.1.1"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kube-router cve
  - kube-router security
  - is kube-router vulnerable
tags:
  - security
  - cve
  - kube-router
sources:
  - type: docs
    path: osv.dev API (github.com/cloudnativelabs/kube-router)
    url: https://osv.dev/list?q=github.com/cloudnativelabs/kube-router
    note: "version-filtered vulnerability data, queried per shipped version"
relations:
  - type: see_also
    target: COMPONENT-KUBE_ROUTER
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
---

# kube-router: known CVEs by shipped version (osv.dev)

## Summary

osv.dev reports **4 distinct CVEs** affecting the kube-router versions Kubespray ships across
v2.27.0–v2.31.0. The newest shipped version (2.1.1, v2.31.0) is affected by **4**;
the worst tag is v2.27.0 with 4.

Counts are distinct advisories. osv.dev returns one record per database (GHSA *and* GO) for the same
CVE, so a raw record count roughly doubles it.

## Problem

Each shipped version carries the CVEs below. osv.dev returns only vulnerabilities that affect the
queried version, so this is authoritative affectedness rather than a guess from release notes.

## Context

| Kubespray | Component version | # CVEs | CVEs |
|---|---|---:|---|
| v2.27.0 | 2.0.0 | 4 | CVE-2026-32254, GHSA-v5mh-h5hx-7v92, GO-2026-5354, GO-2026-5653 |
| v2.27.1 | 2.0.0 | 4 | CVE-2026-32254, GHSA-v5mh-h5hx-7v92, GO-2026-5354, GO-2026-5653 |
| v2.28.0 | 2.1.1 | 4 | CVE-2026-32254, GHSA-v5mh-h5hx-7v92, GO-2026-5354, GO-2026-5653 |
| v2.28.1 | 2.1.1 | 4 | CVE-2026-32254, GHSA-v5mh-h5hx-7v92, GO-2026-5354, GO-2026-5653 |
| v2.29.0 | 2.1.1 | 4 | CVE-2026-32254, GHSA-v5mh-h5hx-7v92, GO-2026-5354, GO-2026-5653 |
| v2.29.1 | 2.1.1 | 4 | CVE-2026-32254, GHSA-v5mh-h5hx-7v92, GO-2026-5354, GO-2026-5653 |
| v2.30.0 | 2.1.1 | 4 | CVE-2026-32254, GHSA-v5mh-h5hx-7v92, GO-2026-5354, GO-2026-5653 |
| v2.31.0 | 2.1.1 | 4 | CVE-2026-32254, GHSA-v5mh-h5hx-7v92, GO-2026-5354, GO-2026-5653 |

## Diagnostics

```bash
kubectl get pods -A -o jsonpath='{range .items[*]}{range .spec.containers[*]}{.image}{"\n"}{end}{end}' \
  | grep -i kube-router | sort -u
```

## Known Issues


CVEs (id — summary — fixed in):

- **CVE-2026-32254** — Kube-router Proxy Module Blindly Trusts ExternalIPs/LoadBalancer IPs Enabling Cluster-Wide Traffic Hijacking and DNS DoS in github.com/cloudnativelabs/kube-router — fixed in: `2.8.0`
- **GHSA-v5mh-h5hx-7v92** — kube-router: GoBGP gRPC Admin Port Exposed on Node Primary IP Without Authentication, Allowing Cluster-Wide BGP Route Injection — fixed in: `2.9.0`
- **GO-2026-5354** — kube-router: BGP Peer Passwords Exposed in Logs at Verbose Logging Level in github.com/cloudnativelabs/kube-router — fixed in: `no fix released`
- **GO-2026-5653** — kube-router: GoBGP gRPC Admin Port Exposed on Node Primary IP Without Authentication, Allowing Cluster-Wide BGP Route Injection in github.com/cloudnativelabs/kube-router — fixed in: `2.9.0`

**Recommendation:** compare the version in use against the "fixed in" column. When Kubespray pins a
version below the fix, the remedy is an explicit pin in inventory plus the matching checksum — the
same pattern as for the container runtime; see [[CONCEPT-SECURITY_INDEX]].

## References

- osv.dev queried per shipped version for `github.com/cloudnativelabs/kube-router` — verified 2026-07-31.
- Component: [[COMPONENT-KUBE_ROUTER]]; tracking: [[CONCEPT-SECURITY_ADVISORIES]].
