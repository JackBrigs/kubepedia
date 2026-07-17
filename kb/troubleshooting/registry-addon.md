---
id: TROUBLE-REGISTRY_ADDON
type: troubleshooting
title: "Kubespray registry addon (2.8.1): image loss, no auth/TLS, can't scale"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: "2.8.1"
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - registry_enabled images disappear
  - registry emptyDir data loss
  - kubespray in-cluster registry auth
  - registry_storage_class pvc
  - registry no tls http insecure
  - registry_htpasswd
tags:
  - troubleshooting
  - registry
  - storage
  - kubespray
sources:
  - type: code
    path: roles/kubernetes-apps/registry/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/registry/defaults/main.yml
    note: "registry_storage_class '' , replica 1, htpasswd '' , tls_secret ''"
  - type: code
    path: roles/kubernetes-apps/registry/templates/registry-rs.yml.j2
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/registry/templates/registry-rs.yml.j2
    note: "emptyDir unless registry_storage_class set; REGISTRY_AUTH htpasswd gated"
relations:
  - type: see_also
    target: COMPONENT-REGISTRY
  - type: see_also
    target: TROUBLE-KCM_VOLUME_MULTIATTACH
  - type: see_also
    target: TROUBLE-CONTAINERD_REGISTRY_CONFIG
---

# Kubespray registry addon (2.8.1): image loss, no auth/TLS, can't scale

## Summary

Kubespray's optional in-cluster registry (`registry_enabled: true`) deploys the **distribution
registry 2.8.1** ([[COMPONENT-REGISTRY]]) with **insecure, ephemeral defaults**. The three
things that bite operators: images **vanish on pod restart** (default storage is `emptyDir`),
the registry is **open** (no auth) and **plain HTTP** (no TLS), and it **won't scale** past one
replica with the default RWO volume. All of this is code-verified and **stable across
v2.27.0–v2.31.0**.

## Problem

- Pushed images **disappear** after the registry pod restarts/reschedules.
- Anyone can push/pull (no credentials); or pushes fail because the client expects TLS.
- Scaling `registry_replica_count > 1` leaves replicas `ContainerCreating` (Multi-Attach).

## Context

- Applies to Kubespray **v2.29.0–v2.31.0** (mechanism identical back to v2.27.0). Registry
  version **2.8.1** — constant across all tags. This is the **Kubespray-managed addon**, not a
  registry you upgrade to v3 ([[TROUBLE-REGISTRY_2_TO_3_MIGRATION]] is that separate case).

## Diagnostics

- **Image loss = `emptyDir` (the #1 gotcha):** the Deployment uses a PVC **only if**
  `registry_storage_class != ""`; otherwise the volume is **`emptyDir: {}`** — wiped on every
  pod restart/reschedule. **Fix:** set **`registry_storage_class`** (+ `registry_disk_size`,
  default `10Gi`, `registry_storage_access_mode: ReadWriteOnce`) so it binds a persistent
  `registry-pvc`. Verify: `kubectl -n kube-system get pvc registry-pvc` is `Bound`, and the pod
  mounts it (not emptyDir).
- **No authentication:** `registry_htpasswd: ""` by default → the registry is **open**. Set
  **`registry_htpasswd`** to a bcrypt htpasswd string (e.g. from `htpasswd -nbB user pass`) to
  enable `REGISTRY_AUTH=htpasswd`; then clients need `imagePullSecrets`/`docker login`.
- **No TLS:** `registry_tls_secret: ""` by default → **plain HTTP** on port `5000`. Either
  configure clients for an **insecure registry** (containerd `hosts.toml` `skip_verify` /
  CRI-O — [[TROUBLE-CONTAINERD_REGISTRY_CONFIG]]), or set **`registry_tls_secret`** (a TLS
  Secret) for HTTPS.
- **Can't scale:** `registry_replica_count: 1`; the PVC is **RWO**, so a second replica hits a
  Multi-Attach error ([[TROUBLE-KCM_VOLUME_MULTIATTACH]]). Keep 1 replica, or use **RWX**
  storage (or an external/S3-backed registry) for HA.
- **Access:** default `registry_service_type: ClusterIP` (reachable in-cluster only). Expose via
  NodePort/LoadBalancer (`registry_service_*`) or the Ingress template if external access is
  needed.

## Known Issues

- This addon is a **simple single-node registry**, not production-grade/HA — for real workloads
  use an external registry (Harbor, cloud registry, or distribution 2.8.1 with S3/GCS storage
  via `registry_config.storage`).
- With `emptyDir`, even a node drain / rolling update loses all cached images — always set a
  storage class in any environment where the registry holds anything you can't re-push.

## References

- registry `defaults/main.yml` + `registry-rs.yml.j2` (v2.31.0, above); component:
  [[COMPONENT-REGISTRY]]; RWO scale: [[TROUBLE-KCM_VOLUME_MULTIATTACH]]; insecure-client config:
  [[TROUBLE-CONTAINERD_REGISTRY_CONFIG]].
