---
id: UPGRADE-V2_30_0__V2_31_0
type: upgrade
title: Upgrade report v2.30.0 → v2.31.0
status: active
kubespray_version: ">=v2.30.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - v2.30.0 to v2.31.0
  - upgrade 2.30.0 2.31.0
tags:
  - upgrade
  - change-report
sources:
  - type: code
    path: roles/kubespray_defaults
    url: https://github.com/kubernetes-sigs/kubespray/compare/v2.30.0...v2.31.0
    note: "version deltas verified from tag code; CVE from osv.dev"
relations:
  - type: see_also
    target: RELEASE-V2_31_0
  - type: see_also
    target: CONFIG-KUBEADM_CONFIG_API_VERSION
---

# Upgrade report v2.30.0 → v2.31.0

## Summary

A **minor** upgrade: Kubernetes window shifts (`1.32` dropped, `1.35` added).
Notable: **etcd 3.6** is introduced for Kubernetes `1.35`, the
`kubeadm_config_api_version` variable is removed, and several component CVEs are
fixed by the version bumps.

## Implementation

Version deltas:

| Item | v2.30.0 | v2.31.0 |
|------|---------|---------|
| Kubernetes default / min | 1.34.3 / 1.32.0 | 1.35.4 / **1.33.0** |
| Supported minors | 1.32, 1.33, 1.34 | **1.33, 1.34, 1.35** |
| etcd | 3.5.26 | 3.5.29 (1.33/1.34) / **3.6.10 (1.35)** |
| containerd | 2.2.1 | 2.2.3 |
| runc | 1.3.4 | **1.4.2** |
| Cilium | 1.18.6 | **1.19.3** |
| CoreDNS (default) | 1.12.1 | 1.12.4 |
| cni-plugins | 1.8.0 | **1.9.1** |
| nerdctl | 2.2.1 | 2.2.2 |

## Upgrade Notes

- **etcd 3.6** first appears (gated to Kubernetes `1.35` via the `<3.7` ceiling;
  older minors stay on `3.5.x`). Review etcd 3.6 operational changes if you run
  `1.35`. See [[COMPONENT-ETCD]].
- **kubeadm config:** the `kubeadm_config_api_version` variable and the `v1beta3`
  fallback are **removed**; the template is pinned to `v1beta4`
  ([[CONFIG-KUBEADM_CONFIG_API_VERSION]]). Remove any override of that variable.
- **Security fixes via bumps:** cni-plugins `1.8.0 → 1.9.1` fixes
  **CVE-2025-67499**; Cilium `1.18.6 → 1.19.3` clears most Cilium CVEs; runc
  `1.3.4 → 1.4.2`. (Some CVEs remain even at these versions — see the per-component
  security docs.)
- **Feature gates / no API removals** documented for `1.33`–`1.35` (see
  [[CONCEPT-K8S_API_REMOVALS]], [[CONCEPT-K8S_FEATURE_GATES]]).
- The legacy `master` run-tag is gone (fully renamed to `control-plane`).
- One minor at a time; snapshot etcd first ([[PRACTICE-UPGRADE_PREFLIGHT]]).

## Compatibility

- Clusters on Kubernetes `1.32` must move to `1.33`+; `1.32` is unsupported in
  v2.31.0.

## References

- [[RELEASE-V2_30_0]] → [[RELEASE-V2_31_0]]; security: [[TROUBLE-CNI_PLUGINS_KNOWN_CVES]],
  [[TROUBLE-CILIUM_KNOWN_CVES]].
