---
id: ROLE-KUBESPRAY_DEFAULTS
type: role
title: kubespray_defaults
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubespray_defaults
  - kubespray-defaults
tags:
  - role
  - defaults
sources:
  - type: code
    path: roles/kubespray_defaults
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/roles/kubespray_defaults
    note: "central defaults, vars (checksums), and version derivation"
relations:
  - type: see_also
    target: VARIABLE-KUBE_VERSION
  - type: see_also
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
---

# kubespray_defaults

## Summary

`kubespray_defaults` is the central role that defines the vast majority of
Kubespray variables and derives component versions. Nearly every play depends on
it, so its `defaults/` and `vars/` are the effective configuration surface of the
whole project.

## Implementation

- `defaults/main/main.yml` — general cluster settings (networking CIDRs, ports,
  feature toggles, deployment types).
- `defaults/main/download.yml` — download coordinates, image repos/tags, and
  version derivations (e.g. `etcd_version`, `containerd_version`, literal
  `cilium_version`/`coredns_supported_versions`).
- `vars/main/main.yml` — computed constants (`kube_major_version`,
  `etcd_supported_versions`).
- `vars/main/checksums.yml` — the checksum tables that enumerate installable
  versions (`kubelet_checksums`, `etcd_binary_checksums`, `containerd_archive_checksums`, …).

In `v2.28.0`+ this canonical role uses the underscore name; a hyphenated
`kubespray-defaults` shim is deprecated.

## Configuration

Effectively all indexed `VARIABLE-*` documents originate here (see
[[VARIABLE-KUBE_VERSION]], [[VARIABLE-CONTAINER_MANAGER]], …). Defaults and version
derivations are the primary tuning surface.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- Included by essentially every play; changing its defaults changes cluster-wide
  behavior.

## References

- `roles/kubespray_defaults/` (tag `v2.31.0` `1c9add4`).
