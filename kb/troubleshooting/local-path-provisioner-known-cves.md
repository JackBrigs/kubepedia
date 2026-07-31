---
id: TROUBLE-LOCAL_PATH_PROVISIONER_KNOWN_CVES
type: troubleshooting
title: "local-path-provisioner: known CVEs by shipped version (osv.dev)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: ">=0.0.24 <=0.0.32"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - local-path-provisioner cve
  - local-path-provisioner security
  - is local-path-provisioner vulnerable
tags:
  - security
  - cve
  - local-path-provisioner
sources:
  - type: docs
    path: osv.dev API (github.com/rancher/local-path-provisioner)
    url: https://osv.dev/list?q=github.com/rancher/local-path-provisioner
    note: "version-filtered vulnerability data, queried per shipped version"
relations:
  - type: see_also
    target: COMPONENT-LOCAL_PATH_PROVISIONER
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
---

# local-path-provisioner: known CVEs by shipped version (osv.dev)

## Summary

osv.dev reports **2 distinct CVEs** affecting the local-path-provisioner versions Kubespray ships across
v2.27.0–v2.31.0. The newest shipped version (0.0.32, v2.31.0) is affected by **2**;
the worst tag is v2.27.0 with 2.

Counts are distinct advisories. osv.dev returns one record per database (GHSA *and* GO) for the same
CVE, so a raw record count roughly doubles it.

## Problem

Each shipped version carries the CVEs below. osv.dev returns only vulnerabilities that affect the
queried version, so this is authoritative affectedness rather than a guess from release notes.

## Context

| Kubespray | Component version | # CVEs | CVEs |
|---|---|---:|---|
| v2.27.0 | 0.0.24 | 2 | CVE-2025-62878, CVE-2026-44543 |
| v2.27.1 | 0.0.24 | 2 | CVE-2025-62878, CVE-2026-44543 |
| v2.28.0 | 0.0.24 | 2 | CVE-2025-62878, CVE-2026-44543 |
| v2.28.1 | 0.0.24 | 2 | CVE-2025-62878, CVE-2026-44543 |
| v2.29.0 | 0.0.32 | 2 | CVE-2025-62878, CVE-2026-44543 |
| v2.29.1 | 0.0.32 | 2 | CVE-2025-62878, CVE-2026-44543 |
| v2.30.0 | 0.0.32 | 2 | CVE-2025-62878, CVE-2026-44543 |
| v2.31.0 | 0.0.32 | 2 | CVE-2025-62878, CVE-2026-44543 |

## Diagnostics

```bash
kubectl get pods -A -o jsonpath='{range .items[*]}{range .spec.containers[*]}{.image}{"\n"}{end}{end}' \
  | grep -i local-path-provisioner | sort -u
```

## Known Issues


CVEs (id — summary — fixed in):

- **CVE-2025-62878** — Local Path Provisioner vulnerable to Path Traversal via parameters.pathPattern — fixed in: `0.0.34`
- **CVE-2026-44543** — Local Path Provisioner Vulnerable to HelperPod Template Injection — fixed in: `0.0.36`

**Recommendation:** compare the version in use against the "fixed in" column. When Kubespray pins a
version below the fix, the remedy is an explicit pin in inventory plus the matching checksum — the
same pattern as for the container runtime; see [[CONCEPT-SECURITY_INDEX]].

## References

- osv.dev queried per shipped version for `github.com/rancher/local-path-provisioner` — verified 2026-07-31.
- Component: [[COMPONENT-LOCAL_PATH_PROVISIONER]]; tracking: [[CONCEPT-SECURITY_ADVISORIES]].
