---
id: TROUBLE-CNI_PLUGINS_KNOWN_CVES
type: troubleshooting
title: "cni-plugins: known CVEs by shipped version (osv.dev)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: ">=1.8.0 <=1.9.1"
verified_at: "2026-07-16"
confidence: verified
aliases:
  - cni-plugins cve
tags:
  - security
  - cve
  - cni
sources:
  - type: docs
    path: osv.dev API (github.com/containernetworking/plugins)
    url: https://osv.dev/list?q=github.com/containernetworking/plugins
    note: "authoritative version-filtered vulnerability data"
relations:
  - type: see_also
    target: COMPONENT-CNI_PLUGINS
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
---

# cni-plugins: known CVEs by shipped version (osv.dev)

## Summary

osv.dev reports **1 unique CVEs** affecting the cni-plugins versions Kubespray ships; the newest (1.9.1, v2.31.0) is still affected by **0**.

## Problem

Each shipped cni-plugins version carries the CVEs below (osv.dev returns only vulns affecting the queried version — authoritative affectedness).

## Context

| Version | Kubespray | # | CVEs |
|---|---|---|---|
| 1.8.0 | v2.29.0-v2.30.0 | 1 | CVE-2025-67499 |
| 1.9.1 | v2.31.0 | 0 | — |

## Diagnostics

```bash
ls /opt/cni/bin ; cat /opt/cni/bin/../version 2>/dev/null
```

## Known Issues

CVEs (id — summary — fixed in):

- **CVE-2025-67499** [CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:H] — CNA Plugins Portmap nftables backend can intercept non-local traffic — fixed in: `1.9.0`

**Recommendation:** upgrade to the newest Kubespray release (v2.31.0). For CVEs still open at 1.9.1, pin/patch cni-plugins to a fixed upstream release or apply mitigation; reduce blast radius with PRACTICE-HARDENING.

## References

- osv.dev (queried per version) for `github.com/containernetworking/plugins` — verified 2026-07-16.
- Tracking: [[CONCEPT-SECURITY_ADVISORIES]].