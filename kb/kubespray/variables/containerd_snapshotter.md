---
id: VARIABLE-CONTAINERD_SNAPSHOTTER
type: variable
title: containerd_snapshotter
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_snapshotter
tags:
  - containerd
  - snapshotter
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Default containerd snapshotter driver, defaults to overlayfs"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd_snapshotter

## Summary
Selects the containerd snapshotter (storage driver) used by the CRI plugin. Default is `overlayfs`. The value is rendered directly into the containerd config's `snapshotter` field.

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml` (line 11):

```yaml
containerd_snapshotter: "overlayfs"
```

Rendered into `templates/config.toml.j2` and `templates/config-v1.toml.j2` as `snapshotter = "{{ containerd_snapshotter }}"`. Value is unchanged (`overlayfs`) across v2.29.0–v2.31.0. The sample inventory `inventory/sample/group_vars/all/containerd.yml` shows a commented example `# containerd_snapshotter: "native"`.

## Compatibility
Present and identical in v2.29.0–v2.31.0. Overridable in inventory (e.g. `native`).

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
