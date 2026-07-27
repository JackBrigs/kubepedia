---
id: TROUBLE-KUBERNETES_KNOWN_CVES
type: troubleshooting
title: "kubernetes: known CVEs by shipped version (osv.dev)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-27"
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

osv.dev reports **7 distinct advisories** across the Kubernetes versions Kubespray ships as the
**default** for each tag. Exposure falls steadily along the envelope — 1.31.4 (v2.27.0) carries
**6**, 1.35.4 (v2.31.0) carries **2** — and the two that remain have no upstream fix at all, so no
Kubespray release clears them.

Counts are **distinct advisories** (osv.dev returns one record per database for the same CVE), and
each row is the tag's **default** `kube_version`. A cluster pinned to a different patch inside the
supported window has a different row — re-query that exact version rather than reading the nearest
line.

## Problem

Each shipped kubernetes version carries the CVEs below (osv.dev returns only vulns affecting the queried version — authoritative affectedness).

## Context

| Version | Kubespray | # | CVEs |
|---|---|---|---|
| 1.31.4 | v2.27.0 | 6 | CVE-2024-7598, CVE-2024-9042, CVE-2025-0426, CVE-2025-13281, CVE-2025-1767, CVE-2025-5187 |
| 1.31.9 | v2.27.1 | 4 | CVE-2024-7598, CVE-2025-13281, CVE-2025-1767, CVE-2025-5187 |
| 1.32.5 | v2.28.0 | 5 | CVE-2024-7598, CVE-2025-13281, CVE-2025-1767, CVE-2025-4563, CVE-2025-5187 |
| 1.32.8 | v2.28.1 | 3 | CVE-2024-7598, CVE-2025-13281, CVE-2025-1767 |
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

- **CVE-2024-7598** — kube-apiserver race condition — fixed in: `—`
- **CVE-2024-9042** [CVSS:3.1/AV:N/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:N] — command injection affecting **Windows nodes** via the `nodes/*/logs/query` API — fixed in: `1.29.13, 1.30.9, 1.31.5, 1.32.1`
- **CVE-2025-0426** [CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H] — node denial of service via the kubelet Checkpoint API — fixed in: `1.29.14, 1.30.10, 1.31.6, 1.32.2`
- **CVE-2025-13281** [CVSS:3.1/AV:N/AC:H/PR:H/UI:N/S:C/C:H/I:N/A:N] — kube-controller-manager half-blind SSRF through the in-tree Portworx StorageClass — fixed in: `1.32.10, 1.33.6, 1.34.2`
- **CVE-2025-1767** [CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:N] — GitRepo volume inadvertent local repository access — fixed in: `—`
- **CVE-2025-4563** [CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:N/I:N/A:L] — nodes can bypass dynamic resource allocation authorization checks — fixed in: `1.32.6, 1.33.2`
- **CVE-2025-5187** [CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:L] — nodes can delete themselves by adding an OwnerReference — fixed in: `1.31.12, 1.32.8, 1.33.4`

**Recommendation:** the tags below v2.28.1 are the ones worth moving off — 1.31.4 and 1.32.5 carry
node-level issues (`CVE-2025-5187`, `CVE-2025-4563`, `CVE-2025-0426`) that a supported patch already
fixes, and Kubespray's own default for a newer tag picks them up. From v2.28.1 onward only two
remain, and **both are unfixed upstream**: the GitRepo volume issue is mitigated by not using
`gitRepo` volumes at all (deprecated since 1.11), and the apiserver race has no published fix —
neither is addressable by choosing a different Kubespray tag. Reduce blast radius with
[[PRACTICE-HARDENING]] and the audit checklist in [[CONCEPT-INSECURE_DEFAULTS]].

## References

- osv.dev (queried per version) for `k8s.io/kubernetes` — verified 2026-07-27.
- Tracking: [[CONCEPT-SECURITY_ADVISORIES]].