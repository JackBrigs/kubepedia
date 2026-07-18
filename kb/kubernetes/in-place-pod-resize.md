---
id: CONCEPT-K8S_IN_PLACE_POD_RESIZE
type: concept
title: "In-place pod resize — mutable CPU/memory without restart (on-by-default 1.33, GA 1.35)"
status: active
kubespray_version: ">=v2.31.0 <=v2.31.0"
kubernetes_version: ">=1.33 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - in-place pod vertical scaling
  - InPlacePodVerticalScaling
  - resize subresource
  - change pod resources without restart
  - pod resize policy
tags:
  - kubernetes
  - kubelet
  - scheduling
sources:
  - type: code
    path: keps/sig-node/1287-in-place-update-pod-resources
    url: https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/1287-in-place-update-pod-resources
    note: "kep.yaml: alpha 1.27, beta/on-by-default 1.33, stable 1.35"
relations:
  - type: see_also
    target: CONCEPT-K8S_UPGRADE_SILENT_CHANGES
  - type: see_also
    target: CONCEPT-K8S_FEATURE_GATES
---

# In-place pod resize — mutable CPU/memory without restart (on-by-default 1.33, GA 1.35)

## Summary

A running pod's CPU/memory `resources` can now be changed **without recreating the pod**, via the new
**`resize` subresource**. `InPlacePodVerticalScaling` is **on by default from K8s 1.33** and **GA in
1.35** (Kubespray v2.31.0). This changes scheduler/kubelet behavior and enables VPA-style right-sizing
with no restart — but also means pod `resources` are no longer immutable, which automation and admission
policies must account for.

## Context

- Milestone (`keps/sig-node/1287-...` kep.yaml): alpha **1.27**, beta/on **1.33**, stable **1.35**.
- **How:** patch the `resize` subresource; each container has a `resizePolicy` per resource
  (`NotRequired` = live resize, `RestartContainer` = restart to apply). `status.resources` reflects the
  actual applied values; `status.resize` shows in-progress/deferred/infeasible.
- **Operator impact:** (1) admission/policy that assumed `spec.resources` is immutable may need
  updating; (2) VPA and custom right-sizers can now act without disruption; (3) memory **decrease** may
  be `RestartContainer` depending on policy. Verify the gate state per release
  ([[CONCEPT-K8S_FEATURE_GATES]]).

## References

- `keps/sig-node/1287-in-place-update-pod-resources` (kep.yaml GA 1.35). Silent changes
  [[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]]; gates [[CONCEPT-K8S_FEATURE_GATES]].
