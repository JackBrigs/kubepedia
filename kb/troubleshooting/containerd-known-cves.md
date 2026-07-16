---
id: TROUBLE-CONTAINERD_KNOWN_CVES
type: troubleshooting
title: "containerd: known CVEs by shipped version (osv.dev)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: ">=2.1.4 <=2.2.3"
verified_at: "2026-07-16"
confidence: verified
aliases:
  - containerd cve
  - containerd security
tags:
  - security
  - cve
  - containerd
sources:
  - type: docs
    path: osv.dev API (github.com/containerd/containerd)
    url: https://osv.dev/list?q=github.com/containerd/containerd
    note: "authoritative, version-filtered vulnerability data (queried per shipped version)"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
---

# containerd: known CVEs by shipped version (osv.dev)

## Summary

osv.dev reports **3 unique CVEs** affecting the containerd versions Kubespray ships (see [COMPONENT-CONTAINERD]). The count drops with newer versions; the newest indexed version **2.2.3** (Kubespray v2.31.0) is still affected by **3** of them — no fully-patched Kubespray release exists yet for those.

## Problem

Each shipped containerd version carries the CVEs listed below (osv.dev returns only vulnerabilities that affect the queried version, so this is authoritative affectedness).

## Context

| Component version | Kubespray | # CVEs | CVEs |
|---|---|---|---|
| 2.1.4 | v2.29.0 | 3 | CVE-2026-50195, CVE-2026-53489, CVE-2026-53492 |
| 2.1.5 | v2.29.1 | 3 | CVE-2026-50195, CVE-2026-53489, CVE-2026-53492 |
| 2.2.1 | v2.30.0 | 3 | CVE-2026-50195, CVE-2026-53489, CVE-2026-53492 |
| 2.2.3 | v2.31.0 | 3 | CVE-2026-50195, CVE-2026-53489, CVE-2026-53492 |

## Diagnostics

```bash
containerd --version ; crictl version
```

## Known Issues

CVEs (id — summary — fixed in):

- **CVE-2026-50195** — containerd: CRI checkpoint import allows local image tag poisoning in github.com/containerd/containerd — fixed in: `—`
- **CVE-2026-53489** — Arbitrary host CRI log file read via symlink following in CRI checkpoint restore in github.com/containerd/containerd — fixed in: `—`
- **CVE-2026-53492** — containerd CRI checkpoint restore CDI annotation smuggling in github.com/containerd/containerd — fixed in: `—`

**Recommendation:** move to the newest Kubespray release to minimize exposure (v2.31.0, containerd 2.2.3). For CVEs still open at 2.2.3, pin `containerd` to a fixed upstream release via the version variable and re-deploy, or apply the upstream mitigation. Reduce blast radius with PRACTICE-HARDENING.

## References

- osv.dev (queried per version) for `github.com/containerd/containerd` — verified 2026-07-16.
- Component: [[COMPONENT-CONTAINERD]]; tracking: [[CONCEPT-SECURITY_ADVISORIES]].