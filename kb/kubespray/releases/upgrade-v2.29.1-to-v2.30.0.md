---
id: UPGRADE-V2_29_1__V2_30_0
type: upgrade
title: Upgrade report v2.29.1 → v2.30.0
status: active
kubespray_version: ">=v2.29.1 <=v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - v2.29.1 to v2.30.0
  - upgrade 2.29.1 2.30.0
tags:
  - upgrade
  - change-report
sources:
  - type: code
    path: roles/kubespray_defaults
    url: https://github.com/kubernetes-sigs/kubespray/compare/v2.29.1...v2.30.0
    note: "version deltas verified from tag code; API removals from K8s docs"
relations:
  - type: see_also
    target: RELEASE-V2_30_0
  - type: see_also
    target: CONCEPT-K8S_API_REMOVALS
---

# Upgrade report v2.29.1 → v2.30.0

## Summary

A **minor** upgrade that shifts the Kubernetes support window: `1.31` is dropped,
`1.34` is added. The most important operator action is the Kubernetes `1.32` API
removal that this transition crosses.

## Implementation

Version deltas:

| Item | v2.29.1 | v2.30.0 |
|------|---------|---------|
| Kubernetes default / min | 1.33.7 / 1.31.0 | 1.34.3 / **1.32.0** |
| Supported minors | 1.31, 1.32, 1.33 | **1.32, 1.33, 1.34** |
| etcd | 3.5.25 | 3.5.26 |
| containerd | 2.1.5 | 2.2.1 |
| runc | 1.3.4 | 1.3.4 |
| Cilium | 1.18.4 | 1.18.6 |
| CoreDNS (default) | 1.12.0 | 1.12.1 |
| kube-vip (deployed) | v0.8.9 | **v1.0.3** |
| nerdctl | 2.1.6 | 2.2.1 |

## Upgrade Notes

- **BREAKING — API removal:** crossing to Kubernetes `1.32` removes
  `flowcontrol.apiserver.k8s.io/v1beta3` (FlowSchema, PriorityLevelConfiguration)
  — migrate any such manifests to `/v1` **before** upgrading. See
  [[CONCEPT-K8S_API_REMOVALS]] / [[API-FLOWCONTROL_APISERVER]].
- **Feature gates:** the `1.32` release removes a large batch of long-GA gates;
  drop any of them from explicit `--feature-gates` (see
  [[CONCEPT-K8S_FEATURE_GATES]]).
- **Do not skip minors** — this must be a one-step Kubespray minor upgrade.
- kube-vip image tag now derives from `kube_vip_version` (`1.0.3`), fixing the
  earlier literal-tag mismatch.
- Standard graceful upgrade; snapshot etcd first ([[PRACTICE-UPGRADE_PREFLIGHT]]).

## Compatibility

- Clusters still on Kubernetes `1.31` must first move to `1.32`+; `1.31` is
  unsupported in v2.30.0.

## References

- [[RELEASE-V2_29_1]] → [[RELEASE-V2_30_0]]; [[CONCEPT-K8S_API_REMOVALS]].
