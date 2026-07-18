---
id: TROUBLE-CILIUM_CLUSTERMESH_LOCAL_POLICY
type: troubleshooting
title: "Cilium 1.19 breaks cross-cluster traffic — policy-default-local-cluster now on by default"
status: active
kubespray_version: ">=v2.30.0 <=v2.31.0"
kubernetes_version: ">=1.33 <=1.35"
component_version: ">=1.18.2 <=1.19.3"
verified_at: "2026-07-18"
confidence: confirmed
aliases:
  - policy-default-local-cluster
  - cilium clustermesh policy broke
  - cross-cluster connectivity denied cilium 1.19
  - network policy selects only local cluster
  - clustermesh default deny remote
tags:
  - cilium
  - troubleshooting
  - clustermesh
  - upgrade
sources:
  - type: docs
    path: Documentation/operations/upgrade.rst
    url: https://github.com/cilium/cilium/blob/v1.19.3/Documentation/operations/upgrade.rst
    note: "policy-default-local-cluster default flips to enabled in 1.19; forward-noticed in 1.18"
relations:
  - type: see_also
    target: UPGRADE-CILIUM_1_15_TO_1_19
  - type: see_also
    target: COMPONENT-CILIUM
  - type: see_also
    target: PRACTICE-RUNBOOK_CONFIG_CHANGE
---

# Cilium 1.19 breaks cross-cluster traffic — policy-default-local-cluster now on by default

## Summary

In Cilium **1.19**, `policy-default-local-cluster` is **enabled by default**. Network-policy `Endpoints`
selectors now match **only local-cluster endpoints** by default, where previously they matched
endpoints across **all** ClusterMesh clusters. In a ClusterMesh setup, cross-cluster traffic that
relied on a policy selecting remote endpoints is **silently denied** after Kubespray moves Cilium to
**1.19.3 (v2.31.0)**. This was forward-noticed in 1.18 (v2.29.0/v2.30.0) via the same flag defaulting
the other way.

## Problem

- After upgrading to Kubespray v2.31.0, pods that talk **across clusters** in a ClusterMesh start
  getting **denied** by network policy; same-cluster traffic is fine.
- CiliumNetworkPolicies that intended to allow remote-cluster endpoints no longer do.

## Context

- Applies to Cilium **1.19+** → Kubespray **v2.31.0** ([[COMPONENT-CILIUM]],
  [[UPGRADE-CILIUM_1_15_TO_1_19]]). The `policy-default-local-cluster` flag existed in **1.18**
  (default kept all-cluster selection) and **flips to on** in **1.19** (`upgrade.rst`@v1.19.3).
- Rationale: safer default (a policy shouldn't accidentally select the whole mesh); but it changes the
  semantics of existing policies in a multi-cluster deployment.

## Diagnostics

- Confirm ClusterMesh is in use: `cilium clustermesh status` — remote clusters connected.
- Check the setting: `kubectl -n kube-system get cm cilium-config -o yaml | grep policy-default-local-cluster`
  — `true` on 1.19 is the new default.
- Hubble: `hubble observe --verdict DROPPED` between a local and a remote-cluster endpoint shows the
  policy drop.

## Known Issues

- **Fix (keep old behavior):** set `policy-default-local-cluster=false` (Helm
  `clustermesh.policyDefaultLocalCluster` / config) to restore all-cluster selection, then plan a
  proper migration. Apply via a canary before rolling ([[PRACTICE-RUNBOOK_CONFIG_CHANGE]]).
- **Fix (adopt new default):** update CiliumNetworkPolicies that must allow remote endpoints to
  explicitly select across clusters (per-cluster selectors), then leave the default on.
- **Pre-upgrade:** for any ClusterMesh cluster, decide this **before** v2.31.0 — it is a silent
  cross-cluster connectivity breaker and one of three ClusterMesh default flips in the range (KVStoreMesh
  on @1.16, mesh-auth off @1.19).

## References

- Cilium `Documentation/operations/upgrade.rst`@v1.19.3 (policy-default-local-cluster). Full jump
  [[UPGRADE-CILIUM_1_15_TO_1_19]]; component [[COMPONENT-CILIUM]]; config-change runbook
  [[PRACTICE-RUNBOOK_CONFIG_CHANGE]].
