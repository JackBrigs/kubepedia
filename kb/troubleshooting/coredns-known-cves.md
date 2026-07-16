---
id: TROUBLE-COREDNS_KNOWN_CVES
type: troubleshooting
title: "coredns: known CVEs by shipped version (osv.dev)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: ">=1.11.3 <=1.12.4"
verified_at: "2026-07-16"
confidence: verified
aliases:
  - coredns cve
  - coredns security
tags:
  - security
  - cve
  - coredns
sources:
  - type: docs
    path: osv.dev API (github.com/coredns/coredns)
    url: https://osv.dev/list?q=github.com/coredns/coredns
    note: "authoritative, version-filtered vulnerability data (queried per shipped version)"
relations:
  - type: see_also
    target: COMPONENT-COREDNS
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
---

# coredns: known CVEs by shipped version (osv.dev)

## Summary

osv.dev reports **10 unique CVEs** affecting the coredns versions Kubespray ships (see [COMPONENT-COREDNS]). The count drops with newer versions; the newest indexed version **1.12.4** (Kubespray v2.31.0) is still affected by **8** of them — no fully-patched Kubespray release exists yet for those.

## Problem

Each shipped coredns version carries the CVEs listed below (osv.dev returns only vulnerabilities that affect the queried version, so this is authoritative affectedness).

## Context

| Component version | Kubespray | # CVEs | CVEs |
|---|---|---|---|
| 1.11.3 | v2.29.x (k8s 1.31/1.32) | 10 | CVE-2025-47950, CVE-2025-58063, CVE-2025-68151, CVE-2026-26017, CVE-2026-26018, CVE-2026-32934, CVE-2026-32936, CVE-2026-33190, CVE-2026-33489, CVE-2026-35579 |
| 1.12.0 | v2.29.x (k8s 1.33) | 10 | CVE-2025-47950, CVE-2025-58063, CVE-2025-68151, CVE-2026-26017, CVE-2026-26018, CVE-2026-32934, CVE-2026-32936, CVE-2026-33190, CVE-2026-33489, CVE-2026-35579 |
| 1.12.1 | v2.30.0 | 10 | CVE-2025-47950, CVE-2025-58063, CVE-2025-68151, CVE-2026-26017, CVE-2026-26018, CVE-2026-32934, CVE-2026-32936, CVE-2026-33190, CVE-2026-33489, CVE-2026-35579 |
| 1.12.4 | v2.31.0 | 8 | CVE-2025-68151, CVE-2026-26017, CVE-2026-26018, CVE-2026-32934, CVE-2026-32936, CVE-2026-33190, CVE-2026-33489, CVE-2026-35579 |

## Diagnostics

```bash
kubectl -n kube-system get deploy coredns -o jsonpath='{.spec.template.spec.containers[0].image}'
```

## Known Issues

CVEs (id — summary — fixed in):

- **CVE-2025-47950** [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H] — CoreDNS Vulnerable to DoQ Memory Exhaustion via Stream Amplification — fixed in: `1.12.2`
- **CVE-2025-58063** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H] — CoreDNS: DNS Cache Pinning via etcd Lease ID Confusion — fixed in: `1.12.4`
- **CVE-2025-68151** [CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:N/VA:H/SC:N/SI:N/SA:N/E:U] — CoreDNS gRPC/HTTPS/HTTP3 servers lack resource limits, enabling DoS via unbounded connections and oversized messages — fixed in: `1.14.0`
- **CVE-2026-26017** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N] — CoreDNS ACL Bypass — fixed in: `1.14.2`
- **CVE-2026-26018** [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H] — CoreDNS Loop Detection Denial of Service Vulnerability — fixed in: `1.14.2`
- **CVE-2026-32934** [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H] — CoreDNS' DoQ worker pool does not bound stream backlog — fixed in: `1.14.3`
- **CVE-2026-32936** [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H] — CoreDNS DoH GET oversized dns= query parameter causes pre-validation CPU and memory amplification — fixed in: `1.14.3`
- **CVE-2026-33190** [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N] — CoreDNS has TSIG authentication bypass on DoT, DoH, DoH3, DoQ, and gRPC — fixed in: `1.14.3`
- **CVE-2026-33489** [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N] — CoreDNS' transfer stanza selection uses lexicographic compare (subzone ACL bypass) — fixed in: `1.14.3`
- **CVE-2026-35579** [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N] — CoreDNS has TSIG authentication bypass on gRPC and QUIC transports — fixed in: `1.14.3`

**Recommendation:** move to the newest Kubespray release to minimize exposure (v2.31.0, coredns 1.12.4). For CVEs still open at 1.12.4, pin `coredns` to a fixed upstream release via the version variable and re-deploy, or apply the upstream mitigation. Reduce blast radius with PRACTICE-HARDENING.

## References

- osv.dev (queried per version) for `github.com/coredns/coredns` — verified 2026-07-16.
- Component: [[COMPONENT-COREDNS]]; tracking: [[CONCEPT-SECURITY_ADVISORIES]].