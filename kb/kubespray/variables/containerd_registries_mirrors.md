---
id: VARIABLE-CONTAINERD_REGISTRIES_MIRRORS
type: variable
title: containerd_registries_mirrors
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_registries_mirrors
tags:
  - containerd
  - registry
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "List of registry mirror definitions; default configures a docker.io mirror"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd_registries_mirrors

## Summary
Defines registry mirror configuration for containerd (per-registry host lists, capabilities, TLS verification). The default provides a single `docker.io` entry mirroring to `https://registry-1.docker.io`.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml`:

```yaml
containerd_registries_mirrors:
  - prefix: docker.io
    mirrors:
      - host: https://registry-1.docker.io
        capabilities: ["pull", "resolve"]
        skip_verify: false
```

The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Applies only when the container runtime is containerd; rendered into per-registry `hosts.toml` files. Related variable: `containerd_registry_auth`.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
