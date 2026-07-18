---
id: CONCEPT-K8S_CGROUP_DRIVER_FROM_CRI
type: concept
title: "kubelet auto-detects cgroup driver from CRI (GA 1.34)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - KubeletCgroupDriverFromCRI
  - cgroup driver auto-detect
  - cgroupDriver systemd mismatch
  - kubelet runtime cgroup driver
  - cgroup driver from CRI
tags:
  - kubernetes
  - kubelet
  - containerd
  - cgroups
sources:
  - type: code
    path: keps/sig-node/4033-group-driver-detection-over-cri
    url: https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/4033-group-driver-detection-over-cri
    note: "kep.yaml: alpha 1.28, beta 1.31, stable 1.34"
relations:
  - type: see_also
    target: PRACTICE-CGROUPS
  - type: see_also
    target: CONCEPT-K8S_UPGRADE_SILENT_CHANGES
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# kubelet auto-detects cgroup driver from CRI (GA 1.34)

## Summary

The kubelet can now **learn the cgroup driver from the container runtime over CRI** instead of needing
it hand-set to match — `KubeletCgroupDriverFromCRI` reached **beta in 1.31** and **GA in 1.34**. This
removes the classic footgun where a **`cgroupDriver` mismatch** between kubelet and the runtime
(`systemd` vs `cgroupfs`) caused nodes to misbehave. It's relevant to Kubespray because Kubespray sets
the driver **explicitly** today.

## Context

- Milestone (`keps/sig-node/4033-...` kep.yaml): alpha **1.28**, beta **1.31**, stable **1.34**.
- **What changes:** when the runtime (containerd ≥ a supporting version — [[COMPONENT-CONTAINERD]])
  advertises its cgroup driver over CRI, the kubelet adopts it; the kubelet `cgroupDriver` setting no
  longer has to be manually aligned. `systemd` is the correct driver on cgroup v2 systems
  ([[PRACTICE-CGROUPS]]).
- **Kubespray note:** Kubespray configures `cgroupDriver: systemd` and the containerd
  `SystemdCgroup = true` consistently, so clusters are already aligned — the value of this KEP is that
  a future misalignment (custom runtime config, an override) is **self-corrected** rather than breaking
  nodes. No action required for a standard Kubespray deploy; do not fight the auto-detected value with a
  conflicting manual override once on 1.34+.

## References

- `keps/sig-node/4033-group-driver-detection-over-cri` (kep.yaml GA 1.34). cgroups [[PRACTICE-CGROUPS]];
  containerd [[COMPONENT-CONTAINERD]]; silent changes [[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]].
