---
id: PRACTICE-CRI_O
type: best_practice
title: Using CRI-O as the Container Runtime in Kubespray
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - CRI-O runtime
tags:
  - cri
  - cri-o
  - runtime
sources:
  - type: docs
    path: docs/CRI/cri-o.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/CRI/cri-o.md
    note: "Enabling CRI-O, registry mirrors and auth, user namespaces, default capabilities, NRI"
relations: []
---

# Using CRI-O as the Container Runtime in Kubespray

## Summary
Describes running Kubespray clusters with CRI-O as the default CRI: the required inventory switches, configuring registry mirrors and insecure registries with authentication, enabling user namespaces, adjusting default container capabilities, and optional NRI. Key takeaway: CRI-O is selected with `container_manager: crio` and requires disabling Kubespray's container download step, plus host-deployed (or kubeadm-managed) etcd.

## Context
Applies when choosing CRI-O (supported on Kubernetes v1.11.1+). Prerequisites: set `download_container: false` and `skip_downloads: false` (all.yml), and configure etcd as either kubeadm-managed or `etcd_deployment_type: host`. Runtime selection and registry/namespace settings are driven by `crio_*` variables.

## Implementation
- Enable download bypass (all/all.yml): `download_container: false`, `skip_downloads: false`, `etcd_deployment_type: host` (optionally kubeadm).
- Select runtime (k8s_cluster): `container_manager: crio`.
- Registry mirrors (all/crio.yml): `crio_registries` — list of entries with `prefix`, `insecure`, `blocked`, `location`, `unqualified`, and `mirrors` (each `{location, insecure}`).
- Insecure registries: `crio_insecure_registries` (list of `host:port`).
- Registry auth: `crio_registry_auth` — list of `{registry, username, password}` for the configured registries.
- User namespaces (optional): define `crio_runtimes` with a runc entry that lists `allowed_annotations: ["io.kubernetes.cri-o.userns-mode"]`, and set `crio_remap_enable: true`. `allowed_annotations` configures `crio.conf`; `crio_remap_enable` adds a `containers` user entry to `/etc/subuid` and `/etc/subgid`. By default 16M uids/gids (256 pods * 65536) are reserved at the end of the uid/gid space.
- Default capabilities: `crio_default_capabilities` sets the container default caps (defaults: CHOWN, DAC_OVERRIDE, FSETID, FOWNER, SETGID, SETUID, SETPCAP, NET_BIND_SERVICE, KILL). Add MKNOD for a Rancher deployment.
- NRI (Node Resource Interface): disabled by default; enable with `nri_enabled: true` (requires CRI-O v1.26.0+).

## References
- docs/CRI/cri-o.md (tag v2.31.0 1c9add4)
