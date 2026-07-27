---
id: TROUBLE-CILIUM_KNOWN_CVES
type: troubleshooting
title: "cilium: known CVEs by shipped version (osv.dev)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: ">=1.15.9 <=1.19.3"
verified_at: "2026-07-27"
confidence: verified
aliases:
  - cilium cve
  - cilium security
tags:
  - security
  - cve
  - cilium
sources:
  - type: docs
    path: osv.dev API (github.com/cilium/cilium)
    url: https://osv.dev/list?q=github.com/cilium/cilium
    note: "authoritative, version-filtered vulnerability data (queried per shipped version)"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
---

# cilium: known CVEs by shipped version (osv.dev)

## Summary

osv.dev reports **11 unique CVEs** affecting the cilium versions Kubespray ships (see [COMPONENT-CILIUM]). The count drops sharply with newer versions — the oldest shipped 1.15.9 (Kubespray v2.27.0/v2.27.1) carries all but one, while the newest indexed **1.19.3** (Kubespray v2.31.0) is affected by **1**, for which no fully-patched Kubespray release exists yet.

Counts here are **distinct advisories**. osv.dev returns one record per database (GHSA *and* GO) for the same CVE, so a raw record count is roughly double; do not read it as the number of vulnerabilities.

## Problem

Each shipped cilium version carries the CVEs listed below (osv.dev returns only vulnerabilities that affect the queried version, so this is authoritative affectedness).

## Context

| Component version | Kubespray | # CVEs | CVEs |
|---|---|---|---|
| 1.15.9 | v2.27.0 / v2.27.1 | 10 | CVE-2024-47825, CVE-2025-23028, CVE-2025-23047, CVE-2025-30162, CVE-2025-32793, CVE-2025-64715, CVE-2026-33726, CVE-2026-41520, CVE-2026-49445, CVE-2026-53935 |
| 1.17.3 | v2.28.0 | 5 | CVE-2025-64715, CVE-2026-33726, CVE-2026-41520, CVE-2026-49445, CVE-2026-53935 |
| 1.17.7 | v2.28.1 | 5 | CVE-2025-64715, CVE-2026-33726, CVE-2026-41520, CVE-2026-49445, CVE-2026-53935 |
| 1.18.2 | v2.29.0 | 6 | CVE-2025-64715, CVE-2026-26963, CVE-2026-33726, CVE-2026-41520, CVE-2026-49445, CVE-2026-53935 |
| 1.18.4 | v2.29.1 | 5 | CVE-2026-26963, CVE-2026-33726, CVE-2026-41520, CVE-2026-49445, CVE-2026-53935 |
| 1.18.6 | v2.30.0 | 4 | CVE-2026-33726, CVE-2026-41520, CVE-2026-49445, CVE-2026-53935 |
| 1.19.3 | v2.31.0 | 1 | CVE-2026-53935 |

## Diagnostics

```bash
kubectl -n kube-system exec ds/cilium -- cilium version
```

## Known Issues

CVEs (id — summary — fixed in):

- **CVE-2024-47825** [CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:L/I:N/A:N] — CIDR deny policies may not take effect when a more narrow CIDR allow is present — fixed in: `1.14.16, 1.15.10`
- **CVE-2025-23028** [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L] — DoS in the Cilium agent DNS proxy from crafted DNS responses — fixed in: `1.14.18, 1.15.12, 1.16.5`
- **CVE-2025-23047** [CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N] — information leakage via an insecure default Hubble UI CORS header — fixed in: `1.14.19, 1.15.13, 1.16.6`
- **CVE-2025-30162** [CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:C/C:L/I:N/A:N] — east-west traffic not subject to egress policy enforcement for requests via Gateway API load balancers — fixed in: `1.15.15, 1.16.8, 1.17.2`
- **CVE-2025-32793** [CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:L/I:N/A:N] — packets from terminating endpoints may not be encrypted in WireGuard-enabled clusters — fixed in: `1.15.16, 1.16.9, 1.17.3`
- **CVE-2025-64715** [CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N] — Cilium with misconfigured toGroups in policies can lead to unrestricted egress traffic — fixed in: `1.16.17, 1.17.10, 1.18.4`
- **CVE-2026-26963** [CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:C/C:L/I:L/A:N] — Cilium may not enforce host firewall policies when Native Routing, WireGuard and Node Encryption are enabled — fixed in: `1.18.6`
- **CVE-2026-33726** [CVSS:3.1/AV:A/AC:L/PR:L/UI:N/S:C/C:L/I:L/A:N] — Cilium L7 proxy may bypass Kubernetes NetworkPolicy for same-node traffic — fixed in: `1.17.14, 1.18.8, 1.19.2`
- **CVE-2026-41520** [CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:N] — Cillium exposes sensitive information included in the cilium-bugtool debug archive — fixed in: `1.17.15, 1.18.9, 1.19.3`
- **CVE-2026-49445** [CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:L/A:H] — Cilium vulnerable to sensitive information disclosure and cluster disruption via local Envoy admin socket access — fixed in: `1.17.14, 1.18.8, 1.19.2`
- **CVE-2026-53935** [CVSS:3.1/AV:A/AC:L/PR:H/UI:N/S:C/C:L/I:N/A:H] — CiliumLocalRedirectPolicy addressMatcher allows cross-namespace service traffic hijacking and can break service translation — fixed in: `1.17.16, 1.18.10, 1.19.4`

**Recommendation:** move to the newest Kubespray release to minimize exposure (v2.31.0, cilium 1.19.3). For CVEs still open at 1.19.3, pin `cilium` to a fixed upstream release via the version variable and re-deploy, or apply the upstream mitigation. Reduce blast radius with PRACTICE-HARDENING.

## References

- osv.dev (queried per version) for `github.com/cilium/cilium` — verified 2026-07-27.
- Component: [[COMPONENT-CILIUM]]; tracking: [[CONCEPT-SECURITY_ADVISORIES]].