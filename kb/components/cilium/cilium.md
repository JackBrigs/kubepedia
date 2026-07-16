---
id: COMPONENT-CILIUM
type: component
title: Cilium
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: ">=1.18.2 <=1.19.3"
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - cilium
tags:
  - cni
  - cilium
  - networking
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    lines: "117 (v2.29.0), 119 (v2.30.0/v2.31.0)"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "cilium_version literal; cilium_image_repo/cilium_image_tag"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_network_plugin selects cilium"
relations:
  - type: see_also
    target: VARIABLE-KUBE_NETWORK_PLUGIN
---

# Cilium

## Summary

Cilium is an eBPF-based CNI plugin, selectable in Kubespray with
`kube_network_plugin: cilium` (see [[VARIABLE-KUBE_NETWORK_PLUGIN]]; the default
plugin is `calico`). Unlike etcd/containerd, the Cilium version is a **literal**
pin in the plugin role, not derived from a checksums table.

## Context

- Covers Kubespray `v2.29.0`–`v2.31.0`.
- Active only when `kube_network_plugin` is `cilium`.
- Installed by the `roles/network_plugin/cilium` role.

## Implementation

The version is a literal in `roles/network_plugin/cilium/defaults/main.yml`:

```yaml
cilium_version: "1.19.3"          # value shown for v2.31.0
cilium_image_repo: "{{ quay_image_repo }}/cilium/cilium"   # quay.io/cilium/cilium
cilium_image_tag: "v{{ cilium_version }}"
```

Concrete version per tag:

| Kubespray | cilium_version | defaults line | Image |
|-----------|----------------|---------------|-------|
| v2.29.0   | 1.18.2         | 117           | quay.io/cilium/cilium:v1.18.2 |
| v2.30.0   | 1.18.6         | 119           | quay.io/cilium/cilium:v1.18.6 |
| v2.31.0   | 1.19.3         | 119           | quay.io/cilium/cilium:v1.19.3 |

Note the minor bump `1.18 → 1.19` in `v2.31.0`.

## Configuration

- Version: `cilium_version` (literal, `roles/network_plugin/cilium/defaults/main.yml`).
- Image: `cilium_image_repo` = `quay.io/cilium/cilium`, `cilium_image_tag` =
  `v{{ cilium_version }}`.
- Selection: [[VARIABLE-KUBE_NETWORK_PLUGIN]] must be `cilium`.
- Further Cilium tunables (datapath mode, kube-proxy replacement, hubble, etc.)
  live in the same `roles/network_plugin/cilium/defaults/main.yml` and are indexed
  separately as needed.

## Compatibility

- Kubespray `v2.29.0` → Cilium `1.18.2`; `v2.30.0` → `1.18.6`; `v2.31.0` →
  `1.19.3`.
- Applies to the Kubernetes versions these releases install (`>=1.31`).
- Because the version is a literal, it does **not** vary with `kube_version`
  within a single Kubespray release (contrast [[COMPONENT-ETCD]]).

## References

- `roles/network_plugin/cilium/defaults/main.yml` (`cilium_version`,
  `cilium_image_repo`, `cilium_image_tag`) — line 117 (v2.29.0), 119
  (v2.30.0/v2.31.0).
- `roles/kubespray_defaults/defaults/main/main.yml` (`kube_network_plugin`).
- Tags: v2.29.0 `9991412`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
