---
id: TROUBLE-CRI_O_KNOWN_CVES
type: troubleshooting
title: "CRI-O: known CVEs by shipped version (osv.dev)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: ">=1.33.5 <=1.35.0"
verified_at: "2026-07-27"
confidence: verified
aliases:
  - cri-o cve
  - crio security
tags:
  - security
  - cve
  - cri-o
  - runtime
sources:
  - type: docs
    path: osv.dev API (github.com/cri-o/cri-o)
    url: https://osv.dev/list?q=github.com/cri-o/cri-o
    note: "both advisories carry commit ranges with no released semver fix — affectedness is per-branch, not per-patch"
relations:
  - type: see_also
    target: COMPONENT-CRI_O
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
---

# CRI-O: known CVEs by shipped version (osv.dev)

## Summary

osv.dev reports **2 distinct advisories** affecting every CRI-O version Kubespray ships (see
[COMPONENT-CRI_O]). Neither has a released semver fix in osv, so the exposure is **identical on all
four shipped versions** — 1.33.5 through 1.35.0. Upgrading Kubespray does not change it.

CRI-O is the alternative runtime: it is installed only when `container_manager: crio`
([[VARIABLE-CONTAINER_MANAGER]]). Clusters on the default containerd are not affected by these.

Counts are **distinct advisories**.

## Problem

Both advisories are reachable from a workload: a path-traversal and an unbounded file read that can
exhaust node memory. The runtime runs as root on every node, so the blast radius is the node.

## Context

| Component version | Kubespray | # CVEs | CVEs |
|---|---|---|---|
| 1.33.5 | v2.29.0 | 2 | CVE-2025-0750, CVE-2025-4437 |
| 1.33.7 | v2.29.1 | 2 | CVE-2025-0750, CVE-2025-4437 |
| 1.34.4 | v2.30.0 | 2 | CVE-2025-0750, CVE-2025-4437 |
| 1.35.0 | v2.31.0 | 2 | CVE-2025-0750, CVE-2025-4437 |

The CRI-O version is **computed** from the first key of its checksum table at each tag, and it
tracks the Kubernetes minor ([[CONCEPT-COMPONENT_VERSION_SELECTION]]). Before v2.29.0 the value is
not statically resolvable from the tagged source, so those tags are not rowed here.

## Diagnostics

```bash
crio version ; crictl version
systemctl status crio --no-pager | head -3
```

## Known Issues

CVEs (id — summary — fixed in):

- **CVE-2025-0750** — CRI-O path-traversal vulnerability — fixed in: `—` (osv carries a fix commit but no released version)
- **CVE-2025-4437** — potential high memory consumption from a file read — fixed in: `—` (same)

**Recommendation:** there is no version to move to — no Kubespray tag in the envelope ships a CRI-O
release that osv records as fixed, and osv has no semver fix for either advisory. Treat this as a
**containment** problem rather than a patching one: both are workload-reachable, so the mitigations
that matter are the pod-level ones — no untrusted images, restricted volume/host-path use, and
memory limits on workloads so a single container cannot exhaust the node
([[PRACTICE-HARDENING]], [[CONCEPT-INSECURE_DEFAULTS]]). If CRI-O is not a requirement, containerd
is the better-patched runtime in this envelope ([[TROUBLE-CONTAINERD_KNOWN_CVES]]).

## References

- osv.dev (queried per version) for `github.com/cri-o/cri-o` — verified 2026-07-27.
- Component: [[COMPONENT-CRI_O]]; tracking: [[CONCEPT-SECURITY_ADVISORIES]].
