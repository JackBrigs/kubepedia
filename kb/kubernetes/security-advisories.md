---
id: CONCEPT-SECURITY_ADVISORIES
type: concept
title: Security advisories and CVE tracking for shipped components
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - security advisories
  - cve tracking
  - vulnerability
tags:
  - security
  - cve
  - operations
sources:
  - type: docs
    path: NVD / GitHub Security Advisories
    url: https://github.com/advisories
    note: "authoritative advisory databases"
relations:
  - type: see_also
    target: TROUBLE-RUNC_CONTAINER_ESCAPE_NOV2025
  - type: see_also
    target: PRACTICE-HARDENING
---

# Security advisories and CVE tracking for shipped components

## Summary

Kubespray pins specific versions of Kubernetes and each managed component (see the
`COMPONENT-*` and `RELEASE-*` docs). Those versions determine which published CVEs
apply. This document is the entry point for CVE tracking: where to check, and how
to map an advisory's affected range onto the version a given Kubespray release
ships.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0` and the versions they install.
- **Never treat a CVE claim as fact without the exact affected/fixed version
  range** from an authoritative source; then compare it to the shipped version.

## Implementation

Authoritative advisory sources per component:

| Component | Where to check |
|-----------|----------------|
| Kubernetes | Kubernetes Security Advisories / `kubernetes/kubernetes` security tab, NVD |
| runc | `opencontainers/runc` GitHub Security Advisories, NVD |
| containerd | `containerd/containerd` GitHub Security Advisories, NVD |
| etcd | `etcd-io/etcd` security releases, NVD |
| Cilium | `cilium/cilium` security advisories |
| CoreDNS | `coredns/coredns` releases, NVD |
| cross-ecosystem | GitHub Advisory DB (github.com/advisories), osv.dev |

Method: take the shipped version from the component doc → look up advisories for
that component → check whether the version is inside an *affected* range and
outside the *fixed* range. Record confirmed hits as `troubleshooting` docs tagged
`security`/`cve` (see the runc example: [[TROUBLE-RUNC_CONTAINER_ESCAPE_NOV2025]]).

Reduce blast radius regardless of specific CVEs via [[PRACTICE-HARDENING]]
(PodSecurity, drop capabilities, no privileged pods, secrets encryption).

## Compatibility

- Shipped versions per release: see [[RELEASE-V2_29_0]], [[RELEASE-V2_29_1]],
  [[RELEASE-V2_30_0]], [[RELEASE-V2_31_0]] and the `COMPONENT-*` docs.

## References

- GitHub Advisory Database, NVD, osv.dev, and each component's security channel.
- Deeper per-component CVE coverage is tracked in `BACKLOG.md` (Security).
