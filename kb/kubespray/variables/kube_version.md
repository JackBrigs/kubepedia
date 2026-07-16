---
id: VARIABLE-KUBE_VERSION
type: variable
title: kube_version
status: active
kubespray_version: v2.29.0
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - kube_version
tags:
  - kubernetes
  - version
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    lines: "25,28"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_version default and kube_version_min_required derivation"
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    lines: "112"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "kubelet_checksums — the set of installable Kubernetes versions"
  - type: code
    path: roles/validate_inventory/tasks/main.yml
    lines: "40-42"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.0/roles/validate_inventory/tasks/main.yml
    note: "assert kube_version >= kube_version_min_required"
relations:
  - type: part_of
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
---

# kube_version

## Summary

`kube_version` is the Kubernetes version Kubespray installs. In `v2.29.0` its
default resolves to `1.33.5`. The value is validated against a minimum and is
constrained in practice to the versions for which Kubespray ships checksums.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/main.yml:25`:

```yaml
kube_version: "{{ (kubelet_checksums['amd64'] | dict2items)[0].key }}"
```

The default is the **first** key of `kubelet_checksums['amd64']`
(`roles/kubespray_defaults/vars/main/checksums.yml`), which in `v2.29.0` is
`1.33.5`. The minimum is the **last** key
(`roles/kubespray_defaults/defaults/main/main.yml:28`):

```yaml
kube_version_min_required: "{{ (kubelet_checksums['amd64'] | dict2items)[-1].key }}"
```

which is `1.31.0`. The value is asserted at inventory validation time
(`roles/validate_inventory/tasks/main.yml:40-42`):

```yaml
- assert:
    that: kube_version is version(kube_version_min_required, '>=')
    msg: "The current release of Kubespray only support newer version of Kubernetes than {{ kube_version_min_required }} - You are trying to apply {{ kube_version }}"
```

There is no explicit upper-bound assertion; a `kube_version` outside
`kubelet_checksums` has no checksum entry and fails later during download. The
practical supported set is therefore exactly the `kubelet_checksums` keys — see
[[CONCEPT-KUBERNETES_VERSION_SUPPORT]].

## Compatibility

- Kubespray: `v2.29.0` (this document).
- Kubernetes: default `1.33.5`; overridable within `>=1.31.0 <=1.33.5` (the
  versions with shipped checksums).
- Setting `kube_version` below `1.31.0` fails the inventory-validation assert.

## References

- `roles/kubespray_defaults/defaults/main/main.yml:25,28`
- `roles/kubespray_defaults/vars/main/checksums.yml` (`kubelet_checksums`)
- `roles/validate_inventory/tasks/main.yml:40-42`
- Tag `v2.29.0`, commit `9991412`.
