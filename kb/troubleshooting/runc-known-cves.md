---
id: TROUBLE-RUNC_KNOWN_CVES
type: troubleshooting
title: "runc: known CVEs by shipped version (osv.dev)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: ">=1.3.2 <=1.4.2"
verified_at: "2026-07-16"
confidence: verified
aliases:
  - runc cve
  - runc security
tags:
  - security
  - cve
  - runc
sources:
  - type: docs
    path: osv.dev API (github.com/opencontainers/runc)
    url: https://osv.dev/list?q=github.com/opencontainers/runc
    note: "authoritative, version-filtered vulnerability data (queried per shipped version)"
relations:
  - type: see_also
    target: COMPONENT-RUNC
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
---

# runc: known CVEs by shipped version (osv.dev)

## Summary

osv.dev reports **4 unique CVEs** affecting the runc versions Kubespray ships (see [COMPONENT-RUNC]). The count drops with newer versions; the newest indexed version **1.4.2** (Kubespray v2.31.0) is still affected by **1** of them — no fully-patched Kubespray release exists yet for those.

## Problem

Each shipped runc version carries the CVEs listed below (osv.dev returns only vulnerabilities that affect the queried version, so this is authoritative affectedness).

## Context

| Component version | Kubespray | # CVEs | CVEs |
|---|---|---|---|
| 1.3.2 | v2.29.0 | 4 | CVE-2025-31133, CVE-2025-52565, CVE-2025-52881, CVE-2026-41579 |
| 1.3.4 | v2.29.1 / v2.30.0 | 1 | CVE-2026-41579 |
| 1.4.2 | v2.31.0 | 1 | CVE-2026-41579 |

## Diagnostics

```bash
runc --version
```

## Known Issues

CVEs (id — summary — fixed in):

- **CVE-2025-31133** [CVSS:4.0/AV:L/AC:L/AT:P/PR:L/UI:A/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H] — runc container escape via "masked path" abuse due to mount race conditions — fixed in: `1.2.8, 1.3.3, 1.4.0-rc.3`
- **CVE-2025-52565** [CVSS:4.0/AV:L/AC:L/AT:P/PR:L/UI:A/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H] — runc container escape with malicious config due to /dev/console mount and related races — fixed in: `1.2.8, 1.3.3, 1.4.0-rc.3`
- **CVE-2025-52881** [CVSS:4.0/AV:L/AC:L/AT:P/PR:L/UI:A/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H] — runc container escape and denial of service due to arbitrary write gadgets and procfs write redirects — fixed in: `1.2.8, 1.3.3, 1.4.0-rc.3`
- **CVE-2026-41579** [CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:L/A:N] — runc: Malicious image with /dev symlink can trigger limited host filesystem integrity violations — fixed in: `1.3.6, 1.4.3, 1.5.0-rc.3`

**Recommendation:** move to the newest Kubespray release to minimize exposure (v2.31.0, runc 1.4.2). For CVEs still open at 1.4.2, pin `runc` to a fixed upstream release via the version variable and re-deploy, or apply the upstream mitigation. Reduce blast radius with PRACTICE-HARDENING.

## References

- osv.dev (queried per version) for `github.com/opencontainers/runc` — verified 2026-07-16.
- Component: [[COMPONENT-RUNC]]; tracking: [[CONCEPT-SECURITY_ADVISORIES]].