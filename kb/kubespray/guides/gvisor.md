---
id: PRACTICE-GVISOR
type: best_practice
title: gVisor sandboxed runtime in Kubespray
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - gVisor runsc
tags:
  - cri
  - gvisor
  - sandbox
sources:
  - type: docs
    path: docs/CRI/gvisor.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/CRI/gvisor.md
    note: "Enabling gVisor sandboxed runtime via containerd"
relations: []
---

# gVisor sandboxed runtime in Kubespray

## Summary
gVisor is an application kernel written in Go that implements a substantial part of the Linux system-call interface, providing an extra isolation layer between applications and the host OS. It ships an OCI runtime called `runsc`, selected in Kubernetes via a RuntimeClass. Kubespray can enable gVisor for supported container managers.

## Context
Applies when you want sandboxed workload isolation. gVisor requires a container manager that supports selecting the Kubernetes RuntimeClass, such as `containerd`. Enable it at cluster configuration time.

## Implementation
Enable gVisor with containerd:

```yaml
container_manager: containerd
gvisor_enabled: true
```

Workloads that should run under gVisor must reference the corresponding RuntimeClass (`runsc`) via the pod spec's `runtimeClassName`, per the Kubernetes RuntimeClass concept.

Caveat: gVisor requires a RuntimeClass-capable container manager; the doc names `containerd` as the compatible option.

## References
- docs/CRI/gvisor.md (tag v2.31.0 1c9add4)
