---
id: UPGRADE-V2_29_0__V2_29_1
type: upgrade
title: Upgrade report v2.29.0 → v2.29.1
status: active
kubespray_version: ">=v2.29.0 <=v2.29.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - v2.29.0 to v2.29.1
  - upgrade 2.29.0 2.29.1
tags:
  - upgrade
  - change-report
sources:
  - type: code
    path: roles/kubespray_defaults
    url: https://github.com/kubernetes-sigs/kubespray/compare/v2.29.0...v2.29.1
    note: "version deltas verified from tag code; CVE from osv.dev"
relations:
  - type: see_also
    target: RELEASE-V2_29_1
  - type: see_also
    target: TROUBLE-RUNC_CONTAINER_ESCAPE_NOV2025
---

# Upgrade report v2.29.0 → v2.29.1

## Summary

A **patch** upgrade: same Kubernetes minor window (1.31–1.33), refreshed patch
and component versions. **Security-motivated:** it fixes the runc container-escape
CVEs present in v2.29.0.

## Implementation

Version deltas:

| Item | v2.29.0 | v2.29.1 |
|------|---------|---------|
| Kubernetes default / min | 1.33.5 / 1.31.0 | 1.33.7 / 1.31.0 |
| etcd | 3.5.23 | 3.5.25 |
| containerd | 2.1.4 | 2.1.5 |
| runc | 1.3.2 | **1.3.4** |
| Cilium | 1.18.2 | 1.18.4 |
| CoreDNS (default) | 1.12.0 | 1.12.0 |

## Upgrade Notes

- **Security:** runc `1.3.2 → 1.3.4` fixes **CVE-2025-31133** and the coordinated
  runc container-escape CVEs (see [[TROUBLE-RUNC_CONTAINER_ESCAPE_NOV2025]]). This
  alone is a strong reason to move off v2.29.0.
- **No API removals** — same Kubernetes minor window; no breaking API changes.
- No default/behavior changes of note beyond version bumps.
- Standard graceful upgrade ([[UPGRADE-KUBESPRAY_SEQUENTIAL]]); patch upgrades are
  low-risk.

## Compatibility

- Kubernetes stays on 1.31–1.33 (patch ranges extended, default 1.33.5 → 1.33.7).

## References

- Component deltas: [[RELEASE-V2_29_0]] → [[RELEASE-V2_29_1]].
- Security: [[TROUBLE-RUNC_KNOWN_CVES]].
