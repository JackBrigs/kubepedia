---
id: CONCEPT-K8S_SIDECAR_CONTAINERS
type: concept
title: "Native sidecar containers — restartable initContainers (on-by-default 1.29, GA 1.33)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - native sidecar containers
  - SidecarContainers
  - initContainer restartPolicy Always
  - sidecar startup ordering
  - sidecar lifecycle kubernetes
tags:
  - kubernetes
  - kubelet
  - workloads
sources:
  - type: code
    path: keps/sig-node/753-sidecar-containers
    url: https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/753-sidecar-containers
    note: "kep.yaml: alpha 1.28, beta/on-by-default 1.29, stable 1.33"
relations:
  - type: see_also
    target: CONCEPT-K8S_UPGRADE_SILENT_CHANGES
  - type: see_also
    target: CONCEPT-K8S_FEATURE_GATES
---

# Native sidecar containers — restartable initContainers (on-by-default 1.29, GA 1.33)

## Summary

Kubernetes has **native sidecars**: an `initContainer` with **`restartPolicy: Always`** starts
**before** the main containers, **keeps running** alongside them, and is **shut down after** them.
`SidecarContainers` is **on by default from K8s 1.29** and **GA in 1.33**. This changes pod startup and
termination ordering — relevant to service meshes (Istio/Cilium/Linkerd), log shippers, and any
"sidecar" that previously raced the main container or blocked Job completion.

## Context

- Milestone (`keps/sig-node/753-...` kep.yaml): alpha **1.28**, beta/on **1.29**, stable **1.33**.
- **Behavior:** native sidecars are guaranteed **started before** app containers and **terminated
  after** them; they no longer block **Job** completion (a classic pain: a sidecar keeping a Job pod
  alive forever). Probes are supported on sidecars.
- **Operator impact (mostly positive, but a change):** mesh/proxy injection can move to native
  sidecars → cleaner startup ordering and Job semantics; tooling that assumed initContainers always
  **run to completion before** app start must account for the always-running variant. On by default
  since 1.29, so it's active across the whole Kubespray range.

## References

- `keps/sig-node/753-sidecar-containers` (kep.yaml GA 1.33). Silent changes
  [[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]]; gates [[CONCEPT-K8S_FEATURE_GATES]].
