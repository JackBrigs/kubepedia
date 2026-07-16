---
id: COMPONENT-ETCD
type: component
title: etcd
status: active
kubespray_version: v2.29.0
kubernetes_version: ">=1.31 <=1.33"
component_version: 3.5.23
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - etcd
tags:
  - etcd
  - datastore
  - control-plane
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    lines: "130,215,216"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "etcd_version, etcd_image_repo, etcd_image_tag"
  - type: code
    path: roles/kubespray_defaults/vars/main/main.yml
    lines: "14"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.0/roles/kubespray_defaults/vars/main/main.yml
    note: "etcd_supported_versions dict keyed by kube_major_version"
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    lines: "425"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "etcd_binary_checksums — supported etcd binaries"
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.0/roles/etcd_defaults/defaults/main.yml
    note: "etcd cluster defaults (etcd_cluster_setup, quota, limits)"
relations: []
---

# etcd

## Summary

etcd is the key-value datastore backing the Kubernetes control plane. In Kubespray
`v2.29.0` the shipped version is `3.5.23`, deployed by default as a static binary
run under systemd on the `etcd` host group. Version selection, image coordinates,
and cluster defaults are owned by the `kubespray_defaults` and `etcd_defaults`
roles.

## Context

- Applies to Kubespray `v2.29.0` (commit `9991412`).
- Compatible Kubernetes major versions in this release: `1.31`, `1.32`, `1.33`.
- The deployment method is governed by [[VARIABLE-ETCD_DEPLOYMENT_TYPE]]
  (`host` by default; `docker` and `kubeadm` also supported).
- etcd is a prerequisite for the API server; it is installed before the control
  plane in `cluster.yml`.

## Implementation

The etcd version is not a literal. It is derived from the target Kubernetes major
version:

```yaml
# roles/kubespray_defaults/defaults/main/download.yml:130
etcd_version: "{{ etcd_supported_versions[kube_major_version] }}"
```

```yaml
# roles/kubespray_defaults/vars/main/main.yml:14
etcd_supported_versions:
  '1.33': "{{ (etcd_binary_checksums['amd64'].keys() | select('version', '3.6', '<'))[0] }}"
  '1.32': "{{ (etcd_binary_checksums['amd64'].keys() | select('version', '3.6', '<'))[0] }}"
  '1.31': "{{ (etcd_binary_checksums['amd64'].keys() | select('version', '3.6', '<'))[0] }}"
```

Each major maps to the newest `etcd_binary_checksums` key below `3.6`. In
`v2.29.0` that key is `3.5.23` (the highest entry in `checksums.yml`), so with the
default Kubernetes version (`kube_version: 1.33.5`) etcd resolves to `3.5.23` for
all three supported majors.

In the default `host` deployment the binary is downloaded and checksum-verified:

```yaml
# roles/kubespray_defaults/defaults/main/download.yml:181
etcd_binary_checksum: "{{ etcd_binary_checksums[image_arch][etcd_version] }}"
```

In container modes the image is used instead:

```yaml
# roles/kubespray_defaults/defaults/main/download.yml:215-216
etcd_image_repo: "{{ quay_image_repo }}/coreos/etcd"   # quay.io/coreos/etcd
etcd_image_tag: "v{{ etcd_version }}"                    # v3.5.23
```

## Configuration

- Version selection: `etcd_version`, `etcd_supported_versions`
  (`kubespray_defaults`).
- Image: `etcd_image_repo` = `quay.io/coreos/etcd`, `etcd_image_tag` = `v3.5.23`.
- Deployment method: [[VARIABLE-ETCD_DEPLOYMENT_TYPE]] (`host` | `docker` |
  `kubeadm`).
- Cluster behavior defaults (`roles/etcd_defaults/defaults/main.yml`):
  - `etcd_cluster_setup: true`
  - `etcd_events_cluster_setup: false`
  - `etcd_quota_backend_bytes: "2147483648"` (2 GiB)
  - `etcd_memory_limit`: `512M` on hosts under 4 GB RAM, otherwise unlimited
    (only relevant for `etcd_deployment_type: docker`).

## Compatibility

- Kubespray: `v2.29.0`.
- Kubernetes: `1.31`, `1.32`, `1.33` (all map to etcd `3.5.23` in this release).
- etcd `3.6`+ is explicitly excluded by the `< 3.6` selection filter in
  `v2.29.0`.
- Architecture: `etcd_binary_checksums` provides `amd64` and `arm64` entries;
  the binary checksum is selected by `image_arch`.

## References

- `roles/kubespray_defaults/defaults/main/download.yml:130,181,215,216`
- `roles/kubespray_defaults/vars/main/main.yml:5,14` (`kube_major_version`,
  `etcd_supported_versions`)
- `roles/kubespray_defaults/vars/main/checksums.yml:425` (`etcd_binary_checksums`)
- `roles/etcd_defaults/defaults/main.yml` (cluster defaults)
- Tag `v2.29.0`, commit `9991412b4597d6eaf37f86e5f20f9f903a731c08`.
