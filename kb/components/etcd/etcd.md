---
id: COMPONENT-ETCD
type: component
title: etcd
status: active
kubespray_version: ">=v2.29.0 <=v2.30.0"
kubernetes_version: ">=1.31 <=1.34"
component_version: ">=3.5.23 <=3.5.26"
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
    lines: "130-132,215-218"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "etcd_version, etcd_image_repo, etcd_image_tag (line numbers shift by tag)"
  - type: code
    path: roles/kubespray_defaults/vars/main/main.yml
    lines: "14"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/kubespray_defaults/vars/main/main.yml
    note: "etcd_supported_versions dict keyed by kube_major_version"
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    lines: "425"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "etcd_binary_checksums — supported etcd binaries per tag"
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/etcd_defaults/defaults/main.yml
    note: "etcd cluster defaults (etcd_cluster_setup, quota, limits)"
relations:
  - type: depends_on
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
---

# etcd

## Summary

etcd is the key-value datastore backing the Kubernetes control plane. Kubespray
deploys it by default as a static binary run under systemd on the `etcd` host
group. The etcd version is not a literal — it is derived from the target
Kubernetes minor line, so it moves with the Kubespray release.

## Context

- Covers Kubespray `v2.29.0`–`v2.30.0`.
- The deployment method is governed by [[VARIABLE-ETCD_DEPLOYMENT_TYPE]]
  (`host` by default; `docker` and `kubeadm` also supported, unchanged across both
  tags).
- The etcd version depends on [[CONCEPT-KUBERNETES_VERSION_SUPPORT]] via
  `kube_major_version`.
- etcd is installed before the control plane in `cluster.yml`.

## Implementation

The version is derived, not pinned
(`roles/kubespray_defaults/defaults/main/download.yml`):

```yaml
etcd_version: "{{ etcd_supported_versions[kube_major_version] }}"
```

```yaml
# roles/kubespray_defaults/vars/main/main.yml:14
etcd_supported_versions:
  '<major>': "{{ (etcd_binary_checksums['amd64'].keys() | select('version', '3.6', '<'))[0] }}"
```

Each supported Kubernetes minor maps to the newest `etcd_binary_checksums` key
below `3.6`. Concrete resolution per tag (all minors of a tag resolve to the same
etcd version in `v2.29.0`–`v2.30.0`):

| Kubespray | Kubernetes minors | etcd version | Image (non-`host`) |
|-----------|-------------------|--------------|--------------------|
| v2.29.0   | 1.31, 1.32, 1.33  | 3.5.23       | quay.io/coreos/etcd:v3.5.23 |
| v2.30.0   | 1.32, 1.33, 1.34  | 3.5.26       | quay.io/coreos/etcd:v3.5.26 |

In the default `host` mode the binary is checksum-verified
(`etcd_binary_checksum: "{{ etcd_binary_checksums[image_arch][etcd_version] }}"`).
In container modes the image `etcd_image_repo`/`etcd_image_tag` is used.

## Configuration

- Version selection: `etcd_version`, `etcd_supported_versions`
  (`kubespray_defaults`).
- Image: `etcd_image_repo` = `quay.io/coreos/etcd`, `etcd_image_tag` =
  `v{{ etcd_version }}`.
- Deployment method: [[VARIABLE-ETCD_DEPLOYMENT_TYPE]] (`host` | `docker` |
  `kubeadm`).
- Cluster defaults (`roles/etcd_defaults/defaults/main.yml`, stable across both
  tags): `etcd_cluster_setup: true`, `etcd_events_cluster_setup: false`,
  `etcd_quota_backend_bytes: "2147483648"` (2 GiB), `etcd_memory_limit` `512M`
  under 4 GB RAM else unlimited (only for `etcd_deployment_type: docker`).

## Compatibility

- Kubespray `v2.29.0` → etcd `3.5.23`; Kubespray `v2.30.0` → etcd `3.5.26`.
- etcd `3.6`+ is excluded by the `< 3.6` selection filter in both tags.
- Architecture: `etcd_binary_checksums` provides `amd64` and `arm64`; the binary
  checksum is chosen by `image_arch`.

## References

- `roles/kubespray_defaults/defaults/main/download.yml` (`etcd_version`,
  `etcd_image_repo`, `etcd_image_tag`, `etcd_binary_checksum`)
- `roles/kubespray_defaults/vars/main/main.yml:14` (`etcd_supported_versions`)
- `roles/kubespray_defaults/vars/main/checksums.yml` (`etcd_binary_checksums`)
- `roles/etcd_defaults/defaults/main.yml` (cluster defaults)
- Tags: v2.29.0 `9991412`, v2.30.0 `f4ccdb5`.
