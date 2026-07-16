---
id: COMPONENT-CNI_PLUGINS
type: component
title: CNI plugins (containernetworking/plugins)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: ">=1.8.0 <=1.9.1"
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - cni-plugins
  - cni_version
tags:
  - cni
  - networking
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    lines: "117,160"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "cni_version = first key of cni_binary_checksums; cni_download_url (containernetworking/plugins)"
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "cni_binary_checksums — installable CNI plugin archives per tag"
relations:
  - type: see_also
    target: TAG-NETWORK
  - type: see_also
    target: COMPONENT-CILIUM
---

# CNI plugins (containernetworking/plugins)

## Summary

The `containernetworking/plugins` set (bridge, host-local, loopback, portmap,
etc.) is the base CNI binary bundle Kubespray installs on nodes; the chosen
network plugin (see [[TAG-NETWORK]], [[COMPONENT-CILIUM]]) builds on top of it.
The version is derived from the per-release checksums table.

## Context

- Covers Kubespray `v2.29.0`–`v2.31.0`.
- Installed on cluster nodes regardless of the selected `kube_network_plugin`.

## Implementation

The version is derived
(`roles/kubespray_defaults/defaults/main/download.yml:117`):

```yaml
cni_version: "{{ (cni_binary_checksums['amd64'] | dict2items)[0].key }}"
cni_download_url: "{{ github_url }}/containernetworking/plugins/releases/download/v{{ cni_version }}/cni-plugins-linux-{{ image_arch }}-v{{ cni_version }}.tgz"
```

The value is the **first** (newest) key of `cni_binary_checksums['amd64']`.
Per tag:

| Kubespray | cni-plugins version |
|-----------|---------------------|
| v2.29.0   | 1.8.0               |
| v2.29.1   | 1.8.0               |
| v2.30.0   | 1.8.0               |
| v2.31.0   | 1.9.1               |

## Configuration

- Version selection: `cni_version`, `cni_binary_checksums` (`kubespray_defaults`).
- Download: `cni_download_url` (GitHub release archive), checksum by `image_arch`.

## Compatibility

- Kubespray `v2.29.0`–`v2.30.0` → cni-plugins `1.8.0`; `v2.31.0` → `1.9.1`.
- Architecture: `cni_binary_checksums` provides `amd64` and `arm64`.

## References

- `roles/kubespray_defaults/defaults/main/download.yml:117,160`.
- `roles/kubespray_defaults/vars/main/checksums.yml` (`cni_binary_checksums`).
- Tags: v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
