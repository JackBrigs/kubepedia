---
id: VARIABLE-CONTAINERD_RUNC_RUNTIME
type: variable
title: containerd_runc_runtime
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_runc_runtime
tags:
  - containerd
  - runtime
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Defines the default runc runtime mapping rendered into the containerd CRI config"
relations: []
---

# containerd_runc_runtime

## Summary
Defines the default `runc` runtime entry that containerd registers as a CRI runtime. It is a mapping (name, type, base_runtime_spec, options) that is combined with `containerd_additional_runtimes` and rendered into `config.toml` / `config-v1.toml`. The runtime type is `io.containerd.runc.v2` in all four tags.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml` (line 13) as a YAML mapping. The exact keys changed between the v2.29.x and v2.30.0+ tags:

| Tag | Structure |
|-----|-----------|
| v2.29.0 / v2.29.1 | `name: runc`, `type: "io.containerd.runc.v2"`, `engine: ""`, `root: ""`, `base_runtime_spec: cri-base.json`, `options.SystemdCgroup`, `options.BinaryName` |
| v2.30.0 / v2.31.0 | `name: runc`, `type: "io.containerd.runc.v2"`, `base_runtime_spec: cri-base.json`, `options.Root: ""`, `options.SystemdCgroup`, `options.BinaryName: "{{ bin_dir }}/runc"` |

Consumed in `templates/config-v1.toml.j2` and `templates/config.toml.j2` via `[containerd_runc_runtime] + containerd_additional_runtimes`.

## Compatibility
Present in v2.29.0–v2.31.0. The top-level `engine`/`root` keys were removed in v2.30.0 and `root` moved into `options.Root`. Related: `containerd_additional_runtimes`, `containerd_use_systemd_cgroup`.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
