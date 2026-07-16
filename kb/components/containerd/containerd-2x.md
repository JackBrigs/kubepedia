---
id: CONCEPT-CONTAINERD_2X
type: concept
title: "containerd 2.x specifics in Kubespray (config v3, CRI plugin paths)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: ">=2.1.4 <=2.2.3"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd 2.x
  - containerd config version 3
  - io.containerd.cri.v1.runtime
  - containerd 2 migration
  - containerd config.toml v3
tags:
  - containerd
  - cri
  - runtime
  - configuration
sources:
  - type: code
    path: roles/container-engine/containerd/templates/config.toml.j2
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/templates/config.toml.j2
    note: "config version = 3; io.containerd.cri.v1.* plugin paths (tag v2.31.0)"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
  - type: see_also
    target: TROUBLE-CONTAINERD_REGISTRY_CONFIG
  - type: see_also
    target: TROUBLE-CGROUP_DRIVER_MISMATCH
---

# containerd 2.x specifics in Kubespray (config v3, CRI plugin paths)

## Summary

Across `v2.29.0`–`v2.31.0` Kubespray ships **containerd 2.x** (`2.1.4` → `2.2.3`), not the
1.x many operators remember. containerd 2.x changed the **config schema** and the **CRI
plugin namespaces**, so 1.x config snippets and troubleshooting habits don't transfer
verbatim. This note captures the 2.x-specific facts that matter when reading or editing
the generated `config.toml`.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`, `container_manager: containerd`
  (component `2.1.4`–`2.2.3`; the `docker` path uses a separate `docker_containerd_version`
  `1.6.x` and is not this).
- The generated file is `/etc/containerd/config.toml`, rendered from `config.toml.j2`.

## Implementation

**What's different from containerd 1.x:**

- **Config version 3.** The file starts with `version = 3` (1.x used `version = 2`).
  containerd 2.x reads v2/v3; Kubespray writes **v3**. Old `version = 2` hand-configs
  should be re-expressed.
- **New CRI plugin namespaces.** Plugins moved from 1.x's
  `io.containerd.grpc.v1.cri` to **`io.containerd.cri.v1.runtime`** (runtimes,
  SystemdCgroup, runtime handlers) and **`io.containerd.cri.v1.images`** (registry,
  pinned/sandbox images). Any override targeting the old path is ignored — target the new
  ones.
- **Registry config via `config_path`.** `io.containerd.cri.v1.images.registry` sets
  `config_path = /etc/containerd/certs.d` (per-registry `hosts.toml`); the old inline
  `registry.mirrors`/`registry.configs` TOML is deprecated —
  [[TROUBLE-CONTAINERD_REGISTRY_CONFIG]].
- **cgroup driver** lives under the new runtime plugin (`SystemdCgroup`,
  `containerd_use_systemd_cgroup: true`) — must match the kubelet
  ([[TROUBLE-CGROUP_DRIVER_MISMATCH]]).
- Runtime handlers (`runc`, `kata-qemu`, `runsc`) are declared under
  `…cri.v1.runtime.containerd.runtimes.<name>`; `sandbox_image` (pause) under
  `…cri.v1.images`.

**Practical impact:** use `crictl` / `ctr` and the new plugin paths when inspecting;
`containerd config dump` shows the effective v3 config.

## Compatibility

- containerd 2.x requires re-expressing any inherited v1/v2 config; do not copy 1.x
  `config.toml` fragments onto a 2.x node.
- Version is selected as the newest entry in the bundled checksums map (moves when you bump
  Kubespray) — see [[CONCEPT-COMPONENT_VERSION_SELECTION]].
- 2.x removed/relocated some 1.x plugin options; validate custom `containerd_*` overrides
  against the 2.x schema after an upgrade.

## References

- `config.toml.j2` (`version = 3`, `io.containerd.cri.v1.*`) at tag `v2.31.0`.
- Component: [[COMPONENT-CONTAINERD]]; registry: [[TROUBLE-CONTAINERD_REGISTRY_CONFIG]];
  cgroup driver: [[TROUBLE-CGROUP_DRIVER_MISMATCH]].
