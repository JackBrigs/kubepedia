---
id: TROUBLE-FLANNEL_KNOWN_CVES
type: troubleshooting
title: "flannel: known CVEs by shipped version (osv.dev)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: ">=0.22.0 <=0.28.4"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - flannel cve
  - flannel security
  - is flannel vulnerable
tags:
  - security
  - cve
  - flannel
sources:
  - type: docs
    path: osv.dev API (github.com/flannel-io/flannel)
    url: https://osv.dev/list?q=github.com/flannel-io/flannel
    note: "version-filtered vulnerability data, queried per shipped version"
relations:
  - type: see_also
    target: COMPONENT-FLANNEL
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
---

# flannel: known CVEs by shipped version (osv.dev)

## Summary

osv.dev reports **1 distinct CVEs** affecting the flannel versions Kubespray ships across
v2.27.0–v2.31.0. The newest shipped version (0.28.4, v2.31.0) is affected by **0**;
the worst tag is v2.27.0 with 1.

Counts are distinct advisories. osv.dev returns one record per database (GHSA *and* GO) for the same
CVE, so a raw record count roughly doubles it.

## Problem

Each shipped version carries the CVEs below. osv.dev returns only vulnerabilities that affect the
queried version, so this is authoritative affectedness rather than a guess from release notes.

## Context

| Component version | Kubespray | # CVEs | CVEs |
|---|---|---|---|
| 0.22.0 | v2.27.0 | 1 | CVE-2026-32241 |
| 0.22.0 | v2.27.1 | 1 | CVE-2026-32241 |
| 0.22.0 | v2.28.0 | 1 | CVE-2026-32241 |
| 0.22.0 | v2.28.1 | 1 | CVE-2026-32241 |
| 0.27.3 | v2.29.0 | 1 | CVE-2026-32241 |
| 0.27.3 | v2.29.1 | 1 | CVE-2026-32241 |
| 0.27.3 | v2.30.0 | 1 | CVE-2026-32241 |
| 0.28.4 | v2.31.0 | 0 | — |

## Diagnostics

```bash
kubectl get pods -A -o jsonpath='{range .items[*]}{range .spec.containers[*]}{.image}{"\n"}{end}{end}' \
  | grep -i flannel | sort -u
```

## Known Issues


CVEs (id — summary — fixed in):

- **CVE-2026-32241** — Flannel has cross-node remote code execution via extension backend BackendData injection — fixed in: `0.28.2`

**Recommendation:** compare the version in use against the "fixed in" column. When Kubespray pins a
version below the fix, the remedy is an explicit pin in inventory plus the matching checksum — the
same pattern as for the container runtime; see [[CONCEPT-SECURITY_INDEX]].

## References

- osv.dev queried per shipped version for `github.com/flannel-io/flannel` — verified 2026-07-31.
- Component: [[COMPONENT-FLANNEL]]; tracking: [[CONCEPT-SECURITY_ADVISORIES]].
