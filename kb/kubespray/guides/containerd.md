---
id: PRACTICE-CONTAINERD
type: best_practice
title: Using containerd as the Container Runtime in Kubespray
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - containerd runtime
tags:
  - cri
  - containerd
  - runtime
sources:
  - type: docs
    path: docs/CRI/containerd.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/CRI/containerd.md
    note: "Enabling containerd, registry mirrors, custom runtimes, base runtime specs, NRI, static binary"
relations: []
---

# Using containerd as the Container Runtime in Kubespray

## Summary
Explains how to run Kubespray clusters with containerd as the default CRI: the required inventory switches, configuring registry mirrors (including insecure/self-hosted registries), defining custom RuntimeClass-backed runtimes, tuning base runtime specs (e.g. file-descriptor limits), and optional NRI and static-binary settings. Key takeaway: containerd is selected with `container_manager: containerd`, and registry/runtime behavior is fully declarative via `containerd_*` variables.

## Context
Applies when choosing containerd as the container runtime. Prerequisites in the inventory: set `container_manager: containerd` (k8s_cluster). When etcd nodes overlap with `kube_node`, etcd must use `etcd_deployment_type: host` because containerd and dockerd cannot run simultaneously.

## Implementation
- Select runtime: `container_manager: containerd` (in k8s_cluster group vars).
- etcd co-location: set `etcd_deployment_type: host` (etcd.yml) when etcd runs on schedulable kube_node hosts under containerd.
- Registry mirrors: `containerd_registries_mirrors` — a list of `{prefix, mirrors: [{host, capabilities, skip_verify}], server}`. containerd falls back to `https://{{ prefix }}` when no mirror has the image; override the fallback with the optional `server` field.
  - Insecure/self-hosted registries: set `skip_verify: true` and use `http://` hosts in the mirror entries (works for hostnames, IP:port, and `repo:5000` style prefixes).
  - `containerd_registries` and `containerd_insecure_registries` are deprecated — use `containerd_registries_mirrors` instead.
- Custom runtimes (RuntimeClass): default runtime is "runc", configured via the `containerd_runc_runtime` dict (name, type `io.containerd.runc.v2`, options like `SystemdCgroup`, `BinaryName`, `base_runtime_spec`). Additional runtimes go in the `containerd_additional_runtimes` list. Change the default with `containerd_default_runtime`.
- Base runtime specs / open-file limits: `base_runtime_spec` points to a runtime spec JSON. runc uses `cri-base.json` (generated with `ctr oci spec > /etc/containerd/cri-base.json`) customized for max file descriptors. Adjust the fd limit for the default runc runtime via `containerd_base_runtime_spec_rlimit_nofile`. Supply fully custom specs with `containerd_base_runtime_specs` (a dict of filename -> JSON content); files land in `/etc/containerd` and are referenced by filename in a runtime's `base_runtime_spec`.
- NRI (Node Resource Interface): disabled by default; enable with `nri_enabled: true` (requires containerd v1.7.0+).
- Static binary: `containerd_static_binary: true` for older distros (e.g. Debian 11). By default a static binary is used automatically when the system glibc is < 2.34, otherwise the default binary is used.

## References
- docs/CRI/containerd.md (tag v2.31.0 1c9add4)
