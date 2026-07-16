---
id: CONCEPT-CONTAINER_MANAGER
type: concept
title: "Choosing the container manager (containerd, CRI-O, Docker)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - container_manager
  - containerd vs cri-o vs docker
  - CRI runtime choice
  - cri_socket
  - container engine kubespray
tags:
  - containerd
  - cri-o
  - docker
  - runtime
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "container_manager: containerd default; cri_socket derived (tag v2.31.0)"
relations:
  - type: see_also
    target: VARIABLE-CONTAINER_MANAGER
  - type: see_also
    target: CONCEPT-CONTAINERD_2X
  - type: see_also
    target: CONCEPT-CONTAINER_RUNTIMES
---

# Choosing the container manager (containerd, CRI-O, Docker)

## Summary

`container_manager` picks the **CRI runtime engine** the kubelet talks to. Kubespray
defaults to **containerd**; alternatives are **CRI-O** and **Docker** (via cri-dockerd).
This is the *engine* choice — distinct from the *low-level OCI runtime* (runc/crun/youki)
that the engine invokes ([[CONCEPT-CONTAINER_RUNTIMES]]). It's a cluster-wide, per-node
decision set at install.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`. `container_manager: containerd` (default);
  accepted `containerd` | `crio` | `docker`.
- Kubespray derives **`cri_socket`** from `container_manager`, and the kubelet's
  `containerRuntimeEndpoint` points at it ([[CONFIG-KUBELET_CONFIGURATION]]).

## Implementation

- **containerd** (default) — the mainstream CRI; config version 3, `cri.v1` plugin paths
  ([[CONCEPT-CONTAINERD_2X]]); socket `unix:///var/run/containerd/containerd.sock`.
  Recommended unless you have a specific reason otherwise.
- **CRI-O** (`container_manager: crio`) — a lightweight, Kubernetes-focused CRI; its
  version tracks the Kubernetes minor (`select('version', next-minor, '<')` —
  [[CONCEPT-COMPONENT_VERSION_SELECTION]]). Socket `unix:///var/run/crio/crio.sock`.
- **Docker** (`container_manager: docker`) — since Kubernetes removed dockershim, the
  kubelet reaches Docker through **cri-dockerd** (a separate shim); Kubespray pins
  `docker_containerd_version` (`1.6.x`) for Docker's embedded containerd. The most legacy
  path — prefer containerd/CRI-O for new clusters.

The chosen manager's runtime handlers then invoke the low-level OCI runtime
(`containerd_default_runtime: runc`, etc. — [[CONCEPT-CONTAINER_RUNTIMES]]).

## Compatibility

- **One manager per node**, set at install; switching an existing node's
  `container_manager` is a runtime migration, not a config toggle — expect to reset/rebuild
  the node (there's a dedicated migrate-docker-to-containerd path for that transition).
- Registry mirror config differs by engine — for containerd it's `certs.d`/`hosts.toml`
  ([[TROUBLE-CONTAINERD_REGISTRY_CONFIG]]); CRI-O/Docker use their own config.
- `cri_socket` must match the running manager; a mismatch makes the kubelet unable to reach
  the runtime (`ContainerCreating` / node `NotReady`).
- Sandboxed/alternative runtimes (kata, gVisor, crun, youki) are configured on top of the
  chosen manager (mostly containerd) — see [[CONCEPT-CONTAINER_RUNTIMES]].

## References

- `container_manager` / `cri_socket` at tag `v2.31.0`. Engine internals:
  [[CONCEPT-CONTAINERD_2X]]; low-level runtimes: [[CONCEPT-CONTAINER_RUNTIMES]];
  variable: [[VARIABLE-CONTAINER_MANAGER]].
