---
id: VARIABLE-KUBE_VERSION
type: variable
title: kube_version
status: active
kubespray_version: ">=v2.29.0 <=v2.30.0"
kubernetes_version: ">=1.31.0 <=1.34.3"
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
    note: "v2.29.0: kube_version default / kube_version_min_required derivation"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    lines: "25,28"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "v2.30.0: same derivation, values shift with checksums"
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    lines: "112"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "kubelet_checksums enumerates installable versions (per tag)"
  - type: code
    path: roles/validate_inventory/tasks/main.yml
    lines: "39-43"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.0/roles/validate_inventory/tasks/main.yml
    note: "assert kube_version >= kube_version_min_required (unchanged v2.29.0–v2.30.0)"
relations:
  - type: part_of
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
---

# kube_version

## Summary

`kube_version` is the Kubernetes version Kubespray installs. Its default and its
enforced minimum are both derived from the per-release `kubelet_checksums` table,
so they shift from tag to tag. The value is asserted against the minimum at
inventory-validation time.

## Implementation

The definition is stable across `v2.29.0`–`v2.30.0`
(`roles/kubespray_defaults/defaults/main/main.yml`):

```yaml
kube_version: "{{ (kubelet_checksums['amd64'] | dict2items)[0].key }}"                 # line 25
kube_version_min_required: "{{ (kubelet_checksums['amd64'] | dict2items)[-1].key }}"   # line 28
```

The default is the **first** key of `kubelet_checksums['amd64']`; the minimum is
the **last**. The concrete values per tag:

| Kubespray | Default (`kube_version`) | Minimum (`kube_version_min_required`) |
|-----------|--------------------------|----------------------------------------|
| v2.29.0   | 1.33.5                   | 1.31.0                                  |
| v2.30.0   | 1.34.3                   | 1.32.0                                  |

Enforcement is identical in both tags
(`roles/validate_inventory/tasks/main.yml`, task *"Stop if unsupported version of
Kubernetes"*):

```yaml
- assert:
    that: kube_version is version(kube_version_min_required, '>=')
    msg: "The current release of Kubespray only support newer version of Kubernetes than {{ kube_version_min_required }} - You are trying to apply {{ kube_version }}"
```

There is no explicit upper-bound assertion; a `kube_version` outside
`kubelet_checksums` has no checksum and fails during download. The full supported
set per tag is in [[CONCEPT-KUBERNETES_VERSION_SUPPORT]].

## Compatibility

- Kubespray `v2.29.0`: default `1.33.5`, overridable `>=1.31.0 <=1.33.5`.
- Kubespray `v2.30.0`: default `1.34.3`, overridable `>=1.32.0 <=1.34.3`.
- Below the per-tag minimum: rejected by the inventory-validation assert.

## References

- `roles/kubespray_defaults/defaults/main/main.yml:25,28` (v2.29.0 `9991412`,
  v2.30.0 `f4ccdb5`)
- `roles/kubespray_defaults/vars/main/checksums.yml` (`kubelet_checksums`)
- `roles/validate_inventory/tasks/main.yml` (version assert)
