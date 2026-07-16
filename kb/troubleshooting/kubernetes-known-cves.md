---
id: TROUBLE-KUBERNETES_KNOWN_CVES
type: troubleshooting
title: "kubernetes: known CVEs by shipped version (osv.dev)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.33 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - kubernetes cve
tags:
  - security
  - cve
  - k8s
sources:
  - type: docs
    path: osv.dev API (k8s.io/kubernetes)
    url: https://osv.dev/list?q=k8s.io/kubernetes
    note: "authoritative version-filtered vulnerability data"
relations:
  - type: see_also
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
---

# kubernetes: known CVEs by shipped version (osv.dev)

## Summary

osv.dev reports **3 unique CVEs** affecting the kubernetes versions Kubespray ships; the newest (1.35.4, v2.31.0) is still affected by **2** — no fully-patched Kubespray release yet.

## Problem

Each shipped kubernetes version carries the CVEs below (osv.dev returns only vulns affecting the queried version — authoritative affectedness).

## Context

| Version | Kubespray | # | CVEs |
|---|---|---|---|
| 1.33.5 | v2.29.0 | 3 | CVE-2024-7598, CVE-2025-13281, CVE-2025-1767 |
| 1.33.7 | v2.29.1 | 2 | CVE-2024-7598, CVE-2025-1767 |
| 1.34.3 | v2.30.0 | 2 | CVE-2024-7598, CVE-2025-1767 |
| 1.35.4 | v2.31.0 | 2 | CVE-2024-7598, CVE-2025-1767 |

## Diagnostics

```bash
kubectl version
```

## Known Issues

CVEs (id — summary — fixed in):

- **CVE-2024-7598** — Kubernetes kube-apiserver Vulnerable to Race Condition in k8s.io/kubernetes — fixed in: `—`
- **CVE-2025-13281** [CVSS:3.1/AV:N/AC:H/PR:H/UI:N/S:C/C:H/I:N/A:N] — kube-controller-manager is vulnerable to half-blind Server Side Request Forgery through in-tree Portworx StorageClass — fixed in: `1.32.10, 1.33.6, 1.34.2`
- **CVE-2025-1767** — Kubernetes GitRepo Volume Inadvertent Local Repository Access in k8s.io/kubernetes — fixed in: `—`

**Recommendation:** upgrade to the newest Kubespray release (v2.31.0). For CVEs still open at 1.35.4, pin/patch kubernetes to a fixed upstream release or apply mitigation; reduce blast radius with PRACTICE-HARDENING.

## References

- osv.dev (queried per version) for `k8s.io/kubernetes` — verified 2026-07-16.
- Tracking: [[CONCEPT-SECURITY_ADVISORIES]].