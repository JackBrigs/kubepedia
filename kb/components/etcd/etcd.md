---
id: COMPONENT-ETCD
type: component
title: etcd
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: ">=3.5.23 <=3.6.10"
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
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/main.yml
    note: "etcd_supported_versions — per-minor filter (<3.6, and <3.7 for 1.35 in v2.31.0)"
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "etcd_binary_checksums — supported etcd binaries per tag"
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
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
Kubernetes minor line, so it moves with the Kubespray release and, since
`v2.31.0`, may differ between minors within one release.

## Context

- Covers Kubespray `v2.29.0`–`v2.31.0`.
- The deployment method is governed by [[VARIABLE-ETCD_DEPLOYMENT_TYPE]]
  (`host` by default; `docker` and `kubeadm` also supported, unchanged across all
  three tags).
- The etcd version depends on [[CONCEPT-KUBERNETES_VERSION_SUPPORT]] via
  `kube_major_version`.
- etcd is installed before the control plane in `cluster.yml`.

## Implementation

The version is derived, not pinned
(`roles/kubespray_defaults/defaults/main/download.yml`):

```yaml
etcd_version: "{{ etcd_supported_versions[kube_major_version] }}"
```

`etcd_supported_versions` (`roles/kubespray_defaults/vars/main/main.yml:14`) maps
each supported Kubernetes minor to the newest `etcd_binary_checksums` key below a
ceiling. In `v2.29.0`–`v2.30.0` the ceiling is `3.6` for every minor. In `v2.31.0`
the ceiling is raised to `3.7` for `1.35` only, which is how etcd `3.6` enters the
picture:

```yaml
# v2.31.0
etcd_supported_versions:
  '1.35': "{{ (etcd_binary_checksums['amd64'].keys() | select('version', '3.7', '<'))[0] }}"
  '1.34': "{{ (etcd_binary_checksums['amd64'].keys() | select('version', '3.6', '<'))[0] }}"
  '1.33': "{{ (etcd_binary_checksums['amd64'].keys() | select('version', '3.6', '<'))[0] }}"
```

Concrete resolution per tag and minor:

| Kubespray | Kubernetes minors | etcd version | Image (non-`host`) |
|-----------|-------------------|--------------|--------------------|
| v2.29.0   | 1.31, 1.32, 1.33  | 3.5.23       | quay.io/coreos/etcd:v3.5.23 |
| v2.30.0   | 1.32, 1.33, 1.34  | 3.5.26       | quay.io/coreos/etcd:v3.5.26 |
| v2.31.0   | 1.33, 1.34        | 3.5.29       | quay.io/coreos/etcd:v3.5.29 |
| v2.31.0   | 1.35              | 3.6.10       | quay.io/coreos/etcd:v3.6.10 |

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
- Cluster defaults (`roles/etcd_defaults/defaults/main.yml`, stable across all
  three tags): `etcd_cluster_setup: true`, `etcd_events_cluster_setup: false`,
  `etcd_quota_backend_bytes: "2147483648"` (2 GiB), `etcd_memory_limit` `512M`
  under 4 GB RAM else unlimited (only for `etcd_deployment_type: docker`).

## Compatibility

- Kubespray `v2.29.0` → etcd `3.5.23`; `v2.30.0` → `3.5.26`; `v2.31.0` → `3.5.29`
  for Kubernetes `1.33`/`1.34` and `3.6.10` for Kubernetes `1.35`.
- etcd `3.6` first appears in `v2.31.0`, gated to Kubernetes `1.35` by the `< 3.7`
  ceiling; older minors remain on the newest `3.5.x`.
- Architecture: `etcd_binary_checksums` provides `amd64` and `arm64`; the binary
  checksum is chosen by `image_arch`.

## References

- `roles/kubespray_defaults/defaults/main/download.yml` (`etcd_version`,
  `etcd_image_repo`, `etcd_image_tag`, `etcd_binary_checksum`)
- `roles/kubespray_defaults/vars/main/main.yml:14` (`etcd_supported_versions`)
- `roles/kubespray_defaults/vars/main/checksums.yml` (`etcd_binary_checksums`)
- `roles/etcd_defaults/defaults/main.yml` (cluster defaults)
- Tags: v2.29.0 `9991412`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
