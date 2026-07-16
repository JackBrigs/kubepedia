---
id: CONCEPT-CONTAINER_RUNTIMES
type: concept
title: "Container runtimes in Kubespray (runc default, crun/youki, kata/gVisor)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - container runtimes
  - low-level runtime
  - containerd_default_runtime
  - runc crun youki
  - kata gvisor runsc
  - sandboxed runtime RuntimeClass
tags:
  - containerd
  - runtime
  - runc
  - sandbox
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "container_manager, kata/gvisor/crun/youki enable flags (tag v2.31.0)"
  - type: code
    path: roles/container-engine/containerd/templates/config.toml.j2
    lines: "51-75"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/templates/config.toml.j2
    note: "runtime handlers kata-qemu / runsc + configurable runtimes (tag v2.31.0)"
relations:
  - type: see_also
    target: CONCEPT-CONTAINERD_2X
  - type: see_also
    target: COMPONENT-RUNC
  - type: see_also
    target: COMPONENT-KATA_CONTAINERS
---

# Container runtimes in Kubespray (runc default, crun/youki, kata/gVisor)

## Summary

With `container_manager: containerd` (the default), containerd delegates actual container
execution to a **runtime handler**. Kubespray's default low-level runtime is **runc**;
you can swap it for a compatible OCI runtime (**crun**, **youki**) or add **sandboxed**
runtimes (**Kata Containers**, **gVisor/runsc**) exposed through Kubernetes
**RuntimeClass**. All alternatives are **off by default**.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`, `container_manager: containerd`
  ([[CONCEPT-CONTAINERD_2X]]). `nri_enabled` is on when containerd is the manager.
- Two categories of runtime:
  - **Low-level OCI runtimes** (drop-in for runc): `runc` (default), `crun`, `youki` —
    same container model, different implementation (crun/youki are C/Rust, lighter).
  - **Sandboxed runtimes** (stronger isolation, own handler): `kata-qemu` (VM-based),
    `runsc` (gVisor, userspace kernel) — selected per-Pod via RuntimeClass.

## Implementation

- `containerd_default_runtime: "runc"` — the default handler for all Pods. Set it to
  `crun`/`youki` (with `crun_enabled`/`youki_enabled: true`) to replace runc cluster-wide.
- **Enable flags** (all default `false`): `kata_containers_enabled`, `gvisor_enabled`,
  `crun_enabled`, `youki_enabled`.
- **Runtime handlers** are rendered into `config.toml` under
  `io.containerd.cri.v1.runtime.containerd.runtimes.<name>`:
  - `kata-qemu` → `runtime_type = io.containerd.kata-qemu.v2`
  - `runsc` (gVisor) → `runtime_type = io.containerd.runsc.v1`
  - plus any entries in the configurable `containerd_runtimes` list.
- **Consuming a sandboxed runtime:** create a `RuntimeClass` referencing the handler
  (e.g. `kata-qemu`/`runsc`) and set `runtimeClassName` on the Pod. Without a RuntimeClass
  + Pod opt-in, workloads keep using the default runtime.
- Component specifics: [[COMPONENT-RUNC]], `COMPONENT-CRUN`, `COMPONENT-YOUKI`,
  [[COMPONENT-KATA_CONTAINERS]].

## Compatibility

- runc → crun/youki is transparent to workloads (same OCI); verify the alternative's
  version is bundled (checksums map) before pinning.
- Sandboxed runtimes need host support (kata: virtualization/KVM; gVisor: kernel
  features) and add overhead — use RuntimeClass to target only the Pods that need
  isolation, not the whole cluster.
- Runtime handlers live under the containerd 2.x plugin path — a 1.x handler snippet won't
  apply ([[CONCEPT-CONTAINERD_2X]]).

## References

- `main.yml` (runtime enable flags) and `config.toml.j2:51-75` (handlers) at tag
  `v2.31.0`. Runtime engine: [[CONCEPT-CONTAINERD_2X]].
