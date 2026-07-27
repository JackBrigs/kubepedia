---
id: TROUBLE-ETCD_KNOWN_CVES
type: troubleshooting
title: "etcd: known CVEs by shipped version (osv.dev)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: ">=3.5.16 <=3.6.10"
verified_at: "2026-07-27"
confidence: verified
aliases:
  - etcd cve
  - etcd security
tags:
  - security
  - cve
  - etcd
sources:
  - type: docs
    path: osv.dev API (go.etcd.io/etcd/v3)
    url: https://osv.dev/list?q=go.etcd.io/etcd
    note: "the module carrying most etcd server advisories; queried per shipped version"
  - type: docs
    path: osv.dev API (go.etcd.io/etcd/server/v3)
    url: https://osv.dev/list?q=go.etcd.io/etcd/server
    note: "the server module — some advisories are filed only here; both paths are unioned"
relations:
  - type: see_also
    target: COMPONENT-ETCD
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
---

# etcd: known CVEs by shipped version (osv.dev)

## Summary

osv.dev reports **8 distinct advisories** affecting the etcd versions Kubespray ships (see
[COMPONENT-ETCD]). Exposure barely moves across the whole envelope: **every** shipped version
carries at least **6**, and the newest — 3.5.29 / 3.6.10 at Kubespray v2.31.0 — still carries 6,
because the fixes land in 3.5.28+ / 3.6.9+ (two of them only in 3.5.33 / 3.6.14) while Kubespray
tracks the version Kubernetes pins.

Counts are **distinct advisories**. etcd is a multi-module repo: advisories are filed against
`go.etcd.io/etcd/v3` and `go.etcd.io/etcd/server/v3`, and neither path alone is complete — at 3.5.16
the first returns 8 and the second 1. Both are queried and unioned.

## Problem

Each shipped etcd version carries the advisories listed below. etcd is the cluster's source of
truth, so an authorization bypass here is a full data-plane read, not a scoped one.

## Context

| Component version | Kubespray | # CVEs | CVEs |
|---|---|---|---|
| 3.5.16 | v2.27.0 / v2.28.0 | 8 | CVE-2026-33343, CVE-2026-33413, CVE-2026-44283, GHSA-6vch-q96h-7gc3, GHSA-xg4h-6gfc-h4m8, GO-2024-2528, GO-2024-2529, GO-2024-2530 |
| 3.5.21 | v2.27.1 | 8 | CVE-2026-33343, CVE-2026-33413, CVE-2026-44283, GHSA-6vch-q96h-7gc3, GHSA-xg4h-6gfc-h4m8, GO-2024-2528, GO-2024-2529, GO-2024-2530 |
| 3.5.22 | v2.28.1 | 8 | CVE-2026-33343, CVE-2026-33413, CVE-2026-44283, GHSA-6vch-q96h-7gc3, GHSA-xg4h-6gfc-h4m8, GO-2024-2528, GO-2024-2529, GO-2024-2530 |
| 3.5.23 | v2.29.0 | 8 | CVE-2026-33343, CVE-2026-33413, CVE-2026-44283, GHSA-6vch-q96h-7gc3, GHSA-xg4h-6gfc-h4m8, GO-2024-2528, GO-2024-2529, GO-2024-2530 |
| 3.5.25 | v2.29.1 | 8 | CVE-2026-33343, CVE-2026-33413, CVE-2026-44283, GHSA-6vch-q96h-7gc3, GHSA-xg4h-6gfc-h4m8, GO-2024-2528, GO-2024-2529, GO-2024-2530 |
| 3.5.26 | v2.30.0 | 8 | CVE-2026-33343, CVE-2026-33413, CVE-2026-44283, GHSA-6vch-q96h-7gc3, GHSA-xg4h-6gfc-h4m8, GO-2024-2528, GO-2024-2529, GO-2024-2530 |
| 3.5.29 | v2.31.0 (K8s 1.33 / 1.34) | 6 | CVE-2026-44283, GHSA-6vch-q96h-7gc3, GHSA-xg4h-6gfc-h4m8, GO-2024-2528, GO-2024-2529, GO-2024-2530 |
| 3.6.10 | v2.31.0 (K8s 1.35) | 6 | CVE-2026-44283, GHSA-6vch-q96h-7gc3, GHSA-xg4h-6gfc-h4m8, GO-2024-2528, GO-2024-2529, GO-2024-2530 |

At v2.31.0 the etcd version depends on the Kubernetes minor: 3.5.29 for 1.33/1.34, 3.6.10 for 1.35
([[RELEASE-V2_31_0]]). Both rows are identical in exposure.

## Diagnostics

```bash
etcdctl version                                     # client + server
kubectl -n kube-system get pod -l component=etcd -o jsonpath='{.items[*].spec.containers[*].image}'
```

## Known Issues

CVEs (id — summary — fixed in):

- **CVE-2026-33343** [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:N] — nested etcd transactions bypass RBAC authorization checks — fixed in: `3.4.42, 3.5.28, 3.6.9`
- **CVE-2026-33413** [CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:L/VI:L/VA:H/SC:N/SI:N/SA:N] — authorization bypasses in multiple APIs — fixed in: `3.4.42, 3.5.28, 3.6.9`
- **CVE-2026-44283** [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:N] — RBAC bypass allows unauthorized data access via `PrevKv`/lease attachment in nested-transaction Put requests — fixed in: `3.4.44, 3.5.30, 3.6.11`
- **GHSA-6vch-q96h-7gc3** [CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:N/VA:H/SC:N/SI:N/SA:N] — `tlsListener.acceptLoop` spawns unbounded handshake goroutines with no deadline (unauthenticated DoS) — fixed in: `3.5.33, 3.6.14, 3.7.1`
- **GHSA-xg4h-6gfc-h4m8** [CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:H/VI:N/VA:N/SC:N/SI:N/SA:N] — Watch API authorization bypass via open-ended range requests — fixed in: `3.5.33, 3.6.14, 3.7.1`
- **GO-2024-2528** — Gateway TLS endpoint validation only confirms TCP reachability — fixed in: `—`
- **GO-2024-2529** — `embed` auto-compaction retention accepts a negative value, causing a compaction loop or crash — fixed in: `—`
- **GO-2024-2530** — inaccurate logging of authentication attempts for CN-only auth users — fixed in: `—`

**Recommendation:** etcd is **not** an independently pinnable component in the way containerd or
Cilium are — Kubespray selects it per Kubernetes minor
([[CONCEPT-COMPONENT_VERSION_SELECTION]]), so a version bump is an upgrade decision, not a variable
change. Practical mitigations, in order: keep the client/peer certificates enforced and the etcd
ports off any shared network (all five open advisories need reachability plus, at most, low
privileges); do not expose the etcd gateway; and treat the RBAC-bypass class as a reason to keep
etcd credentials scoped to the control plane rather than shared with add-ons
([[PRACTICE-HARDENING]], [[CONCEPT-KUBESPRAY_ETCD_OWNERSHIP]]).

## References

- osv.dev (queried per version) for `go.etcd.io/etcd/v3` and `go.etcd.io/etcd/server/v3` — verified 2026-07-27.
- Component: [[COMPONENT-ETCD]]; per-tag versions: [[RELEASE-V2_31_0]]; tracking: [[CONCEPT-SECURITY_ADVISORIES]].
